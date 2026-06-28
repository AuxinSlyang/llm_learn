---
type: phase_plan
date_range: 2026-07_to_2027-04
target_role: AI Core Storage -> LLM Inference Runtime -> Robot/VLA Runtime
scenario_anchor: DeepSeek Storage + 3FS + KVCache + LLM Inference Systems
status: active
linked_roadmap:
  - [[11_DeepSeek_Storage_to_Inference_to_Robot_Runtime_Roadmap]]
  - [[2026-06-28_DeepSeek_Storage_Inference_Interview_Plan_2027Q1]]
---

# 2026-07 到 2027-04 DeepSeek Storage + Inference 月周计划

## 总目标

目标窗口：

```text
2027-01/02：开始正式面试
2027-03：拿完年终奖后做决策
2027-04：理想入职窗口
```

主线不是泛学 AI Infra，而是：

```text
TokaDB / DB storage kernel
-> AI Core Storage / ByteStore / 3FS / KVCache Storage
-> LLM Inference Runtime / vLLM / SGLang / Mooncake / DeepSeek systems
-> long-term Robot/VLA Runtime
```

## 月计划

| 月份 | 主线 | 最低完成线 | 核心产出 |
|---|---|---|---|
| 2026-07 | TokaDB TabletServer 核心链路 + mini-lsm/RocksDB 核心学习 | 能画出 TabletServer RPC -> ReplicaManager -> Replica -> ReplicaFsm -> Engine 主链路；mini-lsm Week1+Week2 写通主要机制；RocksDB WAL/memtable/SST/compaction/open-recovery 形成对照 | `TabletServer_Request_Path_Map`、`TinyLSM_First_Month_Project`、`RocksDB_LSM_Refresh` |
| 2026-08 | ByteStore 初窥 + RocksDB 深入 + brpc/bthread 深入 | 能讲清 ByteStore 基本模型；能深入 RocksDB compaction/options/iterator/perf；能解释 brpc/bthread/RPC latency、bvar、rpcz、backpressure；复习经典系统论文 | `ByteStore_Shared_Storage_Map_v0`、`RocksDB_Deep_Dive_Note`、`brpc_bthread_Model_Note` |
| 2026-09 | ByteStore & 3FS 结合 + IO Path | 对照 ByteStore IO path 和 3FS IO path；能讲清 metadata/data path、chunk/blob、FUSE/USRBIO/RDMA/SSD、io_uring/SPDK/RDMA 在高性能存储链路中的位置 | `ByteStore_IO_Path_Map`、`3FS_IO_Path_RDMA_SSD_Note`、`ByteStore_3FS_IO_Path_Comparison` |
| 2026-10 | KVCache Storage + 推理代码接入 | 从 storage 视角接入 KVCache：prefill/decode、block/page、prefix reuse、offload、HBM/DRAM/SSD tier；开始读 vLLM/LMCache/Mooncake 核心代码 | `KVCache_Storage_System_Map_v0`、`LMCache_KVCache_Layer_Note`、`Mooncake_DistServe_Disaggregation_Note` |
| 2026-11 | LLM inference runtime 深入 | 能讲清 vLLM/SGLang request path、scheduler、continuous batching、KV cache manager、token streaming、prefix cache；形成推理系统全图 | `vLLM_PagedAttention_KVCache_Scan`、`SGLang_RadixCache_Note`、`LLM_Inference_System_First_Pass` |
| 2026-12 | DeepSeek + 外部系统思路变化 | 能讲清 DeepSeek V2/V3/R1 的 MLA/MoE/reasoning workload 对 serving 和 KVCache 的影响；同步外部 Mooncake/LMCache/SGLang/OSDI/SOSP 系统趋势 | `DeepSeek_Inference_System_Reading_Map`、`MoE_Long_Context_Serving_Note`、`External_Inference_System_Trends_2026Q4` |
| 2027-01 | 综合分析 + 面试材料生产 | 系统故事、系统设计、简历主叙事、刷题节奏、C++/系统基础补洞；先冻结材料，不急着大规模投递 | `AI_Core_Storage_Resume_v0`、`5_System_Stories_v0`、`System_Design_Pack_v0`、`Coding_Interview_Plan_v0` |
| 2027-02 | 春节后投递 + 正式面试 + 补洞 | 2027 春节后启动集中投递；根据面试反馈补 C++/Rust/IO/RDMA/serving；持续 mock 和材料迭代 | `Interview_Pipeline_Log_v0`、`Interview_Review_Log`、`Gap_Fix_List` |
| 2027-03 | 年终奖后决策 | offer / 团队 / 方向 / 薪资 / 年终奖损失 / 成长路径决策表 | `2027_Q1_Offer_Decision_Table`、`Onboarding_or_Second_Round_Plan` |
| 2027-04 | 入职或第二轮推进 | 入职则 30 天补真实系统；未入职则继续投 AI Core Storage / KVCache / LLM Infra | `First_30_Days_AI_Infra_Onboarding` 或 `Second_Round_Interview_Plan` |

## 周计划

| Week | 日期 | 主线 | 代码 / 系统 | 夜间论文 / 课程 | 周产出 |
|---|---|---|---|---|---|
| W27 | 2026-06-29 ~ 07-05 | TabletServer 入口索引 + TinyLSM setup | Tablet RPC/Admin RPC 入口、ReplicaManager、Replica/FSM 初索引；mini-lsm 1.1/1.2 | 本地 LLM TOREAD 总览；Sarathi-Serve scan | `TabletServer_Request_Path_Index`、`TinyLSM_W1_Memtable_Iterator_Log` |
| W28 | 2026-07-06 ~ 07-12 | Tablet read/write path + TinyLSM Block/SST | TabletServer read/write 入口到 Replica/FSM/Engine；mini-lsm 1.3-1.7；RocksDB read/write path | DistServe、Orca / continuous batching | `TabletServer_Read_Write_Path_Map`、`TinyLSM_Block_SST_ReadWrite_Note` |
| W29 | 2026-07-13 ~ 07-19 | Replica lifecycle + RocksDB compaction | Replica open/close/recover、Consensus/Journal/Snapshot 边界；mini-lsm 2.1-2.4；RocksDB compaction | PagedAttention revisit、SGLang/RadixAttention scan | `Replica_Lifecycle_Open_Close_Recover_Map`、`RocksDB_Compaction_Deep_Dive` |
| W30 | 2026-07-20 ~ 07-26 | TabletServer 核心链路收口 + WAL/Manifest/Recovery | mini-lsm 2.5-2.7；RocksDB Open/Recovery；TokaDB close/flush/reopen；TabletServer 主链路图 | FlashAttention、DeepSeek-V2 MLA/KVCache sections | `TabletServer_Request_Path_Map`、`TinyLSM_Manifest_WAL_Recovery_Note` |
| W31 | 2026-07-27 ~ 08-02 | 7 月复盘：TabletServer + mini-lsm/RocksDB | mini-lsm Week3 first pass；TokaDB/RocksDB options、CF、metrics、failure cases；整理 8 月 gap | OSDI 2026 KV Cache session watchlist | `TinyLSM_Month1_Project_Review`、`TokaDB_RocksDB_LSM_Integration_Review` |
| W32 | 2026-08-03 ~ 08-09 | ByteStore first pass + RocksDB 深入 1 | ByteStore client/meta/chunkserver/blob/chunk 初索引；RocksDB options/CF/iterator/cache/metrics | GFS、Bigtable refresh | `ByteStore_Component_Map_v0`、`RocksDB_Options_CF_Iterator_Note` |
| W33 | 2026-08-10 ~ 08-16 | brpc / bthread 深入 1 | brpc server/client/channel/controller/closure、bthread、bvar、rpcz、backup request | Dynamo、Spanner refresh | `brpc_bthread_Model_Note`、`Classic_Distributed_Systems_Refresh_W33` |
| W34 | 2026-08-17 ~ 08-23 | brpc / bthread 深入 2 + 锁优化 | TokaDB mutex/RWLock/threadpool/queue/backpressure 热点；bthread 调度；RPC timeout/retry | 高性能编程、锁优化、tail latency 材料 | `TokaDB_Locks_ThreadPool_Backpressure_Map`、`brpc_Perf_Debug_Playbook` |
| W35 | 2026-08-24 ~ 08-30 | ByteStore 初窥收口 + RocksDB 深入 2 | ByteStore metadata/replication/recovery；RocksDB compaction/perf/write stall；ByteStore 和 RocksDB 能力对照 | FoundationDB / CRAQ 预读 | `ByteStore_Shared_Storage_Map_v0`、`RocksDB_Deep_Dive_Note` |
| W36 | 2026-08-31 ~ 09-06 | ByteStore IO path | ByteStore client -> metadata -> blob/chunk/chunkserver 数据路径；page cache/direct IO/io_uring 初步 | Fire-Flyer AI-HPC | `ByteStore_IO_Path_Map` |
| W37 | 2026-09-07 ~ 09-13 | 3FS architecture + IO path first pass | 3FS client/mgmtd/meta/storage/FUSE/USRBIO/FDB；FUSE/USRBIO/RDMA/SSD 路径 | 3FS design notes | `3FS_Architecture_First_Pass`、`3FS_IO_Path_Skeleton` |
| W38 | 2026-09-14 ~ 09-20 | ByteStore vs 3FS metadata / consistency | ByteStore metadata/placement/replication 对照 3FS meta/FDB/CRAQ/ChainTable | FoundationDB、CRAQ | `ByteStore_3FS_Metadata_Consistency_Comparison` |
| W39 | 2026-09-21 ~ 09-27 | io_uring / SPDK / RDMA core path | syscall/copy/interrupt/polling/queue depth/memory registration；ByteStore/3FS IO path 回填 | DDIA Ch5/Ch8 + IO path notes | `IO_Path_io_uring_SPDK_RDMA_Note_v0`、`TinySharedStorage_Design_v0` |
| W40 | 2026-09-28 ~ 10-04 | ByteStore & 3FS IO Path 月度收口 | 两套系统 IO path、metadata path、failure/recovery、性能瓶颈对照 | 3FS / Fire-Flyer / classic storage review | `ByteStore_3FS_IO_Path_Comparison`、`3FS_IO_Path_RDMA_SSD_Note` |
| W41 | 2026-10-05 ~ 10-11 | KVCache model | prefill/decode、block/page、HBM/DRAM/SSD tier | PagedAttention deep read | `KVCache_Storage_System_Map_v0` |
| W42 | 2026-10-12 ~ 10-18 | KVCache offload | LMCache/Mooncake/remote KV movement | LMCache | `LMCache_KVCache_Layer_Note` |
| W43 | 2026-10-19 ~ 10-25 | Disaggregated serving | prefill/decode disaggregation、TTFT/TPOT | Mooncake / DistServe | `Mooncake_DistServe_Disaggregation_Note` |
| W44 | 2026-10-26 ~ 11-01 | KVCache system design | 45-60 分钟系统设计演练 | CacheGen / KV compression | `KVCache_Storage_System_Design_v0` |
| W45 | 2026-11-02 ~ 11-08 | vLLM first pass | scheduler、block manager、KV cache manager | vLLM docs/code | `vLLM_PagedAttention_KVCache_Scan` |
| W46 | 2026-11-09 ~ 11-15 | Serving request path | HTTP/RPC -> scheduler -> prefill/decode -> streaming | Orca / continuous batching | `LLM_Inference_Request_Path_v0` |
| W47 | 2026-11-16 ~ 11-22 | SGLang / prefix cache | radix cache、structured generation、cache-aware scheduling | SGLang paper | `SGLang_RadixCache_Note` |
| W48 | 2026-11-23 ~ 11-29 | Inference system map | vLLM/SGLang/LMCache/Mooncake 对照 | CS336 inference/serving lectures | `LLM_Inference_System_First_Pass` |
| W49 | 2026-11-30 ~ 12-06 | DeepSeek V2/V3 | MLA、MoE、KV cache compression、expert routing | DeepSeek-V2 | `DeepSeek_V2_MLA_MoE_Note` |
| W50 | 2026-12-07 ~ 12-13 | DeepSeek V3 | auxiliary-loss-free load balance、MTP、inference implications | DeepSeek-V3 | `DeepSeek_V3_System_Note` |
| W51 | 2026-12-14 ~ 12-20 | DeepSeek R1 workload | reasoning RL、long CoT、serving cost、KV pressure | DeepSeek-R1 | `DeepSeek_R1_Inference_Workload_Note` |
| W52 | 2026-12-21 ~ 12-27 | MoE / long context serving | expert parallel、routing、load balance、long context memory | Switch / Mixtral selective | `MoE_Long_Context_Serving_Note` |
| W53 | 2026-12-28 ~ 01-03 | 年终复盘 | 产出材料盘点，确定 1 月投递版本 | 复盘，不开新论文 | `2026_Storage_Inference_Year_End_Review` |
| W01 | 2027-01-04 ~ 01-10 | 简历 v0 | AI Core Storage 简历、项目故事骨架 | 面试题复盘 | `AI_Core_Storage_Resume_v0` |
| W02 | 2027-01-11 ~ 01-17 | 系统故事 | zero-copy/shared storage/RocksDB/3FS/KVCache 五故事 | mock 1 | `5_System_Stories_v0` |
| W03 | 2027-01-18 ~ 01-24 | 系统设计 | KVCache storage、AI shared storage、LLM serving runtime | mock 2 | `System_Design_Pack_v0` |
| W04 | 2027-01-25 ~ 01-31 | 材料冻结 + 小规模沟通 | 简历、系统故事、系统设计、刷题节奏冻结；少量内推预沟通 | 轻阅读 | `Interview_Materials_v0` |
| W05 | 2027-02-01 ~ 02-07 | 春节周轻量补洞 | C++ systems、并发、内存、RPC、性能分析；不安排重负载 | 复盘 | `Cpp_Systems_Gap_Fix_List` |
| W06 | 2027-02-08 ~ 02-14 | 春节后投递启动 + IO/RDMA 补洞 | 内推、岗位沟通、面试反馈表；RDMA/SPDK/io_uring 常见问答 | 面试复盘 | `Interview_Pipeline_Log_v0`、`IO_RDMA_Interview_QA` |
| W07 | 2027-02-15 ~ 02-21 | 面试 + inference 补洞 | vLLM/SGLang/KVCache/MoE 常见问答 | 面试复盘 | `Inference_Interview_QA` |
| W08 | 2027-02-22 ~ 02-28 | 第二轮材料 | 根据反馈更新简历和系统设计 | 轻阅读 | `Interview_Materials_v1` |
| W09 | 2027-03-01 ~ 03-07 | offer / 团队判断 | 团队、方向、薪资、年终奖损失评估 | 不开新坑 | `Offer_Decision_Table_v0` |
| W10 | 2027-03-08 ~ 03-14 | 决策收口 | 继续谈 / 拒 / 接 / 观望策略 | 不开新坑 | `Career_Decision_Log` |
| W11 | 2027-03-15 ~ 03-21 | 入职前准备 | 若确定入职，补目标团队系统；否则二轮投递 | 定向阅读 | `Onboarding_Prep_or_Second_Round_v0` |
| W12 | 2027-03-22 ~ 03-28 | 交接 / 稳定 | 当前工作交接风险、材料归档 | 轻阅读 | `Transition_Checklist` |
| W13 | 2027-03-29 ~ 04-04 | 入职前最后检查 | 30/60/90 天目标 | 不开新坑 | `First_30_60_90_Days_Plan` |
| W14 | 2027-04-05 ~ 04-11 | 入职窗口 | 代码、指标、oncall、核心 owner 边界 | 入职学习 | `First_30_Days_AI_Infra_Onboarding` |

## 固定日节奏

| 时间 | 用途 | 规则 |
|---|---|---|
| 10:00-12:00 | 昨晚收口 + 杂事 + 计划整理 | 不开新大坑，只清尾巴 |
| 14:00-18:00 | 工作 / 写代码 / 测试 / 看业务代码 | 优先服务当前 TokaDB 工作，同时抽象可迁移系统点 |
| 19:00-21:00 | 代码学习 | 只看一条代码路径或一个模块 |
| 22:00-24:00 | 论文 / 课程 / DDIA / CS336 | 只读能解释当前代码和系统问题的材料 |

## 今晚安排

目标：确认计划后，先把 W27 的代码主线立住，再读一篇 LLM serving 论文。

```text
19:00-20:00：确认本计划、TOREAD 队列、OSDI reading pack
20:00-21:00：读 [[TokaDB_RocksDB_OpenClose_Map]]，标出明天要进源码验证的 5 个点
22:00-24:00：读 Sarathi-Serve structured scan
```

今晚只回答 5 个问题：

- 一个 existing replica open 时，TokaDB/RocksDB 从 `CURRENT` 到 CF handles 的路径是什么？
- close 前为什么要 `PrepareClose -> FlushAllCFStrategy`？
- Sarathi-Serve 为什么要做 chunked prefill？
- prefill/decode 的 TTFT、TPOT、throughput 为什么互相牵制？
- 这套 serving scheduler 问题，和 RocksDB compaction / flush / tail latency 的共同抽象是什么？

## 2026-06-28 校准：前三个月项目化

已知内容：

- TokaDB table / tablet / replication group / migration 已有基础理解。
- PagedAttention / vLLM 已经看过一轮。
- mini-lsm 本地已经位于 `/home/yangshunlei/study/mini-lsm`，适合作为 7 月 Rust + LSM 项目。
- 3FS 本地已经位于 `/home/yangshunlei/study/3FS`，但它是 C++ 为主，Rust 只覆盖少量组件；不能把 3FS 当 Rust 主项目。

因此前三个月调整为：

```text
2026-07：TokaDB TabletServer 核心链路 + mini-lsm/RocksDB 核心学习
2026-08：ByteStore 初窥 + RocksDB 深入 + brpc/bthread 深入
2026-09：ByteStore & 3FS IO path 结合 + io_uring/SPDK/RDMA 核心链路
```
