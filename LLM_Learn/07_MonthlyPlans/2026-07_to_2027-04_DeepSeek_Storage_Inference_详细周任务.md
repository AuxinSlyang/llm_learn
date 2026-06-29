---
type: detailed_weekly_plan
date_range: 2026-07_to_2027-04
target_role: AI Core Storage -> LLM Inference Runtime -> Robot/VLA Runtime
status: active
linked_plan:
  - [[2026-07_to_2027-04_DeepSeek_Storage_Inference_月周计划]]
---

# 2026-07 到 2027-04 DeepSeek Storage + Inference 详细周任务

## 每周固定交付

每周不追求读很多，只保 4 个可检查结果：

1. 一张系统图：组件、数据流、状态流或 IO path。
2. 一篇结构化笔记：论文、代码路径或系统设计。
3. 一个可讲 5-10 分钟的问题：面试化表达。
4. 一个下周 gap list：还没懂什么，下一步看哪里。

## 2026-07：TokaDB TabletServer 核心链路 + mini-lsm/RocksDB 核心学习

### W27：2026-06-29 ~ 2026-07-05

- 项目主线：mini-lsm 1.1 Memtable、1.2 Merge Iterator；建立 Rust 项目编译、测试、CLI 基线。
- 代码主线：TokaDB TabletServer 入口索引：Tablet RPC / Admin RPC、ReplicaManager、Replica、ReplicaFsm、EngineFactory；同时保留 `RocksdbEngine::Open/Close` / `TokaDBEngine::Open` 作为 engine 入口。
- 论文 / 课程：`LSM in a Week.pdf` Preface / Course Overview / Write Path / Read Path；不排 Sarathi-Serve。
- 输出物：`TabletServer_Request_Path_Index`、`TinyLSM_W1_Memtable_Iterator_Log`、`RocksDB_LSM_Refresh_v0`。
- 验收问题：一个 TabletServer read/write/admin 请求从 RPC 入口到 Replica/FSM/Engine 的入口在哪里？mini-lsm 的 memtable / merge iterator 如何支撑 read path？

### W28：2026-07-06 ~ 2026-07-12

- 项目主线：mini-lsm 1.3 Block、1.4 SST、1.5 Read Path、1.6 Write Path、1.7 Prefix Key Encoding + Bloom Filters。
- 代码主线：TabletServer read/write path：RPC handler -> ReplicaManager -> Replica -> ReplicaFsm -> Engine；对照 RocksDB block format、Bloom/filter、block cache、iterator、WAL、WriteBatch、memtable、flush。
- 论文 / 课程：RocksDB docs / wiki 中与 block、SST、iterator、Bloom/filter、WAL、WriteBatch 直接相关的材料；不排 serving 论文。
- 输出物：`TabletServer_Read_Write_Path_Map`、`TinyLSM_Block_SST_ReadWrite_Note`、`RocksDB_Read_Write_Path_Comparison`。
- 验收问题：一条 write 如何从 TabletServer mutation 走到 Replica/FSM/Engine，再变成 RocksDB WriteBatch / WAL / memtable？一次 point lookup 和 range scan 如何从 memtable 走到 SST block？

### W29：2026-07-13 ~ 2026-07-19

- 项目主线：mini-lsm 2.1 Compaction Implementation、2.2 Simple Compaction、2.3 Tiered Compaction、2.4 Leveled Compaction。
- 代码主线：Replica lifecycle：open / close / recover、Consensus / Journal / Snapshot / Migration 边界；对照 RocksDB leveled / universal compaction、L0 stalls、write stall、WAF/RAF/SAF。
- 论文 / 课程：RocksDB compaction / write stall / amplification 相关文档和源码注释；不排 PagedAttention / SGLang。
- 输出物：`Replica_Lifecycle_Open_Close_Recover_Map`、`TinyLSM_Compaction_Strategies_Note`、`RocksDB_Compaction_Deep_Dive`。
- 验收问题：Replica 生命周期和 Engine 生命周期怎么绑定？Compaction 为什么既是 RocksDB 性能核心，也是 tail latency 风险源？

### W30：2026-07-20 ~ 2026-07-26

- 项目主线：mini-lsm 2.5 Manifest、2.6 WAL、2.7 Batch Write and Checksums。
- 代码主线：TabletServer 核心链路收口；RocksDB Open/Recovery、WAL replay、MANIFEST、TokaDB close/flush/reopen；回看 close 前 flush 的意义。
- 论文 / 课程：RocksDB recovery / MANIFEST / WAL / column family options；DeepSeek-V2 只保留为 KVCache 背景，不作为本周阅读任务。
- 输出物：`TabletServer_Request_Path_Map`、`TinyLSM_Manifest_WAL_Recovery_Note`、`RocksDB_Open_Recovery_WAL_Note`。
- 验收问题：crash 后如何从 manifest + WAL 恢复 memtable/SST view？TabletServer 主链路里哪些状态由 Replica/FSM 管，哪些状态由 Engine/RocksDB 管？

### W31：2026-07-27 ~ 2026-08-02

- 项目主线：mini-lsm Week3 MVCC first pass：timestamp key encoding、snapshot read、watermark、compaction filter。
- 代码主线：7 月复盘：TabletServer core path、Replica lifecycle、TokaDB/RocksDB options、column families、open/recovery、read/write/compaction、metrics、failure cases。
- 论文 / 课程：OSDI 2026 KV Cache session watchlist 整理。
- 输出物：`TinyLSM_Month1_Project_Review`、`TokaDB_RocksDB_LSM_Integration_Review`、`TabletServer_Core_Path_Review`。
- 验收问题：如果让你负责一个 TokaDB TabletServer / RocksDB-style storage engine 的性能问题，你会先看哪些指标、哪些配置、哪些路径？TinyLSM 和 TokaDB/RocksDB 的工程差异在哪里？

## 2026-08：ByteStore 初窥 + RocksDB 深入 + brpc/bthread 深入

### W32：2026-08-03 ~ 2026-08-09

- 代码主线：ByteStore first pass：client、meta、chunkserver、blob、chunk、replication 初索引；RocksDB 深入 1：options、column family、iterator、cache、metrics。
- 论文 / 课程：GFS、Bigtable refresh。
- 输出物：`ByteStore_Component_Map_v0`、`RocksDB_Options_CF_Iterator_Note`。
- 验收问题：ByteStore 的基本数据模型是什么？RocksDB options / CF / iterator / cache 如何决定线上行为？

### W33：2026-08-10 ~ 2026-08-16

- 代码主线：brpc / bthread 深入 1：server、client、channel、controller、closure、bthread、bvar、rpcz、backup request。
- 论文 / 课程：Dynamo、Spanner refresh。
- 输出物：`brpc_bthread_Model_Note`、`Classic_Distributed_Systems_Refresh_W33`。
- 验收问题：RPC latency、serialization、bthread scheduling、backpressure、observability 如何影响 storage / serving tail latency？

### W34：2026-08-17 ~ 2026-08-23

- 代码主线：brpc / bthread 深入 2 + 锁优化：TokaDB mutex/RWLock/threadpool/queue/backpressure 热点；bthread 调度；RPC timeout/retry。
- 论文 / 课程：高性能编程、锁优化、tail latency 材料。
- 输出物：`TokaDB_Locks_ThreadPool_Backpressure_Map`、`brpc_Perf_Debug_Playbook`。
- 验收问题：怎么判断一个性能问题来自锁竞争、线程池排队、IO backpressure、RPC 超时，还是 compaction/flush 后台任务？

### W35：2026-08-24 ~ 2026-08-30

- 代码主线：ByteStore 初窥收口 + RocksDB 深入 2：ByteStore metadata、replication、recovery；RocksDB compaction/perf/write stall；ByteStore 和 RocksDB 能力对照。
- 论文 / 课程：FoundationDB / CRAQ 预读。
- 输出物：`ByteStore_Shared_Storage_Map_v0`、`RocksDB_Deep_Dive_Note`。
- 验收问题：ByteStore 的 blob / chunk / metadata / replication 如何迁移到 AI shared storage 叙事？RocksDB 的 compaction/perf/write stall 和分布式存储 tail latency 有什么共同抽象？

## 2026-09：ByteStore & 3FS IO Path 结合

### W36：2026-08-31 ~ 2026-09-06

- 代码主线：ByteStore IO path：client -> metadata -> blob/chunk/chunkserver 数据路径；page cache/direct IO/io_uring 初步。
- 论文 / 课程：Fire-Flyer AI-HPC。
- 输出物：`ByteStore_IO_Path_Map`。
- 验收问题：ByteStore 一次读写如何经过 metadata 和 data path？哪些步骤可能产生 copy、queue、lock、network、disk latency？

### W37：2026-09-07 ~ 2026-09-13

- 代码主线：3FS architecture + IO path first pass：client、mgmtd、meta、storage、FUSE、USRBIO、FDB；FUSE/USRBIO/RDMA/SSD 路径。
- 论文 / 课程：3FS design notes。
- 输出物：`3FS_Architecture_First_Pass`、`3FS_IO_Path_Skeleton`。
- 验收问题：3FS 为什么不是普通 NFS / object storage？FUSE、USRBIO、RDMA、SSD 分别处在哪条 IO path 上？

### W38：2026-09-14 ~ 2026-09-20

- 代码主线：ByteStore vs 3FS metadata / consistency：ByteStore metadata/placement/replication 对照 3FS meta/FDB/CRAQ/ChainTable。
- 论文 / 课程：FoundationDB、CRAQ。
- 输出物：`ByteStore_3FS_Metadata_Consistency_Comparison`、`CRAQ_to_3FS_Consistency_Note`。
- 验收问题：ByteStore 和 3FS 在 metadata ownership、placement、replication、recovery 上的共同抽象和差异是什么？

### W39：2026-09-21 ~ 2026-09-27

- 代码主线：io_uring / SPDK / RDMA core path：syscall、copy、interrupt、polling、queue depth、memory registration；回填 ByteStore/3FS IO path。
- 论文 / 课程：DDIA Ch5 / Ch8 + IO path notes。
- 输出物：`IO_Path_io_uring_SPDK_RDMA_Note_v0`、`TinySharedStorage_Design_v0`。
- 验收问题：io_uring、SPDK、RDMA 分别解决 IO 栈里的什么问题？为什么高性能系统常常不是缺 FLOPs，而是缺 bandwidth、queue management 和 tail control？

## 2026-10：KVCache Storage + 推理代码接入

### W40：2026-09-28 ~ 2026-10-04

- 代码主线：ByteStore & 3FS IO Path 月度收口：两套系统 IO path、metadata path、failure/recovery、性能瓶颈对照。
- 论文 / 课程：3FS / Fire-Flyer / classic storage review。
- 输出物：`ByteStore_3FS_IO_Path_Comparison`、`3FS_IO_Path_RDMA_SSD_Note`。
- 验收问题：ByteStore 和 3FS 的 IO path 在 API、metadata、data movement、failure、SLO 上有什么差异？这些差异如何映射到 KVCache storage？

### W41：2026-10-05 ~ 2026-10-11

- 代码主线：vLLM KV block / page / block table / scheduler first pass。
- 论文 / 课程：PagedAttention revisit。
- 输出物：`KVCache_Storage_System_Map_v0`。
- 验收问题：KVCache 的 hit、miss、eviction、offload 分别如何影响 TTFT、TPOT、throughput、cost？

### W42：2026-10-12 ~ 2026-10-18

- 代码主线：LMCache / vLLM connector / KV movement / offload。
- 论文 / 课程：LMCache。
- 输出物：`LMCache_KVCache_Layer_Note`。
- 验收问题：为什么 KVCache 应该暴露成一等 storage/communication medium，而不是 engine 内部临时张量？

### W43：2026-10-19 ~ 2026-10-25

- 代码主线：Mooncake / DistServe 的 prefill-decode disaggregation。
- 论文 / 课程：Mooncake、DistServe。
- 输出物：`Mooncake_DistServe_Disaggregation_Note`。
- 验收问题：prefill 和 decode 为什么适合拆到不同资源池？拆开后 KV 传输成本如何控制？

### W44：2026-10-26 ~ 2026-11-01

- 代码主线：KVCache storage system design mock。
- 论文 / 课程：CacheGen / KV compression awareness。
- 输出物：`KVCache_Storage_System_Design_v0`。
- 验收问题：45-60 分钟讲清一个 KVCache 存储系统：API、metadata、tiering、eviction、recovery、SLO。

## 2026-11：LLM Inference Runtime First Pass

### W45：2026-11-02 ~ 2026-11-08

- 代码主线：vLLM scheduler、block manager、KV cache manager。
- 论文 / 课程：vLLM docs / code。
- 输出物：`vLLM_PagedAttention_KVCache_Scan`。
- 验收问题：vLLM 的性能来自 kernel、scheduler、block manager 还是它们的协同？

### W46：2026-11-09 ~ 2026-11-15

- 代码主线：HTTP/RPC request -> scheduler -> prefill -> decode -> streaming。
- 论文 / 课程：Orca / continuous batching。
- 输出物：`LLM_Inference_Request_Path_v0`。
- 验收问题：一个线上 LLM 请求从进入 server 到返回 token，中间有哪些排队和资源竞争？

### W47：2026-11-16 ~ 2026-11-22

- 代码主线：SGLang radix cache、prefix matching、structured generation runtime。
- 论文 / 课程：SGLang。
- 输出物：`SGLang_RadixCache_Note`。
- 验收问题：agent / tool-use / multi-turn workload 为什么比单轮 chat 更依赖 prefix / KV reuse？

### W48：2026-11-23 ~ 2026-11-29

- 代码主线：vLLM / SGLang / LMCache / Mooncake 对照。
- 论文 / 课程：CS336 inference / serving lectures。
- 输出物：`LLM_Inference_System_First_Pass`。
- 验收问题：如果设计一个 LLM serving runtime，哪些模块必须有，哪些模块是优化项？

## 2026-12：DeepSeek-style Inference Systems

### W49：2026-11-30 ~ 2026-12-06

- 代码主线：DeepSeek V2/V3 模型结构 awareness；MLA / MoE / KVCache 压缩。
- 论文 / 课程：DeepSeek-V2。
- 输出物：`DeepSeek_V2_MLA_MoE_Note`。
- 验收问题：MLA 为什么能大幅降低 KVCache 压力？这对 storage / serving 有什么意义？

### W50：2026-12-07 ~ 2026-12-13

- 代码主线：DeepSeek V3 system notes：MoE load balance、MTP、training/inference implications。
- 论文 / 课程：DeepSeek-V3。
- 输出物：`DeepSeek_V3_System_Note`。
- 验收问题：DeepSeek V3 的系统效率来自模型结构、训练策略、kernel，还是 serving/runtime？

### W51：2026-12-14 ~ 2026-12-20

- 代码主线：reasoning workload 对 serving 的压力：长输出、长上下文、多轮、tool pause。
- 论文 / 课程：DeepSeek-R1。
- 输出物：`DeepSeek_R1_Inference_Workload_Note`。
- 验收问题：reasoning model 为什么会放大 KVCache、scheduler、SLO 和成本问题？

### W52：2026-12-21 ~ 2026-12-27

- 代码主线：MoE / long context serving：expert routing、expert parallel、load balance。
- 论文 / 课程：Switch Transformer / Mixtral selective。
- 输出物：`MoE_Long_Context_Serving_Note`。
- 验收问题：MoE serving 和 dense model serving 的主要系统差异是什么？

### W53：2026-12-28 ~ 2027-01-03

- 代码主线：产出材料盘点，冻结 1 月投递版本。
- 论文 / 课程：复盘，不开新论文。
- 输出物：`2026_Storage_Inference_Year_End_Review`。
- 验收问题：到 1 月开始面试时，哪些故事已经能讲深，哪些还是空的？

## 2027-01：综合分析 + 面试材料生产

### W01：2027-01-04 ~ 2027-01-10

- 代码主线：简历主叙事和项目经历重写。
- 面试主线：AI Core Storage 简历 v0 + 刷题节奏启动。
- 输出物：`AI_Core_Storage_Resume_v0`、`Coding_Interview_Plan_v0`。
- 验收问题：为什么从 DB / storage 转 AI Core Storage，而不是泛 LLM 或机器人？

### W02：2027-01-11 ~ 2027-01-17

- 代码主线：5 个系统故事整理。
- 面试主线：zero-copy、shared storage、RocksDB、3FS、KVCache。
- 输出物：`5_System_Stories_v0`。
- 验收问题：每个故事能否讲 10 分钟，并经得起 2 层追问？

### W03：2027-01-18 ~ 2027-01-24

- 代码主线：3 个系统设计题。
- 面试主线：KVCache storage、AI shared storage、LLM serving runtime。
- 输出物：`System_Design_Pack_v0`。
- 验收问题：是否能在白板上讲清 API、metadata、data path、failure、SLO、tradeoff？

### W04：2027-01-25 ~ 2027-01-31

- 代码主线：材料冻结、小规模内推预沟通、mock 2-3 次。
- 面试主线：简历、5 个系统故事、系统设计、刷题节奏、面试反馈表模板全部冻结。
- 输出物：`Interview_Materials_v0`。
- 验收问题：春节后正式投递前，哪些材料已经可以直接发，哪些问题还需要最后补洞？

## 2027-02：春节后投递 + 正式面试 + 补洞

### W05：2027-02-01 ~ 2027-02-07

- 补洞主线：春节周轻量补洞：C++ systems、并发、内存、RPC、性能分析；不安排重负载。
- 输出物：`Cpp_Systems_Gap_Fix_List`。
- 验收问题：能否回答 buffer ownership、lifetime、lock-free / thread pool / async 的基础追问？

### W06：2027-02-08 ~ 2027-02-14

- 补洞主线：春节后集中投递启动；同步补 IO / RDMA / SPDK / io_uring。
- 输出物：`Interview_Pipeline_Log_v0`、`IO_RDMA_Interview_QA`。
- 验收问题：能否解释 syscall、copy、interrupt、polling、queue depth、memory registration 的 tradeoff？

### W07：2027-02-15 ~ 2027-02-21

- 补洞主线：vLLM / SGLang / KVCache / MoE。
- 输出物：`Inference_Interview_QA`。
- 验收问题：能否从模型请求、scheduler、GPU memory、KV movement 四层解释一次性能问题？

### W08：2027-02-22 ~ 2027-02-28

- 补洞主线：根据面试反馈更新简历、系统设计、故事。
- 输出物：`Interview_Materials_v1`。
- 验收问题：2 月底是否已有稳定面试 pipeline，是否需要降低或调整岗位目标？

## 2027-03：年终奖后决策

### W09：2027-03-01 ~ 2027-03-07

- 主线：offer / 团队 / 方向 / 薪资 / 年终奖损失评估。
- 输出物：`Offer_Decision_Table_v0`。
- 验收问题：岗位是否真在 AI Core Storage / KVCache / Inference Infra 核心，而不是边缘平台岗？

### W10：2027-03-08 ~ 2027-03-14

- 主线：继续谈 / 拒 / 接 / 观望策略。
- 输出物：`Career_Decision_Log`。
- 验收问题：如果不跳，接下来 3 个月补什么；如果跳，入职前补什么？

### W11：2027-03-15 ~ 2027-03-21

- 主线：入职前准备或第二轮投递。
- 输出物：`Onboarding_Prep_or_Second_Round_v0`。
- 验收问题：目标团队核心系统的代码、指标、oncall、owner 边界是什么？

### W12：2027-03-22 ~ 2027-03-28

- 主线：当前工作交接风险、材料归档。
- 输出物：`Transition_Checklist`。
- 验收问题：离开前是否干净，学习材料是否可复用，面试材料是否稳定？

## 2027-04：入职窗口

### W13：2027-03-29 ~ 2027-04-04

- 主线：30/60/90 天目标。
- 输出物：`First_30_60_90_Days_Plan`。
- 验收问题：入职第一个月要读哪些代码、跟哪些指标、解决什么小问题？

### W14：2027-04-05 ~ 2027-04-11

- 主线：入职或第二轮推进。
- 输出物：`First_30_Days_AI_Infra_Onboarding` 或 `Second_Round_Interview_Plan`。
- 验收问题：是否已经进入真实 AI Core Storage / Inference 系统；如果没有，下一轮主攻什么？
