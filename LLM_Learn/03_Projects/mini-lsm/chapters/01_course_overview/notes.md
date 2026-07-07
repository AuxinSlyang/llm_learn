---
type: chapter_notes
project: mini-lsm
chapter: 01_course_overview
title: Mini-LSM Course Overview
source_pages: p6-p8
status: done
---

# Mini-LSM Course Overview Notes

## Summary

- 本章给出 MiniLSM 的整体系统图：内存侧有 MemTable/WAL，磁盘侧有 L0/L1/... SST、data blocks、block index、manifest，后续 Week 3 再加入 timestamp、snapshot read、transaction、watermark、OCC、serializable snapshot isolation 等 MVCC/事务能力。
- 课程分三周：Week 1 关注 storage structure / storage format，Week 2 关注 compaction / persistence，Week 3 关注 MVCC。
- LSM storage engine 一般包含三类核心组件：WAL、SST、MemTable。
- 对外常见接口：`Put(key, value)`、`Delete(key)`、`Get(key)`、`Scan(range)`、`Sync()`。有些系统会用 `WriteBatch` 合并 Put/Delete。
- 本课程默认使用 real-world systems 常见的 leveled compaction algorithm。
- Write path 的顺序：先写 WAL，再写 MemTable；用户写入可以在 WAL + MemTable 完成后返回；后台再 freeze memtable、flush SST、compaction。
- Read path 的顺序：先查 memtables，按 newest -> oldest；再查 SSTs，按 top layer -> bottom layer。
- 读分两类：lookup 查单个 key，scan 遍历一个 range。

## Key Concepts

- `WAL`: write-ahead log，用于 crash recovery。先落日志，避免 memtable 中的数据在崩溃后丢失。
- `MemTable`: 内存中的有序写入缓冲，用于 batch small writes。
- `SST`: sorted string table，磁盘上的不可变有序文件。注意是 SST，不是 SSD。
- `Manifest`: 记录 LSM 状态变化的元数据日志，Week 2 处理 persistence 时会展开。
- `WriteBatch`: 批量写接口，把多个 put/delete 作为一个批处理。
- `Flush`: mutable/immutable memtable 写成 L0 SST。
- `Compaction`: 后台合并 SST 到更低层，维持 LSM tree 的形状，控制 read amplification / space amplification。
- `Watermark`: MVCC 中追踪最低活跃读时间戳，用于决定哪些旧版本可以 GC。
- `Lookup`: point read，查一个 key。
- `Scan`: range read，按顺序遍历 key range。

## MiniLSM Code Mapping

- Week 1 Day 1 会先实现 MemTable 相关 read/write path。
- Week 1 Day 2 会实现 MemTable iterator 和 MergeIterator，为 scan 服务。
- Week 1 Day 3/4 会实现 Block/SST 编码，建立磁盘格式。
- Week 1 Day 5/6 会把 memtable 和 SST 串成完整 read/write path。
- Week 1 Day 7 会补 Bloom Filter / Key Compression 这类 SST 优化。
- Week 2 再进入 compaction、manifest、WAL 和持久化恢复。
- Week 3 再进入 timestamp key、snapshot read、watermark、transaction/OCC。

## RocksDB / Real System Mapping

- `WAL` 对应 RocksDB write-ahead log。
- `MemTable / immutable memtable` 对应 RocksDB 中的 mutable memtable 与 imm memtables。
- `SST / data block / block index` 对应 RocksDB block-based table 的核心磁盘结构。
- `WriteBatch` 是 RocksDB 真实存在的批量写入抽象。
- `Manifest` 对应 RocksDB 的 MANIFEST/version edit 体系，用于恢复 DB 的文件集合和 level 状态。
- `Compaction` 是 RocksDB LSM 读写/空间放大的核心调参点。
- 对 TokaDB/TabletServer 一类真实服务端，本章对应的是底层 engine 的内部链路骨架：request -> engine put/get/scan -> WAL/MemTable/SST/Compaction。
