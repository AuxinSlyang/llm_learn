---
type: chapter_notes
project: [[systems-rust-for-storage]]
status: first_pass_done
updated: 2026-07-05
---

# Ch3 Common Programming Concepts Notes

## Materials

- [[chapter.pdf]]
- [[questions]]
- [[answers]]

## Takeaways

- 本章定位：Rust 通用语言基础，包含 variables / mutability / constants / shadowing / data types / functions / control flow。
- Rust 默认 `let` binding 不可变；需要修改同一个 binding 时必须显式写 `mut`。
- `nags` 在原文里是“编译器唠叨/提醒”的意思：Rust 会用编译期错误逼你把“哪些值应该可变”表达清楚。
- `const` 不是“默认不可变变量”，而是永远不可变的常量：必须标注类型，值必须是编译期可计算表达式，命名惯例是全大写加下划线。
- `shadowing` 是用同名 `let` 创建一个新 binding，新的 binding 遮住旧 binding；它不是原地修改旧变量。
- `mut` 和 `shadowing` 的核心区别：
  - `mut`：同一个 binding 的值可以变，类型不能随便变。
  - `shadowing`：创建新 binding，可以改变值，也可以改变类型。
- Rust 是 statically typed language：编译期必须知道所有变量类型。多数情况下编译器能推断；但像 `parse()` 这种泛型返回，需要类型标注来消除歧义。
- scalar types：integer / floating-point / boolean / character。
- integer 类型同时区分 signed / unsigned 和 bit width，例如 `i32`、`u32`、`u8`。
- debug mode 下 integer overflow 会 panic；release mode 下默认可能发生 wrapping。需要明确语义时使用 `wrapping_*`、`checked_*`、`overflowing_*` 等方法。
- floating point 类型是 `f32` / `f64`，默认是 `f64`，遵循 IEEE 754。
- `bool` 只有 `true` / `false`。
- `char` 表示 Unicode scalar value，不只是 ASCII 字母；一个 `char` 不等于一个 UTF-8 byte。
- compound types 可以把多个值组合成一个类型；Rust 基础 compound types 是 tuple 和 array。
- tuple 固定长度，可以混合不同类型；空 tuple `()` 是 unit type / unit value，常用于“没有有意义返回值”。
- array 固定长度，所有元素类型相同，适合栈上固定大小数据；越界访问会 panic，而不是像 C/C++ 那样读到未定义内存。
- functions 使用 `fn` 定义；参数必须写类型；函数返回值通过 `-> Type` 标注。
- statements 不返回值，expressions 返回值；Rust 很多控制流结构都是 expression。
- control flow 包括 `if`、`loop`、`while`、`for`。`if` 分支返回值时，各分支类型必须一致。

## Code / System Mapping

- MiniLSM 里大量函数返回 `Result<()>`；这里的 `()` 就是 unit type，表示成功时没有额外返回值。
- `let mut snapshot = ...` 这类代码表示后续会修改局部变量；如果只是绑定当前 state snapshot，则默认 immutable 更安全。
- `let state = self.state.read().clone();` 这种代码里的 `state` 默认不可变，降低后续误改状态的风险。
- `let x = ...; let x = ...;` 的 shadowing 后续会在解析、类型转换、借用缩短生命周期时经常见到。
- `key: &[u8]` / `value: &[u8]` 里的 `u8` 是 unsigned 8-bit integer，也就是 byte；这和 storage engine 的 key/value bytes 直接相关。
- `Bytes` 后续可以理解为“堆上/引用计数的字节缓冲”，而 `[u8; N]` 是固定长度数组，`&[u8]` 是 slice；Ch4 会正式解释 slice。
- array 越界 panic 对应 Rust 的 memory safety 原则：宁愿运行时报错，也不允许静默读写非法内存。

## Session Notes / 2026-07-02 Late Night

- 已读到 Ch3 的 `Functions` 入口，重点完成了 variables/mutability、constants、shadowing、data types、scalar/compound types、tuple、array 的口头复述。
- 用户确认：今天不继续写 MiniLSM 代码，周五/周六继续补 Rust，周日集中写 MiniLSM。
- 下一次继续从 Ch3 `Functions` / `Control Flow` 快速收尾，然后进入 Ch4 ownership。

## Session Notes / 2026-07-05 Functions and Control Flow Review

### Overall Review

- 本轮已经完成 Ch3 第一轮学习：variables / mutability / shadowing / data types / functions / statements / expressions / return values / comments / control flow。
- 大部分内容对已有 C/C++ / 通用编程经验来说是熟悉的；真正需要在 Rust 里额外记住的是 expression-based language、末尾表达式隐式返回、`if` / `loop` 可以作为 expression、以及 Rust 对类型和边界的编译期/运行期约束更严格。

### Functions

- Rust 函数用 `fn` 定义，结构是：

```rust
fn function_name(param: Type) -> ReturnType {
    body
}
```

- 函数名和变量名惯例使用 `snake_case`。
- 参数是 function signature 的一部分。`x: i32` 的含义是：参数名是 `x`，类型是 `i32`。
- 函数参数和 `let x = ...` 一样，默认不可变。如果函数体内需要重新赋值，参数可以写成 `mut x: i32`。
- 这里的 `mut` 只表示该函数调用栈帧里的局部 binding 可变，不表示调用者传入的值被原地修改。真正修改外部数据需要 Ch4 的 mutable reference：`&mut T`。
- 函数定义本身是 item statement。它不是普通 expression，所以不能把 `fn foo() {}` 当作右值赋给变量；后续如果要传函数，可以传 function item/function pointer，这是另一个主题。

### Statements vs Expressions

- Rust 函数体由一系列 statements 组成，并且可以用一个末尾 expression 作为返回值。
- Statement：执行动作，不返回可用值。典型例子：

```rust
let y = 6;
fn another_function() {}
```

- Expression：求值后产生一个值，可以放在 `let x = ...` 的右侧。典型例子：

```rust
5 + 6
{
    let x = 3;
    x + 1
}
if condition { 5 } else { 6 }
loop { break 20; }
```

- `let x = (let y = 6);` 错误，因为 `let y = 6;` 是 statement，不是 expression。
- 分号很关键：末尾 expression 加上 `;` 会变成 statement，不再产生返回值。比如 `x + 1` 可以作为返回值，`x + 1;` 返回的是 unit `()`。

### Return Values

- Rust 函数返回类型写在 `->` 后面，例如：

```rust
fn five() -> i32 {
    5
}
```

- Rust 常见风格是用函数体最后一个 expression 隐式返回；也可以用 `return value;` 提前返回。
- `fn main()` 没有显式返回类型，默认返回 unit `()`。
- MiniLSM 里常见的 `Result<()>` 可以理解为：成功时没有额外值，失败时返回 error。

### Comments

- 单行注释使用 `//`，和 C++ 风格接近。
- 注释本身不是 Ch3 重点；后续写 MiniLSM 笔记时只在解释 non-obvious 设计时加注释，不把代码直译成注释。

### Control Flow

- `if` 是 expression，因此可以写：

```rust
let number = if condition { 5 } else { 6 };
```

- `if` condition 必须是 `bool`。Rust 不会像 C/C++ 那样把整数隐式转成 bool；需要显式写 `number != 0`。
- `if` / `else` 各 arm 如果作为 expression 返回值，类型必须一致；否则变量无法在编译期确定单一类型。
- `else if` 可以处理多个条件，但条件链太长时，后续 Ch6 的 `match` 往往更清晰。

### Loops

- Rust 有三种循环：`loop`、`while`、`for`。
- `loop` 是无限循环，直到显式 `break`。它也可以作为 expression，用 `break value` 把值返回到外层：

```rust
let result = loop {
    counter += 1;
    if counter == 10 {
        break counter * 2;
    }
};
```

- loop label 只对词法嵌套中的当前循环和外层循环有效。内层循环可以 `break 'outer` / `continue 'outer` 跳到带 label 的外层循环；不能从一个并行/兄弟循环里去 break 另一个没有包住自己的循环。
- `while` 是常见的“每轮检查条件，条件为 true 就继续”的循环，本质上可以看作 `loop + if + break` 的常用模式。
- `for element in collection` 是遍历集合的推荐方式，避免手写 index 造成越界或漏元素，也通常更简洁安全。
- `(1..4).rev()` 表示生成 `1,2,3` 的 range，再反转成 `3,2,1`；range 右端不包含 4。

### MiniLSM Mapping

- 函数签名：`pub fn put(&self, key: &[u8], value: &[u8]) -> Result<()>` 可以拆成：
  - `pub fn put`：公开方法，名字是 `put`。
  - `&self`：共享借用 receiver，Ch4 重点解释。
  - `key: &[u8]` / `value: &[u8]`：参数名 + 类型，表示借用的 byte slice。
  - `-> Result<()>`：成功时无额外返回值，失败时带 error。
- statement / expression 对 MiniLSM 有直接影响：
  - `Ok(())` 放在函数最后且无分号，表示返回成功。
  - `Ok(());` 加分号会变成 statement，函数最后返回 `()`，类型不匹配。
  - `if let Some(value) = ... { ... } else { ... }` 后续常用于处理 `Option`。
- `for` 会频繁出现在 iterator / memtable / SST 遍历中；`while` 和 `loop` 更多用于需要手工控制退出条件的场景。

## Open / Corrected Points

- 已校准：函数参数默认 immutable；需要局部重绑定时写 `mut x: T`，但这不等于修改调用者的数据。
- 已校准：function definition 是 item statement，不是普通右值 expression；不能用 `let x = fn foo() {}` 这种形式理解。
- 已校准：`loop label` 只作用于嵌套作用域内可见的 loop；不能跨到并行兄弟 loop。
- 已校准：`if` 和 `loop` 在 Rust 中可以作为 expression，但只有各分支/`break value` 类型满足要求时才能作为右值使用。
