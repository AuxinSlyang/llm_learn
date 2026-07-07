---
type: learning_log
track: LSM / mini-lsm
status: active
created: 2026-07-01
project: [[mini-lsm]]
---

# TinyLSM W1 Memtable Iterator Log

## 定位

本文件记录 mini-lsm Week 1 的最小代码学习证据：

```text
Memtable
-> Merge Iterator
-> Block / SST
-> Read Path / Write Path
```

当前只做 W1 Day 1/2，不提前展开 compaction / manifest / WAL / MVCC。

## 环境状态

- 代码仓库：dev2 `~/workspace/learn/mini-lsm`；物理路径 `/data00/work/learn/mini-lsm`
- 当前 head：`427c6cc`
- 本地 Mac：无全局 `rustc/cargo`；2026-07-02 为验证 patch 临时安装隔离工具链到 `/tmp/codex-rustup` / `/tmp/codex-cargo`
- dev2：`cargo/rustc` 可用，当前 head `427c6cc`
- PDF：`/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/mini-lsm/materials/LSM in a Week.pdf` 已放入项目目录，是今天下午/晚上阅读 MiniLSM 第一部分的主材料。

## 命令入口

```bash
ssh dev2
cd ~/workspace/learn/mini-lsm
git status --short

# Rust toolchain ready 后再执行：
cargo x install-tools
cargo x copy-test --week 1 --day 1
cargo x scheck
```

## 2026-07-01 Repo / Test Gate

已完成：

- dev2 repo：`~/workspace/learn/mini-lsm`（物理路径 `/data00/work/learn/mini-lsm`）
- 2026-07-05 路径复核：旧路径 `/home/yangshunlei/study/mini-lsm` 不存在；真实入口为 root 用户下的 `~/workspace/learn/mini-lsm`，物理路径 `/data00/work/learn/mini-lsm`
- host：`dc01-pd-tc22-n037`
- head：`427c6cc`
- Rust：`cargo 1.96.1` / `rustc 1.96.1`
- `cargo x install-tools`：成功
- `cargo x copy-test --week 1 --day 1`：成功
- `cargo x scheck`：失败，但这是 starter 的预期状态

失败点：

```text
mini-lsm-starter/src/mem_table.rs:56
MemTable::create -> unimplemented!()
```

失败测试：

```text
test_task1_memtable_get
test_task1_memtable_overwrite
test_task2_storage_integration
test_task3_storage_integration
test_task3_freeze_on_capacity
test_task4_storage_integration
```

下一步：下午读第一部分；晚上一起读 Week 1 Day 1 tests 和 starter，再实现 `MemTable::create / get / put`。

## W1 Day 1: Memtable

### 2026-07-01 初读结论

- Mini-LSM 课程三段：Week 1 做 storage structure / format / read-write path，Week 2 做 compaction / persistence，Week 3 做 MVCC。
- LSM 基本三件套：WAL 负责 crash recovery，memtable 负责 batch small writes，SST 负责磁盘上的有序不可变数据。
- Write path 第一版：`write WAL -> write memtable -> acknowledge -> background freeze/flush -> background compaction`。
- Read path 第一版：先从最新到最老查 memtables，再查 SST tree；lookup 找单 key，scan 迭代 range。
- Week 1 Day 1 的最小实现不是完整 LSM，而是先让内存 read/write path 跑通：`MemTable::create / get / put`。
- 当前测试 gate 已建立：`cargo x copy-test --week 1 --day 1` 成功，`cargo x scheck` 因 starter 的 `unimplemented!()` 失败，失败点是今天要实现的任务。

### 要回答的问题

- Memtable 在 LSM write path 中承担什么角色？
- 为什么先写 WAL，再写 memtable？
- Memtable 中 key/value 的排序结构是什么？
- immutable memtable 什么时候出现？
- 这个 toy engine 和 RocksDB memtable 的差别在哪里？

### 代码观察

- 文件：`mini-lsm-starter/src/mem_table.rs`
- 当前结构：
  - `map: Arc<SkipMap<Bytes, Bytes>>`
  - `wal: Option<Wal>`
  - `id: usize`
  - `approximate_size: Arc<AtomicUsize>`
- 当前失败点：
  - `MemTable::create` at `mem_table.rs:56`
  - 后续还有 `get` / `put` / WAL recovery / scan 等未实现点，但 Week 1 Day 1 第一刀只做内存 memtable。
- 测试暴露的行为：
  - `put` 后 `get` 能取回 value。
  - 同一 key 重复 put 时应覆盖旧值。
  - `delete` 在 storage 层用 empty value tombstone 表示。
  - freeze 后 read path 要从最新 memtable 向更老 memtable 查。

### 当前不懂的问题

- `Bytes` clone / slice 的零拷贝语义。
- `crossbeam_skiplist::SkipMap` 为什么 `insert` 不需要 `&mut self`。
- `Arc<AtomicUsize>` 的 approximate size 为什么要共享且原子更新。
- `state: Arc<RwLock<Arc<LsmStorageState>>>` 和 `state_lock` 的分工。

### 2026-07-02 预备整理与误提前沙盒实现

说明：这一段是误提前做的实现验证记录，不代表 Day 1 20 个问题已经逐题讲解完成。真正学习仍从 P0-01 开始逐题过。

- 已收敛 Day 1 20 个问题：P0 10 / P1 6 / P2 4。
- dev2 当前 SSH blocked：`Permission denied (gssapi-keyex,gssapi-with-mic)`，真实 repo 暂未写入。
- 用官方 `skyzh/mini-lsm` HEAD `427c6cc` clone 到本地临时目录 `.openclaw/tmp/mini-lsm-codex-read`，与 dev2 head 一致。
- 曾在隔离 Rust 1.96.1 下提前实现并验证 Day 1 patch；该 patch 只作为后续写代码时参考，不作为当前学习完成证据。

实现范围：

- `MemTable::create`
- `MemTable::get`
- `MemTable::put`
- `LsmStorageInner::get`
- `LsmStorageInner::put`
- `LsmStorageInner::delete`
- `LsmStorageInner::force_freeze_memtable`

验证命令：

```bash
cd .openclaw/tmp/mini-lsm-codex-read
RUSTUP_HOME=/tmp/codex-rustup CARGO_HOME=/tmp/codex-cargo PATH=/tmp/codex-cargo/bin:$PATH cargo x copy-test --week 1 --day 1
RUSTUP_HOME=/tmp/codex-rustup CARGO_HOME=/tmp/codex-cargo PATH=/tmp/codex-cargo/bin:$PATH cargo x scheck
```

验证结果：

```text
6 tests run: 6 passed, 0 skipped
cargo check: passed
cargo fmt: passed
cargo clippy: passed
```

关键实现结论：

- `MemTable` 用 `Arc<SkipMap<Bytes, Bytes>>` 保存 owned key/value。
- `put` 每次 `Bytes::copy_from_slice` 后 insert，并用 `AtomicUsize` 近似累加 `key.len() + value.len()`。
- storage `get` 按 current memtable -> immutable memtables newest-first 查找；空 value 解释为 tombstone。
- storage `put` 写当前 memtable 后检查 size；触发 freeze 时拿 `state_lock`，re-check，并用 `Arc::ptr_eq` 避免基于旧 snapshot freeze 新 memtable。
- `force_freeze_memtable` 把旧 current memtable 插到 `imm_memtables[0]`，再创建新的 current memtable。

## W1 Day 2: Merge Iterator

### 要回答的问题

- 为什么 read path 需要 merge iterator？
- 多个有序输入如何合并？
- duplicate key / newer value / tombstone 如何处理？
- point lookup 和 range scan 走 iterator 时有什么区别？

### 代码观察

- 待填：

### 当前不懂的问题

- 待填：

## 今日最小 takeaway

- LSM 的第一性原理不是“复杂树结构”，而是把小随机写先吸收到内存有序结构，再批量落成不可变有序文件；MemTable 是这条链路的第一个可运行证据。

## 和 TokaDB / RocksDB 的连接

- Memtable / immutable memtable 对照 RocksDB write buffer / flush。
- Merge iterator 对照 RocksDB internal iterator / merging iterator / range scan。
- 后续需要回到 TokaDB TabletServer：请求如何进入 Engine，Engine 如何调用 RocksDB/TokaDBEngine。

## MiniLSM -> RocksDB 对象映射

今天只做对象概念映射，不展开 RocksDB 源码深挖。

| MiniLSM 概念 | RocksDB 对应概念 / 对象 | 今天只需要理解到 |
|---|---|---|
| `MemTable` | `MemTable` / `MemTableRep` | 内存中的有序写缓冲，承接最新写入 |
| `SkipMap<Bytes, Bytes>` | skiplist-based memtable rep | 用有序内存结构支持 put/get/scan |
| empty value tombstone | deletion marker / tombstone | delete 不是立即物理删除，而是写入删除标记 |
| immutable memtable | immutable memtable list | 当前 memtable freeze 后等待 flush |
| `MergeIterator` | `InternalIterator` / merging iterator | 把多个有序输入合并为一个有序视图 |
| `Block` | data block | SST 内部的数据块 |
| `SsTable` | SST file / table reader | 磁盘上的不可变有序文件 |
| `Wal` | WAL / log writer | crash recovery 的顺序日志 |
| `LsmStorageInner` | DBImpl / ColumnFamilyData 相关边界 | storage engine 的内部状态与读写入口 |

后续读 RocksDB 时优先找这些问题：

- 写入如何从 `DB::Put` / `WriteBatch` 到 memtable。
- memtable 什么时候变成 immutable。
- flush 如何把 immutable memtable 写成 SST。
- read path 如何同时查 memtable、immutable memtable、L0/Ln SST。
- iterator 如何处理重复 key、sequence number、tombstone。
