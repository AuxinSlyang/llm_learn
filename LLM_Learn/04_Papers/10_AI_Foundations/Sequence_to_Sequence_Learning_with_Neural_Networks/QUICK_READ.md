---
type: paper_note
title: Sequence to Sequence Learning with Neural Networks
category: 10_AI_Foundations
status: reading
read_mode: Structured Read
phase: 2026-05 / Transformer prelude
source_url: https://arxiv.org/abs/1409.3215
arxiv: 1409.3215
pdf_url: https://arxiv.org/pdf/1409.3215
local_pdf: Sequence_to_Sequence_Learning_with_Neural_Networks.pdf
---

# Sequence to Sequence Learning with Neural Networks

## 为什么现在读

- 这是理解 Transformer 前必须补的 seq2seq 前传。
- Transformer 原论文默认读者知道 encoder-decoder sequence transduction 框架。
- 今天读这篇，不是为了复现 LSTM，而是为了理解：RNN encoder-decoder 当时解决了什么，又留下了什么瓶颈。

## 今日导读问题

1. sequence-to-sequence 任务到底是什么？
2. encoder 和 decoder 各自负责什么？
3. fixed-length vector 为什么是潜在瓶颈？
4. RNN / LSTM 在这里为什么天然串行？
5. 这篇论文和后面的 attention / Transformer 是什么关系？

## 今日最低产出

- 写清 `input sequence -> encoder -> context vector -> decoder -> output sequence` 主链路。
- 写出一个问题：为什么把整句输入压成一个向量会限制长句翻译？
- 写出和 Transformer 的连接：Transformer 保留 sequence transduction 目标，但替换掉 RNN 主干。

## 前置理解：RNN / LSTM

- RNN 的作用：用 `x_t + h_{t-1} -> h_t` 的循环结构逐步处理变长序列，让当前状态携带历史信息。它比固定窗口 MLP 更适合序列，但代价是串行计算和长距离依赖困难。
- LSTM 的作用：作为增强版 RNN cell，引入 `c_t` 长期记忆状态和 gates，把“记什么、忘什么、输出什么”显式建模。它缓解普通 RNN 的长距离依赖问题，但仍然是逐步 recurrent 计算。
- Seq2Seq 选择 LSTM 的原因：机器翻译需要把变长 source sentence 编码成内部表示，再用 decoder 逐 token 生成 target sentence；LSTM 比普通 RNN 更适合在较长句子里保存信息。

## 和 Transformer 前传的连接

- `RNN` 解决了 MLP 固定输入维度不适合变长序列的问题。
- `LSTM` 解决了普通 RNN 长距离依赖太弱的问题。
- `Seq2Seq` 把 LSTM 用成 encoder-decoder，实现 `sequence -> sequence`。
- 但原始 Seq2Seq 仍然把整句输入压进最终 hidden/cell state，形成 fixed-length vector bottleneck。
- 下一步 `Bahdanau Attention` 要解决这个瓶颈：decoder 每一步动态读取 encoder states，而不是只依赖一个最终向量。
- 再下一步 `Transformer` 把 attention 从辅助机制升级为主计算机制，替代 RNN / LSTM 的 recurrent 主干。

## 通读 Takeaway：Seq2Seq 的核心思想

- 普通对齐式序列预测更自然处理 `x_t -> y_t`，适合输入输出长度接近、时间步对应明确的任务。
- Seq2Seq 把监督粒度提升到句子 / 序列级别：训练样本只需要 `(source sequence, target sequence)` 成对，不需要 token-level alignment。
- Encoder LSTM 负责把变长 source sequence 编码成固定维度状态；decoder LSTM 是一个 conditioned language model，基于该状态逐 token 生成 target sequence。
- 训练 loss 概念上是 target token 级别 cross entropy 的累加 / 平均；工程上可以一次性计算整段 target 的 logits 和 labels。
- 推理时没有真实 target token，只能使用模型自己上一步输出，并通过 `<EOS>` 决定停止。
- 这篇论文的“窗户纸”是：既然语言模型能逐 token 生成序列，那么给语言模型加上 source sentence 的内部表示作为条件，就能生成与输入相关的目标序列。

## 后续精读入口

- Section 2：读公式 `p(y_1, ..., y_T' | x_1, ..., x_T)` 如何分解。
- Section 2：看清 encoder final state `v` 如何作为 decoder 条件。
- Section 2：区分训练阶段 teacher forcing 和推理阶段自回归生成。
- Section 3 / 4：只抓 dataset、vocabulary、model size、beam search、reverse source trick、long sentence behavior。
- 当前不做复现，不追完整 LSTM 公式和 BLEU 细节。

## 阅读记录

| 日期 | 阅读模式 | 进度 | 产出 |
|---|---|---|---|
| 2026-05-24 | Structured Read | planned | 理解 encoder-decoder seq2seq 作为 Transformer 前传 |
| 2026-05-25 | Structured Read | in_progress | 补入 RNN / LSTM 前置 takeaway，准备继续读 encoder-decoder 主链路 |
| 2026-05-25 | Quick Read | in_progress | 形成 Seq2Seq 作为句子级 paired supervision + conditioned decoder LM 的核心理解 |
