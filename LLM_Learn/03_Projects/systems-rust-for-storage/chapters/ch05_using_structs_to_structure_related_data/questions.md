---
type: chapter_questions
project: [[systems-rust-for-storage]]
status: active
updated: 2026-07-06
---

# Ch5 Using Structs to Structure Related Data Questions

## Questions

- [ ] Struct 和 tuple 都能组合多个值，为什么需要 struct？
- [ ] `Instantiating Structs` 是不是就是创建/初始化一个实例？
- [ ] struct 字段顺序是否重要？访问字段为什么用 `.field`？
- [ ] 为什么修改字段时整个 binding 要是 `mut`？能不能只让某个字段 mutable？
- [x] Field init shorthand 解决什么重复？
- [x] Struct update syntax `..user1` 到底 copy 还是 move？为什么可能导致 `user1` 部分失效？
- [x] Tuple struct 适合什么场景？和普通 tuple 的区别是什么？
- [x] Unit-like struct 没有字段，有什么用？
- [x] 为什么 `User` 字段用 `String` 而不是 `&str` 会牵涉 lifetime？
- [x] `Rectangle` 例子为什么从两个 loose variables 变成 tuple，再变成 struct？
- [x] `#[derive(Debug)]` 是什么？为什么 `println!("{:?}", rect)` 需要 trait？
- [x] `impl` block 是什么？它和 class method 的关系是什么？
- [x] `self` / `&self` / `&mut self` 三种 receiver 怎么选？
- [x] Method call 为什么会自动引用 / 自动解引用？
- [x] Associated function 和 method 有什么区别？为什么 constructor 常写成 `Type::new` / `MemTable::create`？
- [x] Multiple `impl` blocks 有什么意义？
- [x] MiniLSM `MemTable::create/get/put` 分别对应本章哪些概念？
- [ ] MiniLSM `LsmStorageState` 为什么是 struct，而不是 tuple 或一堆变量？

## Follow-ups

- 回 MiniLSM Day 1 前确认：
  - `MemTable::create(id) -> Self` 为什么是 associated function。
  - `get(&self, ...)` / `put(&self, ...)` 为什么 receiver 是 `&self`。
  - `LsmStorageState` clone / state pointer swap 如何依赖 struct 字段组织。
