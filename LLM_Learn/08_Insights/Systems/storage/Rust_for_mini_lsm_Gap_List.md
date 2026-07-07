---
type: gap_list
track: Rust / mini-lsm / storage engine
status: active
created: 2026-07-01
project: [[mini-lsm]]
---

# Rust for mini-lsm Gap List

## 原则

只记录 mini-lsm 代码里真实遇到的 Rust 缺口，不开泛 Rust 课程。

## 旧学习继承

- 继承索引：`/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/mini-lsm/notes/Rust_Study_Inheritance_for_MiniLSM.md`
- Rust 总入口：`/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/systems-rust-for-storage/README.md`
- 分布式 KV 代码能力图：`/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/systems-rust-for-storage/01_Distributed_KV_Code_Capability_Map.md`
- 已迁入 Rust 笔记：
  - `/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/systems-rust-for-storage/legacy-vault/Rust/2. 📘 写一个简单的猜词小游戏：Rust 初窥.md`
  - `/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/systems-rust-for-storage/legacy-vault/Learning Language/Rust/CS110L/Lec/Lec 1 Safety in System Programming.md`
- 今天不是从零学 Rust，而是复习旧内容，再补 MiniLSM Day1 真实遇到的 `Bytes`、`Arc`、`SkipMap`、`AtomicUsize`、`Result`、`Option`。

## 时间预算判断

- 第 1 周：每天 20-30m，只补能完成 mini-lsm Week 1 的概念：`Bytes`、`Arc`、`AtomicUsize`、`Result`、`SkipMap`、borrow/ownership 基本报错。
- 第 2 周：每天 20-30m，补 iterator trait、range bound、trait object、锁和 shared state。
- 两周后不再单独排 Rust 学习块，Rust 只作为代码任务中的随手补洞。
- 总量预估：10-15 小时足以支撑 mini-lsm 第一轮；要形成比较舒服的系统 Rust 代码阅读能力，需要 30-40 小时分散补。

## 当前环境阻塞

- 本地 Mac：无全局 `rustc/cargo`；2026-07-02 曾临时安装隔离工具链到 `/tmp/codex-rustup` / `/tmp/codex-cargo` 用于沙盒验证。
- dev2：`cargo 1.96.1`、`rustc 1.96.1` 可用。
- dev：可用但规格较小，不作为主入口。
- dev1：GPU 机器，不作为 mini-lsm 主入口。
- 当前节奏：2026-07-03 / 2026-07-04 先补 Rust；2026-07-05 周日集中写 MiniLSM 代码。

## 缺口分类

### Ownership / Borrowing

- [ ] `&self`：shared reference receiver。需要解释为什么普通 struct 不能通过 `&self` 直接改字段。
- [ ] `&mut self`：exclusive / mutable reference。需要解释“独占”由 borrow checker 在编译期保证。
- [ ] `&[u8]`：borrowed byte slice。需要解释它不拥有 key/value 数据，不能长期存进 MemTable。
- [ ] `Bytes::copy_from_slice(key)`：需要解释为什么把 borrowed slice 复制成 owned/shared buffer。
- [ ] `SkipMap::insert(&self, ...)`：需要解释 interior mutability / concurrent data structure 与普通 `&self` 的区别。

### Iterator Trait / Trait Object

- [ ] Week 1 Day 2 前补：`Iterator` / associated type / `next()` / range scan。

### Arc / Mutex / Shared State

- [ ] `Arc<T>`：线程安全引用计数，支撑 shared ownership。
- [ ] `Mutex<T>` / `RwLock<T>`：运行时同步，与 `&mut` 的编译期独占不同。
- [ ] `Arc<RwLock<Arc<LsmStorageState>>>`：需要结合 Ch4/Ch15/Ch16 拆开理解。

### Result / Error Handling

- [ ] `Result<()>`：成功时没有返回值，失败时返回 error。
- [ ] `Result<Option<Bytes>>`：外层表示操作是否失败，内层表示 key 是否存在。
- [ ] `?` operator：周五/周六补 Ch9 时理解。

### Tests / Cargo Workflow

- [x] `cargo x copy-test --week 1 --day 1`：启用指定 week/day 测试，不切分支。
- [x] `cargo x scheck`：运行 fmt / check / nextest / clippy。
- [ ] dev2 GSSAPI 登录恢复后，在真实 repo 跑一次 Day 1 gate。

### Background Task / Channel

- 待填：

## 每次记录格式

```text
日期：
代码位置：
卡住的问题：
最小解释：
后续是否需要系统补 Rust：
```
