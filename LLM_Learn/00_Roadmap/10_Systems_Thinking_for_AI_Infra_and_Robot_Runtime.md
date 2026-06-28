---
type: support_roadmap
track: Systems Thinking / Distributed Systems / Storage / AI Infra / Robot Runtime
status: active_support_line
created: 2026-06-22
linked_files:
  - "[[03_Annual_Plan_2026]]"
  - "[[08_One_Year_Roadmap_LLM_Inference_to_Robot_Runtime]]"
  - "[[09_One_Year_Robot_Learning_Full_Stack_Roadmap]]"
---

# Systems Thinking for AI Infra and Robot Runtime

## 定位

这条线用于沉淀经典存储系统、分布式系统、分布式计算系统里的可迁移思考。

2026-06-28 修订：基于 DeepSeek `高性能分布式存储工程师` / AI Core Storage 岗位判断，这条线从普通支撑线升级为近期职业第一跳主线。它仍然不是 TokaDB 主业务日志，也不取消机器人长期目标；它服务新的三级跳路径：

```text
AI Core Storage / KVCache Storage
-> LLM Inference / KVCache / Serving Runtime
-> Robot Runtime / VLA Runtime / Robot Data Loop
```

核心问题：

```text
经典系统思想
-> AI training / serving / checkpoint / scheduling
-> robot runtime / logging / replay / reliability
-> robot learning data loop
```

## 为什么放在 LLM learner 里

- LLM / VLA / Robot Learning 都绕不开系统问题：数据、调度、容错、延迟、可观测性、版本、重放。
- 存储和分布式计算经验是当前已有优势，可以转化成 AI Infra / Robot Runtime 的工程判断力。
- 这类思考如果单独开 workspace，容易和机器人主线脱节；放在这里可以强制每条系统 insight 回接到 AI / Robot。

## 放什么

### 适合

- 经典存储系统思想：LSM、WAL、snapshot、checkpoint、compaction、replication、consistency。
- 分布式系统思想：lease、membership、failure detector、backpressure、flow control、scheduler、straggler、tail latency。
- 分布式计算系统思想：MapReduce、Spark、Ray、dataflow、lineage、checkpoint、task retry、resource isolation。
- AI Infra 连接：distributed training、parameter / optimizer state、DDP/FSDP/ZeRO、checkpoint/restart、serving scheduler、KV cache、batching。
- Robot Runtime 连接：watchdog、timeout、fallback、logging、replay、episode metadata、eval harness、data loop。

### 不适合

- 具体 TokaDB 主业务排障流水账。
- 平台治理、项目管理、业务交付细节。
- 只对某个内部系统成立、无法抽象迁移的实现细节。
- 完整重开数据库 / 分布式系统课程主线。

## 默认输出形态

每条系统思考尽量压成四段：

```text
1. 系统问题：这个机制原本解决什么问题？
2. 关键抽象：它真正稳定下来的抽象是什么？
3. 失败模式：系统在什么边界下会坏？
4. AI / Robot 迁移：它如何帮助 training、serving、runtime、data loop？
```

## 存放位置

- 系统思考短文：`LLM_Learn/08_Insights/Systems/`
- 系统论文 / 经典材料：`LLM_Learn/04_Papers/60_Systems/`
- 与 AI Infra / Robot Runtime 的路线关系：本文件。

## 初始主题池

### Storage / DB Systems

- WAL / replay：如何迁移到 robot episode replay、failure replay、training checkpoint。
- LSM / compaction：如何迁移到 dataset version、offline data pipeline、增量训练数据整理。
- snapshot / checkpoint：如何迁移到 distributed training restart、policy checkpoint、eval reproducibility。
- replication / consistency：如何迁移到多机器人状态同步和任务协调。

### Distributed Computing

- MapReduce / dataflow：如何迁移到大规模数据预处理、trajectory cleaning、feature extraction。
- Spark lineage / task retry：如何迁移到训练数据 pipeline 的可重算和失败恢复。
- Ray / actor model：如何迁移到 distributed RL、simulation workers、policy serving actors。
- Scheduler / straggler：如何迁移到 GPU job scheduling、serving tail latency、robot fleet task dispatch。

### Runtime / Serving

- Backpressure：如何避免 serving / logging / control loop 中的队列堆积。
- Tail latency：为什么 robot runtime 比平均延迟更关心 p95 / p99。
- Timeout / fallback / watchdog：机器人系统里的安全边界。
- Observability：日志、metrics、trace 如何服务 failure taxonomy 和数据闭环。

### DeepSeek Storage Route

- KVCache storage：生命周期、prefix cache、eviction、SSD offload、tail latency、failure recovery。
- AI training storage：分布式文件系统、对象存储、数据读取加速、checkpoint/restart。
- High-performance IO：page cache、direct IO、io_uring、SPDK、NVMe、RDMA、zero-copy。
- Storage engine design：RocksDB / LSM、FoundationDB、ClickHouse 中可迁移的简洁设计范式。

## 和当前主线的边界

- 2026-07 起，DeepSeek Storage / KVCache Storage 是近期 P0；Robot Learning / SO-ARM101 / Unitree 降级为长期探索副线。
- Systems Thinking 可以进入 daily mainline，但必须服务 AI Core Storage / KVCache / inference runtime，不记录 TokaDB 主业务流水账。
- 如果某条系统思考能直接帮助机器人，例如 `episode replay`、`checkpoint`、`eval harness`，保留为长期回接点，不抢近期职业第一跳。
- 如果 AI Core Storage 连续多周成为主任务，可以围绕 `DeepSeek_AI_Core_Storage_JD_Mapping` 和 `KVCache_Storage_System_Map` 建立阶段项目。

## 一句话回锚

> 系统思考不是偏离长期机器人目标，而是先把已有存储 / 分布式系统能力转化为 AI Core Storage 和 LLM inference runtime，再在更合适的时机回接 Robot Runtime 和 VLA 数据闭环。
