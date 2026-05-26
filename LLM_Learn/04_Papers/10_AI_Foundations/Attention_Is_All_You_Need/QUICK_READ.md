---
type: paper_note
title: Attention Is All You Need
category: 10_AI_Foundations
status: queue
read_mode: Structured Read
phase: 2026-05 / nanoGPT closure
linked_project: [[embodied-ai-mini-stack]]
source_url: https://arxiv.org/abs/1706.03762
arxiv: 1706.03762
doi: https://doi.org/10.48550/arXiv.1706.03762
pdf_url: https://arxiv.org/pdf/1706.03762
local_pdf: Attention_Is_All_You_Need.pdf
subjects: cs.CL, cs.LG
submitted: 2017-06-12
last_revised: 2023-08-02
---

# Attention Is All You Need

## 元信息

- Authors: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin
- Submitted: 2017-06-12 (v1), last revised 2023-08-02 (v7)
- arXiv: `1706.03762`
- Source: https://arxiv.org/abs/1706.03762
- PDF: https://arxiv.org/pdf/1706.03762
- Local PDF: [Attention_Is_All_You_Need.pdf](/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/04_Papers/10_AI_Foundations/Attention_Is_All_You_Need/Attention_Is_All_You_Need.pdf)
- Subjects: cs.CL; cs.LG

## Abstract (arXiv)

The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.
Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles by over 2 BLEU.
On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.

## 一句话 Takeaway

- Transformer 用纯 attention 架构替代 RNN / CNN 式序列建模，是后续 GPT、nanoGPT、LLM inference / runtime 理解的结构起点。

## 为什么现在读

- 当前正在收口 `nanoGPT from scratch`。
- 这篇论文提供 Transformer 的模块语言：attention、multi-head、feed-forward、positional encoding、residual、layernorm。
- 明天的目标不是完整吃透论文所有实验，而是把论文里的结构模块映射到 nanoGPT 代码。

## 8 问

- 任务是什么？
- 输入 / 输出序列是什么？
- attention 解决了什么问题？
- multi-head attention 相比 single-head 增强了什么？
- feed-forward 在 block 内承担什么角色？
- positional encoding 为什么必要？
- residual + layernorm 为什么成为稳定训练的关键结构？
- decoder-only GPT / nanoGPT 和原论文 encoder-decoder Transformer 有什么差异？

## 方法结构

- Scaled Dot-Product Attention
- Multi-Head Attention
- Position-wise Feed-Forward Networks
- Positional Encoding
- Encoder / Decoder Stack
- Residual Connection + Layer Normalization

## 系统 / 工程启发

- attention 把序列建模改成可并行的矩阵计算路径，是后续 GPU 友好训练和推理优化的基础。
- decoder-only GPT 只保留和生成相关的 causal self-attention 路径，后续可以自然接到 decode、KV cache、serving runtime。

## 和 Embodied AI Mini-Stack 的连接

- 语言智能模块未来用于高层任务理解、任务分解、多机器人语言协调。
- 当前读这篇论文，是为了把语言模型内部结构吃透，后续再把语言模型作为 embodied AI 系统中的一个可部署组件，而不是把 LLM 学习变成独立主线。

## 可以转成的实验 Idea

- 用 nanoGPT 代码逐模块对应论文结构，写一张 `paper module -> code module -> runtime implication` 表。
- 对比 `single-head attention`、`multi-head attention` 和 `causal mask` 的张量流。

## 疑问

- 原论文 encoder-decoder 结构和 nanoGPT decoder-only 结构具体删去了哪些部分？
- layernorm 在 nanoGPT 代码里是 pre-norm 还是 post-norm？它和原论文写法有什么差异？
- nanoGPT 的 `generate` 路径如何从训练 forward 复用模型结构？

## 阅读记录

| 日期 | 阅读模式 | 进度 | 产出 |
|---|---|---|---|
| 2026-05-21 | Structured Read | planned | 对应到 `nanogpt-from-scratch/notes/transformer.md` |
