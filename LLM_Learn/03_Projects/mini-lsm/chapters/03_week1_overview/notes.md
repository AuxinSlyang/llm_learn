---
type: chapter_notes
project: mini-lsm
chapter: 03_week1_overview
title: Week 1 Overview: Mini-LSM
source_pages: p11-p12
status: done
---

# Week 1 Overview: Mini-LSM Notes

## Summary

- Week 1 目标是建立一个能处理 `get/scan/put` 的 Mini-LSM KV store。
- Week 1 重点是 storage structure、storage format、read path 和 write path，不包含完整 LSM state persistence 和复杂磁盘 level 组织。
- 七天路线：
  - Day 1: Memtable，内存读写路径。
  - Day 2: Merge Iterator，scan/range read 的基础。
  - Day 3: Block Encoding，磁盘 data block 编解码。
  - Day 4: SST Encoding，由 blocks 组成 SST 文件。
  - Day 5: Read Path，组合 memtables + SSTs。
  - Day 6: Write Path，memtable flush 到 L0 SST。
  - Day 7: SST Optimizations，Bloom Filter 和 Key Compression。
- Week 1 结束后会有一个可工作的 Mini-LSM，但 manifest/WAL/persistence/compaction deep dive 主要在 Week 2。

## Key Concepts

- `MemTable`: 内存有序表，承接写入。
- `MergeIterator`: 合并多个有序 iterator，保证 scan 输出有序且返回最新版本。
- `Block`: SST 内部的 data block，是磁盘编码的基本单元。
- `SST`: sorted string table，多个 block + index/meta 组成的不可变磁盘文件。
- `Bloom Filter`: read path 的快速否定过滤，减少不必要 SST 读取。
- `Key Compression`: SST 内部压缩优化，减少存储空间。
- `L0 SST`: memtable flush 后直接产生的第一层 SST。

## MiniLSM Code Mapping

- Day 1 主要看 `src/mem_table.rs` 和 `src/lsm_storage.rs`。
- Day 2 主要看 `src/mem_table.rs`、`src/iterators/merge_iterator.rs`、`src/lsm_iterator.rs`。
- Day 3/4 进入 `src/block/*`、`src/table/*`。
- Day 5/6 回到 `src/lsm_storage.rs`，把内存结构和磁盘结构接入完整 read/write path。
- 当前执行顺序：先读 Day 1 PDF，再读测试，再读 starter code，最后一起实现。

## RocksDB / Real System Mapping

- Day 1 MemTable -> RocksDB `MemTable` / `MemTableRep`。
- Day 2 MergeIterator -> RocksDB `InternalIterator` / `MergingIterator`。
- Day 3 Block -> RocksDB block-based table 的 data block。
- Day 4 SST -> RocksDB `SSTable` / `BlockBasedTable`。
- Day 5/6 read/write path -> RocksDB `DBImpl`、flush、L0 file、read options/iterator 路径。
- Day 7 Bloom/Compression -> RocksDB bloom filter/prefix compression 等 table options。
