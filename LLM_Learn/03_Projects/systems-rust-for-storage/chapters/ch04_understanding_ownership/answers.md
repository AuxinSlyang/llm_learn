---
type: chapter_answers
project: [[systems-rust-for-storage]]
status: first_pass_done
updated: 2026-07-05
---

# Ch4 Understanding Ownership Answers

## Materials

- [[chapter.pdf]]
- [[notes]]
- [[questions]]

## Answered

### Ownership 到底解决什么问题？

Ownership 解决的是内存资源归属和释放时机的问题。Rust 不依赖 GC，也不要求程序员手动 `free` 大多数内存；它用编译期规则确保每个 value 同一时间只有一个 owner，并在 owner 离开 scope 时自动 `drop`。

核心目标是避免：

- use-after-free：内存释放后继续访问。
- double free：同一块 heap 内存被释放两次。
- memory leak：资源长期无人释放。
- data race：后续 borrowing 规则会进一步约束并发访问。

### Stack / heap 和 ownership 有什么关系？

Stack 保存函数调用栈帧、局部变量、参数和一些固定大小 metadata。Heap 保存运行期动态分配、大小可能变化或需要更长生命周期的数据。

Ownership 主要让 Rust 能确定 heap resource 应该由谁释放。例如 `String` 的 metadata 在 stack 上，真实文本 buffer 在 heap 上；当 owning `String` 离开 scope，Rust 自动 drop 它并释放 heap buffer。

### heap allocation / allocating 是什么意思？

Heap allocation 是向 allocator 请求一块可用 heap 内存。allocator 找到足够大的空闲区域，标记为使用中，并返回这块区域的地址 pointer。Rust Book 说 abbreviated as allocating，只是把 “allocating on the heap” 简写成 “allocating”。

### Stack allocation 为什么通常更快？

Stack push/pop 基本是移动 stack pointer，大小和生命周期也由编译器/调用约定明确控制。Heap allocation 需要 allocator 查找空闲块、维护元数据、处理碎片，必要时还要向 OS 申请更多内存。

访问 heap 数据通常还要先读 pointer，再访问 pointer 指向的地址。CPU cache 可以让某些 heap 访问很快，但不会消除 allocator 管理成本和 pointer indirection。

当前本机 shell：`ulimit -s` 为 `8176 KB`，page size 为 `16384` bytes。常见 Linux/glibc 主线程 stack limit 常见约 `8192 KB`，但具体取决于系统配置和 `ulimit`。

### `String` 和 string literal 有什么区别？

String literal 如 `"hello"` 是编译期已知的不可变文本，类型通常是 `&'static str`，数据在程序静态区域。

`String::from("hello")` 创建 owned、growable 的 UTF-8 string。`String` metadata 可理解为 pointer / length / capacity，metadata 在当前 binding 的存储位置上，文本 buffer 通常在 heap 上。

### move 是什么？为什么 `let s2 = s1` 后 `s1` 不能继续用？

对 `String` 来说：

```rust
let s1 = String::from("hello");
let s2 = s1;
```

这会 move ownership。Rust 可能只移动/copy stack 上的 metadata，不深拷贝 heap buffer；但语义上 heap buffer 的 owner 从 `s1` 变成 `s2`。为了避免两个 owner 最后 double free，同一时间只能保留一个有效 owner，所以 `s1` 失效。

### clone 和 copy 的区别是什么？

`clone()` 是显式复制，可能进行 heap deep copy，例如 `String::clone()` 会复制文本 buffer。

`Copy` 是类型级别的隐式按位复制能力，适合 `i32`、`bool`、`char`、只包含 Copy 类型的 tuple 等。实现 `Copy` 的类型在赋值后旧 binding 仍可用。

不能简单说“stack 上的都是 Copy，heap 上的都 move”。关键是类型是否实现 `Copy`，以及它是否需要 `Drop` 管理资源。`String` 的 metadata 在 stack 上，但它拥有 heap buffer 并实现 Drop，所以不实现 Copy。

### What types implement `Copy`?

一般规则：只由简单、固定大小、可安全按位复制的数据组成，并且不需要释放外部资源的类型，可以实现 `Copy`。

常见例子：

```rust
i32
u64
bool
f64
char
(i32, i32)
```

不能实现 `Copy` 的典型例子：

```rust
String
(i32, String)
Vec<u8>
```

原因是这些类型拥有 heap allocation 或其他资源，并且需要在离开 scope 时 `Drop`。Rust 不允许一个实现了 `Drop` 或包含 non-Copy 字段的类型随便实现 `Copy`，否则可能发生 double free 或资源语义错误。

### Is stack assignment always deep copy and heap assignment always shallow copy?

这个说法作为直觉有帮助，但不够精确。

更准确的规则是：

- `Copy` 类型赋值时复制值本身，旧 binding 仍有效。
- non-`Copy` 类型赋值时发生 move，ownership 转移，旧 binding 失效。
- `clone()` 是显式复制，具体是 deep copy 还是共享引用计数，取决于类型实现。

`i32` 这种值没有额外 heap resource，所以 shallow/deep copy 没有区别；复制 bits 就是复制完整值。

`String` 的 stack metadata 可以很容易复制，但 metadata 指向 heap buffer。Rust 不能让两个普通 `String` 同时拥有同一个 heap buffer，所以赋值是 move；如果想复制文本内容，需要 `clone()`。

后续 `Bytes` 会带来一个新例子：`Bytes::clone()` 通常不是深拷贝底层字节，而是共享引用计数 buffer。这说明 `clone()` 的成本和语义要看具体类型文档。

### `String` move 时，stack metadata 是不是被 copy 了一份？

可以从实现直觉上这么理解：`String` 的 stack metadata 是 pointer / length / capacity，`let s2 = s1` 时这些固定大小的 bytes 很容易被搬到 `s2` 的位置，heap 上的文本 buffer 不会被 clone。

但 Rust 的语言语义不是“产生两个可用的 metadata 对象，共享同一块 heap buffer”。Rust 语义是 move：heap buffer 的唯一 owner 从 `s1` 转移到 `s2`，`s1` 立即失效，之后不能读，也不会在离开 scope 时 drop 那块 heap buffer。

所以更好的说法是：

- metadata 物理上可能被复制/移动，成本很低。
- heap resource 没有被复制。
- object-level ownership 发生转移，旧 binding 不再是一个可用对象。

这也是 Rust 避免 double free 的关键。

### 函数传参和返回值如何影响 ownership？

Passing a value to a function follows the same rules as assignment.

`String` 例子：

```rust
fn takes_ownership(s: String) {
    println!("{s}");
} // s goes out of scope and drops the String

let s1 = String::from("hello");
takes_ownership(s1);
// s1 is no longer valid here
```

`s1` 的 ownership 被 move 给参数 `s`。函数结束时，`s` 离开 scope，`String` 被 drop。

`i32` 例子：

```rust
fn makes_copy(x: i32) {
    println!("{x}");
}

let x = 5;
makes_copy(x);
println!("{x}"); // still valid
```

`i32` 实现 `Copy`，所以参数拿到的是一份 copy，调用方的 `x` 仍然有效。

返回值也会转移 ownership：

```rust
fn gives_ownership() -> String {
    String::from("hello")
}

let s1 = gives_ownership();
```

函数内部创建的 `String` ownership 被返回给 caller，`s1` 成为 owner。

如果函数既要读取 `String` 又要把它还给调用方，可以返回 tuple：

```rust
fn calculate_length(s: String) -> (String, usize) {
    let len = s.len();
    (s, len)
}

let s1 = String::from("hello");
let (s2, len) = calculate_length(s1);
```

这里 `s1` 被 move 进函数，函数再把 `s` move 出来给 `s2`。`len: usize` 是 `Copy` 标量，复制/移动都很便宜。这个写法能工作，但很笨重；下一节 references and borrowing 就是为了解决“不想转移 ownership，只想借用一下”的问题。

### string literal 是不是 scalar？为什么它可以 copy？

`"hello"` 这种 string literal 的类型通常是 `&'static str`，不是 `String`，也不准确说它是 scalar。

`&str` 是一个 borrowed string slice，可以理解为 fat pointer：pointer + length。`'static` 表示它指向程序静态区域里的只读文本，生命周期覆盖整个程序运行。

`&'static str` 本身实现 `Copy`，所以：

```rust
let a = "hello";
let b = a;
println!("{a}, {b}");
```

这里 copy 的只是 reference metadata，不会复制底层 `"hello"` 文本，也没有 heap ownership 需要释放。它和 `String::from("hello")` 的 owned heap buffer 是两套语义。

### 可以把 ownership 理解成 stack owner pop 时 callback free heap 吗？

可以作为第一层直觉，但要加几个限定。

对最常见的局部变量例子：

```rust
{
    let s = String::from("hello");
} // s is dropped here, heap buffer is freed
```

可以理解为：`s` 这个 owning value 离开 scope 时，Rust 调用 `drop(s)`；`String` 的 `Drop` 逻辑释放它拥有的 heap buffer。这个模型非常接近 C++ 的 RAII / destructor，而不是 GC。

所以“owner 离开 scope 时统一释放它拥有的 heap resource”这个理解是对的。

但更精确地说，不是“stack 内存 pop 自动 free heap”，而是：

- 编译器在 value 的 drop point 插入 drop 逻辑。
- 普通局部变量的 drop point 通常就是 scope 结束，发生在 stack frame 回收之前。
- 如果 value 被 move 走，旧 binding 不再 drop；最终 owner drop 时释放资源。
- 如果旧值被赋值覆盖，旧值会先被 drop。
- 可以显式调用 `std::mem::drop(x)` 提前释放。
- owner 不一定在 stack 上，也可以在 struct 字段、`Box<T>`、`Vec<T>`、`Arc<T>` 等结构里面。

对 `String` / `Vec<T>` / `Box<T>` 这种单 owner 类型，owner drop 时通常就释放底层 heap allocation。

对 `Arc<T>` / `Rc<T>` / `Bytes` 这类共享所有权或引用计数类型，某一个 owner drop 通常只是减少引用计数；只有最后一个 owner drop 时，底层 heap 数据才释放。

因此最终模型是：

```text
owning value reaches drop point
-> Rust runs Drop/destructor logic
-> that logic releases owned resources
```

Stack scope 是最常见触发点，但 ownership 真正绑定的是 value 的 drop 语义，而不是物理 stack pop 本身。

### 后面很多类型都需要自己定义 `Drop` 函数吗？

不一定。大多数普通业务 struct 不需要手写 `Drop`。

Rust 默认会自动递归 drop 字段：

```rust
struct User {
    name: String,
    age: u32,
}

{
    let u = User {
        name: String::from("alice"),
        age: 18,
    };
} // User is dropped, then name: String is dropped, heap buffer is freed
```

这里 `User` 自己没有实现 `Drop`，但它的字段 `name: String` 会被正常 drop。`String` 的标准库 `Drop` 实现负责释放它拥有的 heap buffer。

只有当类型直接管理某种需要自定义释放的资源时，才通常需要手写 `impl Drop for T`，例如：

- FFI handle / C library resource。
- 手写 allocator 或 unsafe heap memory。
- 文件、socket、临时目录等需要特殊关闭/清理的资源。
- lock guard、transaction guard、tracing span guard 这类 RAII guard。

所以日常 Rust 代码更多是在“组合已有会 Drop 的类型”，而不是每个 struct 都自己写 destructor。

### 如果 `String` 是 struct 字段，而且 struct 在 heap 上，生命周期怎么理解？

例子：

```rust
struct Record {
    key: String,
}

let r = Box::new(Record {
    key: String::from("k1"),
});
```

这里有两层 heap：

- `Box<Record>` 拥有一块 heap allocation，用来存放 `Record` 这个 struct。
- `Record.key: String` 又拥有另一块 heap buffer，用来存放 `"k1"` 的文本。

当 `r` 到达 drop point：

```text
drop(Box<Record>)
-> drop Record inside the Box
-> drop Record.key: String
-> free String's text buffer
-> free Box's Record allocation
```

所以你的理解是对的：如果一个 owning value 被放进 struct / container，字段的生命周期会跟随外层 owner。外层 owner 到达 drop point 时，会递归 drop 内部字段。

但注意：owner 不一定在 stack 上。`Record` 可以在 `Box` 的 heap allocation 里，`String` 可以在 `Vec<Record>` 的元素里，或者被 `Arc<Record>` 共享。ownership 看的不是“在哪块物理内存”，而是谁负责最终 drop。

### `Copy` 能理解成 stack 上 deep copy 吗？

对 `i32` / `bool` / `char` 这种标量，可以这么粗略理解：复制 bits 就是复制完整值。

但更精确地说，`Copy` 是复制 value 自身的表示，而不是递归复制它可能指向的所有东西。

例如：

```rust
let s = String::from("hello");
let a: &String = &s;
let b = a; // Copy the reference, not the String
```

`a` 和 `b` 都是 reference。复制的是 reference value 本身，也就是类似 pointer 的东西；底层 `String` 没有被复制。

再比如：

```rust
let a: &str = "hello";
let b = a;
```

`&str` 可以理解为 pointer + length。`b = a` 复制的是 pointer + length，不是复制 `"hello"` 文本。

所以：

- `i32` 的 Copy：复制完整整数。
- `[i32; 10000]` 的 Copy：语义上复制整个数组，可能很大，不一定便宜。
- `&str` / `&[u8]` 的 Copy：复制 borrowed view，不复制底层数据。
- `String` 不 Copy：因为它拥有 heap buffer，需要唯一 owner 来负责释放。

Copy 的关键不是“stack only”，而是“这个类型可以安全地隐式复制 value 自身，并且不需要自定义 Drop 来释放唯一资源”。

还有一个容易漏掉的点：自定义 struct 不会因为字段全是 `Copy` 就自动 `Copy`。

```rust
struct Point {
    x: i32,
    y: i32,
}

let p1 = Point { x: 1, y: 2 };
let p2 = p1;
// p1 is moved and no longer usable
```

如果希望它像 `i32` 一样赋值后旧 binding 仍可用，需要显式声明：

```rust
#[derive(Copy, Clone)]
struct Point {
    x: i32,
    y: i32,
}
```

这相当于类型作者明确承诺：这个类型可以安全地做隐式复制，并且没有需要唯一释放责任的资源。

### `&T` shared reference 是什么？reference 可以指向 stack 吗？

可以。reference 可以指向 stack 上的 value，也可以指向 heap 上的 value、static data、struct 字段、slice 的一段区域。

例子：

```rust
let x = 5;
let y = &x;
println!("{y}");
```

这里 `x: i32` 是一个局部变量，通常在 stack frame 里；`y: &i32` 是对 `x` 的 shared reference。`y` 本身也是一个 value，可以理解成受 Rust 规则约束的 pointer。

所以 reference 不是“只能指向 heap”。它指向的是某个已经存在的 value 或 value 的一部分。被指向的数据由别人拥有，reference 只是临时访问路径。

对 `String` 来说：

```rust
let s = String::from("hello");
let r = &s;
```

`r` 借的是 `s` 这个 `String` value 本身。`String` value 里有 pointer / length / capacity metadata，通过这些 metadata 可以访问 heap buffer。`r` 不拥有 heap buffer，也不会在自己结束时释放它。

### borrowing 为什么能替代 tuple return ownership？

没有 borrowing 时，如果函数拿走 `String` ownership，就要把它还回来：

```rust
fn calculate_length(s: String) -> (String, usize) {
    let len = s.len();
    (s, len)
}
```

这能工作，但很笨重，因为函数只是想读长度，并不需要拥有 `String`。

borrowing 写法是：

```rust
fn calculate_length(s: &String) -> usize {
    s.len()
}

let s1 = String::from("hello");
let len = calculate_length(&s1);
println!("{s1}, {len}");
```

`&s1` 创建一个 shared reference，函数参数 `s: &String` 只借用它。函数结束时，reference 离开 scope，但因为 reference 不拥有数据，所以不会 drop `String`。`s1` 的 ownership 一直在 caller 手里。

这就是 borrowing：临时借用访问权，不转移释放责任。

### `&` 和 `*` 分别是什么？

`&x` 是取引用，也就是创建 reference。

`*r` 是解引用，也就是沿着 reference/pointer 访问它指向的值。

例子：

```rust
let x = 5;
let r = &x;
assert_eq!(5, *r);
```

很多实际代码里你不会频繁看到 `*`，因为 Rust 会做自动 deref 和 method call deref。例如 `s.len()` 里如果 `s: &String`，Rust 可以自动把 `&String` 解引用到 `String` 来调用方法。

### `&mut T` mutable reference / exclusive reference 是什么？

`&mut T` 表面意思是 mutable reference，可变引用；更核心的意思是 exclusive reference，独占引用。

如果你有一个活跃的 `&mut T`，同一段数据在这段时间里不能再有其他 reference，也不能通过 owner binding 直接访问：

```rust
let mut s = String::from("hello");
let r = &mut s;

r.push_str(", world");
// println!("{s}"); // not allowed while r is still active
```

`let mut s` 只表示 `s` 这个 binding 允许被修改。它不表示可以绕过 borrow checker。

一旦 `s` 被 `&mut s` 借出，`r` 的有效区间内，`s` 本身也暂时不能被直接使用。等 `r` 最后一次使用结束，borrow 结束，`s` 才能继续使用。

### 能把 `mut s` 理解成每次修改时临时创建一个 `&mut s` 吗？

可以作为读代码时的直觉，但不要理解成 `mut s` 本身长期持有一个隐藏的 `&mut s`。

`let mut s` 的意思只是：这个 binding 允许被重新赋值或被可变借用。

当你写：

```rust
let mut s = String::from("hello");
s.push_str("!");
```

`push_str` 的方法签名本质上需要 `&mut self`，所以编译器会为这次 method call 建立一个很短的独占借用区间，类似：

```rust
String::push_str(&mut s, "!");
```

这个短暂的 `&mut s` 不能和其他活跃 borrow 重叠：

```rust
let mut s = String::from("hello");
let r = &s;
s.push_str("!"); // not allowed if r will be used later
println!("{r}");
```

所以你的理解方向是对的：每次通过 `s` 修改，都需要满足“此刻可以拿到独占访问”。但更精确地说，Rust 检查的是每次 place 使用和 borrow 的有效区间是否冲突，而不是给 `mut s` 安排一个贯穿生命周期的隐藏 mutable reference。

### 为什么不能同时有一个 mutable reference 和其他 shared references？

规则可以记成：

```text
either one mutable reference
or any number of shared references
```

多个 `&T` 可以共存，因为大家都只读。

一个 `&mut T` 必须独占，因为它可能修改数据。如果同时还有 `&T`，读者可能看到数据突然变化；如果同时还有另一个 `&mut T`，两个 writer 可能互相踩。

这很像读写锁的静态版本：

- shared reference = reader。
- mutable reference = writer。
- writer 必须独占。

但 Rust 的规则不只是为了多线程 data race。单线程里也会出问题，例如你一边持有指向 `Vec` 元素的 reference，一边 push 导致 `Vec` reallocate，旧 reference 就可能悬垂。Rust 用同一套 borrowing 规则提前挡住这类 aliasing mutation。

### borrow checker 在编译期到底保证了什么？

在 safe Rust 中，borrow checker 主要保证：

- reference 指向的数据在 reference 有效期间不会被 drop。
- 同一时间不能既有人读又有人无同步写同一份数据。
- `&mut T` 是独占访问，不会和其他 active references 重叠。
- move 后的旧 binding 不会继续被使用。

这能防止 use-after-free、dangling reference、double free 和很多 aliasing mutation bug。

对 data race，Rust Book 给的三条件是：

- 两个或更多 pointer 同时访问同一数据。
- 至少一个 pointer 用于写。
- 没有同步机制。

Rust 的 safe code 会要求你要么遵守 borrowing 的静态互斥，要么使用 `Mutex` / `RwLock` / atomic / channel 等同步类型。跨线程时还会有 `Send` / `Sync` 这些 trait 约束。

### Rust 怎么解决多线程 data race？

Rust 不是不允许多线程，而是不允许 safe code 在没有同步机制时跨线程共享可变数据。

主要靠三层机制：

第一，ownership 控制数据如何进入线程。

```rust
let s = String::from("hello");
std::thread::spawn(move || {
    println!("{s}");
});
```

`move` closure 把 `s` 的 ownership 移到新线程。旧线程不再拥有 `s`，所以不会两个线程同时修改同一个 `String`。

第二，`Send` / `Sync` trait 限制什么类型能跨线程移动或共享。

- `T: Send`：`T` 的 ownership 可以安全移动到另一个线程。
- `T: Sync`：`&T` 可以安全地在多个线程之间共享。

例如 `Rc<T>` 不是线程安全引用计数，不能直接跨线程；`Arc<T>` 是 atomic reference counting，可以用于跨线程共享。

第三，共享可变状态必须通过同步类型。

典型写法：

```rust
use std::sync::{Arc, Mutex};

let counter = Arc::new(Mutex::new(0));

let c = Arc::clone(&counter);
std::thread::spawn(move || {
    let mut guard = c.lock().unwrap();
    *guard += 1;
});
```

这里多个线程可以拥有同一个 `Arc<Mutex<i32>>` 的 clone，但不能同时直接拿到内部 `i32` 的 `&mut i32`。`Mutex` 在运行时保证同一时间只有一个线程能拿到 `MutexGuard`。`MutexGuard` 活着时，你才可以通过它修改内部数据。

所以：

```text
多个线程可以共享 Mutex 本身
但不能无同步地共享 Mutex 里面的可变数据
```

这就是 Rust 的设计：静态类型系统负责禁止明显不安全的共享；需要共享可变状态时，把同步机制显式放进类型里。

MiniLSM 后面会看到类似模式：`Arc<...>` 表示跨 owner 共享，`Mutex` / `RwLock` / concurrent map 表示内部有受控并发修改机制。

### `Arc` 到底是什么？

`Arc` 是 `Atomic Reference Counted`，可以理解为线程安全版本的 shared ownership smart pointer。

它解决的问题是：有些数据不是单一 owner 能表达的。多个线程、多个任务、多个 iterator、后台 flush task 都需要“共同持有同一个对象”，并且对象要等最后一个使用者结束后才能释放。

核心模型：

```text
Arc<T>
-> heap allocation:
   - strong refcount
   - weak refcount
   - T
-> Arc handle:
   - 指向这块 allocation 的指针
```

`Arc::clone(&x)` 做的事情不是 clone `T`，而是：

```text
atomic strong_count += 1
return another Arc handle pointing to same T
```

`Arc` drop 时：

```text
atomic strong_count -= 1
if strong_count == 0:
    drop T
    when weak_count == 0, free allocation
```

所以 `Arc` 是 ownership 层面的工具：

- 让多个 owner 共享同一个 `T`。
- 用 atomic refcount 保证跨线程 clone/drop 安全。
- 保证最后一个 strong owner 消失时才 drop `T`。
- 通过 `Deref` 让你像 `&T` 一样读取内部数据。

但 `Arc` 不是锁：

- 它不保证同一时间只有一个线程访问 `T`。
- 它不自动允许修改 `T`。
- 它不保护 `T` 的内部临界区。

能不能跨线程共享 `Arc<T>`，还要看 `T` 是否满足线程安全约束。直觉上：

```text
Arc<Vec<i32>>         -> 共享只读 OK，不能直接 push
Arc<Mutex<Vec<i32>>>  -> 共享可变 OK，通过 Mutex lock 修改
Arc<AtomicUsize>      -> 共享可变 OK，通过 atomic 操作修改
Arc<SkipMap<K, V>>    -> 共享可变 OK，前提是 SkipMap 自己是并发数据结构
```

典型使用场景：

- 多线程共享只读配置：`Arc<Config>`。
- 多线程共享可变状态：`Arc<Mutex<State>>` / `Arc<RwLock<State>>`。
- async / background task 共享服务句柄：`Arc<Service>`。
- storage engine 里共享 MemTable、SST metadata、block cache、manifest state。
- iterator / flush task 延长某个对象生命周期，防止前台切换后旧对象被释放。

什么时候不用 `Arc`：

- 单一 owner 足够时，用普通 ownership。
- 只是临时读一下，用 `&T`。
- 单线程引用计数，用 `Rc<T>`。
- 需要共享可变状态但内部没有同步机制时，不要只套 `Arc<T>`；需要 `Mutex` / `RwLock` / atomic / concurrent data structure。

从 ownership 角度看，`Arc` 是对 “one owner” 规则的受控扩展：不是让 Rust 失去 owner，而是把 owner 从“一个 binding”变成“多个 counted handles”。释放责任由引用计数决定，最后一个 strong owner 负责触发 `T` 的 drop。

### `Arc` 和 C++ 智能指针是什么关系？strong / weak 怎么实现？

你的直觉是对的：`Arc<T>` 非常像 C++ 的 `std::shared_ptr<T>`，`Weak<T>` 非常像 C++ 的 `std::weak_ptr<T>`。

粗略对应：

```text
Rust Arc<T>   ~= C++ std::shared_ptr<T>
Rust Weak<T>  ~= C++ std::weak_ptr<T>
Rust Rc<T>    ~= 单线程版 shared pointer，引用计数非原子
```

概念实现大概是：

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

真实标准库实现更复杂，但这个模型足够理解。

`Arc<T>` 是 strong pointer。只要 `strong > 0`，`data: T` 就还活着，可以通过 `Arc<T>` deref 成 `&T`。

`Weak<T>` 是 weak pointer。它不保持 `T` 活着，只保留一个指向控制块的弱引用。想使用数据时必须：

```rust
weak.upgrade() -> Option<Arc<T>>
```

如果 strong count 已经是 0，说明 `T` 已经被 drop，`upgrade()` 返回 `None`。

生命周期流程：

```text
Arc::clone
-> atomic strong += 1
-> 产生另一个 strong owner

drop Arc
-> atomic strong -= 1
-> 如果 strong 变成 0，drop data: T
-> 如果 weak 也归零，释放整块 allocation/control block

Weak::clone
-> atomic weak += 1

Weak::upgrade
-> 如果 strong == 0，返回 None
-> 否则 strong += 1，返回 Some(Arc<T>)
```

为什么需要 weak？主要是打破循环引用。

错误模型：

```text
Parent --Arc--> Child
Child  --Arc--> Parent
```

两边都 strong-own 对方，strong count 永远不会归零，内存泄漏。

正确模型：

```text
Parent --Arc--> Child
Child  --Weak--> Parent
```

Parent 强拥有 Child；Child 只是弱观察 Parent。Parent 如果已经释放，Child 的 weak back-pointer `upgrade()` 会得到 `None`。

从 Rust 角度理解，`Arc` 仍然是 ownership，只是 owner 不是一个，而是一组 counted strong handles。`Weak` 不是 owner，只是一个可升级的 observer。

### `Arc` 本身会保护里面的 `T` 吗？

不会。`Arc` 保护的是共享 ownership 和引用计数，不是 `T` 的临界区。

`Arc<T>` 可以理解成 atomic reference counting pointer：

```text
Arc clone/drop
-> 用原子操作更新 refcount
-> 最后一个 Arc drop 时释放 T
```

所以 `Arc` 自己的 refcount 是线程安全的。多个线程 clone/drop `Arc` 不会把引用计数搞乱，也不会提前释放 `T`。

但 `Arc` 不会自动给 `T` 加锁：

```rust
Arc<T>
```

只表示多个 owner 共享同一个 `T`。如果只有 `Arc<T>`，通常你只能拿到 `&T` 这种 shared access。能不能跨线程共享，取决于 `T` 是否满足 `Sync`；能不能修改，取决于 `T` 内部是否提供安全的 mutation 机制。

因此：

```rust
Arc<Vec<i32>>
```

多个线程可以共享读取这个 `Vec`，但不能直接 push。

如果要共享可变状态，常见写法是：

```rust
Arc<Mutex<Vec<i32>>>
```

这里职责分开：

```text
Arc   -> 多线程共享 ownership，保证对象活得够久
Mutex -> 临界区/互斥，保证同一时间只有一个 writer
```

多个线程可以各自持有 `Arc<Mutex<T>>` 的 clone，但修改内部 `T` 必须先 `lock()`：

```rust
let mut guard = shared.lock().unwrap();
guard.push(1);
```

`guard` 活着时，锁处于持有状态；`guard` drop 时，锁释放。这也是 RAII。

如果你写的是：

```rust
Arc<AtomicUsize>
```

那同步机制不是 `Mutex`，而是 `AtomicUsize` 自己的原子操作。

如果你写的是：

```rust
Arc<RwLock<T>>
```

那同步机制是读写锁：多个 reader 或一个 writer。

所以最终模型是：

```text
Arc 负责共享所有权，不负责保护 T 的内容
Mutex/RwLock/Atomic 负责同步访问 T
Arc<Mutex<T>> = 共享所有权 + 互斥可变访问
```

### `Arc` 的最小例子是什么？

先看只读共享：

```rust
use std::sync::Arc;
use std::thread;

fn main() {
    let data = Arc::new(vec![10, 20, 30]);
    let mut handles = Vec::new();

    for i in 0..3 {
        let data_for_thread = Arc::clone(&data);

        let handle = thread::spawn(move || {
            println!("value = {}", data_for_thread[i]);
        });

        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }
}
```

这里发生了几件事：

- `Arc::new(vec![10, 20, 30])` 创建一个可跨线程共享 ownership 的对象。
- `Arc::clone(&data)` 不复制整个 `Vec`，只增加 atomic refcount。
- 每个线程通过 `move` 拿走一个 `Arc` clone。
- 所有线程共享同一个 `Vec`，但只是读，所以不需要 `Mutex`。
- 最后一个 `Arc` drop 时，底层 `Vec` 才会被释放。

注意：这个例子不能直接 `push`：

```rust
// data_for_thread.push(40); // not allowed
```

因为 `Arc<Vec<i32>>` 只给你共享 ownership，不给你对 `Vec` 的独占可变访问。

如果要多个线程共享修改，需要 `Arc<Mutex<T>>`：

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let counter = Arc::new(Mutex::new(0));
    let mut handles = Vec::new();

    for _ in 0..4 {
        let counter_for_thread = Arc::clone(&counter);

        let handle = thread::spawn(move || {
            let mut guard = counter_for_thread.lock().unwrap();
            *guard += 1;
        });

        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("counter = {}", *counter.lock().unwrap());
}
```

这里：

- `Arc` 让多个线程拥有同一个 `Mutex<i32>`。
- `Mutex` 控制临界区。
- `lock()` 返回 `MutexGuard`。
- `MutexGuard` 活着时，可以通过 `*guard` 修改内部 `i32`。
- `guard` 离开 scope 自动 drop，锁被释放。

LSM / MiniLSM 里更接近这种形态：

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

这里 `Arc<SkipMap<Bytes, Bytes>>` 的意思是：

- `Arc` 让多个 owner 共享同一个 memtable map，例如 foreground writer、iterator、flush task。
- `SkipMap` 自己是并发数据结构，内部已经提供受控 mutation，所以 `insert` 可以通过 shared reference 调用。
- `Bytes::copy_from_slice` 把 borrowed `&[u8]` 变成 owned/shared byte buffer，避免 caller 的 slice 失效后 MemTable 里留下 dangling data。

所以 LSM 里常见组合是：

```text
Arc<ConcurrentMap<K, V>>
```

或者：

```text
Arc<Mutex<PlainMap<K, V>>>
```

前者同步逻辑在 concurrent map 内部；后者同步逻辑在 Mutex 里。`Arc` 只是让这份结构被多个任务/线程共同拥有。

### reference 的 scope 是整个花括号吗？

现代 Rust 使用 non-lexical lifetimes。reference 的有效借用区间从创建开始，到最后一次使用结束，不一定持续到整个 `{}` scope 结束。

例子：

```rust
let mut s = String::from("hello");

let r1 = &s;
let r2 = &s;
println!("{r1}, {r2}");

let r3 = &mut s;
r3.push_str("!");
```

这里 `r1` / `r2` 的最后一次使用在 `println!`，所以之后 shared borrows 结束，可以创建 `r3: &mut String`。

但如果后面还要用 `r1`：

```rust
let mut s = String::from("hello");
let r1 = &s;
let r3 = &mut s;
println!("{r1}");
```

这就不允许，因为 `r1` 的 shared borrow 和 `r3` 的 mutable borrow 重叠了。

### dangling reference 为什么在 Rust 里不能通过编译？

dangling reference 是 reference 指向的数据已经离开 scope 或被释放。

错误例子：

```rust
fn dangle() -> &String {
    let s = String::from("hello");
    &s
}
```

`s` 是函数内部局部变量。函数结束时 `s` 被 drop，heap buffer 被释放。如果允许返回 `&s`，caller 拿到的就是悬垂引用。

Rust 的规则是：reference must always be valid。也就是说，被引用的数据生命周期必须覆盖 reference 的生命周期。上面的代码不能证明这一点，所以编译器拒绝。

正确做法通常是返回 owned value：

```rust
fn no_dangle() -> String {
    String::from("hello")
}
```

这样 ownership 被 move 给 caller，没有悬垂 reference。

### slice 是什么？

Slice 是一种 reference，不拥有数据。它引用 collection 中一段连续元素。

最常见两类：

```rust
&str   // string slice
&[T]   // general slice
```

`String` 是 owned、growable string；`&str` 是借来的 string view。`Vec<T>` / array 是 owned 或固定容器；`&[T]` 是借来的连续元素 view。

可以把 slice 理解成 fat pointer：

```text
slice = pointer + length
```

例如：

```rust
let s = String::from("hello world");
let hello = &s[0..5];
let world = &s[6..11];
```

`hello: &str` 指向 `s` 的前 5 个字节；`world: &str` 指向后 5 个字节。它们都不拥有底层数据，底层数据仍由 `s: String` 拥有。

Range 语法里：

```rust
&s[0..2] == &s[..2]
&s[3..s.len()] == &s[3..]
&s[0..s.len()] == &s[..]
```

注意 `end` 是 exclusive，不包含右边界。

### 为什么 `first_word` 返回 `usize` 不好，返回 `&str` 更好？

返回 `usize` 的版本类似：

```rust
fn first_word(s: &String) -> usize {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return i;
        }
    }

    s.len()
}
```

这个 `usize` 只是一个 index。它本身不知道自己来自哪个 string，也不知道 string 后来有没有变化。

问题是：

```rust
let mut s = String::from("hello world");
let word = first_word(&s); // word = 5
s.clear();                // s is now empty
// word is still 5, but no longer meaningful
```

`word` 这个 index 和 `s` 的状态脱节了。

返回 slice 的版本：

```rust
fn first_word(s: &String) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[..i];
        }
    }

    &s[..]
}
```

现在返回值 `&str` 和输入 `s` 的 borrow 绑定在一起。如果 `word: &str` 后面还要使用，那么 Rust 不允许你中途调用 `s.clear()`：

```rust
let mut s = String::from("hello world");
let word = first_word(&s);
s.clear();          // error if word will be used later
println!("{word}");
```

原因是：

- `word` 是对 `s` 内部数据的 shared borrow。
- `clear()` 需要 `&mut self`，也就是 mutable borrow。
- shared borrow 还活着时，不能创建 mutable borrow。

这不是严格意义上的多线程 data race，而是单线程 aliasing mutation。Rust 用同一套 borrowing 规则防止“旧 view 还要用，但底层数据已经被改坏”的问题。

### aliasing mutation 是什么？

拆开看：

```text
aliasing = 同一份数据有多个访问路径 / 多个名字 / 多个 reference
mutation = 其中某条路径正在修改这份数据
```

所以 aliasing mutation 就是：**还有别名能看到这份数据时，你又通过另一路径去改它**。

最小例子：

```rust
let mut s = String::from("hello world");

let word = &s[..5]; // alias: word 指向 s 内部的一段数据
s.clear();          // mutation: 想通过 s 修改底层数据

println!("{word}"); // 如果允许，这个 word 可能已经无效
```

`word` 是 `s` 内部 buffer 的一个 borrowed view。`s.clear()` 会修改 `s`，甚至可能让原来 slice 的语义失效。Rust 不允许这个操作重叠：

```text
shared borrow word still active
mutable borrow for clear requested
-> reject
```

这不一定是多线程问题。单线程也会出 bug。

`Vec` 例子更典型：

```rust
let mut v = vec![1, 2, 3];
let first = &v[0];

v.push(4);          // 可能触发 reallocation，旧引用 first 可能悬垂
println!("{first}");
```

如果 `push` 让 `Vec` 重新分配 buffer，`first` 原来指向的地址可能已经失效。Rust 会拒绝这种“旧 alias 还要用，同时 mutation 可能破坏底层存储”的写法。

Rust 的核心规则可以记成：

```text
many aliases + no mutation is OK
one mutable access + no aliases is OK
many aliases + mutation is dangerous
```

这就是为什么：

```text
多个 &T 可以共存
一个 &mut T 必须独占
```

### string literal 为什么是 slice？

```rust
let s = "hello world";
```

这里 `s` 的类型是 `&'static str`。

含义是：

- 字符串字面量内容存放在程序二进制/静态只读区域。
- `s` 是一个指向这段静态数据的 string slice。
- `'static` 表示这段数据在整个程序运行期间都有效。

所以 string literal 不是 owned `String`，而是一个 borrowed `&str`。

### 为什么函数参数应该优先写 `&str` 而不是 `&String`？

更推荐：

```rust
fn first_word(s: &str) -> &str
```

而不是：

```rust
fn first_word(s: &String) -> &str
```

因为 `&str` 更 general：

```rust
let owned = String::from("hello world");
let literal = "hello world";

first_word(&owned);      // &String can coerce to &str
first_word(&owned[..]);  // explicit string slice
first_word(literal);     // already &str
```

这里用到的是 deref coercion，不是 derive coercion。`String` 实现了 deref 到 `str` 的能力，所以 `&String` 在需要 `&str` 的地方可以自动转换。

API 设计原则：

```text
只需要读字符串内容 -> 参数用 &str
需要 owned/growable string -> 参数用 String
需要修改 caller 的 String -> 参数用 &mut String
```

### `&[u8]`、`[u8; N]`、`Vec<u8>`、`Bytes` 有什么区别？

这组会直接出现在 MiniLSM。

```text
[u8; N]  固定长度数组，长度 N 是类型的一部分，通常 owned。
Vec<u8>  owned growable byte buffer，数据通常在 heap 上。
&[u8]    borrowed byte slice，不拥有数据，只是 pointer + length。
Bytes    owned/shared byte buffer，clone 通常是引用计数共享，适合长期保存和廉价 clone。
```

例子：

```rust
fn read_key(key: &[u8]) {
    println!("key length = {}", key.len());
}

let arr = [1_u8, 2, 3];
let vec = vec![1_u8, 2, 3];

read_key(&arr);
read_key(&vec);
read_key(&vec[..]);
```

`&[u8]` 的好处是它不关心 caller 的底层容器是什么，只要求“给我一段连续 bytes 的 borrowed view”。

### 为什么 MiniLSM `put(&self, key: &[u8], value: &[u8])` 传入 borrowed bytes？

因为 `put` 的调用者可能有各种形式的 key/value：

- array。
- `Vec<u8>`。
- `Bytes`。
- string literal 的 `.as_bytes()`。
- 网络 buffer 的一段 slice。

如果 API 写成 `key: &[u8]`，调用者只需要借给 MemTable 看一眼：

```rust
mem.put(b"k1", b"v1");
mem.put(&vec_key, &vec_value);
mem.put(bytes_key.as_ref(), bytes_value.as_ref());
```

这让 API 更 general，也避免不必要地要求 caller 交出 ownership。

但 `&[u8]` 只是借用，不能长期保存。`put` 如果要把 key/value 存进 MemTable，就必须在内部转成 owned/shared buffer：

```rust
Bytes::copy_from_slice(key)
```

### 为什么 `Bytes::copy_from_slice(key)` 要把 borrowed data 变成 owned buffer？

因为 MemTable 的数据要在 `put` 返回后继续存在，而 `key: &[u8]` / `value: &[u8]` 的生命周期只由 caller 保证。

错误直觉：

```text
把 &[u8] 存进 MemTable
```

这会要求 caller 的 buffer 活得和 MemTable 一样久，通常不现实，也容易 dangling。

正确做法：

```rust
let key = Bytes::copy_from_slice(key);
let value = Bytes::copy_from_slice(value);
self.map.insert(key, value);
```

这样 MemTable 拥有 key/value 的 bytes。后续 iterator、flush、get 都可以安全使用。

### `SkipMap::insert(&self, ...)` 为什么共享引用也能写？

普通 struct 的 `&self` 不能直接修改字段：

```rust
struct Table {
    x: i32,
}

impl Table {
    fn set(&self) {
        // self.x = 1; // not allowed
    }
}
```

但某些类型把 mutation 封装在内部同步或内部可变性机制里，例如：

- `Mutex<T>`：通过 lock 拿 guard。
- `RwLock<T>`：读写锁。
- atomic：原子操作。
- concurrent map：内部自己做并发控制。

`SkipMap` 是并发数据结构，它的 API 允许通过 `&self` 调用 `insert`，因为它在内部保证修改是安全的。

所以 MiniLSM 里：

```rust
Arc<SkipMap<Bytes, Bytes>>
```

可以读成：

```text
Arc     -> 多个 owner 共享同一个 map
SkipMap -> 内部支持并发修改
Bytes   -> key/value 是可长期保存的 owned/shared bytes
```

## Target Questions For MiniLSM

- `&self` 是什么？为什么它不是“自己的拷贝”？
- `&mut self` 的“独占”到底由谁保证？
- `&[u8]` 是什么？和 `[u8; N]`、`Vec<u8>`、`Bytes` 有什么区别？
- 为什么 `SkipMap::insert(&self, ...)` 可以写？这和普通 struct 的 `&self` 有什么区别？
- `Bytes::copy_from_slice(key)` 为什么需要把 borrowed slice 变成 owned buffer？
