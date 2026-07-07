---
type: chapter_notes
project: mini-lsm
chapter: w1d1_memtables
title: Week 1 Day 1: Memtables
source_pages: p13-p19
status: overview-read
---

# Week 1 Day 1: Memtables Notes

## Summary

- Day 1 目标是实现 LSM 的内存读写路径：基于 skiplist 的 MemTable、memtable freeze 逻辑，以及只覆盖 memtables 的 `get` read path。
- 课程测试入口是 `cargo x copy-test --week 1 --day 1` 和 `cargo x scheck`。`copy-test` 会把当前章节对应测试复制/启用到 starter code 中；不是切换分支。
- 当前应在官方 repo 的 `main` 分支和 `mini-lsm-starter` 下完成学习实现；不需要切到 chapter/task 分支。参考实现和 checkpoint 只作为卡住时 diff 用。
- Task 1 修改 `src/mem_table.rs`：实现 `MemTable::get` / `put`。MemTable 不提供 delete API，删除由 `key -> empty value` 的 tombstone 表示。
- Task 2 修改 `src/lsm_storage.rs`：把 `LsmStorageInner::get/put/delete` dispatch 到当前 mutable memtable。
- Task 3 修改 `src/lsm_storage.rs` / `src/mem_table.rs`：统计 approximate memtable size，超过 soft limit 后 freeze 当前 memtable 并创建新的 mutable memtable。
- Task 4 修改 read path：多个 memtables 存在时，必须 newest -> oldest 查找，返回最新版本。

## Key Concepts

- `MemTable`: LSM 内存写入缓冲，承接小写入，并保持 key 有序以支持 scan。
- `crossbeam-skiplist`: 并发 skiplist，提供类似 `BTreeMap` 的 `insert/get/iter`，但修改接口只需要 `&self`，内部负责并发安全。
- `&self` put 不等于对象不可变；它表示外部接口不需要 `&mut self` 独占借用。内部可以通过并发数据结构/内部可变性安全修改。
- 不需要额外 `Mutex` 的原因是 skiplist 自身已经提供并发安全；额外加锁会降低并发，并且违背本章让 memtable 支持并发读写的设计目的。
- `Bytes`: 类似引用计数的字节缓冲。clone/slice 通常只增加引用或创建视图，不深拷贝底层数据，因此适合在 memtable/SST/iterator 间传递 key/value。
- `delete tombstone`: 用空 value 表示删除。真正清理通常发生在后续 compaction，而不是在 memtable 里立即物理删除。
- `mutable memtable`: 当前唯一接收写入的 memtable。
- `immutable memtable`: mutable memtable 达到 size limit 后被冻结，后续不再接收新写入，等待 flush 成 SST。
- `Arc<RwLock<Arc<LsmStorageState>>>`: 外层 `Arc` 共享锁对象；`RwLock` 保护当前 state snapshot 指针；内层 `Arc<LsmStorageState>` 让读者拿到一致快照并快速释放锁。
- `Copy-on-Write state`: 写者不原地改旧 state，而是基于旧 state 构造新 state，再用写锁原子替换当前 state 指针。

## MiniLSM Code Mapping

- 阅读顺序：
  - PDF Day 1 overview
  - `mini-lsm-starter/src/tests/week1_day1.rs`
  - `mini-lsm-starter/src/mem_table.rs`
  - `mini-lsm-starter/src/lsm_storage.rs`
- 明天实现时不要先看完整 solution；先根据 tests 和 starter 接口完成最小行为。
- 需要重点确认：
  - `MemTable::create/get/put`
  - approximate size 如何累加 key/value bytes
  - `LsmStorageInner::put/delete/get`
  - `force_freeze_memtable`
  - `imm_memtables` 的 newest-first 顺序

## RocksDB / Real System Mapping

- MiniLSM `MemTable` 对应 RocksDB `MemTable`。
- MiniLSM skiplist memtable 对应 RocksDB 的 skiplist-based `MemTableRep`。
- tombstone 对应 RocksDB deletion marker。
- mutable -> immutable memtable 对应 RocksDB write buffer 切换和 flush pipeline。
- newest -> oldest 查 memtable 对应真实 LSM 中“同 key 多版本/多位置时必须返回最新可见版本”的基本规则。

## Open Questions

- crossbeam skiplist 的并发实现和 API 需要单独读 docs/source。
- `parking_lot::RwLock` 是否公平，以及读写竞争时 writer/readers 的调度策略，需要后续专项看。
- `state_lock` 与 `state: RwLock<Arc<LsmStorageState>>` 的分工需要结合代码确认。
- read lock -> drop -> write lock 与 lock upgrade 的差异，需要结合 freeze race condition 画时序图。
- MemTable 可替代数据结构：BTree、vector、ART、hash table 的 tradeoff 后续单独比较。
