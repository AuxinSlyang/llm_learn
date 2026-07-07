---
type: project
status: active
track: LSM / RocksDB / TokaDB TabletServer / AI Core Storage
created: 2026-07-01
code_repo_dev2: ~/workspace/learn/mini-lsm
local_notes: /Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/mini-lsm
---

# mini-lsm

## 一句话定位

这是 2026-07 storage 主线的第一个代码项目：

```text
mini-lsm / LSM 机制
-> RocksDB 生产实现对照
-> TokaDB TabletServer 数据链路 / 线程模型 / IO 模型
-> 后续 AI Core Storage / KVCache / 推理系统
```

项目目标不是把 toy engine 当成最终作品，而是用它把 LSM 的核心机制写清楚，再回到 TokaDB / RocksDB 的真实系统边界。

## 本地与远端分工

| 位置 | 用途 | 当前状态 |
|---|---|---|
| 本地 Mac / Obsidian | 阅读、计划、笔记、链路图、复盘 | 使用本目录作为项目控制台 |
| dev2 `~/workspace/learn/mini-lsm` | 代码阅读、编译、测试、后续实现 | 已 clone 官方 repo，当前 head `427c6cc`，Rust / cargo baseline 可用 |
| `LLM_Learn/08_Insights/Systems/storage/` | 长期可复用系统笔记 | 放 TinyLSM / IO path / RocksDB / TabletServer 的结构化产出 |

本地 Mac 当前没有 `rustc/cargo`，所以第一阶段不在 Mac 本地编译。若后续需要本地 IDE 体验，再单独安装 Rust toolchain。

## 材料入口

- 本地 MiniLSM PDF：`/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/mini-lsm/materials/LSM in a Week.pdf`
- 单章 PDF 索引：`/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/mini-lsm/chapters/README.md`
- 官方网页：`https://skyzh.github.io/mini-lsm/`
- 官方 GitHub：`https://github.com/skyzh/mini-lsm`
- dev2 book 源码：`~/workspace/learn/mini-lsm/mini-lsm-book`

## 7 月核心问题

```text
一次读写请求，从 TabletServer 入口，到 Replica/FSM/Engine，再到底层 LSM/RocksDB/IO，是怎么发生的？
```

这个项目回答其中的 storage engine 机制部分：

```text
write -> WAL -> memtable -> immutable memtable -> flush -> SST -> compaction
read -> memtable / immutable memtable / SST levels -> merge iterator -> point lookup / range scan
```

## 本项目目录

- [[01_Environment_And_Repo]]：本地 / dev 分工、repo 状态、命令入口。
- [[02_LSM_in_a_Week_Read_Control]]：课程 / PDF / 官方网页入口和读法。
- `chapters/`：按课程章节拆分的单章 PDF、笔记和问题记录。
- `notes/`：阶段性跟读草稿，必要时再新增。
- `logs/`：命令输出、测试记录、blocker 记录。
- `reports/`：阶段总结或面试化复述稿。

## 长期输出位置

- `LLM_Learn/08_Insights/Systems/storage/TinyLSM_W1_Memtable_Iterator_Log.md`
- `LLM_Learn/08_Insights/Systems/storage/IO_Path_From_DB_Write_to_Device_v0.md`
- `LLM_Learn/08_Insights/Systems/storage/Storage_Classics_Reading_Map_v0.md`
- `LLM_Learn/08_Insights/Systems/storage/TabletServer_Request_Path_Index.md`
- `LLM_Learn/08_Insights/Systems/storage/TabletServer_Thread_IO_Model_v0.md`
- `LLM_Learn/08_Insights/Systems/storage/RocksDB_LSM_Refresh_v0.md`

## 今日下一步

1. 在 dev2 上继续 Week 1 Day 1 的 MemTable 实现。
2. 从 `mini-lsm-book` / 官方网页读 course overview。
3. 写 `TinyLSM_W1_Memtable_Iterator_Log.md` 骨架。
4. 明确 `1.1 Memtable` 和 `1.2 Merge Iterator` 的代码任务、测试命令和不懂的问题。
