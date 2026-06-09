---
type: paper_note
title: "Efficient Memory Management for Large Language Model Serving with PagedAttention"
authors:
  - Woosuk Kwon
  - Zhuohan Li
  - Siyuan Zhuang
  - Ying Sheng
  - Lianmin Zheng
  - Cody Hao Yu
  - Joseph E. Gonzalez
  - Hao Zhang
  - Ion Stoica
arxiv: "2309.06180"
source_url: "https://arxiv.org/abs/2309.06180"
pdf_url: "https://arxiv.org/pdf/2309.06180"
local_pdf: "/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/04_Papers/10_AI_Foundations/Efficient_Memory_Management_for_Large_Language_Model_Serving_with_PagedAttention/Efficient_Memory_Management_for_Large_Language_Model_Serving_with_PagedAttention.pdf"
published: "2023-09-12"
venue: "SOSP 2023"
categories:
  - cs.LG
  - cs.DC
status: in_progress
read_mode: Quick Scan
phase: LLM inference / serving / robot runtime support
linked_project: "[[SO-ARM101 + LeRobot 首闭环]]"
---

# Efficient Memory Management for Large Language Model Serving with PagedAttention

## 一句话 Takeaway

PagedAttention 把每个请求的 KV cache 从“连续大数组”改成“logical KV blocks -> physical KV blocks”的分页映射，核心目标是减少 KV cache 的预留、碎片和重复拷贝，让 vLLM 在相似 latency 下用更大的 batch 提高 serving throughput。

## 为什么现在读

- 这篇对应后续 `vLLM / TensorRT-LLM / VLA runtime` 推理工程能力线。
- 对当前机器人项目的意义不是马上优化 SO-ARM101 的 ACT 小模型，而是建立一个问题框架：大模型/VLA 接入 robot runtime 时，推理延迟、显存、batching、KV cache、吞吐和 tail latency 怎么影响系统设计。
- 当前读法只做 Quick Scan：抓问题、抽象、系统结构和 eval 指标，不进入源码。

## Metadata

- Title: Efficient Memory Management for Large Language Model Serving with PagedAttention
- Authors: Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E. Gonzalez, Hao Zhang, Ion Stoica
- Venue / Date: SOSP 2023 / arXiv 2023-09-12
- Source URL: https://arxiv.org/abs/2309.06180
- PDF URL: https://arxiv.org/pdf/2309.06180
- Local PDF: /Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/04_Papers/10_AI_Foundations/Efficient_Memory_Management_for_Large_Language_Model_Serving_with_PagedAttention/Efficient_Memory_Management_for_Large_Language_Model_Serving_with_PagedAttention.pdf
- Categories: cs.LG, cs.DC
- Code: https://github.com/vllm-project/vllm
- Reading mode: Quick Scan

## Pass 0: Metadata and Position

- 领域：LLM serving / systems / memory management。
- 核心对象：KV cache。
- 系统：vLLM。
- 关键抽象：PagedAttention。
- 今天要回答的问题：
  - KV cache 为什么会成为 serving 的显存瓶颈？
  - PagedAttention 怎么借鉴 virtual memory / paging？
  - vLLM 提升的是 throughput、latency、memory utilization 里的哪几项？
  - 这个问题未来如何回接 VLA / robot runtime？

## Pass 1: Abstract + Introduction 理解

### 问题

LLM serving 的成本瓶颈不是只在模型参数，而是在 autoregressive decoding 时每个 request 都要不断增长的 `KV cache`。

论文里给了一个很有用的数量级：OPT-13B 中单个 token 的 KV cache 约为：

```text
2  // key + value
* 5120  // hidden size
* 40  // layers
* 2 bytes  // FP16
= ~800KB / token
```

如果最大长度是 2048 tokens，一个 request 的 KV cache 上限可以到约 1.6GB。GPU 上模型权重常驻，activation 只短暂存在，所以 serving 时能同时 batch 多少请求，很大程度取决于 KV cache 怎么管理。

### 旧系统为什么不够

旧 serving 系统一般把每个 request 的 KV cache 放到连续内存里，并且因为输出长度未知，会按最大长度或预估长度提前分配。这样产生三类浪费：

- `reserved memory`：未来可能会用，但当前还没用，仍然被占着。
- `internal fragmentation`：实际生成长度比预留长度短。
- `external fragmentation`：不同大小连续 chunk 造成 allocator 层碎片。

论文 profiling 里指出，旧系统实际用于 token state 的 KV cache 内存比例可能只有 20.4%-38.2%。这会直接限制 batch size。

### 关键 insight

把 KV cache 管理问题看成 OS virtual memory 问题：

```text
request ~= process
token state ~= byte
KV block ~= page
block table ~= page table
physical GPU blocks ~= physical memory pages
```

一个 request 逻辑上仍然看到连续 token context，但物理 GPU memory 里不要求连续。每次生成新 token，只在需要时分配新的 physical KV block。

### 贡献

- 提出 PagedAttention：attention kernel 可以从非连续 KV blocks 中读取 key/value。
- 构建 vLLM：scheduler + KV block manager + custom CUDA kernels。
- 支持 block-level sharing：parallel sampling、beam search、shared prefix 都能共享部分 KV cache。
- 在相似 latency 下，相比 FasterTransformer / Orca 类系统实现 2-4x throughput improvement；长序列、大模型、复杂 decoding 场景更明显。

## Pass 2: Structure Map

| Section | 作用 | 首轮是否精读 |
|---|---|---|
| Abstract / Introduction | 定义 serving 瓶颈和 KV cache 问题 | 是 |
| Background / Motivation | 解释 existing serving systems 为什么浪费显存 | 是 |
| PagedAttention | 核心抽象和 KV cache block 管理 | 是 |
| vLLM System | scheduler、block manager、parallel sampling 等系统实现 | 选读 |
| Evaluation | throughput、latency、memory、不同模型/序列长度/decoding 场景 | 是 |
| Discussion / Limitations | 适用边界和后续系统问题 | 扫 |

## Pass 3: Systems Reading Questions

- Workload：在线 LLM serving，请求长度动态变化，decode 阶段 KV cache 持续增长。
- Assumption：模型参数大，KV cache 也大；batching 能提高吞吐，但显存浪费会限制 batch size。
- Key abstraction：把每个 request 的 KV cache 拆成 blocks，用类似 page table 的方式映射 logical blocks 到 physical blocks。
- Resource question：减少 internal/external fragmentation，支持共享 KV blocks。
- Scheduling question：vLLM 如何把 PagedAttention 接进 batching / decoding / sampling。
- Evaluation question：相同 latency 约束下，throughput 相比 FasterTransformer / Orca 等 baseline 如何变化。

## Pass 3: Method

### 1. KV block

PagedAttention 把 KV cache 切成固定 token 数的 block。论文默认认为 block size 要在两件事之间折中：

- block 太小：kernel 读取和调度开销变大，GPU parallelism 不够好。
- block 太大：最后一个 block 的空洞更大，internal fragmentation 增加，共享概率下降。

论文实验里 vLLM 默认 block size 取 `16 tokens`，因为它在多数 workload 下足够利用 GPU，又不会带来太明显碎片。

### 2. Block table

每个 request 维护一张 block table：

```text
logical block 0 -> physical block 7
logical block 1 -> physical block 1
logical block 2 -> physical block 3
...
```

生成新 token 时：

1. 如果最后一个 logical block 还有空位，就把新 token 的 KV 写进去。
2. 如果最后一个 block 满了，就申请一个新的 physical KV block。
3. block table 更新 logical -> physical 映射。

因此 request 不需要一开始占满最大长度，只按需增长。request 完成后，physical blocks 释放回全局 pool。

### 3. Paged attention kernel

传统 attention 假设 KV cache 在连续内存里；PagedAttention 的 kernel 在计算 attention 时按 block table 找到每段 key/value 所在的 physical block，然后分块读取。

额外成本来自：

- block table indirection
- 非连续 memory access
- 分支和变长序列处理

vLLM 用 fused kernels 降低这些成本，例如 fused reshape/block write、fused block read + attention、fused block copy。

### 4. Sharing and copy-on-write

PagedAttention 还支持 block-level sharing：

- parallel sampling：多个 sample 共享同一个 prompt 的 KV blocks。
- beam search：beam candidates 在分叉前共享 KV blocks。
- shared prefix：系统 prompt / few-shot examples 可被多个请求共享。

当某个共享 block 需要写入时，用 copy-on-write：

```text
shared physical block ref_count > 1
-> allocate new physical block
-> copy old block
-> writer writes to its own block
```

这个点和 OS fork / shared library 的直觉完全一致。

### 5. Scheduling and eviction

当 GPU KV blocks 不够时，vLLM 需要决定 preempt 哪些 sequence group。论文讨论了两种恢复方式：

- swapping：把 KV blocks 搬到 CPU memory，之后搬回 GPU。
- recomputation：重新跑 prefill/generation 来恢复 KV cache。

论文里的系统倾向用 request/sequence group 作为调度单位，因为一个 request 的 generation 需要它的全部 context KV cache。

更完整地说，vLLM 的 scheduling / preemption 逻辑是：

- 请求调度策略：FCFS，先到先服务，避免 starvation。
- 当资源不够需要 preempt 时：优先保留早到请求，优先 preempt 晚到请求。
- Eviction granularity：all-or-nothing，驱逐一个 sequence 的全部 blocks，而不是驱逐其中几个 block。
- Sequence group：同一个 request 里的多个 sequences，例如 beam search 的 beam candidates，会 gang-schedule；要么一起继续，要么一起 preempt，因为它们之间可能共享 KV blocks。
- Recovery：
  - `swap`：把 evicted KV blocks 拷到 CPU memory，之后再搬回 GPU。
  - `recompute`：丢弃 KV cache，恢复时把 prompt + 已生成 tokens 作为一个长 prompt 重新跑 prefill 来重建 KV cache。

这里的关键是：KV cache 虽然被切成 page/block，但 decode 一个 sequence 时需要完整历史上下文，所以 scheduler 不能像 OS 那样随便只换出某几个未来可能不用的 page。它利用 LLM workload 的语义做更粗粒度的 preemption。

### 6. Distributed execution

如果模型太大，单卡放不下，vLLM 支持 Megatron-LM 风格的 tensor model parallelism。

核心设定：

- 模型参数被切到多张 GPU 上。
- 每张 GPU worker 处理一部分 attention heads / linear layer shard。
- 所有 GPU worker 每个 step 处理同一批 input tokens。
- 中间结果通过 all-reduce 同步。

KV cache 管理的关键点是：

```text
single centralized scheduler / KV cache manager
-> one common logical-to-physical block mapping
-> broadcast input token IDs + block tables to all GPU workers
```

虽然所有 GPU worker 使用相同的 physical block IDs / block table 视图，但每张卡只存自己负责的那部分 KV cache，例如自己负责的 attention heads。

每个 decoding step：

```text
scheduler:
  1. 选择本轮 batch
  2. 分配需要的新 physical blocks
  3. 准备 input token IDs + block table
  4. broadcast 给所有 GPU workers

GPU workers:
  1. 按 block table 读取本卡上的 KV cache shard
  2. 执行 attention / MLP shard
  3. all-reduce 同步中间结果
  4. 返回 sampled token
```

所以大模型多卡时，PagedAttention 的抽象仍然成立：逻辑 block table 是统一的，physical KV cache 被分布式切片存储。GPU workers 不需要彼此协商 memory management，只要在每轮开始收到 scheduler 发来的 block table。

### 7. Implementation details

论文实现的 vLLM 是一个 end-to-end serving system：

- Frontend：FastAPI，扩展 OpenAI API 风格接口，支持 max sequence length、beam width 等 sampling 参数。
- Control plane：Python 实现 scheduler、block manager。
- Model executor：PyTorch / Transformers 实现 GPT、OPT、LLaMA。
- Distributed communication：NCCL。
- Data plane / hot path：C++/CUDA custom kernels。

代码规模：论文写的是约 8.5K 行 Python + 2K 行 C++/CUDA。

Kernel-level optimization 主要有三个：

1. `Fused reshape and block write`
   - 每层新生成的 KV cache 要切成 blocks、reshape 成适合 block read 的布局、写到 block table 指定位置。
   - 如果拆成多个 kernel，会有 launch overhead，所以融合成一个 kernel。

2. `Fusing block read and attention`
   - 改造 FasterTransformer attention kernel，让它根据 block table 读取非连续 KV blocks，并直接做 attention。
   - 为了 coalesced memory access，论文说给每个 block 分配一个 GPU warp 去读。
   - 同时支持 batch 内 variable sequence lengths。

3. `Fused block copy`
   - COW 时可能要复制多个不连续 blocks。
   - 如果对每个 block 调一次 `cudaMemcpyAsync`，小拷贝太多，开销大。
   - 所以实现一个 batched block copy kernel，把多个 block copies 合成一次 kernel launch。

实现层直觉：

```text
Python scheduler/block manager:
  管 request、sequence group、block table、free block pool、preemption

CUDA kernels:
  按 block table 读写真实 KV cache，尽量减少非连续访问和小 kernel overhead

NCCL:
  多卡 tensor parallel 时同步 model shard 的中间结果
```

所以 PagedAttention 的真正工程点不只是 block table，而是让 block table 不把 GPU hot path 拖慢。

## Pass 4: Experiments

实验主要验证一个假设：如果 KV cache 管得更细，显存浪费减少，就能 batch 更多请求，从而在相似 latency 下提高 throughput。

主要设置：

- Models：OPT-13B/66B/175B、LLaMA-13B。
- Hardware：Google Cloud A2, NVIDIA A100。
- Workloads：ShareGPT、Alpaca 生成请求长度分布。
- Baselines：FasterTransformer、Orca variants。
- Metric：normalized latency 和可承受 request rate / throughput。

关键结果：

- 基础 sampling：vLLM 可承受更高 request rate，长输入/长输出 workload 更明显。
- parallel sampling：共享 prompt KV，sample 数越多收益越大。
- beam search：共享比例更高，memory saving 更明显。
- shared prefix：few-shot prefix 越长，共享 KV cache 带来的吞吐提升越明显。

边界：

- 如果 workload 很短，或 GPU memory 充足到系统变成 compute-bound，PagedAttention 的优势会变小。
- 它适合动态长度、memory-bound、KV cache 大的 LLM serving；不一定适合所有 GPU workload。

## 和 SGLang / RadixAttention 的关系

是的，后续可以接 `SGLang / RadixAttention`。两者都围绕 KV cache，但解决层次不同：

| 技术 | 对应系统 | 核心问题 | 直觉 |
|---|---|---|---|
| PagedAttention | vLLM | 单个/批量请求的 KV cache 如何低碎片、高利用地放进 GPU memory | OS paging / page table |
| RadixAttention | SGLang | 多次 LLM calls / agent / few-shot / chat / self-consistency 中，公共 prefix 的 KV cache 如何自动复用 | radix tree / prefix cache |

更具体：

- PagedAttention 解决的是 `memory layout and allocation`。
- RadixAttention 解决的是 `prefix matching and cache reuse across calls`。
- SGLang 论文明确说 RadixAttention 与 paged attention、continuous batching、tensor parallelism 兼容。

后续阅读顺序建议：

```text
PagedAttention / vLLM
-> Continuous batching / scheduler
-> Automatic prefix caching
-> SGLang / RadixAttention
-> TensorRT-LLM / engine build / deployment
```

## Robot Learning / Runtime Connection

- VLA / LLM 作为机器人高层模块时，推理不是孤立函数调用；它会影响 action frequency、timeout、fallback 和资源预算。
- 如果后续用 LingBot-VLA / OpenVLA / SmolVLA，必须知道：
  - 模型跑在哪里：Mac、V100、云 GPU、边缘设备。
  - 输入上下文有多长：image tokens、state、language task、history。
  - 推理指标是什么：latency、tail latency、throughput、GPU memory。
  - 慢推理如何和低层 policy/action chunk 对接。

## Open Questions

- PagedAttention 对单 robot / low concurrency 的 VLA 推理是否仍然有价值，还是主要服务多请求 serving？
- Robot runtime 更关心 latency 还是 throughput？不同层级是否不同：高层 VLA vs 低层 policy。
- VLA 的 multi-modal KV cache 和纯文本 LLM KV cache 有哪些额外问题？
- TensorRT-LLM 与 vLLM 在 robot deployment 场景里分别适合解决什么问题？
- SGLang / RadixAttention 对机器人 agent workflow 是否更直接：例如 task planning、multi-step reasoning、skill selection、self-consistency、RAG memory。

## Sources

- arXiv: https://arxiv.org/abs/2309.06180
- vLLM docs: https://docs.vllm.ai/en/latest/design/paged_attention/
- SGLang arXiv: https://arxiv.org/abs/2312.07104
- SGLang docs: https://docs.sglang.io/
- LMSYS SGLang blog: https://www.lmsys.org/blog/2024-01-17-sglang/

## 阅读记录

| 日期 | 阅读模式 | 进度 | 产出 |
|---|---|---|---|
| 2026-06-08 | Quick Scan | Pass 0 metadata + note skeleton | 下载 PDF，建立 QUICK_READ |
| 2026-06-08 | Structured Quick Read | Pass 1/3/4 + RadixAttention 对照 | 补齐问题、方法、实验和 SGLang 后续阅读连接 |
