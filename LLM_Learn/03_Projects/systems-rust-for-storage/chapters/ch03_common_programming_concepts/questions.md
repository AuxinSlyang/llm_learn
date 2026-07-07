---
type: chapter_questions
project: [[systems-rust-for-storage]]
status: first_pass_done
updated: 2026-07-05
---

# Ch3 Common Programming Concepts Questions

## Materials

- [[chapter.pdf]]
- [[notes]]
- [[answers]]

## Questions

- [x] `nags` 在 “Rust gives you many nags” 里是什么意思？
- [x] `let x = 5` 默认 immutable，是否可以写 `let immutable x = 5`？
- [x] `mut` 和 shadowing 的区别是什么？
- [x] 为什么 shadowing 可以改变变量类型，而 `mut` 不适合这么做？
- [x] `const` 和 immutable variable 的区别是什么？
- [x] 为什么 `parse()` 有时必须写类型标注，例如 `let guess: u32 = ...`？
- [x] scalar type 和 compound type 分别是什么？
- [x] signed / unsigned integer 和 bit width 怎么理解？
- [x] integer overflow 在 debug / release 下有什么差异？
- [x] `char` 是不是 UTF-8 byte？
- [x] compound type 中文叫“复合类型”还是“组合类型”？
- [x] tuple 和 array 的区别是什么？
- [x] `()` unit type / unit value 表示什么？
- [x] Rust array 越界为什么会 panic？这和 memory safety 有什么关系？
- [x] function parameter / return type / statement / expression 怎么区分？
- [x] `if` / `loop` / `while` / `for` 在 Rust 中哪些是 expression？和 C/C++ 有什么差异？
- [x] function parameter 默认是否 immutable？如果想在函数体里改参数 binding 怎么写？
- [x] `fn` definition 能否像普通 expression 一样作为 `let x = ...` 的右值？
- [x] `break 'label` / `continue 'label` 能否跳到并行的兄弟 loop？
- [x] 为什么 `Ok(())` 和 `Ok(());` 在函数末尾语义不同？

## Follow-ups

- Ch3 第一轮已完成，后续只需要在 MiniLSM 代码里随遇随查。
- Ch4 需要重点连接 `&self`、`&[u8]`、borrow、mutable reference、slice。
- 后续 MiniLSM coding 前，需要能解释 `pub fn put(&self, key: &[u8], value: &[u8]) -> Result<()>` 每一部分的语义。
