---
type: chapter_questions
project: [[systems-rust-for-storage]]
status: first_pass_done
updated: 2026-07-05
---

# Ch4 Understanding Ownership Questions

## Materials

- [[chapter.pdf]]
- [[notes]]
- [[answers]]

## Questions

- [x] Ownership 到底解决什么问题？为什么 Rust 不需要 GC 也能管理内存？
- [x] move 是什么？为什么 `let s2 = s1` 后 `s1` 不能继续用？
- [x] clone 和 copy 的区别是什么？
- [x] stack / heap 和 ownership 有什么关系？
- [x] `String` 和 string literal 的内存位置、可变性、所有权有什么区别？
- [x] heap allocation / allocating 在 Rust Book 里具体是什么意思？
- [x] stack allocation 为什么通常比 heap allocation 快？cache 是否会改变这个结论？
- [x] Linux / 本机默认 stack 大小大概是多少？
- [x] `String` move 时 stack metadata 是 copy 还是 move？为什么旧 binding 失效？
- [x] 函数传参和返回值如何转移 ownership？
- [x] string literal `&'static str` 为什么可以 Copy？它和 `String` 有什么区别？
- [x] 可以把 ownership 理解成 owner 离开 scope 时触发 drop/free heap 的 RAII 模型吗？
- [x] 后面很多类型都需要自己定义 `Drop` 函数吗？
- [x] 如果 `String` 是 struct 字段，而且 struct 在 heap 上，生命周期怎么理解？
- [x] `Copy` 能理解成 stack 上 deep copy 吗？
- [x] `&T` shared reference 是什么？reference 可以指向 stack 吗？
- [x] borrowing 为什么能替代 tuple return ownership？
- [x] `&` 和 `*` 分别是什么？
- [x] `&mut T` mutable reference / exclusive reference 是什么？
- [x] 能把 `mut s` 理解成每次修改时临时创建一个 `&mut s` 吗？
- [x] 为什么同一有效借用区间里不能同时有一个 mutable reference 和其他 shared references？
- [x] borrow checker 在编译期到底保证了什么？
- [x] Rust 怎么解决多线程 data race？`Mutex` 是否允许多个线程共享？
- [x] `Arc` 到底是什么？它的内部模型、典型场景和不用场景是什么？
- [x] `Arc` 和 C++ 智能指针是什么关系？strong / weak pointer 怎么实现？
- [x] `Arc` 本身会保护里面的 `T` 吗？它和 `Mutex` 的职责怎么分？
- [x] `Arc` 的最小例子是什么？它和 MiniLSM 的 `Arc<SkipMap<Bytes, Bytes>>` 怎么对应？
- [x] reference 的 scope 是整个花括号吗？
- [x] dangling reference 为什么在 Rust 里不能通过编译？
- [x] slice 是什么？`&[u8]` 和 `[u8; N]` / `Vec<u8>` / `Bytes` 的区别是什么？
- [x] 为什么 `first_word` 返回 `usize` 不好，返回 `&str` 更好？
- [x] aliasing mutation 是什么？为什么单线程也会出问题？
- [x] string literal 为什么是 slice？
- [x] 为什么函数参数应该优先写 `&str` 而不是 `&String`？
- [x] 为什么 MiniLSM `put(&self, key: &[u8], value: &[u8])` 传入 borrowed bytes？
- [x] 为什么 `Bytes::copy_from_slice(key)` 要把 borrowed data 变成 owned buffer？
- [x] `SkipMap::insert(&self, ...)` 为什么共享引用也能写？它和普通 struct 的 `&self` 有什么区别？

## Follow-ups

- 读完本章后回到 MiniLSM P0-03：`SkipMap::insert(&self, ...)`。
- 需要画一个 `&self` / `&mut self` / `Mutex` / `SkipMap` 的对照表。
