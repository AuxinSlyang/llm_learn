---
type: paper_note
title: Neural Machine Translation by Jointly Learning to Align and Translate
category: 10_AI_Foundations
status: quick_read_done
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

## 背景理解：从 Seq2Seq 到 Attention

- 传统 token-to-token / step-to-step 序列预测的问题是太死板：它更适合 `x_t -> y_t` 这种输入输出时间步基本对齐的任务。
- Seq2Seq 解决了这个旧的不灵活：训练样本只需要 `(source sequence, target sequence)` 成对，不需要 source token 和 target token 一一对齐。
- 但原始 Seq2Seq 又引入了新的不灵活：整个 source sentence 被压成一个 fixed-length vector，decoder 生成每个 target token 时主要依赖同一个压缩表示。
- 翻译虽然不是严格一一对应，但仍然存在局部映射关系，例如 `cats -> chats`、`red car -> voiture rouge`。这些细粒度关系不应该被完全压扁到一个全局向量里。
- Attention 的动机就是：保留 Seq2Seq 处理非一一对应翻译的灵活性，同时让 decoder 在每一步都能动态访问 source 的 token-level / position-level representations。
- 在这篇论文里，attention 可以理解成 soft alignment：生成第 `i` 个 target token 时，模型给 source 每个位置一个权重，再加权读取相关信息。

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

## 通读 Takeaway：Bahdanau Attention 的核心思想

- Seq2Seq 解决了 token-to-token 对齐太死板的问题，但带来了 fixed-length source vector 太粗糙的问题。
- Bahdanau Attention 的核心是：decoder 每生成一个 target token 时，都对 source sequence 的每个位置计算一个关注权重，然后加权读取 source 信息。
- 这里的 attention 更准确地说是 decoder 对 encoder source states 的 soft alignment，不是 decoder 对自己历史 target tokens 的 self-attention。
- 算法主链路是：`decoder state -> score encoder states -> softmax weights -> weighted context vector -> predict target token`。
- `soft alignment` 的含义是：不是硬选某一个 source position，而是给所有 source positions 连续权重；因为 `score -> softmax -> weighted sum -> loss` 都可微，所以可以通过翻译 loss 端到端学习。
- 这篇论文的 attention 仍然依附在 RNN encoder-decoder 上；它没有替代 RNN，只是在 decoder 每一步加入动态读取 source 的机制。
- Transformer 后续的关键变化是：把 attention 从 RNN 旁边的辅助模块升级成主计算机制，并进一步标准化成 Q/K/V 的 self-attention / cross-attention。

## 和 Transformer 的关系

- 相同点：都在做“根据当前状态 / 当前位置，对一组候选表示打分，再加权读取信息”。
- Bahdanau Attention：`query` 直觉上来自 decoder state，`keys/values` 直觉上来自 encoder hidden states，但论文还没有使用 Transformer 里的标准 Q/K/V 表达。
- Transformer Attention：显式构造 `Q/K/V`，用 scaled dot-product attention 作为核心算子，并用它替代 RNN/CNN 主干。

## 阅读记录

| 日期 | 阅读模式 | 进度 | 产出 |
|---|---|---|---|
| 2026-05-24 | Structured Read | planned | 理解 attention 如何从 seq2seq 瓶颈中长出来 |
| 2026-05-26 | Quick Read | done | 形成 Bahdanau Attention 作为 soft alignment / dynamic source reading 的核心理解 |
