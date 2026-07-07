---
type: chapter_index
project: [[systems-rust-for-storage]]
status: active
updated: 2026-07-05
---

# Ch5 Using Structs to Structure Related Data

## Materials

- `chapter.pdf`

## Learning Goal

- 理解 Rust 如何用 `struct` 把相关数据组织成一个类型，并用 `impl` 给这个类型挂方法 / associated functions。
- 能读懂 MiniLSM 里的 `MemTable`、`LsmStorageState`、`LsmStorageInner` 这类结构体定义、字段初始化和方法调用。

## Current Mainline Connection

- MiniLSM Day 1 直接依赖 Ch5：
  - `MemTable { map, wal, id, approximate_size }`
  - `LsmStorageState { memtable, imm_memtables, ... }`
  - `impl MemTable { create/get/put/... }`
  - `impl LsmStorageInner { get/put/delete/force_freeze_memtable/... }`
- Ch5 要解决的是“这些字段属于谁、怎么初始化、方法里的 `self` / `&self` / `&mut self` 各自意味着什么”。

## Outputs

- `notes.md`
- `questions.md`
