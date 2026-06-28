# DeepSeek Storage 三级跳职业策略

日期：2026-06-28

## 结论

短期职业第一跳调整为：

```text
高性能分布式存储工程师 / AI Core Storage
-> AI 推理工程师 / KVCache / serving / kernel optimization
-> 机器人系统工程师 / VLA runtime / robot data loop
```

这不是放弃机器人，而是把短期可落地路径改成更贴近当前能力基本盘的 AI 核心系统入口。机器人保留为长期 North Star、应用牵引和差异化方向。

## 为什么先走 DeepSeek Storage

- 当前最强资产是 DB / 存储内核 / 分布式系统 / 性能优化，而不是机器人硬件、控制或 robot learning 算法。
- DeepSeek `高性能分布式存储工程师` 的问题足够核心：KVCache 存储、上亿级 IOPS、毫秒级延迟、分布式文件系统、对象存储、RDMA、io_uring/SPDK。
- 这条路可以把已有存储经验直接迁移到大模型推理和训练基础设施，不需要职业叙事清零。
- 机器人方向短期还没有进入最适合切入的 turning point；现在直接转机器人更像探索，职业落地不如 AI Core Storage 稳。

## 三级跳

### 第一跳：分布式存储工程师

目标岗位：

- 高性能分布式存储工程师
- AI Core Storage Engineer
- KVCache Storage / Training Data Storage Engineer

重点能力：

- RocksDB / LSM / WAL / compaction / snapshot / iterator
- 分布式文件系统、对象存储、共享存储层
- Raft / Paxos / lease / consistency / failure recovery
- io_uring / SPDK / NVMe / RDMA / zero-copy
- tail latency、backpressure、IO scheduler、cache hierarchy

### 第二跳：AI 推理工程师

目标岗位：

- LLM Inference Infra Engineer
- KVCache / Serving Runtime Engineer
- GPU / Kernel / Performance Engineer

重点能力：

- prefill / decode / KVCache lifecycle
- PagedAttention / block table / prefix cache / cache eviction
- batching、load balancing、routing、tail latency
- CUDA / Triton / TileLang awareness
- MoE serving、long-context serving、多模态 serving

### 第三跳：机器人系统工程师

目标岗位：

- Robot Systems Engineer
- VLA Runtime Engineer
- Robot Data / Eval / Runtime Infra Engineer

重点能力：

- VLA / policy inference latency
- robot data loop：teleop、episode、replay、eval、failure taxonomy
- edge-cloud robot runtime、日志、回放、watchdog、fallback
- 多模态模型与低层 policy runtime 的接口

## 机器人路线的新定位

机器人不再作为短期转岗第一跳，而是：

- 长期 North Star：最终仍希望成为机器人全栈工程师 / roboticist。
- 应用牵引：用 SO-ARM101 / LeRobot / Unitree repo 理解 VLA runtime、数据闭环和系统接口。
- 差异化叙事：不是通用 AI Infra，而是能把 AI core infra 迁移到 Physical AI / robot runtime 的系统工程师。

短期不要用机器人项目挤占 DeepSeek Storage 主线。机器人每周最多保留一个轻量探索槽，目标是保持兴趣和系统直觉不断线。

## 7 月执行含义

7 月 P0：

```text
DeepSeek Storage JD mapping
-> RocksDB / LSM refresh
-> KVCache storage system map
-> vLLM / PagedAttention KVCache scan
-> io_uring / SPDK / RDMA IO path note
```

7 月 P1：

```text
LLM inference / KVCache serving 支撑线
```

7 月 P2：

```text
SO-ARM101 blocker/report 或 Unitree lightweight repo map
```

## 9-10 月面试准备

详细路线见：[[2026-06-28_DeepSeek_Storage_Interview_Preparation_2026Q3]]

节奏判断：

- 7 月补齐 JD mapping、RocksDB/LSM、KVCache storage 和 vLLM/PagedAttention 基础。
- 8 月形成 2-3 个能讲深的系统专题：LSM/AI Storage、KVCache offload/tail latency、IO path/RDMA/SPDK。
- 9 月开始 mock interview、简历叙事、小范围内推沟通。
- 10 月如果材料和 mock 反馈稳定，开始正式投递 DeepSeek 或同类 AI Core Storage 岗位。

## 一句话回锚

> 先用存储系统基本盘进入 AI core infra，再从 KVCache / 推理服务走向 VLA runtime，最后在更合适的行业时间点切入机器人系统。
