---
type: active_roadmap
time_window: 2026-07_to_2030
target_role: AI Core Storage -> LLM Inference Runtime -> Robot/VLA Runtime
current_role: DB / Storage Kernel Engineer
created: 2026-06-28
status: active
linked_files:
  - "[[00_North_Star]]"
  - "[[03_Annual_Plan_2026]]"
  - "[[05_Career_Strategy_2026_2030]]"
  - "[[08_One_Year_Roadmap_LLM_Inference_to_Robot_Runtime]]"
  - "[[10_Systems_Thinking_for_AI_Infra_and_Robot_Runtime]]"
---

# DeepSeek Storage -> Inference -> Robot Runtime Roadmap

## 一句话战略

接下来不再把短期目标放在直接切机器人，而是走三步：

```text
1. 夯实分布式存储基本盘，做好 TokaDB 工作，用 2026-H2 完整准备 DeepSeek-style AI Core Storage
2. 2027-01/02 开始正式面试，2027-03 拿完年终奖后决策，2027-04 争取进入 DeepSeek 或同级 AI Core Storage / LLM Infra 团队
3. 在 DeepSeek / AI Core Storage 工作 1-2 年，学习 3FS、KVCache、训练/推理存储和核心 AI Infra
4. 再用 3-4 年在推理系统 / KVCache / serving / runtime 方向深扎，等待合适时机进入机器人 / 具身智能系统
```

长期 North Star 仍是机器人全栈工程师 / roboticist；近期第一跳改为更现实、更能复用当前优势的 `AI Core Storage / 高性能分布式存储`。

## 为什么这样走

- 当前最强基本盘是 DB / 存储 / 分布式系统 / 性能优化，而不是机器人硬件、控制或 robot learning 算法。
- TokaDB 到 LLM 业务有距离，但它提供了非常关键的底层能力：零拷贝、共享存储、存储引擎、性能分析、并发与故障恢复。
- DeepSeek Storage JD 和当前能力连接紧：KVCache 存储、上亿级 IOPS、毫秒级延迟、分布式文件系统、对象存储、RDMA、io_uring/SPDK、RocksDB/FoundationDB/ClickHouse。
- 机器人方向短期还没到最适合切入的 turning point；现在更适合长期探索，不适合作为 2026-Q3/Q4 的主求职方向。
- 先进入 AI core infra，再从 KVCache / 推理服务 / 多模态 runtime 回接 robot/VLA runtime，路径更稳。

## Step 1：分布式存储第一跳

时间窗：

```text
2026-07 ~ 2027-04
```

目标：

- 很好地完成 TokaDB 当前工作，把实际工程经验转成可迁移系统能力。
- 准备 DeepSeek `高性能分布式存储工程师` 或同级 AI Core Storage / LLM Infra 岗位，2027-01/02 开始正式面试，2027-04 作为理想入职窗口。
- 建立 `TokaDB -> RocksDB/brpc/ByteStore/3FS -> KVCache storage` 的能力叙事。

核心系统：

| 系统 / 主题 | 学什么 | 输出 |
|---|---|---|
| TokaDB | 零拷贝、共享存储、data path、性能分析、故障恢复 | `TokaDB_Transferable_Systems_Review_v0` |
| RocksDB | LSM、WAL、memtable、SST、compaction、snapshot、iterator、amplification | `RocksDB_LSM_Refresh.md` |
| brpc | bthread、RPC latency、zero-copy attachment、backpressure、bvar/observability | `brpc_Systems_Model_Note.md` |
| ByteStore | namespace、metadata、placement、replication、recovery、shared storage | `ByteStore_Shared_Storage_Map_v0` |
| 3FS | SSD + RDMA shared storage、FoundationDB metadata、CRAQ、USRBIO/FUSE、dataloader/checkpoint/KVCache | `3FS_Architecture_First_Pass.md` |
| KVCache | prefill/decode、block/page、eviction、offload、prefix reuse、tail latency | `KVCache_Storage_System_Map_v0` |
| RDMA / SPDK / io_uring | zero-copy、kernel bypass、queue、polling、NVMe、memory registration | `IO_Path_io_uring_SPDK_RDMA_Note_v0` |

Step 1 的最低完成线：

- [ ] 能讲清 DeepSeek Storage JD 为什么匹配当前背景。
- [ ] 能讲清 TokaDB 工作如何抽象为 AI Core Storage 能力，而不是只讲内部业务。
- [ ] 能做一次 `设计 KVCache 存储系统` 的 45-60 分钟系统设计。
- [ ] 能讲清 3FS 的组件边界和性能路径。
- [ ] 能解释 RocksDB / FoundationDB / ClickHouse 这类系统设计范式，而不是只背概念。

## Step 2：DeepSeek / AI Core Storage 阶段

时间窗：

```text
2026-Q4 / 2027 ~ 2028
```

目标：

- 进入 DeepSeek 或同级 AI Core Storage 团队。
- 用 1-2 年掌握真实 AI core infra：训练数据链路、推理 KVCache、分布式文件系统、对象存储、checkpoint、性能与稳定性。
- 从存储 owner 逐步贴近 inference runtime / serving / KVCache。

应该争取的工作类型：

- KVCache storage / offload / GC / eviction / prefix reuse。
- 训练 dataloader / checkpoint / distributed file system / object storage。
- RDMA / SSD / NVMe / SPDK / kernel bypass / zero-copy data path。
- metadata / consistency / replication / recovery / rebalance。
- serving tail latency / throughput / cost optimization。

阶段性目标：

- [ ] 负责或深度参与一个 AI storage / KVCache / data path 子系统。
- [ ] 能解释真实 workload 下的瓶颈：HBM、DRAM、SSD、RDMA、CPU、metadata、RPC、scheduler。
- [ ] 能从 storage 视角理解 inference service 的成本和用户体验。
- [ ] 开始往 inference runtime / serving 方向靠，而不是停留在纯存储。

## Step 3：Inference Runtime -> Robot/VLA Runtime

时间窗：

```text
2028 ~ 2030+
```

目标：

- 在 LLM inference / KVCache / serving / runtime 方向工作 3-4 年，形成核心系统能力。
- 同步低频学习机器人 / VLA / Physical AI 的 runtime 和数据闭环。
- 等机器人行业、个人作品和岗位质量同时成熟时，再考虑切入机器人 / 具身智能方向。

需要长期积累：

- vLLM / SGLang / TensorRT-LLM / serving scheduler。
- KVCache lifecycle、long context、MoE serving、多模态 serving。
- GPU kernel / CUDA / Triton / TileLang awareness。
- VLA / robot policy inference latency。
- robot data loop：teleop、episode、replay、eval、failure taxonomy。
- edge-cloud robot runtime：watchdog、fallback、logging、observability。

机器人切入条件：

- [ ] AI core infra 已经形成可迁移的核心能力，而不是浅层了解。
- [ ] 机器人岗位不是边缘 demo，而是 data / runtime / eval / deployment / VLA 系统核心。
- [ ] 自己能讲清 `LLM inference / KVCache / storage` 如何服务 `robot/VLA runtime`。
- [ ] 行业和团队时机合适，薪资和成长折损可接受。

## 近期学习重心

2026-Q3 起，默认学习焦点改为：

```text
LLM & KVCache
推理系统
brpc
RocksDB
分布式存储
SPDK / io_uring
3FS
RDMA
```

暂停主动扩展：

- 泛 LLM post-training / reasoning / agent，除非直接服务 inference / KVCache / DeepSeek。
- CV / VLA / diffusion / robot learning，除非直接服务 robot runtime 长期回接。
- 大量机器人硬件 / Modern Robotics 深挖，保留低频探索即可。

## 2026-H2 到 2027-Q1 执行计划

### 2026-07：TokaDB TabletServer + mini-lsm/RocksDB 核心

- `TabletServer_Request_Path_Map`
- `TabletServer_Read_Write_Path_Map`
- `Replica_Lifecycle_Open_Close_Recover_Map`
- `TinyLSM_Month1_Project_Review`
- `RocksDB_LSM_Refresh`

### 2026-08：ByteStore 初窥 + RocksDB 深入 + brpc/bthread 深入

- `TokaDB_Transferable_Systems_Review_v0`
- `ByteStore_Shared_Storage_Map_v0`
- `RocksDB_Deep_Dive_Note`
- `brpc_bthread_Model_Note`
- `TokaDB_Locks_ThreadPool_Backpressure_Map`

### 2026-09：ByteStore & 3FS IO Path

- `ByteStore_IO_Path_Map`
- `3FS_Architecture_First_Pass`
- `ByteStore_3FS_Metadata_Consistency_Comparison`
- `IO_Path_io_uring_SPDK_RDMA_Note_v0`
- `ByteStore_3FS_IO_Path_Comparison`
- `3FS_IO_Path_RDMA_SSD_Note`

### 2026-10：KVCache Storage 接入

- `KVCache_Storage_System_Map_v0`
- `LMCache_KVCache_Layer_Note`
- `Mooncake_DistServe_Disaggregation_Note`
- `KVCache_Storage_System_Design_v0`

### 2026-11：Inference Runtime 深入

- `vLLM_PagedAttention_KVCache_Scan`
- `LLM_Inference_Request_Path_v0`
- `SGLang_RadixCache_Note`
- `LLM_Inference_System_First_Pass`

### 2026-12：DeepSeek + 外部系统变化

- `DeepSeek_V2_MLA_MoE_Note`
- `DeepSeek_V3_System_Note`
- `DeepSeek_R1_Inference_Workload_Note`
- `MoE_Long_Context_Serving_Note`
- `External_Inference_System_Trends_2026Q4`

### 2027-01：综合分析 + 面试材料生产

- AI Core Storage 简历叙事。
- 5 个系统故事：
  - 零拷贝 / IO path
  - 共享存储 / metadata / consistency
  - RocksDB / LSM
  - 3FS architecture
  - KVCache storage design
- 4-6 次 mock interview。
- 刷题节奏、系统设计、C++/IO/RDMA 补洞计划。
- 小范围内推预沟通，春节后再集中投递。

### 2027-02：春节后投递 + 正式面试 + 补洞

- 春节后正式投递 DeepSeek 或同类 AI Core Storage / LLM Infra 岗位。
- 根据面试反馈补 C++ systems、IO/RDMA、KVCache、inference runtime。

### 2027-03/04：决策与入职

- 2027-03 拿完年终奖后，对 offer、团队、方向、薪资和成长路径做清晰决策。
- 2027-04 作为理想入职窗口。
- 面试主叙事固定为：

```text
TokaDB / DB storage systems
-> AI Core Storage / 3FS / KVCache
-> LLM inference runtime
-> long-term Robot/VLA runtime
```

## 一句话回锚

> 近期不要急着跳机器人；先把分布式存储做到足够强，进入 DeepSeek AI Core Storage，再从 KVCache 和推理系统走向未来的机器人 / VLA runtime。
