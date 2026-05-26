---
type: paper_note
title: Finding Structure in Time
category: 10_AI_Foundations
status: skimmed
read_mode: Quick Architecture Read
phase: 2026-05 / Transformer prelude
source_url: https://web.stanford.edu/class/psych209a/ReadingsByDate/02_20/Elman90.pdf
local_pdf: Finding_Structure_in_Time.pdf
---

# Finding Structure in Time

## 为什么现在读

- 这是理解简单 RNN / Elman network 的经典前置材料。
- 当前只读架构直觉：时间如何通过 recurrent / context units 进入网络。
- 它服务于 Seq2Seq：先理解 RNN 如何处理变长序列，再看 encoder-decoder 如何用 RNN 做翻译。

## 今日导读问题

1. 为什么把时间展开成固定输入维度会有问题？
2. recurrent / context units 给网络带来了什么“记忆”？
3. RNN 的一步计算为什么必须依赖上一步状态？
4. 这种结构为什么天然串行？
5. 它和后续 LSTM / Seq2Seq / Transformer 的关系是什么？

## 最低产出

- 能写出 `x_t + h_{t-1} -> h_t -> y_t` 的主链路。
- 能说明 RNN 相比 MLP 为什么更适合序列。
- 能说明 RNN 的代价：长距离依赖与串行计算。

## 通读 Takeaway

- 这篇论文首先要解决的问题是：神经网络如何表示时间与序列，而不是把所有时间步硬塞进一个固定长度输入向量。
- MLP / 固定窗口方法要求输入维度预先固定，面对变长序列时需要 padding、截断或外部 buffer；RNN 则用内部状态把时间影响留在网络处理过程中。
- RNN 的最小计算链路可以写成 `x_t + h_{t-1} -> h_t -> y_t`。其中 `h_t` 是到当前 token 为止的历史压缩表示。
- RNN 的“记忆”不是完整保存历史，而是用同一组参数逐步处理序列，并把过去通过 hidden state 传到下一步。
- RNN 因此天然支持变长输入：长度为 3 就展开 3 步，长度为 100 就展开 100 步。
- RNN 的代价也来自同一结构：`h_t` 依赖 `h_{t-1}`，所以计算天然串行；长距离信息和梯度都要跨很多时间步传递。

## 和后续论文的连接

- `LSTM`：在 RNN 的基础上增强记忆机制，缓解长距离依赖和梯度衰减。
- `Seq2Seq`：用 RNN / LSTM encoder 读取输入序列，再用 RNN / LSTM decoder 生成输出序列。
- `Attention`：缓解 Seq2Seq 把整句压进最后一个 hidden state 的信息瓶颈。
- `Transformer`：保留序列建模目标，但用 self-attention 替代 recurrent hidden state 主干。

## 阅读记录

| 日期 | 阅读模式 | 进度 | 产出 |
|---|---|---|---|
| 2026-05-24 | Quick Architecture Read | planned | RNN 架构直觉 |
| 2026-05-25 | Quick Architecture Read | skimmed | 形成 RNN 作为“内部状态记忆”的最小 takeaway |
