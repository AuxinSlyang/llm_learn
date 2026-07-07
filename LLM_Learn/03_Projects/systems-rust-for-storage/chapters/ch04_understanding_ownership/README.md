---
type: chapter_index
project: [[systems-rust-for-storage]]
status: first_pass_done
updated: 2026-07-05
---

# Ch4 Understanding Ownership

## Materials

- `chapter.pdf`

## Learning Goal

- 建立 Rust ownership / borrowing / slice 的核心模型，用来解释 MiniLSM 里的 `&self`、`&mut self`、`&[u8]`、`Bytes`、`Arc` 以及为什么普通共享引用不能随便修改内部状态。

## Current Mainline Connection

- 直接服务 MiniLSM Day 1 的核心疑问：`SkipMap::insert(&self, ...)` 为什么共享引用也能写；`MemTable::put(&self, key: &[u8], value: &[u8])` 为什么这样设计。

## Outputs

- `notes.md`
- `questions.md`
- `answers.md`
