---
type: project_ladder
track: shared storage / LSM / AI storage
status: active
created: 2026-06-28
---

# Shared Storage Project Ladder 2026Q3

## 定位

3FS 不适合作为第一个“玩具项目”：它是 C++ 为主的生产级共享文件系统，涉及 FDB、RDMA、FUSE、USRBIO、CRAQ、storage service、metadata service。

更稳的路径是用一组项目形成梯子：

```text
mini-lsm
-> SlateDB / Tonbo
-> JuiceFS
-> ByteStore
-> 3FS
```

## 项目梯子

| 层级 | 项目 | 语言/定位 | 我们读它解决什么问题 |
|---|---|---|---|
| L0 | mini-lsm | Rust，本地 LSM toy | memtable、SST、WAL、manifest、compaction、MVCC |
| L1 | SlateDB | Rust，LSM over object storage | immutable SST 放到对象存储后，manifest/compaction/recovery 怎么变 |
| L1 | Tonbo | Rust，Arrow/Parquet + LSM | columnar LSM、Parquet SST、serverless/edge storage 格式 |
| L2 | JuiceFS | Go，POSIX FS over object storage | metadata/data separation、client cache、object storage backend |
| L2 | ByteStore | 内部 shared storage 样本 | blob/chunk/meta/replication/recovery |
| L3 | 3FS | C++ 为主，AI shared file system | SSD+RDMA、FDB metadata、CRAQ、FUSE/USRBIO、AI workloads |

## 为什么不是直接写 3FS toy

真正像 3FS 的 toy 很容易失控，因为它至少要包含：

- metadata service
- namespace / inode / chunk mapping
- placement / chain replication
- client cache
- storage node
- recovery / rebalance
- FUSE 或 client API
- IO benchmark

前三个月更合理的 toy 是：

```text
TinySharedStorage Design Sketch
```

它不是完整实现，只做系统设计 + 最小 demo：

- 单机 metadata map：file -> chunks。
- 本地 chunk store：chunk_id -> file block。
- client read/write API。
- 一个 placement policy。
- 一个 manifest / version 文件。
- 一个 crash-recovery demo。

这个 sketch 的价值是帮助面试讲清 3FS/ByteStore/对象存储的共同抽象，而不是成为生产项目。

## 9 月执行建议

### W36：3FS architecture first pass

- README / design notes / docs。
- 画 client / mgmtd / meta / storage / FUSE / USRBIO / FDB 边界。

### W37：metadata / FDB

- `src/meta`
- `src/fdb`
- namespace、inode、chunk、transactional KV。

### W38：storage / CRAQ / replication

- `src/storage`
- chain replication、chunk engine、update path、recovery。

### W39：shared storage ladder comparison

- SlateDB / Tonbo / JuiceFS / ByteStore / 3FS 对照。
- 写 `TinySharedStorage_Design_v0`。

### W40：IO path

- FUSE / USRBIO / RDMA / SSD / fio benchmark。
- 对接 10 月 KVCache storage。

## 面试叙事

这条线最后应该能讲成：

```text
我先用 mini-lsm 写通 LSM 内核；
再看 SlateDB/Tonbo 如何把 LSM 搬到对象存储；
再用 JuiceFS/ByteStore/3FS 理解 metadata/data separation 和 shared storage；
最后把这些抽象迁移到 KVCache offload 和 AI serving storage。
```
