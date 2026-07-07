---
type: read_control
project: mini-lsm
created: 2026-07-01
status: active
---

# LSM in a Week Read Control

## 材料入口

- 官方网页：`https://skyzh.github.io/mini-lsm/`
- 官方 GitHub：`https://github.com/skyzh/mini-lsm`
- dev2 book 源码：`~/workspace/learn/mini-lsm/mini-lsm-book`
- 本地 PDF：`/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/mini-lsm/materials/LSM in a Week.pdf`
- 单章 PDF 索引：`/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/mini-lsm/chapters/README.md`

## PDF 状态

2026-07-01 更新：

```text
/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/mini-lsm/materials/LSM in a Week.pdf exists
```

本地完整 PDF 保留为母本；默认阅读单章拆分版：

```text
/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/mini-lsm/chapters/
```

dev2 的 `mini-lsm-book` 源码与 starter/tests 用来对照代码实现。dev2 repo 入口为 `~/workspace/learn/mini-lsm`。

## 7 月读法

7 月 MiniLSM 的真实目标是完整吃透 current course，而不是只完成 Week 1。
读法仍然按代码任务驱动，但需要覆盖 Week 1/2/3 的实现、测试、设计复盘和系统映射。

```text
Week 1: storage structure / format，完整实现并讲清 get/scan/put
Week 2: compaction / persistence，完整实现并讲清 compaction/manifest/WAL/recovery
Week 3: MVCC，完整实现并讲清 timestamp/snapshot/watermark/transaction/OCC
```

7 月收口产出：

- MiniLSM current course 全部章节至少完成一遍实现与测试。
- 每个核心对象写 RocksDB 对象映射，但不在 7 月做 RocksDB 源码级深挖。
- TokaDB TabletServer 只做请求链路/线程模型/IO 模型对照，不抢 MiniLSM 主线时间。
- 7 月底输出一份从 write/read request 到 WAL/MemTable/SST/Compaction/MVCC 的完整系统复述。

## 本周目标：2026-07-02 ~ 2026-07-05

本周到 7 月 5 日的目标不是只看 MemTable，而是完成 MiniLSM Week 1 主干的第一轮：

```text
MemTable
MergeIterator
Block
SST
Read Path
Write Path
```

完成标准：

- 每天快速补 Rust，只补当天 MiniLSM 代码需要的部分。
- 大块时间用于读 starter/tests/codebase 并实现对应任务。
- 7 月 5 日前，至少完成 Week 1 Day 1-6 的代码任务第一遍，形成一个能讲清楚的 LSM read/write path。
- Day 7 Bloom Filter / Key Compression 可作为 7 月 5 日后的补充优化，不影响主干闭环。
- 每个对象同步记录 RocksDB 映射：MemTable、MergingIterator、Block、SSTable、DBImpl read/write path。

当前只读：

- `chapters/00_preface/chapter.pdf`
- `chapters/01_course_overview/chapter.pdf`
- `chapters/02_environment_setup/chapter.pdf`
- `chapters/03_week1_overview/chapter.pdf`
- `chapters/w1d1_memtables/chapter.pdf`
- `chapters/w1d2_merge_iterators/chapter.pdf`

## 2026-07-01 今日读法

今天先快速过一遍 Rust 基本核心概念，然后进入 MiniLSM 前两段：

1. Rust quick pass：`let/mut`、ownership 直觉、`&self` / `&mut self`、`Result`、`Option`、`Vec` / `&[u8]` / `Bytes`、`Arc`、trait 的基本形状。
2. MiniLSM Day 1：`MemTable::create/get/put`，理解 memtable 在 write path 中的角色。
3. MiniLSM Day 2：先读 merge iterator 的问题定义，不急着深挖所有 lifetime 细节。
4. RocksDB 映射：每读一个 MiniLSM 对象，都写一条 RocksDB 对应对象或概念。

## 今日要回答的问题

- `mini-lsm-starter` 里 Week 1 起始状态是什么？
- `Memtable` 在 write path 里承担什么角色？
- `Merge Iterator` 在 read path 里解决什么问题？
- 课程测试命令如何启动？
- 哪些 Rust 概念会阻塞阅读：ownership、iterator trait、`Arc` / `Mutex`、`Result`、tests？
- MiniLSM 对象如何映射到 RocksDB：`MemTable`、`MemTableRep`、`WriteBatch`、`ColumnFamilyData`、`InternalIterator`、`MergingIterator`、`SSTable`、`BlockBasedTable`。

## 不做什么

- 今天不读完整 compaction。
- 今天不读 MVCC。
- 今天不开始 RocksDB 源码深挖；只做对象概念映射。
- 今天不把 brpc / 3FS / KVCache 加入 mini-lsm 代码任务。
