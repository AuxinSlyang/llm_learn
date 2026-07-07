---
type: chapter_notes
project: mini-lsm
chapter: 00_preface
title: Preface: What is LSM and Why LSM
source_pages: p1-p5
status: done
---

# Preface: What is LSM and Why LSM Notes

## Summary

- Preface 是“前言/导言”，作用是说明课程目标、读者前置要求、课程组织方式、测试/solution 使用方式，以及作者背景。
- 本课程目标是用 Rust 构建一个简单的 LSM-tree storage engine。关键词是：`LSM tree`、`storage engine`、`Rust`。
- LSM 是维护 key-value pairs 的数据结构/存储引擎组织方式，广泛用于 TiDB、CockroachDB、RocksDB/LevelDB 等系统或组件。
- LSM 的核心特征是 append-friendly：写入、更新、删除不是直接原地覆盖，而是先延迟进入内存结构/日志/不可变 SST，后续通过后台 compaction 合并生效。
- 相比 B-Tree/RB-Tree 的 in-place update，LSM 把随机写和原地修改转成更顺序、更批量的写入与后台整理。
- 持久化存储上的数据不可变，使并发控制、远程 offload compaction、云存储/S3 风格存储适配更直接。
- LSM 的核心 tradeoff 是 read amplification、write amplification、space amplification；通过 compaction strategy 和参数在不同 workload 下做平衡。
- 课程提供测试和 CLI，但测试不穷尽；通过测试不等于实现完全正确，尤其要注意多线程操作和 race conditions。
- solution checkpoint repo 只是按章节提交的参考版本，但可能落后于主 repo 或不完全正确。遇到卡点时可以 diff checkpoint 理解每章预期修改，但不能无条件信任。

## Key Concepts

- `append-friendly`: 对写入友好，倾向追加和批量整理，而不是原地更新。
- `in-place update`: 在原位置覆盖旧值，典型对照是 B-Tree/RB-Tree。
- `SST`: sorted string table，LSM 磁盘上的不可变有序文件。
- `compaction`: 后台合并 SST，应用更新/删除，控制读/写/空间放大。
- `WAL`: write-ahead log，用于崩溃恢复。
- `mutable memtable / immutable memtable`: 内存写入缓冲与冻结后的待 flush 内存表。
- `read/write/space amplification`: LSM 设计里的核心性能权衡。

## MiniLSM Code Mapping

- Week 1 会先实现 memtable、iterator、block、SST 和基本 read/write path。
- Week 2 会深入 compaction、manifest、WAL 和 persistence。
- Week 3 会加入 MVCC、timestamp key、snapshot read、watermark、transaction/OCC。
- 今日只进入 Week 1 Day 1，不提前展开 compaction/MVCC 代码。

## RocksDB / Real System Mapping

- RocksDB 是 LevelDB 系 LSM storage engine 的生产级实现；MiniLSM 用于建立 RocksDB 对象和链路的简化模型。
- `WriteBatch`、`MemTable`、`Immutable MemTable`、`SSTable`、`Compaction`、`WAL/Manifest` 都可以和 RocksDB 概念对应。
- 对真实服务端系统而言，MiniLSM 重点帮助理解一次 put/get/scan 到存储引擎内部结构的路径，而不是替代 RocksDB 源码阅读。
