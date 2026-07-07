---
type: chapter_notes
project: [[systems-rust-for-storage]]
status: active
updated: 2026-07-06
---

# Ch5 Using Structs to Structure Related Data Notes

## Materials

- [[chapter.pdf]]
- [[questions]]

## Takeaways

- Ch5 的核心问题：当多个值天然属于同一个概念时，用 `struct` 把它们组织成一个自定义类型。
- `struct` 是数据布局 / 字段集合；`impl` 是给这个类型定义行为。
- Rust 方法常见 receiver：
  - `self`：拿走 ownership。
  - `&self`：shared borrow，只读或依赖内部同步的读写。
  - `&mut self`：exclusive borrow，允许直接修改字段。
- Associated function 是定义在 `impl Type` 里的函数，但没有 `self` receiver；常用于 constructor，例如 `String::from` / `MemTable::create`。
- Method call 会使用 auto-referencing / auto-dereferencing。比如 `arc_state.read()` 能工作，是因为 `Arc<T>` 实现 `Deref<Target = T>`；这里是 `Deref`，不是 `derive`。
- Struct update syntax `..other` 会 move non-`Copy` 字段；要注意部分 move 后原对象是否还能使用。
- Tuple struct / unit-like struct 是特殊 struct 形式，系统代码中常用于 newtype wrapper、marker type、zero-sized type。
- Field init shorthand：当局部变量名和 struct 字段名完全相同时，可以把 `field: field` 简写成 `field`。这只是语法糖，不改变 ownership / move / copy 语义。
- Struct 字段默认最好持有自己的数据，例如 `String`；如果字段存 `&str` 这种引用，就需要 lifetime 来证明被引用数据至少和 struct 一样活得久。

## Code / System Mapping

- MiniLSM `MemTable`：

```rust
pub struct MemTable {
    map: Arc<SkipMap<Bytes, Bytes>>,
    wal: Option<Wal>,
    id: usize,
    approximate_size: Arc<AtomicUsize>,
}
```

  - 这是 Ch5 struct 的直接例子：把 map、WAL、id、size counter 组织成一个 MemTable 概念。
  - `MemTable::create(id)` 是 associated function / constructor。
  - `get(&self, key: &[u8])` 用 shared borrow，因为 `SkipMap` 内部支持并发读写。
  - `put(&self, key: &[u8], value: &[u8])` 也用 `&self`，不是因为普通 struct 可随便改，而是因为字段类型 `SkipMap` / `AtomicUsize` 封装了内部并发 mutation。
- MiniLSM `LsmStorageState`：
  - state struct 表示 engine 当前状态快照。
  - `Arc<LsmStorageState>` 让 reader 拿到稳定 snapshot。
  - freeze 时 clone old state value，构造 new state，再用新的 `Arc<State>` 替换全局 state pointer。

## First-Pass Reading Plan

1. Defining and Instantiating Structs：字段、实例化、field init shorthand、struct update syntax。
2. Tuple Structs / Unit-Like Structs：知道存在即可，重点看 newtype 直觉。
3. Example Program Using Structs：从 loose variables 到 `Rectangle` struct，理解“把相关数据绑成类型”。
4. Method Syntax：重点。`impl`、`&self`、`&mut self`、`self`、associated functions、multiple impl blocks。
5. MiniLSM Mapping：回到 `MemTable::create/get/put` 和 `LsmStorageInner::get/put/delete`。

## Section Notes

### 2. Field Init Shorthand

问题：constructor / builder 函数里经常有参数名和字段名相同的重复代码。

普通写法：

```rust
fn build_user(email: String, username: String) -> User {
    User {
        active: true,
        username: username,
        email: email,
        sign_in_count: 1,
    }
}
```

简写：

```rust
fn build_user(email: String, username: String) -> User {
    User {
        active: true,
        username,
        email,
        sign_in_count: 1,
    }
}
```

这里 `username` 等价于 `username: username`，`email` 等价于 `email: email`。字段名和局部变量名必须完全一致。

Ownership 影响：

- `email: String` / `username: String` 是 non-`Copy` owning value。
- 写进 `User { email, username, ... }` 后，参数里的 `email` / `username` 被 move 进 struct。
- shorthand 只是少写一遍名字，不会 clone，也不会改变 move 语义。

MiniLSM 映射：

```rust
pub fn create(id: usize) -> Self {
    Self {
        map: Arc::new(SkipMap::new()),
        wal: None,
        id,
        approximate_size: Arc::new(AtomicUsize::new(0)),
    }
}
```

这里的 `id,` 就是 field init shorthand，等价于：

```rust
id: id,
```

`id: usize` 是 `Copy` 类型，所以这里复制/移动都很便宜；对 `String` / `Arc<T>` 这类 non-`Copy` 类型，shorthand 同样会按正常规则 move 对应变量。

### 3. Struct Update Syntax

问题：创建一个新 struct 实例时，大多数字段和已有实例相同，只想改其中几个字段。

不用 update syntax：

```rust
let user2 = User {
    active: user1.active,
    username: user1.username,
    email: String::from("another@example.com"),
    sign_in_count: user1.sign_in_count,
};
```

使用 update syntax：

```rust
let user2 = User {
    email: String::from("another@example.com"),
    ..user1
};
```

`..user1` 必须放在最后，意思是：没有显式设置的字段，从 `user1` 对应字段取值。

Ownership 影响：

- Struct update syntax 像 assignment 一样，会对字段执行 copy 或 move。
- `active: bool` / `sign_in_count: u64` 是 `Copy`，所以复制后 `user1` 的这些字段仍可用。
- `username: String` 是 non-`Copy`，如果被 `..user1` 带到 `user2`，就是 move，`user1.username` 失效。
- 因为 `user1` 被部分 move，之后不能再把 `user1` 当作完整 struct 使用。
- 但没有被 move 的字段仍可单独使用，例如这个例子里 `user1.email` 没有被 move，因为 `user2` 显式给了新的 email。

如果显式给 `user2` 同时提供新的 `email` 和 `username`，那么 `..user1` 只会使用 `active` 和 `sign_in_count` 这两个 `Copy` 字段，`user1` 仍可继续作为完整值使用。

MiniLSM 映射：

```rust
let mut snapshot = state.as_ref().clone();
snapshot.imm_memtables.insert(0, snapshot.memtable.clone());
snapshot.memtable = Arc::new(MemTable::create(next_id));
```

这里没有直接用 `..old_state`，但思想接近：基于旧 state 构造新 state，只替换部分字段。对于包含 `Arc<MemTable>` / `Vec<Arc<MemTable>>` 的 state，必须清楚每个字段是 clone handle、move field，还是 deep copy。

后续如果看到类似：

```rust
LsmStorageState {
    memtable: Arc::new(MemTable::create(next_id)),
    ..old_state
}
```

就要立刻检查 `old_state` 里哪些 non-`Copy` 字段被 move 了，旧 state 是否还能使用。

更完整的规则：

- `..base` 只能用于同一个 struct 类型。
- `..base` 必须放在 struct literal 的最后。
- 显式写出的字段使用显式值。
- 没写出的字段从 `base` 里逐字段取。
- 每个字段按普通赋值规则处理：`Copy` 就复制，non-`Copy` 就 move。

Partial move 例子：

```rust
let user2 = User {
    email: String::from("new@example.com"),
    ..user1
};
```

这里 `user1.username` 被 move 到 `user2.username`，但 `user1.email` 没有被 move。结果：

```rust
// user1 as whole: not usable
// user1.username: not usable
// user1.email: usable
```

如果字段是 `Arc<T>`：

```rust
struct TableState {
    memtable: Arc<MemTable>,
    size: usize,
}

let s2 = TableState {
    size: 10,
    ..s1
};
```

这里 `s1.memtable` 会被 move 到 `s2.memtable`，不是 `Arc::clone`。如果希望两个 state 都持有同一个 memtable，需要显式 clone：

```rust
let s2 = TableState {
    memtable: Arc::clone(&s1.memtable),
    size: 10,
};
```

这就是为什么 MiniLSM 的 copy-on-write state 更常见写成：

```rust
let mut snapshot = old_state.clone();
snapshot.memtable = Arc::new(MemTable::create(next_id));
```

这里要求 `LsmStorageState: Clone`。clone state 时：

- `Arc<MemTable>` 字段 clone：只增加 memtable strong count，不深拷贝 MemTable。
- `Vec<Arc<MemTable>>` clone：复制一个新的 Vec 容器，并 clone 每个 Arc handle；不深拷贝每个 MemTable。
- 然后再替换 `snapshot.memtable`，得到一个新的 state value。

这种方式比 `..old_state` 更显式地表达：我要保留旧 state 可用，同时构造一个新 state。

### 4. Creating Different Types with Tuple Structs

Tuple struct 是“长得像 tuple 的 struct”：

```rust
struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

fn main() {
    let black = Color(0, 0, 0);
    let origin = Point(0, 0, 0);
}
```

它没有字段名，只有字段类型；但它有一个类型名。这个类型名非常重要，因为 `Color(i32, i32, i32)` 和 `Point(i32, i32, i32)` 虽然内部布局一样，语义上却是两个完全不同的类型。

核心作用：

- 给一组 tuple 数据一个领域名字。
- 让同样底层形状的数据变成不同类型，避免误传。
- 当字段名会显得啰嗦或重复时，比普通 named-field struct 更轻量。

普通 tuple：

```rust
let color = (0, 0, 0);
let point = (0, 0, 0);
```

这两个值类型都是 `(i32, i32, i32)`，函数不容易区分它们到底是 RGB 颜色还是坐标点。

Tuple struct：

```rust
fn draw_color(color: Color) {}

draw_color(black);  // ok
draw_color(origin); // compile error: Point is not Color
```

访问字段和 tuple 类似：

```rust
let r = black.0;
let g = black.1;
let b = black.2;
```

也可以 destructure，但要写类型名：

```rust
let Point(x, y, z) = origin;
```

教学理解：

```text
普通 tuple = 只有形状，没有领域语义。
tuple struct = tuple 形状 + 一个新的类型名字。
```

系统代码里经常用 tuple struct 做 newtype wrapper：

```rust
struct TableId(usize);
struct LogOffset(u64);
struct BytesLen(usize);
```

这样 `TableId(1)` 和 `BytesLen(1)` 就不会因为底层都是整数而被随便混用。这对 storage / OS / distributed system 很有价值，因为系统代码里有大量 `usize` / `u64`，但它们代表的含义完全不同。

MiniLSM 映射：

当前 MiniLSM 代码里很多地方直接用 `usize` 表示 id / size / index。学习阶段这样可以；如果系统继续长大，可以考虑用 tuple struct 把不同含义区分出来：

```rust
struct SstId(usize);
struct MemTableId(usize);
```

这样函数签名会更能表达语义，也能减少把不同 id 传错的风险。

### 5. Defining Unit-Like Structs

Unit-like struct 是没有任何字段的 struct：

```rust
struct AlwaysEqual;

fn main() {
    let subject = AlwaysEqual;
}
```

它像 `()` 这个 unit type，所以叫 unit-like。定义时只有：

```rust
struct TypeName;
```

没有 `{}`，也没有 `()`。

核心作用不是存数据，而是提供一个“类型身份”。它常见用途：

- 给某个没有状态的对象实现 trait。
- 做 marker type。
- 表示某种策略、模式、能力开关。
- 做测试替身或占位类型。

比如后续学 trait 后，可以有：

```rust
trait Comparator {
    fn compare(&self, a: &[u8], b: &[u8]) -> std::cmp::Ordering;
}

struct BytewiseComparator;

impl Comparator for BytewiseComparator {
    fn compare(&self, a: &[u8], b: &[u8]) -> std::cmp::Ordering {
        a.cmp(b)
    }
}
```

`BytewiseComparator` 本身不需要存任何字段，因为比较逻辑完全由类型和实现决定。这个类型只是一个“行为载体”。

教学理解：

```text
named-field struct = 有名字的字段集合。
tuple struct = 有类型名的 tuple。
unit-like struct = 只有类型名，没有数据。
```

MiniLSM 映射：

后续 storage 系统里可能会出现没有状态的策略对象，例如：

```rust
struct NoCompression;
struct LeveledCompaction;
struct BytewiseComparator;
```

如果这些类型的行为不依赖内部字段，就可以是 unit-like struct。

### 6. Ownership of Struct Data

这一节解释为什么前面的 `User` struct 用的是 `String`：

```rust
struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}
```

而不是：

```rust
struct User {
    active: bool,
    username: &str,
    email: &str,
    sign_in_count: u64,
}
```

核心原因：

```text
如果 struct 拥有字段数据，那么只要 struct 活着，字段数据就一定活着。
如果 struct 只保存引用，那么必须证明被引用的数据活得比 struct 更久。
```

`String` 是 owned data。`User` 拥有 `username` 和 `email`，所以 `User` 的生命周期自然覆盖这些字段：

```rust
let user = User {
    active: true,
    username: String::from("someusername123"),
    email: String::from("someone@example.com"),
    sign_in_count: 1,
};
```

这个模型简单、独立、稳定：`user` 活着，里面的 `String` 就活着；`user` drop，里面的 `String` 一起 drop。

`&str` 是 borrowed data。struct 里如果保存 `&str`，就意味着 `User` 不拥有 username/email，只是借用外面的字符串。那编译器必须知道：

```text
被 User 引用的字符串，是否至少和 User 一样长寿？
```

这就需要 lifetime：

```rust
struct User<'a> {
    active: bool,
    username: &'a str,
    email: &'a str,
    sign_in_count: u64,
}
```

Ch5 先不展开 lifetime，Rust Book 把它放到后面讲。当前阶段的经验法则：

- 如果 struct 应该独立拥有数据，用 owned type：`String`、`Vec<T>`、`Bytes`、`Arc<T>`。
- 如果 struct 只是临时视图或借用窗口，才考虑引用字段：`&str`、`&[u8]`、`&T`。
- 一旦 struct 字段里出现引用，通常就会牵涉 lifetime 参数。

MiniLSM 映射：

MiniLSM 的长期结构通常不会在核心 state 里保存裸引用，而是保存 owned / shared-owned 数据：

```rust
pub struct MemTable {
    map: Arc<SkipMap<Bytes, Bytes>>,
    wal: Option<Wal>,
    id: usize,
    approximate_size: Arc<AtomicUsize>,
}
```

这里：

- `Bytes` 是拥有或共享底层字节数据的类型，不是临时 `&[u8]`。
- `Arc<SkipMap<...>>` 是 shared ownership，保证并发 reader/writer 还在使用时 map 不会被释放。
- `Option<Wal>` 表示这个 struct 自己管理 WAL 是否存在。

这和 Ch5 的 `String` 选择是一脉相承的：核心存储结构要有清晰 ownership，不应该轻易把生命周期依赖散落到外部。

### 7. An Example Program Using Structs

这一节用 rectangle 面积计算做一个渐进式重构。核心不是复杂语法，而是建立一个工程直觉：

```text
当几个变量天然描述同一个概念时，应该把它们组织成一个类型。
```

#### 7.1 Separate Variables

最开始写法：

```rust
fn main() {
    let width1 = 30;
    let height1 = 50;

    println!(
        "The area of the rectangle is {} square pixels.",
        area(width1, height1)
    );
}

fn area(width: u32, height: u32) -> u32 {
    width * height
}
```

这能工作，但有两个问题：

- `width1` 和 `height1` 在类型上没有被绑定成一个整体。
- `area(width, height)` 的签名看不出这两个参数共同描述同一个 rectangle。

也就是说，代码知道有两个 `u32`，但类型系统不知道这两个 `u32` 属于同一个领域对象。

#### 7.2 Refactoring with Tuples

进一步可以用 tuple：

```rust
fn main() {
    let rect1 = (30, 50);

    println!(
        "The area of the rectangle is {} square pixels.",
        area(rect1)
    );
}

fn area(dimensions: (u32, u32)) -> u32 {
    dimensions.0 * dimensions.1
}
```

这比散变量好，因为 `width` 和 `height` 被组合成了一个参数。但 tuple 仍然有问题：

- `dimensions.0` / `dimensions.1` 没有名字。
- 调用者和维护者需要记住第 0 个是 width，第 1 个是 height。
- 如果字段变多，可读性会迅速下降。

教学理解：

```text
tuple 能把数据绑在一起，但不能解释每个位置的语义。
```

#### 7.3 Refactoring with Structs

更好的版本是定义 `Rectangle`：

```rust
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!(
        "The area of the rectangle is {} square pixels.",
        area(&rect1)
    );
}

fn area(rectangle: &Rectangle) -> u32 {
    rectangle.width * rectangle.height
}
```

这里的改进是：

- `Rectangle` 成为一个明确的领域类型。
- `width` / `height` 有字段名，不再依赖 tuple index。
- `area` 的签名变成 `area(rectangle: &Rectangle)`，表达的是“计算一个 rectangle 的面积”。
- 传 `&Rectangle` 是借用，不转移 ownership；调用 `area` 后 `rect1` 还可以继续使用。

这一节目前还没有把 `area` 变成 method，所以还是：

```rust
area(&rect1)
```

下一节 `Method Syntax` 会继续改成：

```rust
rect1.area()
```

所以这里是 method syntax 的铺垫：先让数据形成一个类型，再把相关行为放到 `impl Rectangle` 里。

#### 7.4 Adding Useful Functionality with Derived Traits

如果直接打印：

```rust
println!("rect1 is {}", rect1);
```

会失败，因为 Rust 不知道如何用普通 display 格式打印 `Rectangle`。

调试时可以用 `Debug` trait：

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!("rect1 is {:?}", rect1);
    println!("rect1 is {:#?}", rect1);
}
```

`#[derive(Debug)]` 的意思是：让编译器帮这个 struct 自动生成 `Debug` trait 的实现。这样 `{:?}` / `{:#?}` 才能打印它。

也可以用 `dbg!`：

```rust
dbg!(&rect1);
```

`dbg!` 会打印表达式的文件、行号和值，并返回表达式的 ownership。为了避免把 `rect1` move 进去，通常调试时传引用 `&rect1`。

教学理解：

```text
struct 让数据结构清楚。
derive(Debug) 让调试输出方便。
impl/method syntax 会让行为归属更清楚。
```

MiniLSM 映射：

`MemTable` 就是这一节思想的系统版：

```rust
pub struct MemTable {
    map: Arc<SkipMap<Bytes, Bytes>>,
    wal: Option<Wal>,
    id: usize,
    approximate_size: Arc<AtomicUsize>,
}
```

如果没有 struct，代码里会到处传 `map`、`wal`、`id`、`approximate_size`，函数签名会很脏，也很难看出这些值共同构成一个 memtable。

有了 `MemTable` 之后，下一步自然是把行为放到 `impl MemTable`：

```rust
impl MemTable {
    pub fn create(id: usize) -> Self { ... }
    pub fn get(&self, key: &[u8]) -> Option<Bytes> { ... }
    pub fn put(&self, key: &[u8], value: &[u8]) -> Result<()> { ... }
}
```

这就是 Rust 里接近 class 体验的地方：

```text
struct 定义数据。
impl 定义行为。
trait 定义可共享的接口/能力。
```

### 8. Method Syntax

这一节是 Ch5 的重点。前面 `Rectangle` 已经把相关数据组织成了一个 struct；这一节开始把和 `Rectangle` 强相关的函数放回 `Rectangle` 自己的 `impl` block 里。

函数版本：

```rust
fn area(rectangle: &Rectangle) -> u32 {
    rectangle.width * rectangle.height
}

area(&rect1);
```

方法版本：

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!(
        "The area of the rectangle is {} square pixels.",
        rect1.area()
    );
}
```

核心变化：

```text
area(&rect1)  ->  rect1.area()
```

这不是能力变了，而是组织方式变了：`area` 被定义在 `impl Rectangle` 里，表示它是和 `Rectangle` 类型关联的行为。

#### 8.1 impl Block

`impl Rectangle { ... }` 表示：

```text
这里面定义的函数都和 Rectangle 类型关联。
```

`impl` 不是创建对象，也不是继承；它只是给某个类型添加方法 / associated functions。

Rust 里接近 class 的组合是：

```text
struct = data fields
impl = methods / associated functions
trait = shared interface / capability
```

#### 8.2 self / &self / &mut self

方法的第一个参数必须和接收者相关，通常写成：

```rust
fn area(&self) -> u32
```

这里的：

```rust
&self
```

是下面写法的缩写：

```rust
self: &Self
```

在 `impl Rectangle` 里，`Self` 就是 `Rectangle` 的别名，所以也等价于：

```rust
self: &Rectangle
```

常见 receiver 有三种：

```rust
fn read(&self)          // shared borrow，只读或内部同步
fn write(&mut self)     // exclusive borrow，可直接修改字段
fn consume(self)        // take ownership，消费整个对象
```

本节 `area(&self)` 用 shared borrow，因为计算面积只需要读 `width` 和 `height`，不需要修改，也不需要拿走 ownership。

如果方法要修改当前对象，用：

```rust
fn set_width(&mut self, width: u32) {
    self.width = width;
}
```

如果方法要把当前对象转化成另一个对象，并且不希望调用者继续使用原对象，才会用：

```rust
fn into_tuple(self) -> (u32, u32) {
    (self.width, self.height)
}
```

拿 `self` ownership 的方法相对少见，常见于 `into_xxx` 这类转换。

#### 8.3 为什么用 method 而不是普通 function

主要原因是组织性：

```text
所有围绕 Rectangle 实例能做的事情，都放在 impl Rectangle 里。
```

这样使用者不需要在库里到处找 `area(rectangle)`、`can_hold(rectangle, other)` 这些自由函数，而是可以直接看 `Rectangle` 的 `impl`。

这也是系统代码里 `MemTable::create`、`memtable.get`、`memtable.put` 更清楚的原因：行为贴着类型走。

#### 8.4 Method 和 Field 可以同名

Rust 允许 method 和 field 同名：

```rust
impl Rectangle {
    fn width(&self) -> bool {
        self.width > 0
    }
}

if rect1.width() {
    println!("width is {}", rect1.width);
}
```

区分方式：

```text
rect1.width    -> field
rect1.width()  -> method call
```

很多语言会自动生成 getter，Rust 不会自动给 struct field 生成 getter。后续学到 `pub` / private 时，会看到一种常见写法：字段私有，方法公开，外部只能通过 getter 读。

#### 8.5 Rust 没有 C/C++ 的 -> Operator

C/C++ 里对象和指针调用方法有两种写法：

```cpp
object.method()
ptr->method()
```

Rust 没有 `->`。Rust 方法调用会做 automatic referencing and dereferencing：

```rust
p1.distance(&p2);
(&p1).distance(&p2);
```

上面两个在方法调用场景里可以等价。Rust 会根据 method receiver 自动补 `&`、`&mut` 或 `*`，让调用对象匹配方法签名。

这是为什么下面这种写法能自然工作：

```rust
rect1.area()
```

即使 `area` 的签名是：

```rust
fn area(&self) -> u32
```

Rust 会自动把它理解成对 `rect1` 做 shared borrow。

这也能帮助理解之前的 MiniLSM / Arc 代码：

```rust
self.state.read()
```

`self.state` 类型是：

```rust
Arc<RwLock<Arc<LsmStorageState>>>
```

`.read()` 实际是 `RwLock` 的方法，不是 `Arc` 的方法。Rust 能调用成功，是因为 `Arc<T>` 实现了 `Deref<Target = T>`，method call 会自动 deref 到内部的 `RwLock` 再调用 `read()`。

关键校准：

```text
这是 Deref / auto-deref，不是 derive。
```

#### 8.6 Methods with More Parameters

方法除了 `self` receiver 之外，也可以有其他参数：

```rust
impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```

调用：

```rust
rect1.can_hold(&rect2);
rect1.can_hold(&rect3);
```

这里：

- `self` 是 `rect1` 的 shared borrow。
- `other: &Rectangle` 是另一个 rectangle 的 shared borrow。
- 返回 `bool` 表示 `rect1` 是否能容纳 `other`。

为什么 `other` 也传 `&Rectangle`？

```text
因为只需要读 rect2/rect3，不需要拿走 ownership。
```

#### 8.7 Associated Functions

所有定义在 `impl` block 里的函数都叫 associated functions，因为它们和某个类型关联。

其中，有 `self` 参数的是 method：

```rust
fn area(&self) -> u32
```

没有 `self` 参数的，不是 method，但仍然是 associated function：

```rust
impl Rectangle {
    fn square(size: u32) -> Self {
        Self {
            width: size,
            height: size,
        }
    }
}
```

调用方式：

```rust
let sq = Rectangle::square(3);
```

`Self` 在这里等价于 `Rectangle`，所以也可以写成：

```rust
fn square(size: u32) -> Rectangle {
    Rectangle {
        width: size,
        height: size,
    }
}
```

但 `Self` 更适合在 `impl` 里使用，因为它表达“当前 impl 的类型”。

Associated function 常用于 constructor：

```rust
String::from("hello")
Rectangle::square(3)
MemTable::create(id)
```

注意：`new` 不是 Rust 关键字，也不是语言内置构造器。只是社区习惯常把 constructor 命名为 `new`。

和 C++ 类比：

```text
Rust associated function ≈ C++ static member function
```

它和类型关联，但不和某个具体实例绑定。因此它不接收 `self`，也不通过 `value.method()` 调用，而是通过类型命名空间调用：

```rust
let sq = Rectangle::square(3);
```

Rust 没有特殊的构造函数语法。构造对象通常就是普通 associated function 返回 `Self`：

```rust
impl Rectangle {
    fn new(width: u32, height: u32) -> Self {
        Self { width, height }
    }
}
```

这比“构造函数必须是某种特殊语法”更灵活，因为构造函数也可以返回失败：

```rust
impl Wal {
    fn create(path: impl AsRef<std::path::Path>) -> std::io::Result<Self> {
        // open file, create directory, recover state...
        todo!()
    }
}
```

所以系统代码里常见命名：

```text
Type::new(...) -> Self
Type::create(...) -> Result<Self>
Type::open(...) -> Result<Self>
Type::load(...) -> Result<Self>
```

教学理解：

```text
Constructor 不是 Rust 的特殊语言结构；
constructor 只是 associated function 的一种常见用途。
```

#### 8.8 Multiple impl Blocks

一个类型可以有多个 `impl` block：

```rust
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```

在当前例子里没有必要拆开，但语法允许。后面学泛型和 trait 时，多 `impl` block 会很有用，例如：

- 普通方法一个 `impl`。
- 带 trait bound 的方法另一个 `impl`。
- 针对某个 trait 的实现又是一个 `impl Trait for Type`。

#### 8.9 MiniLSM Mapping

MiniLSM 里的 `MemTable` 正是这一节的系统代码版本：

```rust
impl MemTable {
    pub fn create(id: usize) -> Self { ... }

    pub fn get(&self, key: &[u8]) -> Option<Bytes> { ... }

    pub fn put(&self, key: &[u8], value: &[u8]) -> Result<()> { ... }
}
```

对应关系：

- `MemTable::create(id)`：associated function / constructor，没有 `self`，创建一个新实例。
- `memtable.get(key)`：method，`&self` receiver，只读查找。
- `memtable.put(key, value)`：method，表面是 `&self`，但通过 `SkipMap` / `AtomicUsize` 做内部并发 mutation。

所以 Ch5 method syntax 是后续读 MiniLSM 的基础：

```text
看到 Type::xxx(...)，先判断是不是 associated function。
看到 value.xxx(...)，先判断 receiver 是 self / &self / &mut self。
看到 Arc<T>.xxx(...)，要想到可能发生了 auto-deref。
```
