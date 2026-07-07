---
type: capability_map
project: [[systems-rust-for-storage]]
track: Rust / distributed KV / storage engine
status: active
created: 2026-07-01
---

# Distributed KV Code Capability Map

## 目标

用 Rust 学习支撑真实系统代码能力，而不是停在语言语法。

核心目标：

```text
Rust basics
-> MiniLSM single-node KV
-> storage engine components
-> networked KV service
-> replicated / sharded KV readiness
```

## 代码能力分层

| 层级 | 要能写的核心代码 | Rust 关键点 | 对应项目 |
|---|---|---|---|
| L0 语言基础 | guessing game / small CLI / tests | `let mut`、`match`、`Result`、`Option`、Cargo | 旧 Rust 笔记复习 |
| L1 内存 KV | `MemTable::create/get/put/delete` | `Bytes`、`&[u8]`、`Arc`、`SkipMap`、`AtomicUsize` | MiniLSM Week1 Day1 |
| L2 Iterator | merge iterator / range scan | trait、associated type、lifetime、boxed iterator | MiniLSM Week1 |
| L3 File Format | block / SST builder / reader | binary encoding、buffer、file IO、error handling | MiniLSM Week1 |
| L4 Persistence | WAL / manifest / recovery | fsync、append log、serde、crash model | MiniLSM Week2 |
| L5 Background Work | flush / compaction thread | channel、thread、lock scope、snapshot state | MiniLSM Week2 |
| L6 Network KV | TCP/RPC request path | async or thread-per-conn、codec、handler boundary | 后续小项目 |
| L7 Replication | append log / apply / snapshot | state machine、Raft 概念、log index/term | 后续分布式 KV |
| L8 Tablet Service | shard/tablet routing and ownership | shared state、range metadata、concurrency control | TokaDB TabletServer 对照 |

## MiniLSM 当前只要求

今天只做到 L1：

- 看懂 Week1 Day1 tests 在验证什么。
- 看懂 `MemTable` 的字段设计。
- 一起完成 `create/get/put`。
- 知道 storage 层 tombstone 和 freeze 为什么会出现，但不提前深挖。

Rust quick pass 只覆盖：

- `let` / `mut`
- ownership / borrowing 的基本直觉
- `&self` / `&mut self`
- `Result<T, E>` / `Option<T>`
- `Vec<u8>` / `&[u8]` / `Bytes`
- `Arc`
- trait 的基本形状

## 后续不要跳太快

- 不在 Day1 直接学 async。
- 不在 Day1 直接学 Raft。
- 不在 Day1 直接展开 RDMA。
- 不在 Day1 直接把 MiniLSM 做成网络服务。

这些都会来，但顺序必须先把单机 storage engine 的 read/write path 打通。
