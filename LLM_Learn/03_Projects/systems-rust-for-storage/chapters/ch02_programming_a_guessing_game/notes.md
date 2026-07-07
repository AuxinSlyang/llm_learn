---
type: chapter_notes
project: [[systems-rust-for-storage]]
status: done
---

# Ch2 Programming a Guessing Game Notes

## Takeaways

- 本章不是为了学习猜数字游戏，而是用一个最小交互程序串起 Rust 的基本工程和语法入口。
- `let` 是变量绑定，默认 immutable；`let mut` 是可变绑定，允许后续修改同一个绑定的值。
- `&mut value` 是可变引用，表示把值借给函数，并允许函数修改它；和 `let mut` 不是同一个概念。
- `String::new()` 是类型 `String` 的关联函数，用来创建一个新的空字符串。
- `read_line(&mut guess)` 会把输入追加到 `guess` 中，不会自动覆盖旧内容；如果复用同一个 buffer，需要 `guess.clear()`，或者每轮 loop 内重新 `String::new()`。
- `Result` 表达可能失败的操作；`expect("message")` 在 `Ok(value)` 时取出 value，在 `Err(error)` 时 panic 并打印 message 与底层错误。
- `shadowing` 是同名重新绑定：`let guess: u32 = ...` 会创建新的 `guess`，遮住旧绑定；类型可以相同也可以不同。
- `match expression` / `pattern matching` 是 Rust 的模式匹配表达式；每个 `pattern => expression` 叫一个 match arm。
- `match` 可先类比为更强的 `switch case`，但它是表达式、要求穷尽匹配，并且可以通过模式解构内部值，例如 `Ok(num) => num`。

## Code / System Mapping

- `Cargo.toml [dependencies]` 引入第三方 crate；本章用 `rand`，MiniLSM 后续会用到 `bytes`、`anyhow`、`crossbeam-skiplist` 等。
- `Result` / `expect` 对应存储系统里的错误处理入口；MiniLSM 中更常见的是返回 `Result<()>` 或 `Result<T>`，而不是直接 panic。
- `match Ok(num) / Err(_)` 是后续读 `Option`、`Result`、iterator 边界、状态机代码的基础。
- `loop` / `break` / `continue` 是后续 scan、iterator、compaction 循环代码的基础控制流。
- 本章代码暴露的 buffer 复用问题可以迁移到系统直觉：读取 API 是否覆盖、追加、借用、拥有，都必须明确。

## Minimal Mental Model

```text
let mut x  = 可变绑定
&mut x     = 可变引用
Result     = Ok(value) / Err(error)
expect     = Ok 取值，Err panic
shadowing  = 重新 let 同名绑定
match      = 模式匹配表达式，带穷尽检查和解构能力
```
