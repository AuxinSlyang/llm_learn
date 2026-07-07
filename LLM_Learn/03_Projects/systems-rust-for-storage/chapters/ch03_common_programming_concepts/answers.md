---
type: chapter_answers
project: [[systems-rust-for-storage]]
status: first_pass_done
updated: 2026-07-05
---

# Ch3 Common Programming Concepts Answers

## Materials

- [[chapter.pdf]]
- [[notes]]
- [[questions]]

## Answered

### What does `nags` mean here?

`nag` 是“唠叨、反复提醒”的意思。原文说 Rust gives you many nags，意思是 Rust 编译器会经常用错误或警告提醒你把代码写得更安全、更清晰。这里不是贬义重点，而是强调 Rust 会在编译期阻止很多潜在 bug。

### Can we write `let immutable x = 5`?

不能。Rust 没有 `immutable` 关键字。默认 `let x = 5` 就是 immutable binding；只有需要可变时才写 `let mut x = 5`。

### What is the difference between `mut` and shadowing?

`mut` 修改的是同一个 binding 的值：

```rust
let mut x = 5;
x = 6;
```

shadowing 创建的是新的同名 binding：

```rust
let x = 5;
let x = x + 1;
```

所以 shadowing 能改变类型：

```rust
let spaces = "   ";
let spaces = spaces.len();
```

但 `mut` 版本不能把同一个 binding 从 `&str` 改成 `usize`。

### Why does `parse()` need type annotation?

`parse()` 是泛型函数，可能解析成很多类型，例如 `u32`、i32、f64 等。Rust 是静态类型语言，编译期必须知道最终类型；如果上下文不足，就需要写：

```rust
let guess: u32 = "42".parse().expect("not a number");
```

### What are scalar and compound types?

scalar type 表示单个值，例如 integer、float、bool、char。

compound type 把多个值组合成一个类型。中文可以叫“复合类型”，也可以叫“组合类型”；为了贴近 Rust Book 术语，笔记里统一用“复合类型”。Rust 的基础复合类型是 tuple 和 array。

### Is `char` a UTF-8 byte?

不是。Rust 的 `char` 表示 Unicode scalar value，大小是 4 bytes。UTF-8 是一种编码格式，一个 Unicode 字符编码成 UTF-8 时可能占 1 到 4 个 byte。storage 代码里的 `u8` / `&[u8]` 更接近 raw bytes，不等于 `char`。

### What is unit `()`?

`()` 既是 unit type，也是 unit value，表示没有有意义的返回值。MiniLSM 里常见：

```rust
Result<()>
```

意思是：成功时不返回额外数据；失败时返回 error。

### Why does invalid array access panic?

Rust 对 array/slice 做边界检查。越界访问会 panic，避免读写非法内存。这是 Rust memory safety 的一部分：宁愿明确失败，也不允许像 C/C++ 那样产生 undefined behavior。

### How do function parameters, return types, statements, and expressions differ?

函数参数属于 function signature，例如 `x: i32` 表示参数名 `x`、类型 `i32`。参数默认 immutable；如果只想在函数体内重绑定这个局部参数，可以写 `mut x: i32`。

返回类型写在 `->` 后面，例如：

```rust
fn add_one(x: i32) -> i32 {
    x + 1
}
```

Statement 执行动作，不返回可用值，例如 `let y = 6;`。Expression 求值产生值，例如 `5 + 6`、块表达式、`if condition { 5 } else { 6 }`。Rust 函数体可以用最后一个 expression 隐式返回；末尾 expression 不能加分号，否则会变成 statement。

### Which control-flow constructs are expressions?

`if` 是 expression，可以放在 `let` 右侧，但每个 arm 的返回类型必须一致，condition 必须是 `bool`。

`loop` 也可以是 expression，可以通过 `break value` 返回值。

`while` 和 `for` 通常作为循环 statement 使用，不用于产生业务返回值；它们主要控制重复执行。虽然 Rust 的语法体系很 expression-oriented，但日常理解上只需要记住：`if` 和 `loop + break value` 是 Ch3 最重要的可作为右值的控制流。

### Can a function definition be assigned as a normal right-hand-side expression?

不能把函数定义本身当成普通 expression 写成 `let x = fn foo() { ... };`。`fn foo() {}` 是 item statement，用来在作用域中定义一个函数。后续 Rust 可以把已定义函数名作为 function item / function pointer 传递，但那不是 Ch3 这里的重点。

### Can loop labels break sibling loops?

不能。loop label 只在词法嵌套结构中可见。内层 loop 可以 `break 'outer` 或 `continue 'outer` 操作包住它的外层 loop；不能跳到没有包住当前代码位置的并行兄弟 loop。

### Why do `Ok(())` and `Ok(());` differ at the end of a function?

没有分号的 `Ok(())` 是 expression，可以作为函数末尾隐式返回值。

加分号的 `Ok(());` 是 statement，不返回可用值；如果函数声明返回 `Result<()>`，末尾写成 `Ok(());` 通常会导致类型不匹配，因为函数体最后实际返回 unit `()`。

## Still Open / Next

- Ch3 第一轮完成。后续开放问题主要放到 Ch4：`&self`、`&mut self`、borrow、slice、`&[u8]`、`Bytes`。
- 在 MiniLSM coding 时，用真实函数签名和 `Ok(())` / `?` 运算符继续巩固 statement/expression 和 return value。
