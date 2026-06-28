---
type: paper_note
paper: DeepSeek-V2
title: "DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model"
arxiv: "2405.04434"
source_url: "https://arxiv.org/abs/2405.04434"
pdf_url: "https://arxiv.org/pdf/2405.04434"
source_pdf_local: "DeepSeek_V2_A_Strong_Economical_and_Efficient_Mixture_of_Experts_Language_Model.pdf"
status: active
reading_mode: structured_scan
created: 2026-06-28
track: AI Core Storage / KVCache / Inference Runtime
---

# DeepSeek-V2: MLA / MoE / KVCache Structured Scan

## Why Read Now

今晚不读完整 DeepSeek 系列，只读 DeepSeek-V2 中和当前路线直接相关的部分：

```text
MLA -> KV cache compression -> inference throughput / memory bandwidth
DeepSeekMoE -> sparse compute -> training/inference economics
128K context -> KVCache pressure -> storage / serving / offload
```

这篇论文是从 Storage 进入 LLM Inference 的关键桥：

```text
TokaDB / RocksDB / ByteStore / 3FS
-> memory / IO / metadata / cache lifecycle
-> KVCache as inference-time storage object
-> DeepSeek-style model architecture reduces storage pressure at source
```

## Tonight Scope

必读：

- Abstract
- Section 1 Introduction
- Section 2.1 Multi-Head Latent Attention
- Section 2.2 DeepSeekMoE
- Section 3.2.3 Training and Inference Efficiency
- Section 5 Conclusion

可跳过：

- 完整 benchmark 表格细节。
- SFT / RL 全流程，今晚只看它对最终 chat model 的位置。
- Appendix 公式细节，除非 MLA 看不懂再回去补。

## 8-Line Notes

问题：

- 大模型规模变大后，训练成本、推理吞吐和 KV cache 内存占用同时变成瓶颈。

核心抽象：

- MLA 把传统 full KV cache 压成 latent KV cache；DeepSeekMoE 用 sparse expert routing 降低每 token 激活参数和训练/推理成本。

关键机制：

- MLA：low-rank key-value joint compression + decoupled RoPE。
- MoE：fine-grained expert segmentation + shared expert isolation + routed experts。

性能瓶颈：

- decode 阶段的 KV cache 容量和 memory bandwidth。
- MoE 训练/推理里的 expert routing、load balance、communication overhead。

指标 / 证据：

- DeepSeek-V2 有 236B total parameters，每 token 激活 21B，支持 128K context。
- 相比 DeepSeek 67B：训练成本节省 42.5%，KV cache 减少 93.3%，最大生成吞吐提升到 5.76x。

和 LLM big picture 的关系：

- 它不是单纯 scale-up，而是 model architecture + systems efficiency 的共同设计：用 MLA/MoE 同时追求能力和成本。

和 TokaDB / RocksDB / ByteStore / 3FS / KVCache 的关系：

- KV cache 可以被看成推理时的 append-heavy / read-heavy / latency-sensitive storage object。
- MLA 从模型结构层减少 KV cache footprint，ByteStore/3FS/LMCache/Mooncake 则从系统层处理 KV movement、offload、tiering。

一个可面试问题：

- 如果 KV cache 是 LLM serving 的主要 memory bottleneck，应该优先从模型结构、runtime scheduler、cache storage/offload 哪一层优化？各自 tradeoff 是什么？

## Reading Questions

1. MLA 为什么比 MQA / GQA 更激进？
2. 为什么只缓存 latent vector 能减少 KV cache，但还需要 decoupled RoPE？
3. MLA 的收益主要来自容量减少，还是 memory bandwidth 下降？
4. DeepSeekMoE 的 sparse compute 如何影响 serving latency 和 load balance？
5. 128K context 下，KV cache 从 GPU memory 问题如何变成 storage / network / scheduler 问题？
6. 这篇论文给 KVCache Storage 系统设计带来什么前置假设？

## First Takeaway

DeepSeek-V2 的关键不是“又一个大模型”，而是把 LLM 能力提升和推理成本控制放进同一个设计里：MLA 在 attention 侧压缩 KV cache，DeepSeekMoE 在 FFN 侧降低每 token 激活计算。对我们当前路线来说，MLA 是连接模型结构和 AI Core Storage 的入口：如果模型侧能把 KV cache 减少 90% 以上，系统侧的 offload、tiering、prefetch、cache eviction 设计都会随之改变。
