---
type: concept_note
project: [[systems-rust-for-storage]]
status: active
updated: 2026-07-05
---

# ARC 智能指针相关的一些思考、学习事例

## 一句话

`Arc<T>` 可以理解为 Rust 里的线程安全 shared pointer：它让多个 owner handle 共同指向同一个 heap allocation，并用 atomic reference count 决定底层 `T` 什么时候被 drop。

但要记住：

```text
Arc 保护生命周期，不保护内容并发修改。
```

内容的并发安全要由 `Mutex`、`RwLock`、`Atomic*`、`SkipMap` 这类内部同步类型负责。

## Arc Handle 长什么样

概念上：

```rust
struct Arc<T> {
    ptr: NonNull<ArcInner<T>>,
}

struct ArcInner<T> {
    strong: AtomicUsize,
    weak: AtomicUsize,
    data: T,
}
```

所以：

```rust
let a = Arc::new(T);
let b = Arc::clone(&a);
```

不是复制 `T`，而是：

```text
a -> ArcInner { strong: 2, weak: 1, data: T }
b -> same ArcInner
```

`b` 不是 `a` 的 reference；`a` 和 `b` 是两个兄弟 strong owner handle。

## Move vs Clone

```rust
let a = Arc::new(T);
let b = a;
```

这是 move：

```text
strong 不变
a 失效
b 接手同一个 Arc handle
```

```rust
let a = Arc::new(T);
let b = Arc::clone(&a);
```

这是 clone Arc handle：

```text
strong += 1
a 和 b 都有效
底层 T 没有被复制
```

## Weak 的直觉

`Weak<T>` 不保活 `T`，只保留一个可尝试升级的 observer。

```rust
let a = Arc::new(T);
let w = Arc::downgrade(&a);

drop(a);

assert!(w.upgrade().is_none());
```

生命周期可以拆成两层：

```text
strong > 0:
  data: T 活着

strong == 0:
  data: T 被 drop

weak > 0:
  ArcInner/control block 还活着

strong == 0 && weak == 0:
  ArcInner allocation 被释放
```

`weak = 1` 的初始值可以理解为 strong owner group 持有一个 implicit weak slot，用来管理 control block 的最终释放。

## Deref：为什么 Arc 可以像内部对象一样调用方法

`Arc<T>` 实现了 `Deref<Target = T>`。

因此：

```rust
let x: Arc<RwLock<i32>> = Arc::new(RwLock::new(1));
x.read();
```

方法调用时 Rust 会做 auto-deref，近似理解为：

```rust
(*x).read();
```

这里 `.read()` 不是 `Arc` 的方法，而是 `RwLock` 的方法。`Arc` 只是通过 `Deref` 让你能访问里面的 `RwLock`。

注意：这是 `Deref` / dereference，不是 `derive`。

## MiniLSM 核心例子

MiniLSM 里有：

```rust
state: Arc<RwLock<Arc<LsmStorageState>>>
```

从里往外读：

```text
Arc<LsmStorageState>
  稳定的 state snapshot

RwLock<Arc<LsmStorageState>>
  保护当前 state snapshot 指针

Arc<RwLock<Arc<LsmStorageState>>>
  让多个 engine/task 共享同一个 state lock
```

## 这一句完整展开

代码：

```rust
let state = self.state.read().clone();
```

类型：

```rust
self.state: Arc<RwLock<Arc<LsmStorageState>>>
state: Arc<LsmStorageState>
```

更显式地写：

```rust
let state: Arc<LsmStorageState> = {
    let guard = self.state.read(); // RwLockReadGuard<Arc<LsmStorageState>>
    Arc::clone(&*guard)
}; // guard drop, read lock released
```

发生了什么：

```text
1. self.state 是 Arc<RwLock<Arc<State>>>
2. Arc auto-deref 到 RwLock
3. read() 拿到 RwLockReadGuard<Arc<State>>
4. *guard 得到内部 Arc<State>
5. Arc::clone(&*guard) 让内层 Arc<State> strong += 1
6. 语句结束，guard drop，读锁释放
7. state 变量持有稳定 snapshot handle
```

所以 clone 的不是：

```text
不是 clone 外层 Arc<RwLock<...>>
不是 deep clone LsmStorageState
```

clone 的是：

```text
内层 Arc<LsmStorageState> handle
```

## 读路径

```rust
let state = self.state.read().clone();

for memtable in std::iter::once(&state.memtable).chain(state.imm_memtables.iter()) {
    if let Some(value) = memtable.get(key) {
        if value.is_empty() {
            return Ok(None);
        }
        return Ok(Some(value));
    }
}
```

含义：

```text
短暂拿读锁
clone 当前 state snapshot
释放读锁
先查 current memtable
再查 immutable memtables
```

旧 reader 拿到旧 snapshot 后，即使全局 state 后续换成新 snapshot，旧 snapshot 也不会被释放。

## 写路径和 Freeze

```rust
let state = self.state.read().clone();
state.memtable.put(key, value)?;

if state.memtable.approximate_size() >= target {
    let state_lock = self.state_lock.lock();
    let latest_state = self.state.read().clone();

    if Arc::ptr_eq(&state.memtable, &latest_state.memtable)
        && latest_state.memtable.approximate_size() >= target
    {
        self.force_freeze_memtable(&state_lock)?;
    }
}
```

关键点：

```text
state 可能是旧 snapshot
freeze 前必须重新读 latest_state
Arc::ptr_eq 确认我们刚写的 memtable 仍然是 current memtable
state_lock 串行化 freeze/flush/compaction 这类结构性变化
```

`put` 写 memtable 时没有长期拿全局 `RwLock`，因为：

```text
state pointer 的安全由 RwLock 负责
memtable 内部读写安全由 SkipMap 负责
size counter 并发更新由 AtomicUsize 负责
```

## Freeze 发布新 State

```rust
let mut state_guard = self.state.write();
let mut new_state = state_guard.as_ref().clone();

let frozen_memtable = new_state.memtable.clone();
new_state.imm_memtables.insert(0, frozen_memtable);
new_state.memtable = Arc::new(MemTable::create(next_id));

*state_guard = Arc::new(new_state);
```

含义：

```text
拿写锁
复制旧 state 的结构
把旧 current memtable 的 Arc handle 放进 imm_memtables
创建新的 current memtable
用新的 Arc<State> 替换全局 state pointer
释放写锁
```

这就是 copy-on-write state pointer swap。

## 最终心智模型

```text
Arc:
  shared ownership / lifetime

Deref:
  让 Arc<T> 可以像 &T 一样调用 T 的方法

RwLock:
  保护当前 state pointer 的读写和可见性

inner Arc<State>:
  让 reader 拿稳定 snapshot 后快速释放锁

SkipMap:
  保护 memtable 内部并发 insert/get

AtomicUsize:
  保护 approximate_size 的并发更新

state_lock:
  串行化 freeze/flush/compaction 等结构性变化
```

一句话总结：

```text
Arc<RwLock<Arc<LsmStorageState>>>
= 共享一个可安全替换的全局 state pointer，
  并让读者拿到稳定 snapshot 后不长期持锁。
```
