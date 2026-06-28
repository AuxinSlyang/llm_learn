---
type: current_execution_map
date_range: 2026-07_to_2027-04
target_role: AI Core Storage -> LLM Inference Runtime -> Robot/VLA Runtime
status: active
created: 2026-06-28
linked_files:
  - "[[00_North_Star]]"
  - "[[11_DeepSeek_Storage_to_Inference_to_Robot_Runtime_Roadmap]]"
  - "[[2026-07_to_2027-04_DeepSeek_Storage_Inference_月周计划]]"
  - "[[2026-07_to_2027-04_DeepSeek_Storage_Inference_详细周任务]]"
  - "[[TOREAD_Storage_Inference_2026H2_2027Q1]]"
---

# Current Execution Map: DeepSeek Storage + Inference

## 北极星

长期北极星仍然是：

```text
Robot/VLA Runtime / 机器人全栈工程师 / roboticist
```

但近期不直接硬切机器人。当前最稳路径是：

```text
DB / Storage Kernel
-> AI Core Storage / DeepSeek-style Storage
-> LLM Inference Runtime / KVCache / Serving
-> Robot/VLA Runtime
```

这个路径的逻辑：

- 当前最强资产是 TokaDB / DB kernel / storage / distributed systems。
- DeepSeek-style AI Core Storage 正好需要 KVCache、3FS、RDMA、SPDK、io_uring、RocksDB、FoundationDB、ByteStore 这类能力。
- 进入 AI Core Storage 后，再从 KVCache / serving / scheduler / MoE / long context 回接 LLM inference runtime。
- 机器人保留为长期 North Star，等行业和个人系统能力都成熟后再切。

## 年度窗口

当前职业节奏：

```text
2026-07 ~ 2026-12：完整准备期
2027-01 ~ 2027-02：正式面试窗口
2027-03：拿完年终奖后决策
2027-04：理想入职窗口
```

这比 2026-09/10 硬冲更稳。原因是我们不只要会说 storage，还要能把：

```text
TokaDB
RocksDB
ByteStore
brpc
IO path
3FS
KVCache
vLLM / SGLang / Mooncake / LMCache
DeepSeek V2/V3/R1
```

串成一条可深挖的系统能力链。

## 月计划

| 月份 | 主线 | 目标 |
|---|---|---|
| 2026-07 | TokaDB TabletServer 核心链路 + mini-lsm/RocksDB 核心学习 | 以 TabletServer RPC -> ReplicaManager -> Replica/FSM -> Engine 为代码主线，用 mini-lsm/RocksDB 补 LSM 机制 |
| 2026-08 | ByteStore 初窥 + RocksDB 深入 + brpc/bthread 深入 | 建立 ByteStore 基本模型，深入 RocksDB perf/compaction/options，并把 brpc/bthread/tail latency 补扎实 |
| 2026-09 | ByteStore & 3FS 结合 + IO Path | 对照 ByteStore IO path 和 3FS IO path，把 io_uring/SPDK/RDMA/metadata/data movement 串起来 |
| 2026-10 | KVCache Storage + 推理代码接入 | 从 storage 视角接入 KVCache，开始读 vLLM/LMCache/Mooncake 核心代码 |
| 2026-11 | LLM inference runtime 深入 | 补齐 vLLM、SGLang、scheduler、continuous batching、request path、prefix cache |
| 2026-12 | DeepSeek + 外部系统思路变化 | 读 DeepSeek V2/V3/R1，并跟踪 Mooncake/LMCache/SGLang/OSDI/SOSP 这类系统变化 |
| 2027-01 | 综合分析 + 面试材料生产 | 简历、5 个系统故事、3 个系统设计题、刷题节奏、mock；材料冻结 |
| 2027-02 | 春节后投递 + 正式面试 + 补洞 | 春节后集中投递，根据反馈补 C++、IO/RDMA、KVCache、inference runtime |
| 2027-03 | 年终奖后决策 | offer / 团队 / 方向 / 年终奖 / 成长路径决策 |
| 2027-04 | 入职或第二轮推进 | 入职则 30 天上手真实系统；未入职则继续第二轮 |

## 周计划总表

| Week | 日期 | 主线 | 产出 |
|---|---|---|---|
| W27 | 2026-06-29 ~ 07-05 | TabletServer 入口索引 + TinyLSM setup | `TabletServer_Request_Path_Index`、`TinyLSM_W1_Memtable_Iterator_Log` |
| W28 | 2026-07-06 ~ 07-12 | Tablet read/write path + TinyLSM Block/SST | `TabletServer_Read_Write_Path_Map`、`TinyLSM_Block_SST_ReadWrite_Note` |
| W29 | 2026-07-13 ~ 07-19 | Replica lifecycle + RocksDB compaction | `Replica_Lifecycle_Open_Close_Recover_Map`、`RocksDB_Compaction_Deep_Dive` |
| W30 | 2026-07-20 ~ 07-26 | TabletServer 核心链路收口 + WAL/Manifest/Recovery | `TabletServer_Request_Path_Map`、`TinyLSM_Manifest_WAL_Recovery_Note` |
| W31 | 2026-07-27 ~ 08-02 | 7 月复盘：TabletServer + mini-lsm/RocksDB | `TinyLSM_Month1_Project_Review`、`TokaDB_RocksDB_LSM_Integration_Review` |
| W32 | 2026-08-03 ~ 08-09 | ByteStore first pass + RocksDB 深入 1 | `ByteStore_Component_Map_v0`、`RocksDB_Options_CF_Iterator_Note` |
| W33 | 2026-08-10 ~ 08-16 | brpc / bthread 深入 1 | `brpc_bthread_Model_Note` |
| W34 | 2026-08-17 ~ 08-23 | brpc / bthread 深入 2 + 锁优化 | `TokaDB_Locks_ThreadPool_Backpressure_Map`、`brpc_Perf_Debug_Playbook` |
| W35 | 2026-08-24 ~ 08-30 | ByteStore 初窥收口 + RocksDB 深入 2 | `ByteStore_Shared_Storage_Map_v0`、`RocksDB_Deep_Dive_Note` |
| W36 | 2026-08-31 ~ 09-06 | ByteStore IO path | `ByteStore_IO_Path_Map` |
| W37 | 2026-09-07 ~ 09-13 | 3FS architecture + IO path first pass | `3FS_Architecture_First_Pass`、`3FS_IO_Path_Skeleton` |
| W38 | 2026-09-14 ~ 09-20 | ByteStore vs 3FS metadata / consistency | `ByteStore_3FS_Metadata_Consistency_Comparison` |
| W39 | 2026-09-21 ~ 09-27 | io_uring / SPDK / RDMA core path | `IO_Path_io_uring_SPDK_RDMA_Note_v0`、`TinySharedStorage_Design_v0` |
| W40 | 2026-09-28 ~ 10-04 | ByteStore & 3FS IO Path 月度收口 | `ByteStore_3FS_IO_Path_Comparison`、`3FS_IO_Path_RDMA_SSD_Note` |
| W41 | 2026-10-05 ~ 10-11 | KVCache block/page/tiering | `KVCache_Storage_System_Map_v0` |
| W42 | 2026-10-12 ~ 10-18 | LMCache / KV movement / offload | `LMCache_KVCache_Layer_Note` |
| W43 | 2026-10-19 ~ 10-25 | Mooncake / DistServe disaggregation | `Mooncake_DistServe_Disaggregation_Note` |
| W44 | 2026-10-26 ~ 11-01 | KVCache storage system design | `KVCache_Storage_System_Design_v0` |
| W45 | 2026-11-02 ~ 11-08 | vLLM scheduler / block manager | `vLLM_PagedAttention_KVCache_Scan` |
| W46 | 2026-11-09 ~ 11-15 | LLM serving request path | `LLM_Inference_Request_Path_v0` |
| W47 | 2026-11-16 ~ 11-22 | SGLang / RadixAttention / prefix cache | `SGLang_RadixCache_Note` |
| W48 | 2026-11-23 ~ 11-29 | Inference system map | `LLM_Inference_System_First_Pass` |
| W49 | 2026-11-30 ~ 12-06 | DeepSeek-V2 / MLA / MoE | `DeepSeek_V2_MLA_MoE_Note` |
| W50 | 2026-12-07 ~ 12-13 | DeepSeek-V3 system note | `DeepSeek_V3_System_Note` |
| W51 | 2026-12-14 ~ 12-20 | DeepSeek-R1 reasoning workload | `DeepSeek_R1_Inference_Workload_Note` |
| W52 | 2026-12-21 ~ 12-27 | MoE / long context serving | `MoE_Long_Context_Serving_Note` |
| W53 | 2026-12-28 ~ 01-03 | 年终复盘 | `2026_Storage_Inference_Year_End_Review` |
| W01 | 2027-01-04 ~ 01-10 | 简历 v0 | `AI_Core_Storage_Resume_v0` |
| W02 | 2027-01-11 ~ 01-17 | 5 个系统故事 | `5_System_Stories_v0` |
| W03 | 2027-01-18 ~ 01-24 | 3 个系统设计题 | `System_Design_Pack_v0` |
| W04 | 2027-01-25 ~ 01-31 | 材料冻结 + 小规模沟通 | `Interview_Materials_v0` |
| W05 | 2027-02-01 ~ 02-07 | 春节周轻量补洞 | `Cpp_Systems_Gap_Fix_List` |
| W06 | 2027-02-08 ~ 02-14 | 春节后投递启动 + IO/RDMA 补洞 | `Interview_Pipeline_Log_v0`、`IO_RDMA_Interview_QA` |
| W07 | 2027-02-15 ~ 02-21 | Inference runtime 补洞 | `Inference_Interview_QA` |
| W08 | 2027-02-22 ~ 02-28 | 第二轮材料 | `Interview_Materials_v1` |
| W09 | 2027-03-01 ~ 03-07 | offer / 团队判断 | `Offer_Decision_Table_v0` |
| W10 | 2027-03-08 ~ 03-14 | 决策收口 | `Career_Decision_Log` |
| W11 | 2027-03-15 ~ 03-21 | 入职准备或第二轮投递 | `Onboarding_Prep_or_Second_Round_v0` |
| W12 | 2027-03-22 ~ 03-28 | 交接 / 归档 | `Transition_Checklist` |
| W13 | 2027-03-29 ~ 04-04 | 30/60/90 天计划 | `First_30_60_90_Days_Plan` |
| W14 | 2027-04-05 ~ 04-11 | 入职窗口 | `First_30_Days_AI_Infra_Onboarding` |

## 每周固定格式

每周只保 4 个交付：

- 系统图：组件、数据流、状态流或 IO path。
- 结构化笔记：代码路径、论文或系统设计。
- 面试化问题：一个能讲 5-10 分钟的问题。
- 下周 gap list：还没懂什么，下一步看哪里。

## 每日节奏

| 时间 | 内容 | 规则 |
|---|---|---|
| 10:00-12:00 | 昨晚收口 + 杂事处理 | 只清尾巴，不开新坑 |
| 14:00-18:00 | 工作 / 写代码 / 测试 / 看代码 | 优先服务 TokaDB 工作，同时抽象可迁移系统点 |
| 19:00-21:00 | 代码学习 | 一次只看一个模块或一条调用链 |
| 22:00-24:00 | 论文 / 课程 / DDIA / CS336 | 只读能解释当前系统问题的材料 |

## 当前 TOREAD 主线

近期论文阅读顺序：

```text
TokaDB TabletServer + mini-lsm / RocksDB / LSM docs
-> Sarathi-Serve / DistServe / Orca / ServerlessLLM
-> ByteStore + classic distributed systems papers
-> brpc / bthread / high-performance programming notes
-> 3FS + Fire-Flyer AI-HPC + FoundationDB / CRAQ
-> KVCache / PagedAttention / LMCache / Mooncake / DistServe
-> DeepSeek-V3 / R1
```

完整清单见：[[TOREAD_Storage_Inference_2026H2_2027Q1]]

## 2027-01 面试前必须有的材料

- `TokaDB_Transferable_Systems_Review_v0`
- `RocksDB_LSM_Refresh`
- `ByteStore_Shared_Storage_Map_v0`
- `brpc_Systems_Model_Note`
- `IO_Path_io_uring_SPDK_RDMA_Note_v0`
- `3FS_Architecture_First_Pass`
- `3FS_IO_Path_RDMA_SSD_Note`
- `KVCache_Storage_System_Map_v0`
- `vLLM_PagedAttention_KVCache_Scan`
- `LLM_Inference_System_First_Pass`
- `DeepSeek_V2_MLA_MoE_Note`
- `DeepSeek_R1_Inference_Workload_Note`
- `AI_Core_Storage_Resume_v0`
- `5_System_Stories_v0`
- `System_Design_Pack_v0`

## 一句话回锚

> 2026-H2 不追热点，不直接硬切机器人；先把 TokaDB / Storage 基本盘升级成 AI Core Storage，再用 KVCache / vLLM / 3FS / DeepSeek systems 补齐 LLM inference runtime，2027-01/02 开始面试，2027-04 争取入职。
