---
type: reading_guide
paper: Efficient Memory Management for Large Language Model Serving with PagedAttention
url: https://arxiv.org/abs/2309.06180
status: revisit
created: 2026-06-28
---

# PagedAttention / vLLM Revisit 阅读卡片

## 为什么仍然保留

PagedAttention 已经看过一轮，不再作为今晚主菜；但它仍然是后续 KVCache storage / LMCache / Mooncake / 3FS 对齐的基础材料。

这篇把几个核心问题放在同一张图里：

```text
request
-> prefill
-> KVCache allocation
-> decode loop
-> scheduler / batching
-> token streaming
-> throughput / latency
```

它也最适合连接当前主线：

```text
KVCache memory management
-> block/page abstraction
-> storage-style allocation / sharing / eviction
-> 3FS / LMCache / Mooncake / KVCache offload
```

## Revisit 时只读这些部分

### Pass 0：定位

要回答：

- 这篇论文属于 LLM serving / inference runtime，不是模型训练论文。
- 它解决的是 KVCache 显存管理低效导致 batch size 上不去、吞吐受限的问题。
- 它的关键类比是 OS virtual memory / paging。

### Pass 1：Abstract + Introduction

要抓住：

- LLM serving 的吞吐依赖 batching。
- 每个 request 的 KVCache 很大，且随输出长度动态增长。
- naive contiguous allocation 会产生 fragmentation 和 duplication。
- PagedAttention 用 block/page 管理 KVCache，让 vLLM 接近 zero waste，并支持跨 request 的 KV sharing。

### Pass 2：System Map

画这张图：

```text
Client requests
  -> vLLM scheduler
  -> prefill phase
  -> KV blocks allocated by block manager
  -> decode phase loop
  -> PagedAttention reads non-contiguous KV blocks
  -> token output / streaming
```

### Pass 3：重点概念

- `prefill`：一次性处理 prompt，生成初始 KVCache；算力密集，TTFT 关键。
- `decode`：每轮生成一个 token，持续读取历史 KVCache；memory bandwidth / scheduling 关键。
- `KVCache`：每层 attention 的 key/value 历史张量，是长上下文和多并发下的显存大头。
- `block table`：把 logical token positions 映射到 physical KV blocks。
- `copy-on-write / sharing`：多个 request 共享 prompt prefix 时，可以共享 KV blocks。
- `continuous batching`：不同 request 的 decode step 可以动态进出 batch。

### Pass 4：读完要回答

- 为什么 LLM serving 的核心瓶颈不是只有 FLOPs？
- 为什么 KVCache 的生命周期像 storage / memory management 问题？
- 为什么 PagedAttention 可以类比 OS paging？
- vLLM 的性能收益来自 attention kernel，还是来自 scheduler + memory manager + block abstraction 的组合？
- 如果 KVCache 放到 DRAM / SSD / remote storage，PagedAttention 的 block/page 抽象还能不能复用？

## 和我们路线的连接

这篇读完后，后续系统会自然串起来：

```text
PagedAttention / vLLM：GPU HBM 内的 KV block 管理
LMCache：跨 engine / query 的 KVCache storage and movement
Mooncake：prefill/decode disaggregation + distributed KVCache pool
3FS：SSD + RDMA shared storage，支撑 AI workload 和 KVCache offload
TokaDB / ByteStore：已有 shared storage / metadata / IO path / zero-copy 经验的迁移样本
```

## Revisit 输出

复读时只写 10 行：

```text
这篇解决的问题：
核心抽象：
prefill / decode 区别：
KVCache 为什么大：
PagedAttention 为什么像 paging：
vLLM scheduler 做什么：
和 storage 的连接：
我还没懂的问题：
下一篇该读：
```
