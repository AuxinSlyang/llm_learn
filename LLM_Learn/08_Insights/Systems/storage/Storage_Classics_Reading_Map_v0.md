---
type: reading_map
track: Storage / LSM / Distributed Storage / IO
status: draft
created: 2026-07-01
---

# Storage Classics Reading Map v0

## 定位

这不是论文收藏清单，而是服务 2026-07 到 2026-09 的系统问题：

```text
storage engine 如何组织数据？
一次 IO 如何发生？
单机存储如何扩展到分布式 shared storage？
```

## 7 月：LSM / RocksDB / IO Path

- `mini-lsm / LSM in a Week`：代码实验场，先写通机制。
- `The Log-Structured Merge-Tree`：LSM 原始思想，理解为什么把随机写转成批量顺序归并。
- RocksDB wiki / docs：memtable、WAL、SST、iterator、compaction、recovery。
- Linux IO path materials：VFS、page cache、block layer、fsync。
- SSD / HDD / NVMe basics：设备模型和性能差异。

### LSM 经典文献分层

#### 第一层：本周/七月必须读

- O'Neil et al., `The Log-Structured Merge-Tree (LSM-Tree)`, Acta Informatica 1996.
  - 目的：理解 C0/C1、多层归并、延迟批处理写入的原始动机。
  - URL: `https://link.springer.com/article/10.1007/s002360050048`
  - PDF: `https://dsf.berkeley.edu/cs286/papers/lsm-acta1996.pdf`
- LevelDB implementation notes.
  - 目的：把 MiniLSM 的 memtable/log/table/compaction 对应到工业简化实现。
  - URL: `https://github.com/google/leveldb/blob/main/doc/impl.md`
- RocksDB Compaction wiki.
  - 目的：理解 leveled/universal/FIFO compaction 的工程分类。
  - URL: `https://github.com/facebook/rocksdb/wiki/Compaction`
- RocksDB Experience / Evolution paper, FAST 2021.
  - 目的：理解生产级 RocksDB 优化目标如何从 write amplification 转向 space amplification/CPU。
  - URL: `https://www.usenix.org/conference/fast21/presentation/dong`

#### 第二层：MiniLSM Week 2 后读

- Monkey: Optimal Navigable Key-Value Store, SIGMOD 2017.
  - 目的：理解 LSM tuning 中 lookup/update/memory 的 tradeoff，尤其 Bloom filter 分配。
  - URL: `https://dl.acm.org/doi/10.1145/3035918.3064054`
- WiscKey: Separating Keys from Values in SSD-conscious Storage, FAST 2016.
  - 目的：理解 key-value separation 和 SSD-aware LSM 设计。
  - URL: `https://www.usenix.org/conference/fast16/technical-sessions/presentation/lu`

#### 第三层：七月后扩展

- PebblesDB / FLSM：理解 fragmented LSM 和 write amplification 优化。
- Dostoevsky：理解 leveled/tiered 之间的 space-time tradeoff。
- SILT / FASTER / KVell：作为高性能 KV store 对照，不抢 MiniLSM 主线。

#### 书籍与章节

- `DDIA` Chapter 3: Storage and Retrieval。
  - 目的：建立 LSM vs B-Tree、SSTable、compaction、Bloom filter 的宏观理解。
- Alex Petrov, `Database Internals`。
  - 目的：补磁盘数据结构、B-Tree/LSM、page/block、transaction/recovery 等底层概念。

## 8 月：RPC / Coroutine / Tail Latency

- brpc docs：server/client、bthread、bvar、execution queue、RPC in depth。
- bthread / M:N thread model：协程和 pthread 的映射、调度和阻塞边界。
- Tail latency / queueing / backpressure 相关材料。
- 结合 TokaDB 真实线程与 IO 模型，不单独泛读。

## 9 月：Distributed Storage / Shared Storage / High Performance IO

- 3FS：metadata service、storage service、client、RDMA network、SSD shared storage。
- ByteStore：metadata / chunk / blob / replication / recovery。
- MinIO / object storage awareness：object storage API、metadata、consistency、erasure coding。
- SPDK / DPDK / RDMA / io_uring：高性能 IO path 和 kernel bypass。
- FoundationDB / CRAQ：metadata / consistency / replication 经典背景。

## 10-12 月：Inference Storage / KVCache

- PagedAttention / vLLM：KV block / page / block table / scheduler。
- LMCache / Mooncake / DistServe：KV movement、offload、prefill-decode disaggregation。
- DeepSeek-V2/V3/R1：MLA / MoE / long-context / reasoning workload 对 serving 的压力。
- 回到已有代码：RocksDB、brpc、TokaDB 的 zero-copy、queueing、tail latency、recovery 经验如何迁移。

## DDIA 读法

- 7 月：Storage and Retrieval。
- 8 月：Reliability / Scalability / Encoding。
- 9 月：Replication / Partitioning / Transactions。
- 10-12 月：Consistency / Distributed Systems / Stream or Batch 按需补。
