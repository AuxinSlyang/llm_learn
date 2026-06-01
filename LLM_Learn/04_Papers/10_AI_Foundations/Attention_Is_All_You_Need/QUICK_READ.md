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

## 通读算法流程

### 0. 任务视角

原始 Transformer 面向的是 sequence transduction，典型例子是机器翻译：

```text
source: I love cats
target: Ich liebe Katzen
```

它把翻译任务拆成三个能力：

- source sentence 的上下文理解：Encoder Self-Attention
- target language 的自回归生成：Decoder Masked Self-Attention
- target 对 source 的动态读取 / 对齐：Cross-Attention

### 1. Encoder

输入 source tokens：

```text
I love cats
```

先变成向量：

```text
X = token_embedding(source) + positional_encoding
```

每一层 Encoder 做：

```text
Q = XW_Q
K = XW_K
V = XW_V

scores = QK^T / sqrt(d_k)
weights = softmax(scores)
attention_out = weights V

X = LayerNorm(X + MultiHead(attention_out))
X = LayerNorm(X + FFN(X))
```

其中 FFN 是 position-wise 的两层 MLP：

```text
d_model -> d_ff -> activation -> d_model
```

Encoder 最终输出不是一个 fixed vector，而是一组 source hidden states：

```text
H: [source_len, d_model]
```

### 2. Decoder 训练输入

训练时 target 会 shift right：

```text
decoder input: <BOS> Ich liebe Katzen
labels:        Ich   liebe Katzen <EOS>
```

这使得每个位置的 hidden state 用来预测下一个 token。

### 3. Decoder Masked Self-Attention

Decoder 先处理 target prefix：

```text
Y = token_embedding(decoder_input) + positional_encoding
```

然后做 masked self-attention：

```text
Q = YW_Q
K = YW_K
V = YW_V

scores = QK^T / sqrt(d_k)
scores = causal_mask(scores)
weights = softmax(scores)
self_attn_out = weights V

Y = LayerNorm(Y + MultiHead(self_attn_out))
```

causal mask 的作用是让第 `t` 个位置只能看自己和之前的位置，不能看未来 target token。训练时虽然一次性输入完整 target sequence，但 mask 保证每个位置仍然是在做 next-token prediction。

### 4. Cross-Attention

Cross-Attention 连接 Decoder 和 Encoder：

```text
Q = decoder_hidden W_Q
K = encoder_outputs W_K
V = encoder_outputs W_V
```

然后：

```text
scores = QK^T / sqrt(d_k)      # [target_len, source_len]
weights = softmax(scores)
cross_attn_out = weights V

Y = LayerNorm(Y + MultiHead(cross_attn_out))
```

这里不需要 causal mask，因为 source sentence 在推理时本来就是完整已知输入；mask 只用于防止 target 端偷看未来答案。

### 5. Decoder FFN 和输出层

Cross-Attention 之后，每个 target position 经过 FFN：

```text
Y = LayerNorm(Y + FFN(Y))
```

最后映射到词表：

```text
logits = Linear(Y)             # [target_len, vocab_size]
probs = softmax(logits)
```

训练 loss 是每个位置的 cross entropy：

```text
position 0: predict Ich
position 1: predict liebe
position 2: predict Katzen
position 3: predict <EOS>
```

整体 loss 对这些位置求和或平均，然后反向传播。

### 6. 推理过程

推理时没有完整 target answer，只能自回归生成：

```text
<BOS> -> Ich
<BOS> Ich -> liebe
<BOS> Ich liebe -> Katzen
<BOS> Ich liebe Katzen -> <EOS>
```

每一步都可以看完整 source，但只能看已经生成的 target prefix。

### 7. 核心 Takeaway

- Attention 的本质是可微的动态信息路由：`QK^T` 决定从哪里读，`weights V` 决定读出什么。
- Encoder self-attention 负责 source 内部理解。
- Decoder masked self-attention 负责 target 语言自回归生成。
- Cross-attention 负责 target 对 source 的动态对齐和读取。
- Transformer 的关键思想是把序列建模从 RNN 的递推状态，改成 token 之间直接的并行可微信息路由。
- GPT 后续继承的是 decoder-only 的 causal self-attention 路径，去掉了 Encoder 和 Cross-Attention。

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
