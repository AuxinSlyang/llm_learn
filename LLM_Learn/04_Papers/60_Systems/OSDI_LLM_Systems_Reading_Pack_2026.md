---
type: reading_pack
track: OSDI / LLM Systems / KVCache / Serving
status: active
created: 2026-06-28
---

# OSDI / LLM Systems Reading Pack 2026

## 定位

这份清单服务 2026-H2 的 LLM inference systems 主线，重点不是泛读所有 OSDI，而是抓住：

```text
LLM serving
-> KVCache
-> scheduler
-> prefill/decode
-> offload / memory tiering
-> live migration / serverless / observability
-> agentic workflow
```

## P0：已经可读的 OSDI/Systems 论文

| 优先级 | 论文 | venue | 为什么读 |
|---|---|---|---|
| P0 | Sarathi-Serve: Taming Throughput-Latency Tradeoff in LLM Inference | OSDI 2024 | 理解 chunked prefill、stall-free scheduling，以及 throughput/latency tradeoff |
| P0 | DistServe: Disaggregating Prefill and Decoding for Goodput-optimized LLM Serving | OSDI 2024 | 理解 prefill/decode disaggregation、TTFT/TPOT、GPU resource allocation |
| P0 | InfiniGen: Efficient Generative Inference of Large Language Models with Dynamic KV Cache Management | OSDI 2024 | 理解长文本生成下 KV cache offload / prefetch / host memory bottleneck |
| P0 | ServerlessLLM: Low-Latency Serverless Inference for Large Language Models | OSDI 2024 | 理解 checkpoint loading、multi-tier storage、live migration、serverless inference |
| P1 | Llumnix: Dynamic Scheduling for Large Language Model Serving | OSDI 2024 | 理解 request live migration、tail latency、priority/SLO-aware scheduling |
| P1 | Orca: A Distributed Serving System for Transformer-Based Generative Models | OSDI 2022 | 理解 iteration-level scheduling 和 continuous batching 的经典入口 |

## P0：OSDI 2026 重点观察

OSDI 2026 有一个明确的 `KV Cache and Long Context` session，后续论文公开后应优先读：

| 优先级 | 论文 | 为什么关注 |
|---|---|---|
| P0 | Contextra: Hierarchical Context Caching for Long Context Language Model Serving | long context + hierarchical context caching |
| P0 | ECHO: Efficient KV Cache Offloading with Lossless Prefetching for Serving Native Sparse Attention LLMs | native sparse attention + KV offloading + prefetch |
| P0 | No Buffer, No Bottleneck: Efficient Zero-Copy KV Cache Offloading for Long-Context LLMs | zero-copy KV offload，和 TokaDB zero-copy / IO path 直接对齐 |
| P1 | Simple is Better: Multiplication May Be All You Need for LLM Request Scheduling | request scheduling，适合对照 vLLM/Sarathi/DistServe |
| P1 | Chimera: Cost-Efficient Multi-LLM Serving via GPU Memory Ballooning | multi-LLM serving + GPU memory management |

OSDI 2026 另一个相关 session 是 `Agentic AI and LLM Operations`：

| 优先级 | 论文 | 为什么关注 |
|---|---|---|
| P1 | Murakkab: Resource-Efficient Agentic Workflow Orchestration in Cloud Platforms | agentic workflow orchestration |
| P1 | StriaTrace: Efficient Tracing and Diagnosis for Online LLM Inference | online LLM inference tracing / diagnosis |

## 7 月 OSDI / Serving 子队列

7 月整体执行每天至少 1 篇 paper slot；本文件只维护其中的 OSDI / Serving 子队列，不代表全部论文节奏。每周还需要穿插 LLM core、model、kernel、classic systems 论文。

| Week | 论文 |
|---|---|
| W27 | Sarathi-Serve、DistServe、ServerlessLLM scan |
| W28 | InfiniGen、Llumnix、Orca scan |
| W29 | PagedAttention revisit、SGLang/RadixAttention scan |
| W30 | FlashAttention、DeepSeek-V2 MLA/KVCache sections |
| W31 | OSDI 2026 KV Cache session watchlist 整理 |

## 每篇输出格式

每篇只写 8 行：

```text
系统问题：
核心抽象：
关键机制：
性能瓶颈：
指标：
和 vLLM / KVCache 的关系：
和 TokaDB / RocksDB / 3FS 的关系：
一个可面试问题：
```
