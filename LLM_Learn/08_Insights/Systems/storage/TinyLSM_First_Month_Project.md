---
type: project_plan
track: RocksDB / LSM / Rust / TokaDB
status: active
created: 2026-06-28
local_repo: /home/yangshunlei/study/mini-lsm
local_pdf: /Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/mini-lsm/materials/LSM in a Week.pdf
upstream:
  - https://skyzh.github.io/mini-lsm/
  - https://github.com/skyzh/mini-lsm
---

# TinyLSM First Month Project

## 定位

7 月第一个动手项目用 `mini-lsm`，目标不是“写一个玩具 KV 就结束”，而是把 RocksDB/LSM 的核心机制写成可运行小内核，然后反向理解 TokaDB/RocksDB/TokaEngine。

但 7 月的上位代码主线不是纯 TinyLSM，而是：

```text
TokaDB TabletServer core path
+ mini-lsm/RocksDB LSM mechanism
```

也就是说，白天/晚间代码学习优先把 TabletServer RPC -> ReplicaManager -> Replica/FSM -> Engine 主链路画出来；mini-lsm 用来把 WAL、memtable、SST、compaction、manifest、recovery 这些机制写实。

本地路径：

```text
/home/yangshunlei/study/mini-lsm
```

本地课程 PDF：

```text
/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/mini-lsm/materials/LSM in a Week.pdf
```

PDF 概况：

- 标题：`LSM in a Week`
- 页数：133
- 来源：`https://skyzh.github.io/mini-lsm/print.html`
- 内容结构：Week 1 storage structure/format，Week 2 compaction and persistence，Week 3 MVCC。
- 本月读法：先把 PDF 当作 mini-lsm 的课程说明和任务索引，不逐页精读；每次进入代码任务时再回看对应章节。

开发入口：

```text
mini-lsm-starter/
```

参考实现：

```text
mini-lsm/
mini-lsm-mvcc/
```

常用命令：

```bash
cargo x install-tools
cargo x copy-test --week 1 --day 1
cargo x scheck
cargo run --bin mini-lsm-cli
cargo run --bin compaction-simulator
```

## 为什么适合作为 7 月项目

mini-lsm 的课程结构正好覆盖 RocksDB/LSM 最核心的路径：

```text
Week 1: Storage Format + Engine Skeleton
Week 2: Compaction and Persistence
Week 3: MVCC
```

它不是替代 TokaDB 代码阅读，而是作为“可控实验场”：

```text
mini-lsm 写机制
-> RocksDB 对照真实工程复杂度
-> TokaDB 对照业务系统封装和故障恢复
```

## 7 月执行方式

## 2026-06-29 用户校准

本月目标已明确为：

```text
学会 LSM 相关代码
+ TokaDB TabletServer 数据链路核心代码
+ RocksDB / LSM 相关代码学习
```

因此本文件是 7 月 P0 项目说明，而不是可选支线。执行顺序固定为：

```text
LSM in a Week / mini-lsm 机制
-> RocksDB/LSM 生产实现对照
-> TokaDB TabletServer 数据链路使用点
```

KVCache / 3FS / inference runtime 只保留为后续连接，不抢本月代码主线。

晚间执行口径：

```text
晚上主线 = mini-lsm / LSM 代码
顺手补 Rust = 只补代码里遇到的 ownership / iterator / Arc / Mutex / Result / tests
DeepSeek-V2 = 课外读物，20-40m，不抢 coding block
```

### W27：Memtable / Iterator + TokaDB Open-Close

mini-lsm：

- 1.1 Memtable
- 1.2 Merge Iterator
- 建立 Rust 项目编译、测试、CLI 基线

TokaDB：

- `TokaDB_RocksDB_OpenClose_Map`
- `Replica -> EngineFactory -> RocksdbEngine/TokaDBEngine -> DataStore`

输出：

- `TinyLSM_W1_Memtable_Iterator_Log`
- `TokaDB_RocksDB_OpenClose_Map`

验收：

- 能讲清 mutable memtable、immutable memtable、merge iterator 为什么是 LSM read path 的基础。
- 能讲清 TokaDB existing replica open 时为什么先看 `CURRENT`、OPTIONS、CF descriptors。

### W28：Block / SST / Read Path / Write Path

mini-lsm：

- 1.3 Block
- 1.4 SST
- 1.5 Read Path
- 1.6 Write Path
- 1.7 Prefix Key Encoding + Bloom Filters

TokaDB / RocksDB：

- 对照 RocksDB block format、block cache、Bloom/filter、iterator。
- 找 TokaDB TabletServer read/write 请求入口。

输出：

- `TinyLSM_Block_SST_ReadWrite_Note`
- `RocksDB_Read_Write_Path_Comparison`

验收：

- 能画出 point lookup 和 range scan 从 memtable 到 SST block 的路径。
- 能解释 Bloom/filter 为什么是 read amplification 控制点。

### W29：Compaction Strategy

mini-lsm：

- 2.1 Compaction Implementation
- 2.2 Simple Compaction
- 2.3 Tiered Compaction
- 2.4 Leveled Compaction

TokaDB / RocksDB：

- 对照 RocksDB leveled / universal compaction。
- 关注 L0 stalls、WAF/RAF/SAF、write stall、tail latency。

输出：

- `TinyLSM_Compaction_Strategies_Note`
- `RocksDB_Compaction_Deep_Dive`

验收：

- 能解释 compaction 为什么是 LSM 性能核心，也是 tail latency 风险源。
- 能讲清 leveled 和 universal/tiered 的 tradeoff。

### W30：Manifest / WAL / Batch / Recovery

mini-lsm：

- 2.5 Manifest
- 2.6 WAL
- 2.7 Batch Write and Checksums

TokaDB / RocksDB：

- 对照 TokaDB Open/Close、RocksDB `DB::Open` recovery、MANIFEST、WAL replay。
- 回看 close 前 flush 的意义。

输出：

- `TinyLSM_Manifest_WAL_Recovery_Note`
- `RocksDB_Open_Recovery_WAL_Note`

验收：

- 能讲清 crash 后如何从 manifest + WAL 恢复 memtable/SST view。
- 能解释为什么 Open/Close 是 recovery contract，不只是生命周期函数。

### W31：MVCC first pass + 月度复盘

mini-lsm：

- Week 3 MVCC 只做 first pass，不强求写完。
- 重点看 timestamp key encoding、snapshot read、watermark、compaction filter。

TokaDB：

- 回到 TokaDB TabletServer 的 read/write/txn/snapshot 相关路径，建立后续阅读入口。

输出：

- `TinyLSM_Month1_Project_Review`
- `TokaDB_RocksDB_LSM_Integration_Review`

验收：

- 能把 LSM 的 memtable/SST/WAL/manifest/compaction/snapshot 串成完整故事。
- 能说明 TinyLSM 和 TokaDB/RocksDB 的差异：toy engine 解决机制清晰，生产 engine 多了并发、配置、metrics、recovery、业务状态机。

## 和 TokaDB TabletServer 的连接

7 月做 TinyLSM 时，同时前移 TokaDB TabletServer 核心链路，不等到 8 月才开始。

7 月要形成第一版主链路：

```text
Tablet RPC / Admin RPC
-> ReplicaManager
-> Replica
-> ReplicaFsm
-> Consensus / Journal / Snapshot / Migration
-> Engine
```

要形成的 TokaDB 代码地图：

- `TabletServer_Request_Path_Index`
- `TabletServer_Request_Path_Map`
- `TokaDB_Read_Write_Path_Map`
- `Replica_Lifecycle_Open_Close_Recover_Map`
- `TokaDB_Locks_ThreadPool_Backpressure_Map`

8 月再把 TabletServer 链路中的 RPC、bthread、锁、线程池、backpressure 和 RocksDB 性能问题继续挖深。

## 和 Rust 的连接

mini-lsm 的 Rust 学习不是泛语法学习，而是围绕系统代码需要的几个点。建议单独维护一个轻量缺口清单：

```text
Rust_for_mini_lsm_Gap_List
```

只记录真实代码中遇到的问题，不开泛 Rust 全科。

- ownership：buffer / block / iterator / handle 生命周期。
- iterator trait object：RocksDB-style iterator 在 Rust 里如何组合。
- `Arc` / `Mutex` / background task：memtable、flush、compaction 的共享状态。
- error handling：storage engine 的错误边界。
- tests：用单测固定 engine invariant。

## 和共享存储的连接

mini-lsm 是本地 LSM。9 月再把它扩展到 shared/object storage 视角：

```text
mini-lsm: local disk LSM
SlateDB: LSM over object storage
Tonbo: Arrow/Parquet + LSM over object storage
JuiceFS: metadata/data separated POSIX FS over object storage
3FS: SSD + RDMA shared storage for AI workloads
```

这条线的核心问题：

- manifest / metadata 如何原子更新。
- immutable SST/chunk/block 如何放到共享存储。
- compaction / GC / recovery 如何避免破坏读一致性。
- client cache / metadata cache 如何失效。
- tail latency 如何被后台任务放大。

## 不做什么

7 月不做：

- 不从零自研一套完整 TinyLSM。
- 不把 MVCC 全写深。
- 不跑复杂 benchmark。
- 不提前深挖 3FS。

7 月只要做到：

```text
mini-lsm Week1+Week2 写通
TokaDB Open/Close 读通
RocksDB/LSM 核心机制讲通
```
