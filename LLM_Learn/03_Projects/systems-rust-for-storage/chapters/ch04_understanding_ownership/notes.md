---
type: chapter_notes
project: [[systems-rust-for-storage]]
status: first_pass_done
updated: 2026-07-05
---

# Ch4 Understanding Ownership Notes

## Materials

- [[chapter.pdf]]
- [[questions]]
- [[answers]]

## Takeaways

- Ownership 是 Rust 最独特的特性之一：它让 Rust 在没有 GC 的情况下，通过编译期规则管理内存安全。
- Ownership 不是运行期后台回收机制，而是一组编译器检查的规则。如果代码违反 ownership / borrowing 规则，程序不能通过编译。
- 本章主线：ownership -> move / clone / copy -> references / borrowing -> slices；这些概念共同解释 Rust 如何管理 stack / heap 上的数据。
- Ownership rules：
  - Rust 中每个 value 都有一个 owner。
  - 同一时间只能有一个 owner。
  - owner 离开 scope 时，value 会被 dropped。
- Scope 是 binding 有效的词法范围。变量进入 scope 后可用，离开 scope 后 Rust 自动调用 `drop` 清理它拥有的资源。
- Stack / heap 的重点不是“哪个更高级”，而是：
  - stack 适合大小已知、生命周期跟随函数调用的值。
  - heap 适合大小运行期才知道、需要动态增长或跨作用域移动所有权的值。
- Heap allocation 的意思是：向 allocator 请求一块可用内存，allocator 标记这块内存正在使用，并返回指向这块内存的 pointer。Rust Book 里说 abbreviated as allocating，只是把 “allocating on the heap” 简写为 “allocating”。
- Stack 上也是真实内存，通常每个线程有自己的 stack 区域，由 stack pointer 等机制按 call frame 推进/回退。当前本机 shell 的 `ulimit -s` 是 `8176 KB`，page size 是 `16384` bytes；常见 Linux/glibc 主线程 stack limit 常见是约 `8192 KB`，但具体取决于系统和 `ulimit`。
- Heap 不是“天然固定结构”，而是进程虚拟地址空间中由 allocator 管理的动态分配区域。allocator 可能从 OS 申请大块内存，再在用户态做小块分配和复用；不是每次 `String::from` 都直接系统调用。
- Stack allocation 通常更快，因为 push/pop 接近移动 stack pointer，局部性也更好。Heap allocation 通常更慢，因为需要 allocator 查找/维护空闲块、元数据和可能的同步；访问 heap 数据还需要通过 pointer 间接访问。CPU cache 可以缓解差距，但不能改变数据需要间接寻址和 allocator 管理的事实。
- String literal（如 `"hello"`）是编译期已知的字符串数据，通常存放在程序的静态只读区域，类型是 `&'static str`，不是 growable owned string。
- `String::from("hello")` 创建 owned、growable 的 `String`，其文本缓冲区在 heap 上；stack 上保存的是 `String` 元数据，通常可理解为 pointer / length / capacity。
- `let s2 = s1` 对 `String` 来说是 move：stack 上的 String 元数据被移动到 `s2`，heap 上的文本数据不深拷贝；`s1` 随后失效，避免两个 owner 在离开 scope 时 double free 同一块 heap 内存。
- Rust 不把 `String` 的 `let s2 = s1` 称为 shallow copy 后两者都可用；语义上它是 move，旧 binding invalidated。
- `clone()` 表示显式 deep copy heap 数据：

```rust
let s1 = String::from("hello");
let s2 = s1.clone(); // s1 and s2 both valid, heap data duplicated
```

- `Copy` 用于像 `i32`、`bool`、`char`、简单 tuple 等可安全按位复制的类型。`let y = x` 后 `x` 仍可用，是因为这些类型实现了 `Copy`，不是因为它们一定都“只在 stack 上”这么简单。
- `Drop` 和 `Copy` 互斥：如果一个类型需要自定义释放资源，通常不能实现 `Copy`，否则会出现资源重复释放风险。
- 赋值给已有变量时，旧值会被 drop，然后新值进入这个 binding。例如 `s = String::from("world")` 会释放原来 `s` 拥有的 heap buffer，再让 `s` 拥有新的 String。
- `Copy` trait 的直觉：如果一个类型的值完全由固定大小、可安全按位复制的数据组成，赋值时就可以复制实际值，并且旧 binding 仍然有效。
- 常见 `Copy` 类型：integer、float、bool、char，以及所有字段都实现 `Copy` 的 tuple，例如 `(i32, i32)`；如果 tuple 包含 `String`，如 `(i32, String)`，则不能实现 `Copy`。
- 不能把规则简化为“栈上都是 deep copy，堆上都是 shallow copy”。更准确：
  - 如果类型实现 `Copy`，赋值是 implicit copy，旧 binding 继续有效。
  - 如果类型没有实现 `Copy`，赋值通常是 move，旧 binding 失效。
  - 类型是否 `Copy` 取决于语义和 trait，不只取决于值的某部分是否在 stack 上。
- `String` 的 metadata 本身是固定大小，也可以按位复制，但 `String` 拥有 heap buffer 并实现 `Drop`；如果允许它 `Copy`，两个 binding 会在离开 scope 时 double free 同一块 heap buffer。因此 Rust 让 `String` move，而不是 Copy。
- 对只包含 `i32` 这类 Copy 数据的变量，所谓 shallow/deep copy 没有实际区别，因为值本身就是全部数据，没有额外 heap resource 需要复制。
- 对 `String` 这类 non-`Copy` 类型，编译器实现层面可以把 stack 上的 metadata bytes（pointer / length / capacity）搬到新 binding；但语言语义上这叫 move，不叫产生两份可用对象。旧 binding 失效，后续不会再被当成 owner drop。
- 因此更稳的表达是：`String` 赋值不会 clone heap buffer，只会转移 ownership。它不是“两个 binding 都可用的 shallow copy”，而是“metadata 被移动，heap resource 的唯一 owner 改名/换位置”。
- 函数传参和赋值遵循同一套规则：
  - 传入 `Copy` 类型时，参数拿到一份 copy，调用方变量仍有效。
  - 传入 non-`Copy` owning 类型时，参数获得 ownership，调用方变量失效。
  - 传入 reference 时，复制的是 reference 本身，ownership 不转移；这就是后续 borrowing。
- 函数返回值也可以转移 ownership。返回 `String` 会把 ownership 移出函数；返回 `(String, usize)` 时，`String` ownership 被移出，`usize` 是 `Copy` 标量，复制/移动成本都很小。
- String literal 的类型通常是 `&'static str`，不是 `String`，也不准确说它是 scalar。它是指向静态只读字符串数据的 borrowed fat pointer（pointer + length），这个 reference 本身实现 `Copy`，所以复制它不会复制底层静态文本，也不会涉及 heap ownership。
- Ownership 可以理解成 Rust 的 RAII 资源管理模型：拥有资源的 value 到达 drop point 时，编译器插入 `drop` 调用，由类型的 `Drop` 实现释放其拥有的资源。对 `String` / `Vec<T>` 这种单 owner 类型来说，owner 被 drop 时会释放对应 heap buffer。
- “owner 被 pop 时释放 heap”是一个有用直觉，但要校准：
  - 对普通局部变量，离开 scope 时先 drop value，再回收 stack frame。
  - owner 不一定总在 stack 上，也可能作为 struct 字段、`Box<T>` 里的 value、`Vec<T>` 的元素，或被 `Arc<T>` 共享。
  - 释放不一定只发生在函数结束；显式 `drop(x)`、赋值覆盖旧值、容器删除元素时，都可能触发 drop。
  - 如果 value 被 move 走，旧位置不会再 drop；最终 owner 的 drop point 才负责释放资源。
  - 对 `Rc` / `Arc` / `Bytes` 这类共享所有权或引用计数类型，某个 owner drop 通常只是减少计数；底层 heap 数据在最后一个 owner drop 时释放。
- 因此，ownership 的核心不是“stack pop 自动 free heap”本身，而是“资源释放责任绑定在 owning value 的 drop 语义上”。Stack scope 只是最常见、最容易观察到的一种 drop 触发点。
- 大部分业务类型不需要手写 `Drop`。标准库类型如 `String` / `Vec<T>` / `Box<T>` / `File` 已经定义了释放逻辑；自定义 struct 默认会自动按字段顺序 drop 字段。只有当类型直接管理外部资源、unsafe allocation、FFI handle、临时文件、锁状态等需要自定义清理语义时，才需要手写 `impl Drop for T`。
- 如果一个 `String` 是某个 struct 的字段，struct 到达 drop point 时会递归 drop 字段；这个 `String` 字段随后释放自己拥有的 heap buffer。如果这个 struct 本身被 `Box` 放在 heap 上，`Box` drop 时会先 drop struct，再释放保存 struct 的那块 heap allocation。
- `Copy` 不是“深拷贝所有指向的数据”，而是复制这个 value 自身的表示。对 `i32` 来说 value 自身就是整数，所以复制 bits 等于复制完整值；对 `&str` / `&[u8]` 这种 reference/slice 来说，value 自身只是 pointer + length，复制它不会复制底层文本或字节。
- Copy 类型不一定物理位于 stack 上。比如 `Vec<i32>` 的 heap buffer 里存着很多 `i32`，这些元素依然是 `Copy` 类型；如果把某个 `i32` 元素读出来，复制的是这个元素值，而不是由“是否在 stack 上”决定语义。
- 大型 Copy 值会按值复制其组成部分。例如 `[i32; 10000]` 如果被按值赋值/传参，语义上会复制整个数组；编译器可能优化实际机器码，但语言层面不是共享一个隐藏 pointer。Copy 不等于永远便宜，大对象 Copy 也可能有性能成本。
- 自定义 struct 即使所有字段都是 `Copy`，也不会自动成为 `Copy`；需要显式 `#[derive(Copy, Clone)]` 或手写实现。这样做是让“这个类型可以被隐式复制”成为类型作者的显式承诺。
- Reference 是一个不拥有数据的访问路径，可以理解为受 borrow checker 约束的 pointer。reference 本身是一个 value，通常是 `Copy`，可以指向 stack value、heap value、static data 或某个 owned value 的一部分。
- `&x` 创建 shared reference，`*r` 是 dereference。很多场景下 Rust 会自动 deref/coerce，所以读代码时不总是显式看到 `*`。
- 对 `String`，`&s1` 借的是 `String` value 本身，通常可理解为指向 `s1` 的 `String` metadata；通过 metadata 再访问 heap buffer。它不是拥有 heap buffer，也不是直接把 ownership 借走。
- Borrowing 解决的是“只想临时访问，不想转移 ownership”的问题。`calculate_length(&s1)` 让函数读取 `String` 长度，而 caller 仍然保留 `s1` ownership，不需要返回 `(String, usize)`。
- Shared reference `&T` 允许多个同时存在，因为只读访问不会修改底层数据。Mutable reference `&mut T` 更准确叫 exclusive reference：同一时间同一数据只能有一个 `&mut T`，并且不能和任何 active `&T` 同时存在。
- `let mut s` 只表示 binding 本身允许被修改；如果创建了 `let r = &mut s`，在 `r` 的有效借用区间内，owner binding `s` 本身也不能被直接读写，也不能再创建其他 reference。独占性包括 owner 自己的使用。
- 可以把 `s.push_str(...)` 这类直接修改操作理解成编译器为这次操作创建了一个很短的独占访问区间；但 `mut s` 本身不是一个长期存在的隐藏 `&mut s`。独占访问是否允许，仍然由当前是否存在重叠 borrow 决定。
- Rust 的 borrow rule 类似读写锁的静态版本：多个 reader 可以共存；writer 必须独占。但它比运行时锁更基础，不只是为了多线程，也防止单线程里的 iterator invalidation、use-after-realloc、aliasing mutation 等问题。
- Data race 三条件：两个或更多 pointer/reference 同时访问同一数据；至少一个用于写；没有同步机制。Rust safe code 通过 borrowing、`Send` / `Sync`、`Mutex` / atomic 等机制让这类情况不能在未同步情况下编译通过。
- Rust 不是不能多线程，而是 safe Rust 不允许多个线程在无同步机制下共享可变数据：
  - 只读共享可以用 `Arc<T>`，前提是 `T: Sync`。
  - 共享可变状态通常用 `Arc<Mutex<T>>` / `Arc<RwLock<T>>` / atomic。
  - `Mutex<T>` 可以被多个线程同时持有引用，但同一时间只有一个线程能拿到 `MutexGuard`，从而获得对内部 `T` 的独占可变访问。
  - `Rc<T>` / `RefCell<T>` 这类单线程共享/内部可变类型不能直接跨线程共享，因为它们不满足线程安全 trait 约束。
- `Arc<T>` 的职责是线程安全的共享 ownership：它用 atomic refcount 保证多个线程 clone/drop 指针时引用计数不会 data race，并保证最后一个 owner drop 时才释放 `T`。`Arc` 不给 `T` 的内容自动加临界区，也不自动允许 mutation。
- `Arc<Mutex<T>>` 里两层职责不同：
  - `Arc`：让多个线程共同拥有同一个 `Mutex<T>`，管理生命周期。
  - `Mutex`：运行时互斥，保证同一时间只有一个 `MutexGuard` 能访问内部 `T`。
- 因此可以多个线程同时持有 `Arc<Mutex<T>>` clone，但不能多个线程同时拿到内部 `T` 的 mutable access。`Arc<T>` 只解决“共享谁、活多久”，`Mutex<T>` 才解决“谁此刻能改”。
- `Arc::clone(&x)` 不 clone 底层 `T`，只增加 atomic refcount 并产生另一个 owner handle。所有 `Arc` clone 指向同一个 allocation；最后一个 clone drop 时才 drop `T`。
- `Arc<Vec<i32>>` 适合多线程只读共享；如果需要 push，必须让内部类型提供同步，例如 `Arc<Mutex<Vec<i32>>>`。
- MiniLSM 里的 `Arc<SkipMap<Bytes, Bytes>>` 可以理解为：`Arc` 让 MemTable map 被多个 task/iterator/flush path 共享，`SkipMap` 自己提供并发插入/读取机制；它不是 `Arc` 在保护 `SkipMap` 的临界区。
- Reference 的有效区间从创建开始，到最后一次使用结束；现代 Rust 使用 non-lexical lifetimes，借用不一定持续到整个 `{}` 结束。
- Dangling reference 是指 reference 指向的数据已经被释放或离开 scope。Rust 要求 reference must always be valid：被引用的数据生命周期必须覆盖 reference 的生命周期，因此不能返回指向局部 `String` 的 `&String` / `&str`。
- Slice 是一种 reference，不拥有数据；它描述 collection 中一段连续元素。核心形式是 borrowed view：`&str` 是 string slice，`&[T]` 是 general slice。
- `first_word` 返回 `usize` 的问题是 index 和原始 `String` 状态没有绑定。`usize` 只有在对应字符串未被修改时才有意义；如果之后 `clear` 或重分配，旧 index 可能变成逻辑错误。
- String slice `&s[start..end]` 内部可以理解为 pointer + length；`end` 是 exclusive。`&s[..2]` 等价于 `&s[0..2]`，`&s[3..]` 等价于 `&s[3..s.len()]`，`&s[..]` 是整个 string slice。
- `first_word(s: &String) -> &str` 把返回值和输入借用绑定起来。只要返回的 `&str` 还会被使用，原始 `String` 就不能被 `clear()` 这类需要 `&mut self` 的方法修改。
- `clear` 例子不是严格多线程 data race，而是单线程 aliasing mutation：一边保留指向旧数据的 immutable slice，一边尝试 mutable borrow 修改原数据。Rust 用同一套 borrow rule 提前拒绝。
- Aliasing mutation 指“同一份数据有别名 alias/reference 还活着时，又通过另一路径 mutation 这份数据”。它的风险不只是多线程竞态，也包括单线程里旧 reference/slice/iterator 看到的数据被改掉、搬家或失效。
- String literal 的类型是 `&'static str`，也就是指向程序静态只读数据的一段 string slice；它不是 owned `String`。
- API 设计上优先接收 `&str` 而不是 `&String`，因为 `&str` 能同时接受 string literal、`String` 的 slice、整个 `String` 的 borrowed view，更 general。这里靠的是 deref coercion，不是 derive coercion。
- General slice 如 `&[i32]` / `&[u8]` 是对 array / Vec / Bytes 等连续内存的一段 borrowed view。`&[u8]` 在 MiniLSM 中用于表达“调用者借给我看的一段 key/value bytes，我不拥有，也不能长期保存”。
- 如果 MemTable 要长期保存 `&[u8]` 里的内容，就必须复制/转成 owned 或 shared buffer，例如 `Bytes::copy_from_slice(key)`；否则 caller 的数据离开 scope 后会变成 dangling。

## Code / System Mapping

- 目标是解释 MiniLSM 里的 `put(&self, key: &[u8], value: &[u8]) -> Result<()>`：
  - `&self`：共享借用 receiver。
  - `&[u8]`：借用的 byte slice，不拥有数据。
  - `Bytes`：后续把 borrowed data 转成 owned / shared byte buffer。
  - `SkipMap::insert(&self, ...)`：普通 `&self` 不允许直接改字段，但并发数据结构可以把安全修改机制封装在类型内部。
- MiniLSM 里 key/value 是 byte data。`key: &[u8]` / `value: &[u8]` 是借用调用者传入的数据，不拥有；如果 MemTable 要长期保存，就必须复制成 owned buffer，例如 `Bytes::copy_from_slice(key)`。
- `Bytes` 的 clone 通常不是深拷贝所有 bytes，而是引用计数式共享底层 buffer；这和 `String::clone()` 深拷贝文本内容不同，后续需要单独区分。
- `Arc<SkipMap<Bytes, Bytes>>` 说明 MemTable 内部用共享所有权和并发数据结构保存 key/value；这会连接 Ch4 后半的 references/borrowing 和 Ch15/Ch16 的 smart pointers/concurrency。
- `Arc<SkipMap<Bytes, Bytes>>` 的分层：
  - `Arc`：多个 owner 共享同一个 map，避免 map 在 iterator/flush task 还使用时被释放。
  - `SkipMap`：内部并发控制，允许通过 shared reference 做 insert/get。
  - `Bytes`：key/value 的 owned/shared byte buffer，避免 `&[u8]` borrowed data 生命周期不足。

## Session Notes / 2026-07-05 Ownership Opening

- 用户已正确抓住本章总纲：ownership 是 Rust 在无 GC 情况下保证内存安全的核心机制，后续 borrowing / slice / memory layout 都围绕它展开。
- 已校准 stack / heap 理解：
  - stack 是每个线程的调用栈内存区域，不是“寄存器本身”；寄存器里保存 stack pointer/frame pointer 等，用来高效定位 stack frame。
  - heap 是进程虚拟地址空间中由 allocator 管理的动态区域，不是“所有可访问地址”的统称。
  - heap pointer/len/capacity 这类 metadata 可以保存在 stack 上；真实可增长数据通常在 heap 上。
- 已校准 String：
  - string literal 是 `&'static str`，静态存储、不可变、编译期已知。
  - `String` 是 owned/growable UTF-8 buffer，通常 heap allocated。
  - `let s2 = s1` 是 move，不是保留两个可用 binding 的 shallow copy。
  - `clone()` 是显式复制，成本更高但语义清楚。
- 已校准 Copy：
  - 对 `i32` 等固定大小标量，`let y = x` 是复制实际值，`x` 继续有效。
  - 对 `String`，`let s2 = s1` 是 ownership transfer，`s1` 失效。
  - 判断依据不是“stack vs heap”本身，而是类型是否实现 `Copy`、是否拥有需要 `Drop` 的资源。
- 已校准 metadata copy vs semantic move：
  - 可以把 `String` move 理解成 stack metadata bytes 被搬到新 binding，heap buffer 没有被 clone。
  - 但 Rust 语义上旧 binding 立即失效，所以不是“两个对象共享同一个 heap buffer”的普通 shallow copy。
- 已展开 ownership and functions：
  - Passing a value to a function follows assignment rules: `Copy` 类型复制，non-`Copy` 类型 move。
  - Returning values can transfer ownership back to caller；如果用 tuple 返回 `(String, usize)`，就是把 ownership 和计算结果一起还回来。
  - 这解释了为什么没有 references 时，`calculate_length(s)` 需要把 `String` 再返回，否则 caller 会失去 ownership。
- 已形成 RAII / Drop 心智模型：
  - 对 `String` / `Vec<T>`，owner drop 时释放 heap buffer。
  - `drop` 更像确定性 destructor，不是普通运行时 GC callback。
  - owner 不一定在 stack 上；shared ownership 类型要等最后一个 owner drop 才释放底层资源。
- 已展开 references / borrowing / slices：
  - reference 可以指向 stack / heap / static / field / slice，不拥有数据。
  - borrowing 让函数临时访问数据，不转移 ownership。
  - `&mut T` 是 exclusive reference，活跃期间 owner 自己也不能直接访问同一数据。
  - reference lifetime 到最后一次使用结束；borrow checker 保证不会 dangling。
  - slice 是连续元素的 borrowed view；`&str` / `&[u8]` 不拥有数据，但生命周期被 borrow checker 绑定到源数据。
  - `&str` 比 `&String` 更适合作为只读字符串参数；`&[u8]` 是 storage key/value API 的自然参数。
- Ch4 first pass 已完成。下一步快速过 Ch5 structs，然后回到 MiniLSM P0-03：`Arc<SkipMap<Bytes, Bytes>>`、`Bytes::copy_from_slice`、`MemTable::put/get`。
