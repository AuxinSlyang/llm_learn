---
type: learning_inheritance
project: [[mini-lsm]]
track: Rust / MiniLSM / storage engine
status: active
created: 2026-07-01
---

# Rust Study Inheritance for MiniLSM

## 定位

这个文件用于把已经迁入 `llm-learner` 的 Rust 旧学习内容接入当前 `mini-lsm` 主线。

原则：

- 不重开一套 Rust 课程。
- 先复习已有笔记，再按 MiniLSM 代码遇到的问题补洞。
- Rust 学习服务于 `LSM in a Week` 的第一部分实现，而不是脱离代码泛学。

## 当前入口

- Rust 总入口：`/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/systems-rust-for-storage/README.md`
- 分布式 KV 代码能力图：`/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/systems-rust-for-storage/01_Distributed_KV_Code_Capability_Map.md`
- 迁入目录：`/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/systems-rust-for-storage/legacy-vault/`

旧 Obsidian Vault 不再作为后续学习入口。

## 迁入笔记

| 当前笔记 | 当前价值 | 复习方式 |
|---|---|---|
| `/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/systems-rust-for-storage/legacy-vault/Rust/2. 📘 写一个简单的猜词小游戏：Rust 初窥.md` | 已覆盖 `Cargo`、依赖、`mut`、`String`、`Result`、`match`、`parse`、`loop` | 今晚先快速复述，不重新做完整练习 |
| `/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/systems-rust-for-storage/legacy-vault/Learning Language/Rust/CS110L/Lec/Lec 1 Safety in System Programming.md` | 已从 C 的栈溢出/边界问题切入 Rust 的内存安全动机 | 作为 ownership / borrow 的动机材料 |
| `/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/systems-rust-for-storage/legacy-vault/Rust/3. Common Programming Concepts/Variables and Mutability.md` | 当前文件基本为空 | 需要后续补成 MiniLSM 相关的 `let` / `mut` / shadowing 复习 |
| `/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/systems-rust-for-storage/legacy-vault/Rust/3. Common Programming Concepts/Untitled.md` | 当前文件基本为空 | 暂不作为主要材料 |

## 已经学过，可以直接复习的 Rust 点

- `Cargo.toml` / crate / 依赖版本。
- `let` 与 `let mut`。
- `String::new()`、`read_line(&mut guess)`、`trim()`、`parse()`。
- `Result<T, E>` 的 `Ok` / `Err`。
- `match` 对 enum / Result 的穷尽匹配。
- `loop` / `continue` / `break`。
- 为什么 Rust 关注内存安全：C 中栈上 buffer overflow、边界检查缺失、临时变量生命周期。

## MiniLSM Day1 需要补的 Rust 点

下午读第一部分时只观察，不提前实现：

- `Bytes`：为什么 key/value 存成 `Bytes`，和 `&[u8]` / `Vec<u8>` 的关系是什么。
- `Arc<SkipMap<Bytes, Bytes>>`：为什么 `MemTable::put` 可以用 `&self` 写入。
- `AtomicUsize`：为什么 approximate size 不用普通 `usize`。
- `anyhow::Result<()>`：为什么 `put` 即使现在不失败也返回 `Result`。
- `Option<Bytes>`：为什么 `get` 用 `None` 表示没找到。

今晚一起完成代码时再落到实现：

- `MemTable::create`
- `MemTable::get`
- `MemTable::put`
- storage 层如何用空 value 表示 tombstone
- freeze 后为什么 immutable memtables 要按最新到最旧读取

## 今日节奏

下午：

- 读 `LSM in a Week` 第一部分。
- 对照 Week1 Day1 tests，只确认测试在问什么。
- 只记录卡住的 Rust 概念，不提前写实现。

晚上：

- 复习旧 Rust 笔记中和 MiniLSM 相关的部分。
- 一起读 MiniLSM 第一部分。
- 一起完成第一部分 MiniLSM 代码。
- 回看 DeepSeek-V2，重点仍是 `MLA / DeepSeekMoE / KVCache efficiency`。

## 后续记录规则

每次遇到 Rust 问题，先判断来源：

```text
问题：
来自旧笔记已学内容，还是 MiniLSM 新缺口：
最小解释：
代码位置：
是否需要单独补 Rust：
```
