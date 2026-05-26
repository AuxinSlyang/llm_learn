---
type: paper_note
title: Neural Machine Translation by Jointly Learning to Align and Translate
category: 10_AI_Foundations
status: reading
read_mode: Structured Read
phase: 2026-05 / Transformer prelude
source_url: https://arxiv.org/abs/1409.0473
arxiv: 1409.0473
pdf_url: https://arxiv.org/pdf/1409.0473
local_pdf: Neural_Machine_Translation_by_Jointly_Learning_to_Align_and_Translate.pdf
---

# Neural Machine Translation by Jointly Learning to Align and Translate

## 为什么现在读

- 这是 Transformer 前最关键的 attention 前传之一。
- 它把 attention 引入神经机器翻译，用来缓解 encoder-decoder fixed-length vector 的信息瓶颈。
- 今天读这篇，是为了理解 attention 在成为 Transformer 主干之前，最初解决的是什么问题。

## 今日导读问题

1. fixed-length vector bottleneck 是什么？
2. decoder 为什么需要在每一步动态查看 source sentence？
3. alignment / attention weights 表示什么？
4. context vector 和 encoder hidden states 是什么关系？
5. 这里的 attention 和 Transformer self-attention 有什么相同点、不同点？

## 今日最低产出

- 写清 `decoder state -> score encoder states -> softmax weights -> weighted context -> predict next token` 主链路。
- 写出一句自己的理解：attention 的本质是动态读取相关上下文，而不是把所有信息压进一个固定向量。
- 写出和 Transformer 的连接：Transformer 把 attention 从 RNN decoder 的辅助模块升级为整个模型的主计算机制。

## 阅读记录

| 日期 | 阅读模式 | 进度 | 产出 |
|---|---|---|---|
| 2026-05-24 | Structured Read | planned | 理解 attention 如何从 seq2seq 瓶颈中长出来 |
