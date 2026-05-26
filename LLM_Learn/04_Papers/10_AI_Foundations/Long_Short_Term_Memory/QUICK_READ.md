---
type: paper_note
title: Long Short-Term Memory
category: 10_AI_Foundations
status: skimmed
read_mode: Quick Architecture Read
phase: 2026-05 / Transformer prelude
source_url: https://www.bioinf.jku.at/publications/older/2604.pdf
doi: https://doi.org/10.1162/neco.1997.9.8.1735
local_pdf: Long_Short_Term_Memory.pdf
---

# Long Short-Term Memory

## 为什么现在读

- LSTM 是 Seq2Seq 论文使用的核心 RNN 变体。
- 当前只读模型动机和架构直觉，不追完整训练算法与实验细节。
- 它服务于理解：Seq2Seq 为什么选 LSTM，而 Transformer 后来为什么还要替代 recurrent 主干。

## 今日导读问题

1. 普通 RNN 为什么难以学习长距离依赖？
2. vanishing / exploding gradient 在时间展开里是什么问题？
3. LSTM 的 cell state 解决了什么？
4. input / output / forget gate 分别在控制什么？
5. LSTM 为什么仍然保留 RNN 的串行计算瓶颈？

## 最低产出

- 能说明 LSTM 是带门控记忆单元的 RNN。
- 能说明它缓解长距离依赖，但没有解决序列计算串行性。
- 能说明 Seq2Seq 用 LSTM 的原因：更适合把较长输入压成句子表示。

## 通读 Takeaway

- LSTM 不是普通 RNN 的工程实现，而是一种特殊的 RNN cell。它把普通 RNN 中隐含、粗糙的记忆更新拆成了更显式的记忆状态和门控机制。
- 普通 RNN 的 `h_t` 同时承担“历史压缩记忆”和“当前对外输出”两个职责，每一步都会被重新计算，长距离信息容易被覆盖，梯度也容易消失或爆炸。
- LSTM 增加 `c_t` 作为 cell state / 长期记忆向量。`c_t` 和 `h_t` 一样沿序列逐步变化，但它更专门面向记忆保存。
- LSTM cell 的接口可以理解成：`(x_t, h_{t-1}, c_{t-1}) -> (h_t, c_t)`。
- 最关键的记忆更新是：`c_t = f_t * c_{t-1} + i_t * g_t`。其中 `f_t` 控制旧记忆保留多少，`i_t` 控制新候选信息 `g_t` 写入多少。
- 当前输出是：`h_t = o_t * tanh(c_t)`。也就是说，`h_t` 是从内部记忆 `c_t` 中经 output gate 选择性暴露出来的状态。
- 可学习的是计算各个 gate 和候选信息的参数矩阵与偏置；`c_t` / `h_t` 是每条序列 forward 过程里的中间状态，默认不会跨独立训练样本长期保留。
- LSTM 缓解了长距离依赖，但仍然保留 recurrent 结构：下一步依赖上一步的 `h_t` / `c_t`，所以计算仍然天然串行。

## 和后续论文的连接

- `Seq2Seq` 使用 LSTM，是因为 encoder 需要把变长输入读成句子表示，decoder 需要在该表示条件下逐 token 生成输出。
- `Attention` 进一步发现：即使用 LSTM，把完整输入压到最终状态仍然有瓶颈，所以 decoder 应该动态查看 encoder 的所有 hidden states。
- `Transformer` 继续推进：既然 attention 能直接建模依赖，就可以把 recurrent 主干整体替换掉。

## 阅读记录

| 日期 | 阅读模式 | 进度 | 产出 |
|---|---|---|---|
| 2026-05-24 | Quick Architecture Read | planned | LSTM 架构直觉 |
| 2026-05-25 | Quick Architecture Read | skimmed | 形成 LSTM 作为“显式长期记忆 + gates”的最小 takeaway |
