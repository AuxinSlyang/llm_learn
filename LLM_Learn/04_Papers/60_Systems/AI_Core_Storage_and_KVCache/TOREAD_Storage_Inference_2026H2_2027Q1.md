---
type: paper_queue
track: AI Core Storage / LLM Inference Systems
date_range: 2026-07_to_2027-02
status: active
---

# TOREAD: Storage + Inference 论文清单 2026H2-2027Q1

## 读法规则

- P0 必须读成结构化笔记；P1 可以 structured scan；P2 只做 awareness。
- 每篇只回答：解决什么问题、核心抽象是什么、性能瓶颈在哪里、和 TokaDB / 3FS / KVCache / inference runtime 的连接是什么。
- 论文服务面试和系统理解，不做泛读收藏。

## 近期夜间入口

| 顺序 | 论文 | 链接 | 读法 | 为什么今晚读 |
|---|---|---|---|---|
| 1 | Sarathi-Serve: Taming Throughput-Latency Tradeoff in LLM Inference | https://www.usenix.org/conference/osdi24/presentation/agrawal | Structured Scan | PagedAttention 已看过，7 月夜间从 OSDI 2024 serving 主线切入：chunked prefill、stall-free scheduling、TTFT/TPOT/throughput tradeoff。 |

## 每日一篇论文规则

7 月开始，每天至少完成 1 篇 paper slot。不要只局限 serving，每周按下面比例轮转：

- 2 篇 LLM core / model / post-training / context / kernel。
- 2 篇 serving / KVCache / inference runtime。
- 1 篇 storage / distributed systems / IO path。
- 1 篇本周重点 deep read 或复盘。

默认产出不超过 8 行：

```text
问题：
核心抽象：
关键机制：
性能瓶颈：
指标 / 证据：
和 LLM big picture 的关系：
和 TokaDB / RocksDB / ByteStore / 3FS / KVCache 的关系：
一个可面试问题：
```

## 7 月论文池

### LLM core / model / post-training / context

| 优先级 | 论文 / 材料 | 读法 | 备注 |
|---|---|---|---|
| P0 | DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model | Structured Scan | 先看 MLA / MoE / KVCache 相关 sections |
| P0 | FlashAttention | Structured Scan | 连接 attention IO bottleneck 和 storage/IO path 直觉 |
| P1 | LoRA | Scan | 参数高效微调，补现代 LLM 工程常识 |
| P1 | Switch Transformers | Scan | MoE / expert routing 入口，为 DeepSeek-V2/V3 做准备 |
| P1 | Position Interpolation / YaRN | Scan | long context 和 KVCache 压力的前置背景 |
| P2 | DeepSeek-R1 | Scan | 只看 reasoning workload 对 serving/KVCache 的压力，不深挖 RL 细节 |

### Serving / KVCache / runtime

| 优先级 | 论文 / 材料 | 读法 | 备注 |
|---|---|---|---|
| P0 | Sarathi-Serve | Structured Scan | 7 月 serving 候选之一 |
| P0 | DistServe | Structured Scan | prefill/decode disaggregation |
| P0 | Orca | Structured Scan | continuous batching 经典入口 |
| P0 | ServerlessLLM | Structured Scan | model loading / multi-tier storage / live migration |
| P1 | InfiniGen | Structured Scan | dynamic KV cache management |
| P1 | SGLang / RadixAttention | Scan | prefix cache / structured generation runtime |
| P1 | PagedAttention revisit | Structured Scan | 10-11 月结合 vLLM 代码再深读 |
| P1 | DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation | Structured Scan | DeepSeek speculative decoding / live serving paper；后续在 inference runtime 阶段读，不抢今晚 DeepSeek-V2 |

### Speculative decoding / decoding runtime 后续包

| 优先级 | 论文 / 材料 | 链接 | 读法 | 为什么读 |
|---|---|---|---|---|
| P0 | Fast Inference from Transformers via Speculative Decoding | https://arxiv.org/abs/2211.17192 | Structured Scan | speculative decoding 基础：draft model proposes, target model verifies |
| P0 | Accelerating Large Language Model Decoding with Speculative Sampling | https://arxiv.org/abs/2302.01318 | Structured Scan | 和上篇一起建立 lossless speculative sampling 基本算法 |
| P1 | SpecInfer: Accelerating Generative LLM Serving with Tree-based Speculative Inference and Verification | https://arxiv.org/abs/2305.09781 | Structured Scan | token tree + parallel verification；更接近 serving system 视角 |
| P1 | Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads | https://arxiv.org/abs/2401.10774 | Structured Scan | 不依赖独立 draft model，用多 decoding heads + tree attention |
| P1 | EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty | https://arxiv.org/abs/2401.15077 | Scan | feature-level drafter，理解 DSpark / EAGLE 系列背景 |
| P1 | EAGLE-2: Faster Inference of Language Models with Dynamic Draft Trees | https://arxiv.org/abs/2406.16858 | Scan | dynamic draft tree；和 DSpark confidence scheduling 对照 |
| P1 | Break the Sequential Dependency of LLM Inference Using Lookahead Decoding | https://arxiv.org/abs/2402.02057 | Scan | 不用 draft model 的并行解码路线 |
| P1 | Better & Faster Large Language Models via Multi-token Prediction | https://arxiv.org/abs/2404.19737 | Scan | MTP 背景；连接 DeepSeek-V3 MTP 和 speculative decoding |
| P1 | DeepSeek-V3 Technical Report | https://arxiv.org/abs/2412.19437 | Targeted Scan | 只读 MTP / speculative decoding / inference acceleration 相关段落 |
| P1 | DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation | https://github.com/deepseek-ai/DeepSpec/blob/main/DSpark_paper.pdf | Structured Scan | DeepSeek 最新 speculative decoding 系统；和 production serving 直接相关 |
| Code | DeepSpec repository | https://github.com/deepseek-ai/DeepSpec | Code Scan | 后续看 draft model training / evaluation / DSpark implementation |
| Code | vLLM speculative decoding docs/code | https://docs.vllm.ai/ | Code Scan | 看 serving engine 中 speculative decoding 怎么接 scheduler / batch |
| Code | SGLang speculative decoding docs/code | https://docs.sglang.ai/ | Code Scan | 看 runtime 侧 speculative decoding 与 request scheduling 的实现边界 |

### Storage / distributed systems / IO path

| 优先级 | 论文 / 材料 | 读法 | 备注 |
|---|---|---|---|
| P0 | RocksDB / LSM docs | Structured Scan | 和 mini-lsm/TokaDB 同步 |
| P1 | GFS | Scan | 分布式文件系统基本盘 |
| P1 | Bigtable | Scan | LSM / tablet / distributed storage 经典背景 |
| P1 | Fire-Flyer AI-HPC | Structured Scan | DeepSeek storage/3FS 背景 |
| P1 | FoundationDB | Scan | 9 月 3FS metadata 前置 |
| P1 | CRAQ | Scan | 9 月 chain replication / consistency 前置 |

## P0：LLM Big Picture 最小闭环

| 顺序 | 论文 / 材料 | 链接 | 月份 | 输出 |
|---|---|---|---|---|
| 1 | Attention Is All You Need | https://arxiv.org/abs/1706.03762 | 2026-07 | `Transformer_Architecture_Refresh` |
| 2 | Language Models are Few-Shot Learners | https://arxiv.org/abs/2005.14165 | 2026-07 | `GPT3_Scaling_and_InContext_Learning_Note` |
| 3 | Training Compute-Optimal Large Language Models | https://arxiv.org/abs/2203.15556 | 2026-07 | `Chinchilla_Compute_Data_Tradeoff_Note` |
| 4 | Training language models to follow instructions with human feedback | https://arxiv.org/abs/2203.02155 | 2026-07 | `InstructGPT_PostTraining_Refresh` |
| 5 | Llama 2: Open Foundation and Fine-Tuned Chat Models | https://arxiv.org/abs/2307.09288 | 2026-07 | `Modern_LLM_Training_Pipeline_Note` |

## P0：项目 / 代码材料

| 顺序 | 项目 / 材料 | 链接 | 月份 | 输出 |
|---|---|---|---|---|
| P0-1 | TokaDB TabletServer source path | local: `/home/yangshunlei/tokadb/tokadb-blade/tokadb/tokadb/tabletserver` | 2026-07 | `TabletServer_Request_Path_Map` |
| P0-2 | mini-lsm / LSM in a Week | https://skyzh.github.io/mini-lsm/ | 2026-07 | `TinyLSM_Month1_Project_Review` |
| P0-3 | RocksDB source/docs | https://github.com/facebook/rocksdb | 2026-07/08 | `RocksDB_LSM_Refresh`、`RocksDB_Deep_Dive_Note` |
| P0-4 | ByteStore source path | local: `/home/yangshunlei/study/bytestore` | 2026-08/09 | `ByteStore_Shared_Storage_Map_v0`、`ByteStore_IO_Path_Map` |
| P0-5 | brpc / bthread source/docs | local: `/home/yangshunlei/study/brpc` | 2026-08 | `brpc_bthread_Model_Note` |
| P0-6 | 3FS source/docs | https://github.com/deepseek-ai/3FS | 2026-09 | `3FS_Architecture_First_Pass`、`3FS_IO_Path_RDMA_SSD_Note` |
| P1-1 | SlateDB | https://slatedb.io/ | 2026-09 | `Shared_Storage_Project_Ladder_2026Q3` |
| P1-2 | Tonbo | https://github.com/tonbo-io/tonbo | 2026-09 | `Shared_Storage_Project_Ladder_2026Q3` |
| P1-3 | JuiceFS | https://juicefs.com/ | 2026-09 | `Shared_Storage_Project_Ladder_2026Q3` |

## P0：Inference Runtime / KVCache

| 顺序 | 论文 / 材料 | 链接 | 月份 | 输出 |
|---|---|---|---|---|
| 6 | Efficient Memory Management for Large Language Model Serving with PagedAttention | https://arxiv.org/abs/2309.06180 | 2026-07/10 | `vLLM_PagedAttention_KVCache_Scan` |
| 7 | Orca: A Distributed Serving System for Transformer-Based Generative Models | https://www.usenix.org/conference/osdi22/presentation/yu | 2026-08/11 | `Orca_Continuous_Batching_Note` |
| 8 | SGLang: Efficient Execution of Structured Language Model Programs | https://arxiv.org/abs/2312.07104 | 2026-11 | `SGLang_RadixCache_Note` |
| 9 | DistServe: Disaggregating Prefill and Decoding for Goodput-optimized LLM Serving | https://arxiv.org/abs/2401.09670 | 2026-10/11 | `DistServe_Prefill_Decode_Disaggregation_Note` |
| 10 | FlexGen: High-Throughput Generative Inference of Large Language Models with a Single GPU | https://arxiv.org/abs/2303.06865 | 2026-10 | `FlexGen_Offload_Memory_Hierarchy_Note` |
| 10b | DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation | https://github.com/deepseek-ai/DeepSpec/blob/main/DSpark_paper.pdf | 2026-11/12 | `DSpark_Speculative_Decoding_Note` |

## P0：DeepSeek-style Storage / 3FS / KVCache

| 顺序 | 论文 / 材料 | 链接 | 月份 | 输出 |
|---|---|---|---|---|
| 11 | Fire-Flyer File System / 3FS repository and design docs | https://github.com/deepseek-ai/3FS | 2026-09 | `3FS_Architecture_First_Pass` |
| 12 | Fire-Flyer AI-HPC: A Cost-Effective Software-Hardware Co-Design for Deep Learning | https://arxiv.org/abs/2408.14158 | 2026-08/09 | `Fire_Flyer_AI_HPC_Storage_Notes` |
| 13 | FoundationDB: A Distributed Unbundled Transactional Key Value Store | https://www.foundationdb.org/files/fdb-paper.pdf | 2026-09 | `FoundationDB_Metadata_Service_Note` |
| 14 | CRAQ: Chain Replication with Apportioned Queries | https://www.usenix.org/legacy/event/usenix09/tech/full_papers/terrace/terrace.pdf | 2026-09 | `CRAQ_Chain_Replication_Apportioned_Queries_Note` |
| 15 | LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference | https://arxiv.org/abs/2510.09665 | 2026-10 | `LMCache_KVCache_Layer_Note` |
| 16 | Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving | https://arxiv.org/abs/2407.00079 | 2026-10 | `Mooncake_KVCache_Disaggregated_Serving_Note` |

## P0：DeepSeek Model / Inference Context

| 顺序 | 论文 / 材料 | 链接 | 月份 | 输出 |
|---|---|---|---|---|
| 17 | DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model | https://arxiv.org/abs/2405.04434 | 2026-11/12 | `DeepSeek_V2_MLA_MoE_Note` |
| 18 | DeepSeek-V3 Technical Report | https://arxiv.org/abs/2412.19437 | 2026-12 | `DeepSeek_V3_System_Note` |
| 19 | DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning | https://arxiv.org/abs/2501.12948 | 2026-12 | `DeepSeek_R1_Inference_Workload_Note` |

## P1：Attention Kernel / GPU Memory

| 顺序 | 论文 / 材料 | 链接 | 月份 | 输出 |
|---|---|---|---|---|
| 20 | FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness | https://arxiv.org/abs/2205.14135 | 2026-08 | `FlashAttention_IO_Aware_Attention_Note` |
| 21 | FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning | https://arxiv.org/abs/2307.08691 | 2026-11 | `FlashAttention2_Parallelism_Note` |
| 22 | FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision | https://arxiv.org/abs/2407.08608 | 2026-12 | `FlashAttention3_Hopper_Awareness_Note` |

## P1：MoE / Parallelism / Large Model Systems

| 顺序 | 论文 / 材料 | 链接 | 月份 | 输出 |
|---|---|---|---|---|
| 23 | Switch Transformers | https://arxiv.org/abs/2101.03961 | 2026-12 | `Switch_Transformer_MoE_Note` |
| 24 | Mixtral of Experts | https://arxiv.org/abs/2401.04088 | 2026-12 | `Mixtral_MoE_Inference_Note` |
| 25 | Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism | https://arxiv.org/abs/1909.08053 | 2026-12/2027-01 | `Megatron_Parallelism_Awareness_Note` |
| 26 | ZeRO: Memory Optimizations Toward Training Trillion Parameter Models | https://arxiv.org/abs/1910.02054 | 2027-01 | `ZeRO_FSDP_Sharding_Awareness_Note` |

## P2：经典分布式存储补充

| 顺序 | 论文 / 材料 | 链接 | 月份 | 输出 |
|---|---|---|---|---|
| 27 | The Google File System | https://research.google/pubs/the-google-file-system/ | 2026-08 | `GFS_Distributed_File_System_Refresh` |
| 28 | Bigtable | https://research.google/pubs/bigtable-a-distributed-storage-system-for-structured-data/ | 2026-08 | `Bigtable_Storage_Model_Refresh` |
| 29 | Dynamo | https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf | 2026-08 | `Dynamo_Availability_Consistency_Refresh` |
| 30 | Spanner | https://research.google/pubs/spanner-googles-globally-distributed-database/ | 2026-08 | `Spanner_Consistency_Refresh` |

## 暂停队列

这些不是不重要，而是暂时不抢主线：

- VLA / Robot Learning / Diffusion Policy：2027-04 后根据入职情况回接。
- 泛 Agent / Tool-use / RAG：只在和 inference workload、KV reuse、long context 明确相关时读。
- 泛多模态 / CV：不进入 2026-H2 默认 paper slot。

## 当前阅读顺序

今晚开始：

```text
TokaDB TabletServer + mini-lsm / RocksDB / LSM docs
-> Sarathi-Serve / DistServe / Orca / ServerlessLLM
-> ByteStore + RocksDB deep dive + classic systems papers
-> brpc / bthread + high-performance programming notes
-> ByteStore / 3FS / Fire-Flyer AI-HPC
-> FoundationDB / CRAQ + io_uring / SPDK / RDMA
-> KVCache / PagedAttention / LMCache / Mooncake / DistServe
-> SGLang / RadixAttention / vLLM code
-> DeepSeek-V3 / R1
```

## OSDI / LLM Systems Pack

当前单独维护在：[[OSDI_LLM_Systems_Reading_Pack_2026]]
