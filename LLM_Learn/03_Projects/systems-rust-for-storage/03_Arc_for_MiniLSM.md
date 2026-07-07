---
type: concept_note
project: [[systems-rust-for-storage]]
status: active
updated: 2026-07-05
---

# Arc for MiniLSM

## One Sentence

`Arc<T>` is a thread-safe shared ownership smart pointer: many owners can point to the same heap-allocated `T`, and `T` is dropped only when the last strong owner is dropped.

## What Arc Solves

普通 ownership 是 single owner。很多系统代码需要 shared ownership：

- 多个线程共享只读 config / metadata。
- 前台 writer、iterator、flush task 同时持有一个 MemTable。
- cache / service handle / runtime state 被多个 task 共享。
- 对象不能在某个局部 scope 结束时释放，必须等最后一个使用者结束。

`Arc` 解决的是“谁共同拥有、对象活多久”，不是“谁此刻能修改”。

更精确地说，`Arc` 保护的是共享资源的生命周期：只要还有一个 strong owner handle 存在，底层 `T` 就不会被 drop。它不保护 `T` 的内容不被并发写坏；内容的并发安全必须由 `T` 自己的同步机制提供，例如 `Mutex`、`RwLock`、atomic 或 concurrent data structure。

## Mental Model

```text
Arc<T>
-> heap allocation:
   - strong refcount
   - weak refcount
   - T

Arc::clone(&x)
-> atomic strong_count += 1
-> return another handle to the same T

drop Arc
-> atomic strong_count -= 1
-> if strong_count == 0: drop T
-> allocation is freed after weak refs are also gone
```

`Arc::clone` does not clone `T`.

## C++ Mapping

`Arc<T>` is very close to C++ `std::shared_ptr<T>`:

```text
Rust Arc<T>    ~= C++ std::shared_ptr<T> with thread-safe refcount
Rust Weak<T>   ~= C++ std::weak_ptr<T>
Rust Rc<T>     ~= single-thread shared_ptr-like pointer with non-atomic refcount
```

The difference is how Rust's type system composes it with ownership:

- `Arc<T>` is an owning value. Moving an `Arc<T>` moves one owner handle.
- `Arc::clone(&x)` explicitly creates another owner handle.
- `Drop` decrements the strong count automatically.
- `Deref<Target = T>` lets `Arc<T>` behave like `&T` for reads and method calls.
- Thread sharing is still constrained by `Send` / `Sync`; `Arc` does not make non-thread-safe `T` magically safe.

## Implementation Shape

Conceptually, `Arc<T>` points to one heap allocation:

```rust
struct ArcInner<T> {
    strong: AtomicUsize,
    weak: AtomicUsize,
    data: T,
}

struct Arc<T> {
    ptr: NonNull<ArcInner<T>>,
}

struct Weak<T> {
    ptr: NonNull<ArcInner<T>>,
}
```

The real standard library implementation has more details, but this is the core idea.

## What an Arc Handle Looks Like

`Arc<T>` value itself is only a small handle. It does not contain `T`.

Conceptually:

```rust
struct Arc<T> {
    ptr: NonNull<ArcInner<T>>,
    // plus marker/allocator details in the real std implementation
}
```

So a stack variable like:

```rust
let a = Arc::new(SkipMap::<Bytes, Bytes>::new());
let b = Arc::clone(&a);
```

looks like:

```text
stack / owner handles

a: Arc<SkipMap<...>>
   ptr ─────┐
            │
b: Arc<SkipMap<...>>
   ptr ─────┘
            │
            v
heap allocation

ArcInner<SkipMap<...>> {
    strong: 2,
    weak: 1,      // conceptual implicit weak while strong refs exist
    data: SkipMap<Bytes, Bytes>,
}
```

Moving `a` moves the handle. Cloning `a` creates another handle and increments `strong`. Dropping a handle decrements `strong`.

The handle is pointer-sized-ish; the data is in the shared heap allocation.

## Step-by-Step Counts

Use this model:

```rust
let a = Arc::new(T);
let b = Arc::clone(&a);
let c = Arc::downgrade(&a);
drop(a);
drop(b);
drop(c);
```

Step 1:

```rust
let a = Arc::new(T);
```

```text
stack:
  a -> ArcInner

heap:
  ArcInner {
      strong: 1,
      weak: 1,   // implicit weak held by the strong-owner group
      data: T,
  }
```

`a` is one strong owner handle. `data: T` is alive.

Step 2:

```rust
let b = Arc::clone(&a);
```

```text
stack:
  a -> ArcInner
  b -> ArcInner

heap:
  strong: 2
  weak: 1
  data: T
```

`b` is not a reference to `a`. `a` and `b` are sibling handles. Both point to the same allocation.

Step 3:

```rust
let c = Arc::downgrade(&a);
```

```text
stack:
  a: Arc<T>  -> ArcInner
  b: Arc<T>  -> ArcInner
  c: Weak<T> -> ArcInner

heap:
  strong: 2
  weak: 2    // implicit weak + explicit c
  data: T
```

`c` does not keep `T` alive. It only keeps the allocation/control block around and can try `upgrade()`.

Step 4:

```rust
drop(a);
```

```text
strong: 1
weak: 2
data: T still alive
```

Step 5:

```rust
drop(b);
```

```text
strong: 0
drop data: T
drop implicit weak
weak: 1      // only explicit c remains
allocation still alive, but data is gone
```

Now:

```rust
c.upgrade() == None
```

Step 6:

```rust
drop(c);
```

```text
strong: 0
weak: 0
free ArcInner allocation/control block
```

So the lifetimes split:

```text
T lifetime:
  strong > 0

ArcInner allocation lifetime:
  strong > 0 or weak > 0
```

The initial `weak = 1` is an implementation trick: the group of strong references holds one implicit weak slot so the allocation/control block can be managed correctly when the last strong reference drops.

## Move vs Clone

```rust
let a = Arc::new(T);
let b = a;
```

This is move:

```text
strong stays 1
a is invalid
b is the same owner handle moved to a new binding
```

```rust
let a = Arc::new(T);
let b = Arc::clone(&a);
```

This is clone:

```text
strong becomes 2
a and b are both valid strong owner handles
```

That is why Rust diagnostics often say cloning an `Arc` is inexpensive: it does not clone `T`, only the handle/refcount.

## Official Source Pointers

- `Arc<T>` handle fields: `ptr: NonNull<ArcInner<T>>`, marker, allocator.
- `ArcInner<T>` fields: `strong`, `weak`, `data`.
- `Arc::new` initializes `strong = 1`, `weak = 1`.
- `Arc::clone` increments `strong`.
- `Arc::drop` decrements `strong`; if it reaches zero, it drops `data`.
- `Weak::upgrade` increments `strong` only if it is currently nonzero; otherwise it returns `None`.

## Strong vs Weak

Strong references are `Arc<T>` handles:

```text
strong_count > 0
-> T is alive
-> Arc<T> can deref to &T
```

Weak references are `Weak<T>` handles:

```text
weak_count > 0
-> allocation/control block may stay alive
-> T may already be dropped
-> must call upgrade() to get Option<Arc<T>>
```

`Weak<T>` does not keep `T` alive. It only keeps the allocation metadata around so it can test whether `T` is still alive.

## Clone / Drop Flow

`Arc::clone`:

```text
atomic strong += 1
return new Arc handle to same ArcInner<T>
```

`Arc::drop`:

```text
atomic strong -= 1
if strong becomes 0:
    drop data: T
    release the implicit weak held by strong refs
    if weak is also 0:
        deallocate ArcInner allocation
```

`Weak::clone`:

```text
atomic weak += 1
return new Weak handle
```

`Weak::upgrade`:

```text
if strong == 0:
    return None
else:
    atomic strong += 1 if still nonzero
    return Some(Arc<T>)
```

This is why `Weak<T>` avoids cycles: it can point at an allocation without preventing `T` from being dropped.

## Why Weak Exists

If two objects own each other with `Arc`, their strong counts never reach zero:

```text
Parent --Arc--> Child
Child  --Arc--> Parent
```

This creates a reference cycle and leaks memory.

Use `Weak` for back-pointers:

```text
Parent --Arc--> Child
Child  --Weak--> Parent
```

Now the parent owns the child strongly, but the child only observes the parent weakly. If the parent is gone, `child.parent.upgrade()` returns `None`.

This pattern appears in graphs, trees with parent pointers, caches, registries, and runtime/task graphs.

## Arc Is Not a Lock

```text
Arc<T>              = shared ownership
Mutex<T>            = mutual exclusion for T
Arc<Mutex<T>>       = shared ownership + synchronized mutable access
Arc<RwLock<T>>      = shared ownership + many readers / one writer
Arc<AtomicUsize>    = shared ownership + atomic mutation
Arc<SkipMap<K, V>>  = shared ownership + concurrent map handles its own synchronization
```

## Read-Only Sharing

```rust
use std::sync::Arc;
use std::thread;

let data = Arc::new(vec![10, 20, 30]);

for i in 0..3 {
    let data = Arc::clone(&data);
    thread::spawn(move || {
        println!("{}", data[i]);
    });
}
```

`Arc<Vec<_>>` lets threads share the same `Vec` for reading. It does not allow direct `push`.

## Shared Mutation

```rust
use std::sync::{Arc, Mutex};

let counter = Arc::new(Mutex::new(0));
let c = Arc::clone(&counter);

std::thread::spawn(move || {
    let mut guard = c.lock().unwrap();
    *guard += 1;
}); // guard drops here, lock is released
```

`Arc` shares the `Mutex`; `MutexGuard` controls the critical section.

## MiniLSM Mapping

```rust
use std::sync::Arc;
use bytes::Bytes;
use crossbeam_skiplist::SkipMap;

struct MemTable {
    map: Arc<SkipMap<Bytes, Bytes>>,
}

impl MemTable {
    fn put(&self, key: &[u8], value: &[u8]) {
        self.map.insert(
            Bytes::copy_from_slice(key),
            Bytes::copy_from_slice(value),
        );
    }
}
```

Read this as:

```text
Arc     -> foreground / iterator / flush task can share the same map safely by ownership.
SkipMap -> concurrent data structure; insert/get can be called through shared reference.
Bytes   -> key/value stored as owned/shared bytes, not borrowed caller slices.
```

Day 1 also has:

```rust
pub struct MemTable {
    map: Arc<SkipMap<Bytes, Bytes>>,
    approximate_size: Arc<AtomicUsize>,
}
```

`map` and `approximate_size` are two separate shared objects:

```text
map Arc
-> shared ownership of one concurrent SkipMap
-> SkipMap provides synchronization for insert/get

approximate_size Arc
-> shared ownership of one AtomicUsize counter
-> AtomicUsize provides atomic increments/loads
```

Another important MiniLSM shape:

```rust
state: Arc<RwLock<Arc<LsmStorageState>>>
```

Read it inside-out:

```text
Arc<LsmStorageState>
-> immutable-ish state snapshot, cheap to clone for readers

RwLock<Arc<LsmStorageState>>
-> protects the current snapshot pointer
-> write lock swaps pointer to a new state
-> read lock clones current Arc snapshot

Arc<RwLock<...>>
-> lets engine handles / tasks share the same lock object
```

This is copy-on-write state:

```text
reader:
    read lock
    clone inner Arc<LsmStorageState>
    drop read lock
    use stable snapshot

writer:
    build new LsmStorageState
    write lock
    replace inner Arc
    drop write lock
```

Old readers may keep using the old snapshot. New readers see the new snapshot.

## Why `Arc<RwLock<Arc<LsmStorageState>>>` Exists

This type solves three different problems at three different layers:

```text
Arc< RwLock< Arc<LsmStorageState> > >
|    |       |
|    |       +-- stable state snapshot for readers
|    +---------- synchronized current-state pointer
+--------------- shared engine-wide state handle
```

### Outer `Arc`

The outer `Arc` shares the lock object itself.

Without it, only one owner could hold the engine state lock. In a real storage engine, many handles/tasks need to reach the same state:

- foreground `get` / `put`
- freeze / flush / compaction tasks
- iterators or background workers

So the outer `Arc` answers:

```text
How do multiple engine handles point to the same state lock?
```

It does not protect state contents. It only keeps the lock object alive until the last owner is gone.

### `RwLock`

`RwLock` protects the current state pointer.

The state pointer changes when the engine freezes a memtable, installs a new memtable, flushes, or later changes SST metadata.

`RwLock` answers:

```text
Who may observe or replace the current state pointer right now?
```

- read lock: clone the current snapshot pointer
- write lock: replace the current snapshot pointer

The lock gives synchronization and visibility: after a writer releases the write lock, later readers acquiring the read lock see a consistent pointer.

### Inner `Arc<LsmStorageState>`

The inner `Arc` makes a state snapshot stable after the lock is released.

Reader path:

```rust
let state = self.state.read().clone();
// read lock guard drops quickly
// state is Arc<LsmStorageState>, so the snapshot stays alive
```

This avoids holding the `RwLock` while doing all reads. A reader can use the snapshot while a writer prepares and installs a newer snapshot.

So the inner `Arc` answers:

```text
How can a reader keep using the exact state snapshot it saw,
without blocking writers for the whole read?
```

## What If One Layer Is Removed?

No outer `Arc`:

```text
RwLock<Arc<LsmStorageState>>
```

Only one owner has the lock. Hard to share engine state across cloned engine handles or background tasks.

No `RwLock`:

```text
Arc<Arc<LsmStorageState>>
```

There is shared ownership, but no synchronized way to replace the current state pointer.

No inner `Arc`:

```text
Arc<RwLock<LsmStorageState>>
```

Readers must either hold the read lock while using the state, blocking writers longer, or copy the whole state. The snapshot is not cheaply detachable.

The chosen shape:

```text
Arc<RwLock<Arc<LsmStorageState>>>
```

means:

```text
share the lock globally
lock only long enough to clone the current snapshot pointer
use the snapshot without holding the lock
replace state by copy-on-write pointer swap
```

## Day 1 Flow

Read path:

```rust
let state = self.state.read().clone();
for memtable in once(&state.memtable).chain(state.imm_memtables.iter()) {
    ...
}
```

Meaning:

```text
1. acquire read lock
2. clone Arc<LsmStorageState>
3. release read lock
4. search current memtable then immutable memtables in a stable snapshot
```

Write path:

```rust
let state = self.state.read().clone();
state.memtable.put(key, value)?;

if state.memtable.approximate_size() >= target {
    let state_lock = self.state_lock.lock();
    let latest_state = self.state.read().clone();
    if Arc::ptr_eq(&state.memtable, &latest_state.memtable) {
        self.force_freeze_memtable(&state_lock)?;
    }
}
```

Meaning:

```text
1. clone a state snapshot
2. write to the snapshot's current memtable
3. if size threshold is crossed, serialize freeze with state_lock
4. re-read latest state
5. Arc::ptr_eq checks whether the memtable we wrote is still the current memtable
6. only then freeze and swap state
```

Freeze path:

```rust
let mut state = self.state.write();
let mut snapshot = state.as_ref().clone();
let frozen_memtable = snapshot.memtable.clone();
snapshot.imm_memtables.insert(0, frozen_memtable);
snapshot.memtable = Arc::new(MemTable::create(self.next_sst_id()));
*state = Arc::new(snapshot);
```

Meaning:

```text
1. acquire write lock
2. clone old state value into a mutable local snapshot
3. move current memtable into immutable list by cloning its Arc handle
4. create a new current memtable
5. publish new state by replacing inner Arc<LsmStorageState>
```

Old readers keep using old `Arc<LsmStorageState>`. New readers clone the new one.

## Count Changes in `Arc<RwLock<Arc<LsmStorageState>>>`

Assume:

```rust
state: Arc<RwLock<Arc<LsmStorageState>>>
```

There are two different `Arc` allocations:

```text
outer allocation:
  ArcInner<RwLock<Arc<LsmStorageState>>>

inner allocation:
  ArcInner<LsmStorageState>
```

They count different things.

Outer clone:

```rust
let engine2_state = Arc::clone(&self.state);
```

```text
outer strong += 1
inner strong unchanged
```

This creates another handle to the same lock object. It does not clone the state snapshot.

Reader snapshot clone:

```rust
let snapshot = self.state.read().clone();
```

```text
outer strong unchanged
RwLock read lock acquired temporarily
inner strong += 1
RwLock read lock released
```

This keeps the old `LsmStorageState` alive after the lock is released.

Writer state swap:

```rust
let mut guard = self.state.write();
*guard = Arc::new(new_state);
```

```text
new inner ArcInner created:
  new_inner strong = 1

old inner Arc in guard is dropped:
  old_inner strong -= 1
  if old readers still hold snapshots:
      old data stays alive
  else:
      old LsmStorageState is dropped
```

This is the copy-on-write pointer swap.

Reader drop:

```rust
drop(snapshot);
```

```text
inner strong -= 1
if this was the last old snapshot:
    drop old LsmStorageState
```

The outer lock object may live much longer than any particular inner state snapshot.

## Data Race and Visibility

`Arc` alone solves lifetime sharing. It does not solve data visibility or critical sections for `T`.

```text
Arc<T>
-> atomic refcount is safe
-> T access rules still depend on T
```

Visibility/synchronization comes from the inner type:

```text
Mutex<T> / RwLock<T>
-> lock acquire/release synchronizes data visibility

AtomicUsize
-> atomic operation is indivisible
-> memory ordering controls visibility guarantees

SkipMap
-> concurrent data structure handles its own synchronization
```

For MiniLSM:

```text
Arc<SkipMap<Bytes, Bytes>>
-> Arc keeps map alive
-> SkipMap prevents data races in concurrent insert/get

Arc<AtomicUsize>
-> Arc keeps counter alive
-> AtomicUsize prevents torn increments
-> Relaxed is enough for approximate size because it is not publishing data

Arc<RwLock<Arc<LsmStorageState>>>
-> Arc keeps lock alive
-> RwLock gives readers/writers visibility and exclusion for state pointer swaps
-> inner Arc snapshot lets readers use old state without holding lock
```

Rule:

```text
Arc answers: who owns this object and when can it be freed?
Mutex/RwLock/Atomic/SkipMap answer: who can read/write it now, and what becomes visible when?
```

## What Concurrency Is Guaranteed Here

`Arc<RwLock<Arc<LsmStorageState>>>` primarily protects the *state pointer*, not every byte inside the engine.

It guarantees:

```text
current state pointer is not torn
readers clone a valid state snapshot
writers replace the state pointer under exclusive write lock
old snapshots remain alive while readers use them
```

It does not by itself guarantee:

```text
all memtable inserts are serialized
all reads see the newest possible write at every instant
memtable contents are protected by the RwLock
```

The full Day 1 concurrency contract is split across components:

```text
Arc<RwLock<Arc<LsmStorageState>>>
-> protects current state snapshot pointer and snapshot lifetime

Arc<SkipMap<Bytes, Bytes>>
-> protects concurrent memtable insert/get internally

Arc<AtomicUsize>
-> protects approximate size counter increments/loads

state_lock: Mutex<()>
-> serializes structural state changes such as freeze
```

So read/write concurrency works by composition, not by `Arc` alone.

Read path:

```text
reader clones state snapshot
reader releases RwLock quickly
reader searches current + immutable memtables in that snapshot
SkipMap handles concurrent map access
```

Put path:

```text
writer clones state snapshot
writer inserts into snapshot.memtable
SkipMap handles concurrent insert
AtomicUsize updates approximate size
if threshold crossed, state_lock serializes freeze attempt
freeze publishes a new state snapshot through RwLock write lock
```

Visibility sources:

```text
RwLock acquire/release
-> visibility for replacing current state pointer

AtomicUsize ordering
-> visibility/atomicity for size counter only

SkipMap internal synchronization
-> visibility/safety for key/value insert/get
```

Important limitation: this shape gives snapshot consistency and memory safety. It does not automatically mean every operation is globally linearizable unless the write/freeze protocol is designed to guarantee that. In a production LSM, state transitions such as freeze/flush/compaction must be carefully serialized and re-checked so a writer does not continue writing a memtable that has already been logically frozen.

For MiniLSM Day 1, the key idea to learn is:

```text
Arc keeps shared objects alive.
RwLock publishes a new state pointer safely.
Inner Arc lets readers use old snapshots without holding the lock.
SkipMap/Atomic/state_lock provide the actual data-path synchronization.
```

## Complete Code Flow

First, use a simplified shape close to MiniLSM:

```rust
use std::sync::Arc;
use parking_lot::{Mutex, RwLock};
use bytes::Bytes;
use crossbeam_skiplist::SkipMap;
use std::sync::atomic::{AtomicUsize, Ordering};

struct LsmStorageInner {
    state: Arc<RwLock<Arc<LsmStorageState>>>,
    state_lock: Mutex<()>,
    options: LsmStorageOptions,
}

#[derive(Clone)]
struct LsmStorageState {
    memtable: Arc<MemTable>,
    imm_memtables: Vec<Arc<MemTable>>,
}

struct MemTable {
    map: Arc<SkipMap<Bytes, Bytes>>,
    approximate_size: Arc<AtomicUsize>,
    id: usize,
}

struct LsmStorageOptions {
    target_sst_size: usize,
}
```

Initialization:

```rust
let initial_state = LsmStorageState {
    memtable: Arc::new(MemTable::create(0)),
    imm_memtables: vec![],
};

let inner = LsmStorageInner {
    state: Arc::new(RwLock::new(Arc::new(initial_state))),
    state_lock: Mutex::new(()),
    options,
};
```

Read path:

```rust
impl LsmStorageInner {
    pub fn get(&self, key: &[u8]) -> anyhow::Result<Option<Bytes>> {
        let state: Arc<LsmStorageState> = self.state.read().clone();

        for memtable in std::iter::once(&state.memtable).chain(state.imm_memtables.iter()) {
            if let Some(value) = memtable.get(key) {
                if value.is_empty() {
                    return Ok(None);
                }
                return Ok(Some(value));
            }
        }

        Ok(None)
    }
}
```

What happens in `self.state.read().clone()`:

```text
self.state
-> outer Arc<RwLock<Arc<State>>> is dereferenced to RwLock

.read()
-> acquire RwLock read guard
-> guard points to current Arc<State>

.clone()
-> clone the inner Arc<State>
-> inner state strong_count += 1

end of statement
-> read guard drops
-> RwLock read lock released

state variable
-> owns one Arc<State> snapshot
-> snapshot stays alive even if global state pointer changes
```

Write path:

```rust
impl LsmStorageInner {
    pub fn put(&self, key: &[u8], value: &[u8]) -> anyhow::Result<()> {
        let state: Arc<LsmStorageState> = self.state.read().clone();

        state.memtable.put(key, value)?;

        if state.memtable.approximate_size() >= self.options.target_sst_size {
            let state_lock = self.state_lock.lock();

            let latest_state: Arc<LsmStorageState> = self.state.read().clone();

            if Arc::ptr_eq(&state.memtable, &latest_state.memtable)
                && latest_state.memtable.approximate_size() >= self.options.target_sst_size
            {
                self.force_freeze_memtable(&state_lock)?;
            }
        }

        Ok(())
    }
}
```

What happens:

```text
1. Clone current state snapshot.
2. Insert key/value into that snapshot's current memtable.
3. SkipMap handles concurrent insert/get inside the memtable.
4. AtomicUsize updates approximate size.
5. If size threshold might be crossed, acquire state_lock.
6. Re-read latest state snapshot.
7. Arc::ptr_eq checks whether the memtable we wrote is still the current memtable.
8. If still current and still too large, freeze it.
```

Freeze path:

```rust
impl LsmStorageInner {
    pub fn force_freeze_memtable(
        &self,
        _state_lock_guard: &parking_lot::MutexGuard<'_, ()>,
    ) -> anyhow::Result<()> {
        let mut state_guard = self.state.write();

        let mut new_state: LsmStorageState = state_guard.as_ref().clone();

        let frozen_memtable = new_state.memtable.clone();
        new_state.imm_memtables.insert(0, frozen_memtable);
        new_state.memtable = Arc::new(MemTable::create(self.next_sst_id()));

        *state_guard = Arc::new(new_state);

        Ok(())
    }
}
```

What happens:

```text
1. state_lock_guard already serializes structural state changes.
2. acquire RwLock write lock.
3. clone the old state value into a mutable local state.
4. clone old current memtable Arc handle into imm_memtables[0].
5. create a new current memtable.
6. wrap new state in Arc<State>.
7. replace current state pointer under write lock.
8. old readers keep old Arc<State>; new readers see new Arc<State>.
```

Core problem this design solves:

```text
Readers should not hold a global state lock while doing memtable/SST reads.
Writers must be able to publish a new state atomically.
Old readers must not observe a half-updated/torn state.
The old state must stay alive while old readers use it.
Freeze must not accidentally freeze a memtable that is no longer current.
```

The design answer:

```text
read lock briefly -> clone snapshot -> release lock -> read stable snapshot
write lock briefly -> publish new snapshot pointer
state_lock -> serialize structural changes and force re-check
Arc::ptr_eq -> ensure the snapshot decision still matches latest state
```

## When Not to Use Arc

- Use normal ownership when one owner is enough.
- Use `&T` for temporary borrowing.
- Use `Rc<T>` for single-thread reference counting.
- Do not use plain `Arc<T>` to mutate shared state unless `T` itself provides synchronization.

## Key Rule

`Arc` extends ownership from one owner to counted shared owners. It does not weaken Rust's safety model; it makes the release point depend on the last strong owner.
