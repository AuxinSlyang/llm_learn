# DeepSeek Storage 路线总摘要

日期：2026-06-28

## 一句话结论

近期主线从直接切机器人调整为：

```text
TokaDB / DB Storage 基本盘
-> DeepSeek / AI Core Storage / 高性能分布式存储
-> LLM Inference / KVCache / serving runtime
-> Robot/VLA Runtime / 具身智能系统
```

长期 North Star 仍是机器人全栈工程师 / roboticist；近期第一跳改为 DeepSeek Storage，是因为它更贴近当前 DB / 存储 / 分布式系统基本盘，也更容易在 2026-Q3/Q4 形成可面试证据。

## 为什么先走 DeepSeek Storage

- TokaDB 到 LLM 业务有距离，但它沉淀的是核心底层能力：零拷贝、共享存储、data path、性能分析、并发控制、故障恢复。
- DeepSeek `高性能分布式存储工程师` 的 JD 和当前能力连接很紧：KVCache 存储、上亿级 IOPS、毫秒级延迟、分布式文件系统、对象存储、RDMA、io_uring / SPDK、RocksDB / FoundationDB / ClickHouse。
- 机器人方向长期有吸引力，但当前更适合低频探索；短期直接切机器人不如先进入 AI core infra 稳。
- 进入 AI core storage 后，可以自然贴近 LLM inference runtime，再在更合适的行业时机回接 Robot/VLA Runtime。

## 三步走

### Step 1：分布式存储第一跳

时间窗：`2026-07 ~ 2026-10`

目标：

- 做好 TokaDB 当前工作。
- 把 TokaDB 经验抽象成可迁移系统能力。
- 准备 DeepSeek Storage，9 月市场测试，10 月正式窗口。

重点系统：

- `TokaDB`：zero-copy、shared storage、data path、tail latency、failure recovery。
- `RocksDB`：LSM、WAL、memtable、SST、compaction、snapshot、iterator。
- `brpc`：bthread、RPC latency、zero-copy attachment、backpressure、bvar / observability。
- `ByteStore`：namespace、metadata、placement、replication、recovery、shared storage。
- `3FS`：SSD + RDMA shared storage、FoundationDB metadata、CRAQ、USRBIO / FUSE、dataloader / checkpoint / KVCache。
- `KVCache`：prefill / decode、block / page、prefix reuse、eviction、offload、HBM / DRAM / SSD / remote tier。
- `RDMA / SPDK / io_uring`：zero-copy、kernel bypass、polling、NVMe、memory registration。

### Step 2：AI Core Storage 到推理系统

时间窗：`2026-Q4 / 2027 ~ 2028`

目标：

- 进入 DeepSeek 或同级 AI Core Storage 团队。
- 用 1-2 年学习真实 AI storage：训练数据链路、KVCache、checkpoint、分布式文件系统、对象存储、RDMA/SSD data path。
- 从 storage owner 逐渐贴近 inference runtime / serving / KVCache。

### Step 3：Inference Runtime 到 Robot/VLA Runtime

时间窗：`2028 ~ 2030+`

目标：

- 在 LLM inference / KVCache / serving / runtime 方向深扎 3-4 年。
- 低频保留机器人 / VLA / Physical AI 学习。
- 等机器人行业、岗位质量和个人能力成熟后，再切入 Robot/VLA Runtime。

## 2026 H2 执行节奏

```text
2026-07：DeepSeek Storage 基础框架
2026-08：TokaDB / brpc / ByteStore / 3FS IO path / RDMA-SPDK 深水区
2026-09：AI Core Storage 简历叙事 + mock interview + 小范围市场测试
2026-10：DeepSeek Storage 正式面试窗口
2026-11：KVCache -> Inference Runtime bridge
2026-12：年度复盘和 2027 决策
```

## 7 月最低完成线

- `DeepSeek_AI_Core_Storage_JD_Mapping_v0`
- `RocksDB_LSM_Refresh`
- `3FS_Architecture_First_Pass`
- `KVCache_Storage_System_Map_v0`
- `vLLM_PagedAttention_KVCache_Scan`
- `IO_Path_io_uring_SPDK_RDMA_Note_v0`

## 阅读收敛规则

近期只主动读：

- LLM KVCache
- shared storage / distributed file system
- 3FS / Fire-Flyer File System
- vLLM / PagedAttention / LMCache / Mooncake / CacheGen
- FoundationDB / CRAQ / RocksDB
- RDMA / SPDK / io_uring / FUSE / kernel I/O stack

暂停主动新增：

- 泛 LLM post-training / reasoning / agent。
- CV / VLA / Diffusion / Robot Learning。
- 大量机器人硬件 / Modern Robotics 深挖。

这些内容不删除，只作为长期参考保留。

## 当前权威文件

- [[11_DeepSeek_Storage_to_Inference_to_Robot_Runtime_Roadmap]]
- [[03_Annual_Plan_2026]]
- [[05_Career_Strategy_2026_2030]]
- [[10_Systems_Thinking_for_AI_Infra_and_Robot_Runtime]]
- [[2026-07_月计划]]
- [[60_Systems/AI_Core_Storage_and_KVCache/README]]

## 一句话回锚

> 近期不要急着跳机器人；先把分布式存储做到足够强，进入 DeepSeek AI Core Storage，再从 KVCache 和推理系统走向未来的 Robot/VLA Runtime。
