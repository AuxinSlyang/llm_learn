# DeepSeek Storage + Inference 面试周期计划 2027Q1

日期：2026-06-28

## 结论

把正式面试窗口从 2026-09/10 推迟到 2027-01/02，更适合当前目标。

新的节奏不是短冲，而是 6-8 个月的完整准备：

```text
2026-07 ~ 2026-09：Storage / distributed systems 深扎
2026-10 ~ 2026-12：KVCache / inference systems 补完整
2027-01 ~ 2027-02：正式面试窗口
2027-03：年终奖后决策和 offer 收口
2027-04：理想入职窗口
```

这条路线的主叙事：

```text
TokaDB / DB storage kernel
-> DeepSeek-style AI Core Storage / 3FS / KVCache Storage
-> LLM Inference Runtime / serving / scheduler / MoE
-> long-term Robot/VLA Runtime
```

## 为什么延长是对的

- 三个月可以建立面试语言，但很难把 TokaDB、ByteStore、3FS、KVCache、vLLM、RDMA/SPDK/io_uring 和 DeepSeek 推理系统真正串透。
- 6-8 个月可以从“知道名词”变成“能讲系统边界、代码路径、性能瓶颈、失败模式和设计取舍”。
- 2027-01/02 开始面试，2027-04 入职，可以兼顾年终奖、准备完整度和市场机会。
- 这个周期能同时保留两条主线：Storage 是第一跳，Inference 是第二跳提前埋线。

## 阶段 1：Storage Foundation

时间：`2026-07 ~ 2026-08`

目标：把当前 DB / storage 背景变成 AI Core Storage 的硬证据。

P0 内容：

- TokaDB 数据模型、metadata、tablet / replication group、zero-copy migration。
- TokaDB engine / RocksDB engine / LSM / WAL / compaction / iterator / snapshot。
- ByteStore：blob / chunk / metadata / placement / replication / recovery。
- brpc：bthread、RPC latency、zero-copy attachment、backpressure、bvar / observability。
- IO path：page cache、direct IO、io_uring、SPDK、RDMA、NVMe、polling、queue depth。

阶段产出：

- `TokaDB_Transferable_Systems_Review_v0`
- `RocksDB_LSM_Refresh`
- `ByteStore_Shared_Storage_Map_v0`
- `brpc_Systems_Model_Note`
- `IO_Path_io_uring_SPDK_RDMA_Note_v0`

通过标准：

- 能把 TokaDB 经验抽象成 zero-copy、shared storage、metadata、failure recovery、tail latency，而不是只讲内部业务。
- 能解释为什么 AI storage 岗位看重 RDMA、SPDK、io_uring、RocksDB、FoundationDB。

## 阶段 2：3FS + KVCache Storage

时间：`2026-09 ~ 2026-10`

目标：用 3FS 和 KVCache 把存储系统连接到 DeepSeek-style AI workload。

P0 内容：

- 3FS architecture：client、metadata service、storage service、FoundationDB、FUSE、USRBIO。
- 3FS consistency：Chain Replication / CRAQ、metadata consistency、failure recovery、rebalance。
- 3FS IO path：SSD / NVMe / RDMA / user-space IO / kernel path tradeoff。
- KVCache lifecycle：prefill、decode、block/page、prefix reuse、eviction、offload、recovery。
- KVCache tiering：HBM、DRAM、SSD、remote storage。

阶段产出：

- `3FS_Architecture_First_Pass`
- `3FS_Metadata_Consistency_Note`
- `3FS_IO_Path_RDMA_SSD_Note`
- `KVCache_Storage_System_Map_v0`
- `3FS_KVCache_Offload_Note`

通过标准：

- 能做一次 45-60 分钟系统设计：`设计一个支撑大模型推理的 KVCache 存储系统`。
- 能讲清 3FS 为什么是 AI training / inference workload 的 shared storage 样本系统。
- 能解释 KVCache storage 为什么直接影响推理吞吐、成本和 tail latency。

## 阶段 3：Inference Runtime Bridge

时间：`2026-11 ~ 2026-12`

目标：补齐比较完整的推理系统，不停留在 storage 视角。

P0 内容：

- LLM inference 基本链路：tokenization、prefill、decode、sampling、streaming。
- vLLM：PagedAttention、block table、KV cache manager、scheduler、continuous batching。
- SGLang / radix cache：prefix cache、request routing、structured generation awareness。
- LMCache / Mooncake / KVCache offload：CPU / SSD / remote KV tier，cache hit，eviction，tail latency。
- DeepSeek-style 模型系统语境：MoE、MLA、long context、reasoning workload、disaggregated prefill/decode。
- TensorRT-LLM / Megatron-Core / Megatron-LM：只补并行和 GPU cluster 概念，不抢主线。

阶段产出：

- `vLLM_PagedAttention_KVCache_Scan`
- `KVCache_to_Inference_Runtime_Map`
- `LLM_Inference_System_First_Pass`
- `DeepSeek_Inference_System_Reading_Map`
- `MoE_Long_Context_Serving_Note`

通过标准：

- 能讲清一个完整 LLM serving 请求从 HTTP/RPC 到 GPU decode 再到 token streaming 的路径。
- 能解释 prefill 和 decode 为什么资源特征不同。
- 能解释 KVCache、scheduler、batching、routing、MoE、long context 如何共同影响吞吐和延迟。

## 阶段 4：Interview Production

时间：`2027-01 ~ 2027-02`

目标：进入正式面试和材料迭代。

准备内容：

- 简历主叙事：`DB / storage kernel -> AI Core Storage -> KVCache / inference runtime`。
- 5 个核心系统故事：
  - TokaDB zero-copy / IO path / buffer ownership。
  - shared storage / metadata / consistency / failure recovery。
  - RocksDB / LSM / compaction / amplification。
  - 3FS architecture / RDMA / SSD / metadata consistency。
  - KVCache storage / offload / inference tail latency。
- 3 个系统设计题：
  - 设计 KVCache 存储系统。
  - 设计 AI training / inference shared storage。
  - 设计 LLM inference serving runtime。
- 代码题和语言：C++ 为主，Rust 初步代码能力作为加分。
- 每周至少 1 次 mock interview 或复盘。

通过标准：

- 能稳定回答 `为什么从 DB / storage 转 AI Core Storage`。
- 能稳定回答 `为什么不是直接去机器人`。
- 能把 DeepSeek / 3FS / KVCache / inference runtime 的学习讲成一条连续能力链。

## 阶段 5：Offer / 入职收口

时间：`2027-03 ~ 2027-04`

目标：拿完年终奖后做清晰决策，理想 2027-04 入职。

3 月动作：

- 对 offer、团队、方向、薪资、年终奖损失、成长路径做决策表。
- 如果 DeepSeek / 同级 AI Core Storage 机会质量足够，优先进入。
- 如果机会一般，继续保留当前工作，同时补推理系统和 KVCache project。

4 月动作：

- 如果入职，前 30 天目标是快速补齐团队真实系统：代码、oncall、性能指标、核心 owner 边界。
- 如果未入职，继续第二轮面试，重点投 AI Core Storage、KVCache Storage、LLM Inference Infra。

## 每周时间分配

按当前节奏，一周 6 天，建议分配为：

```text
Storage / TokaDB / ByteStore / 3FS：45%
Inference / KVCache / vLLM / DeepSeek systems：30%
论文 / 课程 / DDIA / CS336：15%
面试材料 / 简历 / 系统设计 / mock：10%
```

到 2026-11 后，比例调整为：

```text
Storage：30%
Inference：45%
论文 / 课程：15%
面试材料：10%
```

到 2027-01 后，比例调整为：

```text
面试材料 / mock / 投递：40%
Storage 复盘：25%
Inference 复盘：25%
论文 / 课程：10%
```

## 夜间阅读队列

22:00-24:00 适合阅读和课程，不适合硬啃复杂代码。按顺序读：

1. DDIA：Ch2、Ch3、Ch5、Ch6、Ch8、Ch9。
2. 3FS paper / design notes：architecture、metadata、IO path、KVCache。
3. vLLM / PagedAttention paper and docs。
4. LMCache / Mooncake / KVCache offload materials。
5. CS336：inference、serving、systems、scaling 相关讲次。
6. DeepSeek V3 / R1 / MLA / MoE / inference system 相关材料。
7. TensorRT-LLM / Megatron-Core / Megatron-LM：只读 serving / parallelism / inference 相关部分。

## 近期不要做的事

- 不要把 Megatron / TensorRT-LLM 提到 P0，它们是推理全栈补充，不是当前 storage 第一跳。
- 不要在 2026-Q3 重新主攻机器人硬件 / Modern Robotics / VLA paper。
- 不要泛读 LLM 论文，只读能解释 KVCache、serving、MoE、long context、storage offload 的材料。
- 不要把 3FS 读成代码流水账，必须围绕 architecture、metadata、IO path、KVCache 四轮输出。

## 一句话回锚

> 现在最稳的打法是：用 2026-H2 把 Storage 和 Inference 两条线打通，2027-01/02 开始面试，2027-03 拿完年终奖后决策，2027-04 争取进入 DeepSeek / 同级 AI Core Storage 或 LLM Infra 团队。
