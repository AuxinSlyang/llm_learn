---
type: chapter_questions
project: mini-lsm
chapter: w1d1_memtables
title: Week 1 Day 1: Memtables
source_pages: p13-p19
status: active
updated: 2026-07-02
---

# Week 1 Day 1: Memtables Questions

## Source

- 2026-07-01 voice/text notes from local attachment: `/Users/bytedance/.codex/attachments/bfc247f0-edb5-48bd-8599-4697f411cd23/pasted-text.txt`
- Chapter notes: `LLM_Learn/03_Projects/mini-lsm/chapters/w1d1_memtables/notes.md`
- W1 log: `LLM_Learn/08_Insights/Systems/storage/TinyLSM_W1_Memtable_Iterator_Log.md`
- Starter code inspected on dev2:
  - `mini-lsm-starter/src/tests/week1_day1.rs`
  - `mini-lsm-starter/src/mem_table.rs`
  - `mini-lsm-starter/src/lsm_storage.rs`

## From The Chapter

- What does `cargo x copy-test --week 1 --day 1` do?
- Should we work on `main`, or switch to a chapter/task branch?
- Why use `crossbeam_skiplist::SkipMap` as the MemTable data structure?
- Why do SkipMap mutation APIs take `&self`, not `&mut self`?
- Why should we not add a new `Mutex` around the memtable?
- Why does MemTable not expose a delete API?
- What does it mean that delete is represented by `key -> empty value`?
- What is `Bytes`, and why is clone/slice cheap?
- Why does `LsmStorageInner::get/put/delete` dispatch directly to the current memtable in Day 1?
- Why is there only one mutable memtable at a time?
- When and why does a memtable become immutable?
- How should approximate memtable size be calculated?
- Why can approximate size double-count overwritten keys?
- Why does read path check memtables from newest to oldest?
- What race conditions exist when multiple writers trigger freeze concurrently?
- Why do future chapters care about keeping IO outside the state write-lock region?
- What does `Arc<RwLock<Arc<LsmStorageState>>>` mean?
- What is copy-on-write state here?
- Why acquire a read lock, drop it, then acquire a write/state lock instead of directly upgrading?
- Can older snapshots still exist after a state swap?
- Is `parking_lot::RwLock` fair?
- Is it possible that a thread still writes into an older mutable memtable after freeze?
- Could MemTable use BTree / hash table / vector / ART instead of skiplist?
- Is skiplist memory layout cache-friendly? How could MemTable be optimized?

## Canonical 20 Questions

原始问题是 20 个，不是 6 个。6 个只是学习和讲解时的主题归并，方便一组一组讲清楚。

### P0 / Day 1 implementation blockers (10)

- [ ] P0-01 `cargo x copy-test --week 1 --day 1` 到底是拷贝/启用测试，还是切换分支？
- [ ] P0-02 当前 repo 应该在 `main` 上做，还是切到 `chapter/task` 分支？
- [ ] P0-03 `SkipMap::insert(&self, ...)` 为什么共享引用也能写？这和 `&mut self` / 独占引用是什么关系？
- [ ] P0-04 为什么不应该给 MemTable 外面再包一层 `Mutex`？
- [ ] P0-05 `Bytes` 类似 `Arc<[u8]>` 是什么意思？为什么 clone/slice cheap？
- [ ] P0-06 MemTable 为什么没有 delete API？empty value tombstone 如何表达删除？
- [ ] P0-07 `LsmStorageInner::get/put/delete` 在 Day 1 为什么直接 dispatch 到 current memtable？
- [ ] P0-08 freeze 后多个 memtables 中读同一个 key，为什么必须 newest -> oldest？
- [ ] P0-09 `approximate_size: Arc<AtomicUsize>` 为什么要共享且原子更新？为什么 overwritten key double-count 可以接受？
- [ ] P0-10 Day 1 今天最低实现哪些函数？哪些必须留到 WAL / iterator / SST / compaction 后续章节？

### P1 / concurrency and state model (6)

- [ ] P1-01 `state: Arc<RwLock<Arc<LsmStorageState>>>` 和 `state_lock: Mutex<()>` 分别保护什么？
- [ ] P1-02 Copy-on-write state 会不会导致读者看到“过期状态”？这算不算不一致？
- [ ] P1-03 多个 writer 同时触发 freeze 时有什么 race condition？
- [ ] P1-04 为什么常见模式是 read lock -> drop -> acquire state_lock/write lock -> re-check，而不是直接 upgrade？
- [ ] P1-05 freeze 后，老 snapshot 里的 memtable 还可能被线程继续写吗？怎么防？
- [ ] P1-06 `parking_lot::RwLock` 公平性如何影响 writer/readers？

### P2 / design extensions (4)

- [ ] P2-01 MemTable 是否应该保存所有 write operations，而不是只保存 latest value？
- [ ] P2-02 Skiplist vs BTree / hash table / vector / ART 的 tradeoff 是什么？
- [ ] P2-03 当前 MemTable 内存布局和 data locality 好不好？有哪些优化方向？
- [ ] P2-04 MiniLSM Week1/Week2/Week3 一个月内如何安排才现实？

## Six Study Themes

- Theme 1 / 代码入口与今日边界：P0-01, P0-02, P0-10
- Theme 2 / MemTable 语义：P0-06, P0-09, P2-01
- Theme 3 / Rust + SkipMap + Bytes：P0-03, P0-04, P0-05
- Theme 4 / Storage read/write path：P0-07, P0-08
- Theme 5 / freeze + state snapshot + COW：P1-01..P1-06
- Theme 6 / 设计替代与学习节奏：P2-02, P2-03, P2-04

## Current Focus

- 今天优先清掉 P0-01..P0-10，保证 Day 1 coding 能推进。
- P1 今天只需要理解到“为什么要 re-check + state_lock”；更细的 lock fairness / snapshot race 后续单独画时序图。
- P2 不阻塞实现，作为后续系统设计和 RocksDB 对照问题。

## Learning Status

- [ ] P0：10 个 Day 1 实现相关问题，待逐题讲解。
- [ ] P1：6 个并发与 state model 问题，待逐题讲解。
- [ ] P2：4 个设计扩展问题，待逐题讲解。

## Preliminary Notes

这些是预备整理，不代表已经逐题学习完成。每个问题仍需在 session 中单独讲清、确认直觉、再打勾。

- P0-01 / P0-02: `copy-test` 是把指定 week/day 的测试启用到 starter code；不是切换分支。当前应在官方 repo `main` 分支的 `mini-lsm-starter` 下实现。参考实现/checkpoint 只在卡住时 diff。
- P0-03: `SkipMap` 不是“数据 immutable”。它是并发数据结构，mutation API 用 `&self`，表示调用者不需要独占借用整个 map；内部用并发/原子机制保证多线程 insert/get/iter 可并发调用。
- P0-04: 外层 `Mutex` 不是语法上不能加，而是这个任务不应该加：它会把本来可并发的 memtable 写入串行化，并破坏本章训练点。需要同步的是 state swap / freeze，不是每次 skiplist insert。
- P0-05: `Bytes` 是引用计数式字节缓冲。clone/slice 通常只复制指针、长度、offset 和引用计数，不深拷贝底层 bytes，所以适合 key/value 在 memtable、SST、iterator 间传递。
- P0-06: Day 1 没有 MVCC，也不在 memtable 里物理删除。delete 在 storage 层写入 empty value；read path 看到 empty value 时解释为 deleted / `None`。真正清理发生在后续 compaction。
- P0-07: Day 1 的 storage engine 还没有 SST / compaction。`LsmStorageInner::put/delete/get` 只需要从当前 state 拿到 current memtable，然后调用 memtable 的 `put/get`；delete 调用 `put(key, b"")`。
- P0-08: 同一个 key 可能出现在 mutable memtable 和多个 immutable memtable 中。越新的 memtable 代表越晚的写入。read path 必须 newest -> oldest，否则会返回旧值或忽略最新 tombstone。
- P0-09: approximate size 是 freeze trigger，不是精确内存账本。覆盖同一个 key 时 double-count 可以接受，因为它只决定“差不多该 freeze 了”。用 `AtomicUsize` 是因为 multiple put 可以并发更新同一个 memtable 的 approximate size。
- P0-10: 今天最低实现范围：
  - `MemTable::create`
  - `MemTable::get`
  - `MemTable::put`
  - `LsmStorageInner::get`
  - `LsmStorageInner::put`
  - `LsmStorageInner::delete`
  - capacity check + `force_freeze_memtable`
  - multiple memtable newest-first read path
  Do not implement WAL, scan iterator, flush, SST, compaction, MVCC today.
- P1-01: `state: Arc<RwLock<Arc<LsmStorageState>>>` protects the pointer to the active immutable-ish state snapshot. `state_lock: Mutex<()>` serializes state modifications such as freeze / flush / compaction, so two writers do not both swap state based on stale assumptions.
- P1-02: Old readers may see an older but internally consistent snapshot. That is intentional. The goal is not “every reader always sees the newest global state at every instant”; the goal is no torn state and minimal blocking. For operations that modify state, the code must re-check under `state_lock`.
- P1-03 / P1-05: The risky case is: writer A gets old memtable, writer B freezes and swaps state, then writer A continues writing old memtable. Day 1 avoids this by re-checking capacity and freezing under `state_lock`; the exact implementation must ensure state-changing decisions are made under the synchronization path, not only from a stale read snapshot.
- P1-04: Direct upgrade avoids the gap but can deadlock or is not always supported ergonomically. The common pattern here is read -> decide maybe -> drop -> acquire serialized state lock/write lock -> re-check condition -> modify. The re-check is the critical step that makes the gap safe.
- P1-06: `parking_lot::RwLock` uses a task-fair policy. If a writer is waiting, new readers may block even if the lock is otherwise readable; this avoids writer starvation.
- P2-01: Day 1 memtable stores latest value per key. All write operations belong in WAL / MVCC versions, not in the simple memtable map. Week 3 timestamp-key refactor changes the key model for versions/snapshots.
- P2-02: Other MemTable structures are possible. Hash table is fast for point lookup but poor for ordered scan; BTree has ordered scan and locality but less lock-free concurrent write; vector is compact but expensive to insert/search unless batched; ART/trie can be good for byte keys/prefixes but more complex. Skiplist is a pragmatic first choice: ordered, supports range scan, simple, concurrent.
- P2-03: Skiplist pointer chasing is not ideal for cache locality. Optimizations include arena allocation, prefix compression, vector/block-based immutable memtable, ART/trie for byte keys, hash index for point lookup, or separating mutable write buffer from immutable compact representation.
- P2-04: 一个月安排应按测试边界推进，而不是按源码量推进。第一周完成 Week 1 Day 1-7 的 memtable / iterator / block / SST / read path / write path / optimizations；第二周完成 compaction / WAL / manifest / batch write；第三周完成 timestamp key / snapshot / transaction / OCC / GC；第四周回头做 RocksDB 对照、故障注入和知识沉淀。

## 2026-07-02 Session Study Notes

- P0-01 / P0-02 / P0-10: Day 1 是在 `mini-lsm-starter` 的 `main` 工作区里启用并通过 `week1_day1.rs`，不是切分支。最小代码边界是 `MemTable::create/get/put`、storage `get/put/delete`、freeze、newest-first read path。
- P0-03: `&self` 不是“拿到了自己的拷贝”，而是共享借用。普通类型只有 `&mut self` 才能改自身；`SkipMap` 把同步封装在类型内部，所以 mutation API 可以是 `&self`。这属于 interior mutability / concurrent data structure 的范畴，不是绕过 borrow checker。
- P0-04: 外面再包 `Mutex` 会把所有 memtable 写入串行化，失去 skiplist 并发写的训练目标。真正需要串行化的是 state swap / freeze 这种结构性变化。
- P0-05: `Bytes` 是引用计数式 byte buffer；clone/slice 主要复制元数据和引用，不深拷贝底层字节。Day 1 仍然用 `Bytes::copy_from_slice` 把传入的 `&[u8]` owned 化，避免外部 slice 生命周期问题。
- P0-06: Day 1 delete 不在 MemTable 里物理删除 key，而是写入 empty value tombstone。read path 看到 empty value 后返回 `None`，后续 compaction 再负责真正清理。
- P0-07 / P0-08: Day 1 还没有 SST，因此 storage read path 只查 current memtable 和 immutable memtables。顺序必须是 current -> newest immutable -> older immutable，否则会读到旧值或忽略最新 tombstone。
- P0-09: `approximate_size` 是 freeze trigger，不是精确内存账本。overwrite double-count 可以接受，因为它只会让 memtable 稍早 freeze；`AtomicUsize` 支持多个 writer 并发更新这个近似计数。
- P1-01 / P1-02: `RwLock<Arc<LsmStorageState>>` 保护当前 state 指针；读者 clone 内层 `Arc` 后拿到一致 snapshot。旧 snapshot 可能存在，但它是自洽的，不是 torn state。
- P1-03 / P1-05: 多 writer 的关键风险是基于旧 snapshot 做 freeze 判断。Day 1 patch 使用 `state_lock` + re-check，并用 `Arc::ptr_eq` 确认要 freeze 的仍是当前 memtable；这能避免拿旧 memtable 的 size 去 freeze 新 memtable。
- P1-04: read lock -> drop -> state_lock/write lock -> re-check 的核心是缩短锁持有时间，并避免直接 lock upgrade 带来的死锁/接口限制。安全性来自 re-check。
- P1-06: `parking_lot::RwLock` 是 task-fair / eventual fairness，读多写少时不会无限饿死 writer；这也意味着有 writer 等待时，后来的 reader 可能被挡住。
- P2-01: Day 1 map 只保存 latest value。所有 write operations 的持久日志语义属于 WAL；多版本可见性属于 Week 3 timestamp key / MVCC。
- P2-02 / P2-03: Skiplist 是“实现简单 + 有序 scan + 并发写”的折中；它不是 cache locality 最优。真实系统可考虑 arena、block immutable memtable、ART、hash index 等。
- P2-04: 一个月内 MiniLSM 应按 week/day test gate 推进；每过一个 gate 就沉淀一页系统笔记，而不是一次性追完整课程。

## 2026-07-02 Patch Verification

- dev2 当前 SSH blocked：`Permission denied (gssapi-keyex,gssapi-with-mic)`。
- 本地使用官方 `skyzh/mini-lsm` HEAD `427c6cc` 临时 clone 到 `.openclaw/tmp/mini-lsm-codex-read`，与 dev2 记录 head 一致。
- 在隔离 Rust 工具链 `rustc 1.96.1` / `cargo 1.96.1` 下验证 Day 1 patch。
- 验证命令：`cargo x copy-test --week 1 --day 1 && cargo x scheck`。
- 结果：6 个 `tests::week1_day1::*` 全部通过，`cargo check` / `cargo fmt` / `cargo clippy` 通过。

## Need Code Verification

- P1-03 / P1-05 已在 sandbox patch 中验证 Day 1 单线程测试通过；更严格的并发线性化测试留到后续 freeze / flush / WAL 阶段。
- P2-02 / P2-03 are design exploration; do not block Day 1 coding.
- `crossbeam_skiplist` docs: https://docs.rs/crossbeam-skiplist/latest/crossbeam_skiplist/
- `parking_lot::RwLock` docs: https://docs.rs/parking_lot/latest/parking_lot/type.RwLock.html
