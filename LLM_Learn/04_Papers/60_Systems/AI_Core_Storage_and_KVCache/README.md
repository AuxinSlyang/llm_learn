---
type: reading_track
track: AI Core Storage / KVCache / Shared Storage
status: active_2026Q3
created: 2026-06-28
linked_strategy:
  - [[2026-06-28_DeepSeek_Storage_Three_Hop_Strategy]]
  - [[2026-06-28_DeepSeek_Storage_Interview_Preparation_2026Q3]]
  - [[2026-06-28_DeepSeek_3FS_Study_Plan_2026Q3]]
---

# AI Core Storage and KVCache Reading Track

## 定位

2026-Q3 的论文 / 系统阅读主线从泛 LLM、机器人和 VLA 收敛到：

```text
LLM KVCache
-> shared storage / distributed file system
-> 3FS / RDMA / SSD / IO path
-> DeepSeek Storage 面试证据
```

机器人方向保留为长期 North Star，不作为近期默认 paper slot。

## 读法

每篇材料只回答四个问题：

1. 系统问题：它解决 AI training / serving / storage 的什么瓶颈？
2. 核心抽象：它引入了什么稳定抽象，例如 block、page、chain、metadata、cache tier？
3. 性能边界：瓶颈在 HBM、DRAM、SSD、RDMA、CPU、kernel、RPC、metadata 还是 scheduler？
4. 面试迁移：它如何帮助回答 DeepSeek Storage JD 或自己的 TokaDB / ByteStore / brpc 经历？

## P0 Reading Order

### 1. 3FS / Fire-Flyer File System

- Source：`https://github.com/deepseek-ai/3fs`
- Why：DeepSeek Storage 公开主样本；连接 SSD、RDMA、shared storage、dataloader、checkpoint、KVCache。
- Output：`3FS_Architecture_First_Pass.md`

### 2. Fire-Flyer AI-HPC

- Source：`https://arxiv.org/abs/2408.14158`
- Why：理解 DeepSeek AI-HPC 背景，以及 3FS / 3FS-KV / KV Context Caching on Disk 在系统里的位置。
- Output：`Fire_Flyer_AI_HPC_Storage_Notes.md`

### 3. PagedAttention / vLLM

- Source：`https://arxiv.org/abs/2309.06180`
- Why：KV cache memory management 的基本论文；连接 block/page、fragmentation、sharing、serving scheduler。
- Existing note：`../10_AI_Foundations/Efficient_Memory_Management_for_Large_Language_Model_Serving_with_PagedAttention/`
- Output：`vLLM_PagedAttention_KVCache_Scan.md`

### 4. LMCache

- Source：`https://arxiv.org/abs/2510.09665`
- Why：KV cache 作为跨 engine / query 的 storage and communication medium；直接服务 KVCache storage 设计。
- Output：`LMCache_KVCache_Layer_Note.md`

### 5. Mooncake

- Source：`https://arxiv.org/abs/2407.00079`
- Why：KVCache-centric disaggregated serving；prefill/decode 分离，CPU/DRAM/SSD/NIC 组成 disaggregated KVCache pool。
- Output：`Mooncake_KVCache_Disaggregated_Serving_Note.md`

### 6. CacheGen

- Source：`https://arxiv.org/abs/2310.07240`
- Why：KV cache compression and streaming；回答长上下文 KV 传输和带宽瓶颈。
- Output：`CacheGen_KVCache_Compression_Streaming_Note.md`

## P1 Reading Order

### 7. FoundationDB

- Source：`https://www.foundationdb.org/files/fdb-paper.pdf`
- Why：3FS metadata service 的关键依赖；理解 transactional KV、unbundled architecture、deterministic simulation。
- Output：`FoundationDB_Metadata_Service_Note.md`

### 8. CRAQ

- Source：`https://www.usenix.org/legacy/event/usenix09/tech/full_papers/terrace/terrace.pdf`
- Why：3FS 提到的强一致 replication / read throughput 支撑概念。
- Output：`CRAQ_Chain_Replication_Apportioned_Queries_Note.md`

### 9. RocksDB / LSM

- Source：`https://github.com/facebook/rocksdb`
- Source：`https://rocksdb.org/`
- Why：JD 明确提到顶尖开源系统设计范式；也是现有 DB / storage 经验的面试语言。
- Output：`RocksDB_LSM_Refresh.md`

## 暂停规则

近期暂停主动新增这些阅读：

- 泛 LLM 经典论文，除非直接服务 KVCache / serving / AI storage。
- CV / VLA / Diffusion / Robot Learning，除非用于长期 North Star 的低频探索。
- 新的机器人 repo / paper，除非和 storage / runtime / data loop 直接相关。

## 一句话回锚

> 这条 reading track 的目标不是读更多论文，而是把每篇材料转成 DeepSeek Storage 面试中可讲深的系统证据。
