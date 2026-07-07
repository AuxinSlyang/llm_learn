---
type: annual_plan
year: 2026
target_role: AI Core Storage -> LLM Inference Runtime -> Robot/VLA Runtime
scenario_anchor: DeepSeek Storage + KVCache + Inference Runtime, with Robot/VLA Runtime as long-term North Star
time_budget: 8-14h/week (32-56h/month)
active_roadmap: "[[11_DeepSeek_Storage_to_Inference_to_Robot_Runtime_Roadmap]]"
linked_files:
  - "[[00_North_Star]]"
  - "[[01_Learning_Philosophy]]"
  - "[[02_Capability_Map]]"
  - "[[04_2026_Monthly_Learning_Materials]]"
  - "[[05_Career_Strategy_2026_2030]]"
  - "[[06_Embodied_AI_Software_Engineer_Learning_Curve]]"
  - "[[07_One_Year_Interview_Roadmap_Embodied_AI_Software]]"
  - "[[08_One_Year_Roadmap_LLM_Inference_to_Robot_Runtime]]"
  - "[[09_One_Year_Robot_Learning_Full_Stack_Roadmap]]"
  - "[[10_Systems_Thinking_for_AI_Infra_and_Robot_Runtime]]"
  - "[[11_DeepSeek_Storage_to_Inference_to_Robot_Runtime_Roadmap]]"
---

# 2026 Annual Plan

> 这份文件回答的问题：**2026 年我具体怎么走？**
> 更新频率：月级；当前权威修订时间：2026-06-28。

## 2026-06-28 当前权威修订

2026-H2 的近期主线改为：

```text
DeepSeek Storage / AI Core Storage
-> LLM KVCache / inference runtime
-> long-term Robot/VLA Runtime
```

执行含义：

- 近期第一跳不再是直接切机器人，而是夯实分布式存储，做好 TokaDB 工作，同时准备 2026-09/10 进入 DeepSeek / AI Core Storage。
- 学习主线收敛到 `TokaDB / RocksDB / brpc / ByteStore / 3FS / KVCache / RDMA / SPDK / io_uring`。
- 机器人 / 具身智能保留为长期 North Star 和低频探索，不再作为 2026-Q3/Q4 的求职主战场。
- 旧的 Robot Learning Full-Stack 路线保留为长期参考；当前 active roadmap 改为 [[11_DeepSeek_Storage_to_Inference_to_Robot_Runtime_Roadmap]]。

## 2026 年定位

短期职业目标：

```text
AI Core Storage / 高性能分布式存储
-> DeepSeek Storage / KVCache Storage / Training Data Storage
```

长期能力目标：

```text
机器人全栈工程师 / roboticist
-> 机器人本体 + 感知 + 控制 + 学习 + runtime + 数据闭环 + 语言智能
```

当前执行主线：

```text
DeepSeek Storage / KVCache / LLM Inference Runtime 主线
+ Robot/VLA Runtime 长期支撑线
```

执行含义：

- `DeepSeek Storage / AI Core Storage` 是 2026-Q3/Q4 的近期上位主线。
- `TokaDB / RocksDB / brpc / ByteStore / 3FS / KVCache / RDMA / SPDK / io_uring` 是近期学习和面试证据来源。
- `LLM / KVCache / 推理系统` 是第二跳入口，进入 AI core infra 后逐步靠近 inference runtime。
- `Robot Learning / VLA / 具身智能` 保留为长期目标，等待更合适的行业与个人时机。

## 学习执行原则

- 每个阶段只有一个主课程或主实验，不同时完整刷多门课。
- 每个阶段必须有一个可动手推进的项目；课程、论文和笔记都要服务这个项目的下一个动作。
- 每周至少留下一个可检查证据：笔记、代码、曲线、实验表、失败分析或 JD mapping。
- 论文只作为当前阶段解释器，不随机追热点。
- 实验优先形成闭环：`sim/task -> obs/action -> policy -> train/eval -> log/replay -> runtime -> failure analysis`。
- 看课不是阶段目标本身；看课过程中要同步推进项目里的代码、实验、数据、硬件、日志或报告。
- 月末复盘必须对照月计划，决定下月是继续、降难还是换入口。

## 上半年实际回顾

| 阶段 | 时间 | 实际做了什么 | 结论 |
|---|---|---|---|
| LLM 基础 | 2026-03 ~ 2026-04 | micrograd / makemore / Transformer 基础线推进 | autograd、训练 loop、token 概念有了底座 |
| nanoGPT | 2026-04 ~ 2026-05 | attention、Transformer block、训练/生成主线推进 | LLM 主链路接近收口，但还需要结构化总结 |
| 方向重定义 | 2026-04-27 | 从单一 LLM 工程叙事转向具身智能 / 机器人系统 | 长期目标升级 |
| 职业路径试探 | 2026-05-27 | 曾把 LLM Inference Infra 设为职业第一跳 | 该路径现实但会弱化机器人主线 |
| Unitree JD 校准 | 2026-06-01 | 重新对齐具身智能软件 / Robot Learning Infra / Policy Runtime | 当前权威路线切回 Robot Learning Full-Stack |
| DeepSeek Storage 校准 | 2026-06-28 | 根据 DeepSeek 高性能分布式存储 JD，重新确认 AI Core Storage 是近期第一跳 | 当前权威路线切到 DeepSeek Storage -> KVCache -> Inference -> Robot/VLA Runtime |

H1 的价值不是“已经学完”，而是把语言模型基础、系统工程背景和机器人长期目标重新放到同一条路线里。

## 2026 H2 月度路线

| 月份 | 主模块 | 主资源 | 阶段产出 | 对短期职业目标的帮助 |
|---|---|---|---|---|
| 2026-06 | M1：路线切换 + 实物机器人首闭环预备 | nanoGPT、SO-ARM101、LeRobot、LingBot-VLA walkthrough，Gymnasium/MuJoCo 兜底 | `nanoGPT 主链路总结 v0`、`LLM phase 1 总结 v0`、`SO-ARM101 + LeRobot 首闭环 bring-up 记录`、`robot data schema v0` | 证明能把 LLM 基础收口，并尽早接触真实机器人硬件、示教数据、评估和 failure loop |
| 2026-07 | M2 revised：TabletServer + LSM 核心 | TokaDB TabletServer 核心链路、mini-lsm、RocksDB/LSM、LLM serving 论文主线 | `TabletServer_Request_Path_Map`、`TinyLSM_Month1_Project_Review`、`RocksDB_LSM_Refresh` | 把本地 TokaDB 经验和 RocksDB/LSM 机制连起来 |
| 2026-08 | M3 revised：ByteStore / RocksDB / brpc 深水 | ByteStore 初窥、RocksDB 深入、brpc/bthread、经典分布式系统论文 | `ByteStore_Shared_Storage_Map`、`RocksDB_Deep_Dive_Note`、`brpc_bthread_Model_Note` | 把存储引擎、RPC 和分布式系统基础打厚 |
| 2026-09 | M4 revised：ByteStore & 3FS IO Path | ByteStore IO path、3FS IO path、io_uring/SPDK/RDMA、metadata/data path 对照 | `ByteStore_IO_Path_Map`、`3FS_IO_Path`、`ByteStore_3FS_IO_Path_Comparison` | 建立 AI Core Storage / shared storage 的代码级叙事 |
| 2026-10 | M5 revised：KVCache Storage 接入 | KVCache block/page/offload、vLLM、LMCache、Mooncake、DistServe | `KVCache_Storage_System_Map`、`LMCache_KVCache_Layer_Note` | 从 storage 进入推理系统 |
| 2026-11 | M6 revised：Inference Runtime 深入 | vLLM/SGLang request path、scheduler、continuous batching、prefix cache | `LLM_Inference_System_First_Pass`、`SGLang_RadixCache_Note` | 建立 LLM inference runtime 全图 |
| 2026-12 | M7 revised：DeepSeek + 外部系统变化 | DeepSeek V2/V3/R1、MLA/MoE/reasoning workload、外部 inference/storage 系统趋势 | `DeepSeek_Inference_System_Reading_Map`、`External_Inference_System_Trends_2026Q4` | 为 1-2 月面试材料收口提供最新系统语境 |

## 2026 年度关键产出

- [ ] `DeepSeek_AI_Core_Storage_JD_Mapping_v0`：逐条映射 KVCache storage、分布式文件系统、对象存储、RDMA、io_uring/SPDK、RocksDB/FoundationDB/ClickHouse 到当前能力差距。
- [ ] `TokaDB_Transferable_Systems_Review_v0`：把零拷贝、共享存储、data path、性能分析、故障恢复抽象成可面试系统能力。
- [ ] `RocksDB_LSM_Refresh`：讲清 WAL、memtable、SST、compaction、snapshot、iterator、WAF/RAF/SAF。
- [ ] `brpc_Systems_Model_Note`：讲清 bthread、RPC latency、zero-copy attachment、backpressure、bvar/observability。
- [ ] `ByteStore_Shared_Storage_Map_v0`：讲清 namespace、metadata、placement、replication、recovery、性能隔离。
- [ ] `3FS_Architecture_First_Pass`：讲清 client、metadata、storage service、FoundationDB、CRAQ、USRBIO/FUSE、dataloader/checkpoint/KVCache。
- [ ] `3FS_IO_Path_RDMA_SSD_Note`：讲清 RDMA、SSD/NVMe、USRBIO/FUSE、CPU copy、queue depth、tail latency。
- [ ] `KVCache_Storage_System_Map_v0`：讲清 prefill/decode、block/page、prefix reuse、eviction、offload、HBM/DRAM/SSD/remote tier。
- [ ] `vLLM_PagedAttention_KVCache_Scan`：讲清 PagedAttention 的 block table、fragmentation、sharing、serving scheduler 和 storage boundary。
- [ ] `IO_Path_io_uring_SPDK_RDMA_Note_v0`：讲清 kernel bypass、polling、memory registration、NVMe/RDMA data path。
- [ ] `AI Core Storage 简历叙事 + 5 个系统故事`：零拷贝、共享存储、RocksDB/LSM、3FS、KVCache storage design。
- [ ] `2027 DeepSeek / AI Infra plan`：根据 2026-Q4 面试/入职情况，决定继续投递、入职后学习计划或推理系统第二跳计划。

## 2026 年终自检标准

到 2026-12-31，如果下面这些基本成立，说明 2026 走得稳：

- [ ] 能讲清为什么 DeepSeek Storage 是当前最现实第一跳，而不是直接切机器人。
- [ ] 能把 TokaDB 工作抽象成 AI Core Storage 能力：zero-copy、shared storage、data path、tail latency、failure recovery。
- [ ] 能做一次 `设计支撑大模型推理的 KVCache 存储系统` 的完整系统设计。
- [ ] 能讲清 3FS 的系统边界、metadata / consistency、IO path、RDMA/SSD、KVCache 使用方式。
- [ ] 能讲清 RocksDB / FoundationDB / ClickHouse 等系统的设计范式，而不是只背概念。
- [ ] 能讲清 brpc、ByteStore、RDMA、SPDK、io_uring 在 AI storage 链路中的位置。
- [ ] 有一套可展示材料：JD mapping、系统 notes、设计草图 / benchmark、简历叙事、mock 复盘。

## 风险与降难策略

| 风险 | 降难策略 |
|---|---|
| DeepSeek Storage 准备泛化成系统杂学 | 每月只保 `TokaDB/RocksDB/brpc/ByteStore/3FS/KVCache/IO path` 相关产出 |
| LLM 论文继续泛读 | 只读 KVCache、serving、inference runtime、shared storage 直接相关材料 |
| 机器人兴趣抢回近期主线 | 机器人保留 P2 低频探索，不进入 2026-Q3/Q4 求职验收 |
| TokaDB 工作和转岗准备割裂 | 每周抽象一个可迁移系统点，沉淀到面试故事 |
| RDMA/SPDK/io_uring 太底层 | 第一轮只追性能边界和系统位置，不追 expert 级实现 |
| 3FS 读成代码流水账 | 按 architecture、metadata/consistency、IO path、KVCache 四轮阅读 |
| 9 月准备不足 | 9 月先市场测试和 mock，10 月再作为正式窗口 |

## 与 Roadmap 其他文件的关系

- [[00_North_Star]]：解释**为什么**走机器人全栈 / roboticist 方向。
- [[01_Learning_Philosophy]]：解释**怎么学**。
- [[02_Capability_Map]]：解释**学什么 / 当前 Level**。
- [[05_Career_Strategy_2026_2030]]：解释**职业上怎么在 3-5 年内决策**。
- [[06_Embodied_AI_Software_Engineer_Learning_Curve]]：保留具身智能软件工程师能力曲线。
- [[07_One_Year_Interview_Roadmap_Embodied_AI_Software]]：保留岗位准备材料。
- [[08_One_Year_Roadmap_LLM_Inference_to_Robot_Runtime]]：作为第二跳 `LLM Inference Runtime` 的支撑路线。
- [[09_One_Year_Robot_Learning_Full_Stack_Roadmap]]：保留为长期机器人参考路线，不作为近期执行主线。
- [[10_Systems_Thinking_for_AI_Infra_and_Robot_Runtime]]：当前系统能力主线。
- [[11_DeepSeek_Storage_to_Inference_to_Robot_Runtime_Roadmap]]：当前权威路线。
- 本文件：解释**2026 年怎么排时间和验收产出**。
- `07_MonthlyPlans/2026/`：每月执行细节。
- `02_WeeklyNotes/`：每周执行。
- `01_DailyNotes/`：每日执行。
