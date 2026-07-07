---
type: project
status: active
track: distributed systems / data systems / storage
created: 2026-07-01
---

# DDIA

## 一句话定位

`Designing Data-Intensive Applications` 是后续分布式系统 / KV 存储 / 数据系统基本功的长期 side project。

它不替代 7 月主线：

```text
MiniLSM / RocksDB / IO path
-> TokaDB TabletServer data path
```

它的作用是每天补一点系统概念底座，让后续看 storage engine、replication、partitioning、transaction、stream/batch 系统时有统一语言。

## 材料入口

- 完整 PDF：`/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/ddia/materials/Designing Data-Intensive Applications.pdf`
- 章节学习目录：`/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/ddia/chapters/`

每个章节目录包含：

- `chapter.pdf`：本章 PDF
- `README.md`：本章目标和主线连接
- `notes.md`：学习笔记
- `questions.md`：问题和后续回看点

## 每天读法

- 每天 15-25 分钟。
- 只做主动阅读：读完必须写 3-5 条 takeaway 或 1 个和当前主线的连接。
- 不追求线性赶进度；优先读与当月主线相关的章节。

## 2026-07-03 校准：前几章完整阅读窗口

用户希望从今天开始把 DDIA 前几章完整看一下。执行上不把它挤成今天的新主线，而是和 `Rust for MiniLSM -> Sunday MiniLSM coding` 并行安排：

- `2026-07-03 周五`：完整读 Ch1 `Reliable, Scalable, and Maintainable Applications`，写 3-5 条系统 takeaway。
- `2026-07-04 周六`：读 Ch2 `Data Models and Query Languages` + Ch3 `Storage and Retrieval`；Ch3 是本轮重点，必须连接 LSM / SSTable / B-tree / RocksDB / MiniLSM。
- `2026-07-05 周日`：默认不继续扩 DDIA，主线回到 MiniLSM 学习与编码；只有在 MiniLSM coding 完成最低线后，才用 15-20m 补 DDIA 读后整理。

边界：DDIA 是系统语言和背景，不替代 7 月 P0 的 MiniLSM / RocksDB / TokaDB TabletServer data path。

## 7 月优先级

| 优先级 | 章节 | 为什么现在读 |
|---|---|---|
| P0 | Ch3 Storage and Retrieval | 直接对应 LSM、B-tree、SSTable、RocksDB、MiniLSM |
| P1 | Ch5 Replication | 9 月分布式存储 / replicated storage 前置 |
| P1 | Ch6 Partitioning | Tablet / shard / range ownership 前置 |
| P2 | Ch7 Transactions | MVCC、isolation、storage engine 语义前置 |
| P2 | Ch8/9 Distributed Systems / Consensus | Raft、fault model、consistency 前置 |

## 输出位置

- 每日零散 takeaway：写在 Daily Note。
- 章节级总结：写在 `notes/`。
- 高质量机制沉淀：整理后放到 `LLM_Learn/08_Insights/Systems/storage/` 或后续 distributed systems 目录。

## 不做什么

- 不把 DDIA 变成今天的主线。
- 不逐页做翻译。
- 不脱离 MiniLSM / RocksDB / TokaDB 的当月任务泛读。
