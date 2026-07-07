---
type: project
track: Rust / systems programming / distributed KV storage
status: active
created: 2026-07-01
---

# Systems Rust for Storage

## 定位

这里是后续 Rust 学习在 `llm-learner` 工作区里的统一项目入口。

当前 Rust 学习的第一目标不是泛学语言，而是支撑我们完成分布式系统 / KV 存储相关核心代码：

- MiniLSM / LSM storage engine 代码阅读与实现。
- 后续 RocksDB / IO path / runtime / async / network / RDMA 相关系统代码理解。
- 后续分布式 KV / replicated log / tablet server / storage service 的核心路径理解。
- 更长期的 AI Infra / robot runtime 工程能力。

## 为什么放在 `03_Projects`

这不是已经精加工完成的 insight，而是一个会持续训练、复习、写代码、跑测试的主动项目。

归类规则：

- `03_Projects/systems-rust-for-storage/`：Rust 系统编程训练、旧学习继承、代码能力地图。
- `03_Projects/mini-lsm/`：MiniLSM 这个具体项目的阅读、实现、实验记录。
- `08_Insights/Systems/storage/`：从项目中提炼出来的长期机制总结，例如 WAL、MemTable、SST、IO path。
- `04_Papers/60_Systems/`：系统论文阅读。

## 迁入内容

旧 Obsidian Vault 已废弃为学习入口；已迁入当前工作区：

| 新位置 | 内容 | 当前用途 |
|---|---|---|
| `legacy-vault/Rust/2. 📘 写一个简单的猜词小游戏：Rust 初窥.md` | Rust Book 第二章猜数字游戏总结 | 复习 `Cargo`、依赖、`mut`、`String`、`Result`、`match`、`loop` |
| `legacy-vault/Learning Language/Rust/CS110L/Lec/Lec 1 Safety in System Programming.md` | CS110L 内存安全动机笔记 | 复习 C 内存问题、Rust safety 的出发点 |
| `legacy-vault/Rust/3. Common Programming Concepts/Variables and Mutability.md` | 空壳笔记 | 后续补成 MiniLSM 相关的变量/可变性复习 |
| `legacy-vault/Rust/3. Common Programming Concepts/Untitled.md` | 空壳笔记 | 暂不作为主要材料 |

## 材料入口

- 本地 Rust 教程 PDF：`/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/systems-rust-for-storage/materials/The Rust Programming Language.pdf`
- TRPL 章节学习目录：`/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/systems-rust-for-storage/chapters/`
- TRPL Ch1-Ch3 快速阅读：`/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/systems-rust-for-storage/02_TRPL_Ch1_Ch3_Quick_Read_for_MiniLSM.md`
- Arc / MiniLSM 速查笔记：`/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/systems-rust-for-storage/03_Arc_for_MiniLSM.md`
- 旧学习继承笔记：`legacy-vault/Rust/2. 📘 写一个简单的猜词小游戏：Rust 初窥.md`
- MiniLSM 关联入口：`/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/mini-lsm/`

## 今天的使用方式

2026-07-01 晚上只复习和 MiniLSM Day1 直接相关的内容：

- `let` / `mut`
- `String` / `&[u8]` / `Bytes` 的直觉对照
- `Result<T, E>` / `Option<T>`
- `match`
- `Cargo` / test workflow
- C 内存问题到 Rust ownership/safety 的动机

然后进入 MiniLSM 第一部分：

- 读 `LSM in a Week` 第一部分。
- 读 Week1 Day1 tests。
- 读 `mini-lsm-starter/src/mem_table.rs`。
- 一起完成第一部分代码。

## 核心代码能力目标

### Phase 1: MiniLSM / Single-node KV

- 能读懂并实现 `MemTable::create/get/put`。
- 能理解 `Bytes`、`&[u8]`、`Vec<u8>` 在 key/value 存储里的角色。
- 能读懂 `Arc<SkipMap<Bytes, Bytes>>` 这种 interior mutability / concurrent structure 的使用方式。
- 能写出 WAL / MemTable / immutable memtable / flush / SST 的最小链路。
- 能用 tests 反推接口行为。

### Phase 2: Storage Engine Core

- Iterator trait / merge iterator / two-way merge。
- Block builder / block iterator / SSTable builder。
- Bloom filter / key range / point lookup。
- Compaction 的输入输出与文件生命周期。
- Crash recovery：WAL + manifest。

### Phase 3: Distributed KV Readiness

- 网络请求入口：TCP / RPC handler / request decode / response encode。
- 并发模型：thread pool / async task / channel / lock scope。
- Replicated log：append / commit / apply / snapshot。
- Tablet / shard：request routing、range ownership、split / merge 的基本概念。
- Storage service observability：error handling、metrics、tracing、test harness。

## 后续规则

- 新 Rust 笔记优先放在本目录。
- 项目相关 Rust 复盘可以在项目目录写短 note，但要回链到这里。
- 不再把新学习内容写回旧 Obsidian Vault。
