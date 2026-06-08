---
type: paper_note
title: "RoFormer: Enhanced Transformer with Rotary Position Embedding"
authors:
  - Jianlin Su
  - Yu Lu
  - Shengfeng Pan
  - Ahmed Murtadha
  - Bo Wen
  - Yunfeng Liu
arxiv: "2104.09864"
source_url: "https://arxiv.org/abs/2104.09864"
pdf_url: "https://arxiv.org/pdf/2104.09864"
local_pdf: "/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/04_Papers/10_AI_Foundations/RoFormer_Enhanced_Transformer_with_Rotary_Position_Embedding/RoFormer.pdf"
published: "2021-04-20"
categories:
  - cs.CL
  - cs.LG
status: quick_read_done
read_mode: Quick Scan
phase: LLM support line -> position encoding / context
linked_project: "[[09_One_Year_Robot_Learning_Full_Stack_Roadmap]]"
---

# RoFormer

## 一句话 Takeaway

- `RoPE` 的核心不是给 token embedding 额外加一个位置向量，而是在 attention 里的 `q/k` 上按位置做旋转；这样 `q_m · k_n` 天然携带 `m-n` 的相对位置信息，并保留绝对位置编码的实现简洁性。

## 为什么现在读

- 这篇用来回答：位置信息到底怎么进 attention，以及为什么 `RoPE` 会变成长上下文和现代 LLM 里非常常见的位置编码方案。
- 今天只读作 `tokenizer / nanoGPT` 收口的支撑材料：token ids 进入 transformer 后，模型除了 token identity，还必须知道 token 在序列中的相对/绝对位置。

## Metadata

- Title: RoFormer: Enhanced Transformer with Rotary Position Embedding
- Authors: Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen, Yunfeng Liu
- Affiliation: Zhuiyi Technology Co., Ltd., Shenzhen（深圳追一科技有限公司）
- Venue / Date: arXiv / submitted 2021-04-20, latest version 2023-11-08
- Source URL: https://arxiv.org/abs/2104.09864
- PDF URL: https://arxiv.org/pdf/2104.09864
- Local PDF: /Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/04_Papers/10_AI_Foundations/RoFormer_Enhanced_Transformer_with_Rotary_Position_Embedding/RoFormer.pdf
- Categories: cs.CL, cs.AI, cs.LG
- Code / Project: Hugging Face RoFormer integration mentioned by paper
- Reading mode: Quick Scan

## Abstract + Introduction 理解

- 问题：Transformer self-attention 本身对顺序不敏感；如果不注入位置信息，模型只知道 token 集合，不知道 token 的前后关系。
- 旧方法为什么不够：
  - 绝对位置编码通常是把 `position embedding` 加到 token embedding 上，实现简单，但相对距离关系不够直接。
  - 相对位置编码会把 `m-n` 注入 attention score，但很多方法通过额外 bias / embedding / expanded terms 实现，不够统一，也不自然兼容 linear attention。
- 核心 insight：把每个位置 `m` 对应成一个旋转角度，对 query/key 做旋转；两个旋转后向量的内积会自然依赖相对位置 `m-n`。
- 贡献：
  - 提出 Rotary Position Embedding（RoPE）。
  - 在 `q/k` 层面注入位置，而不是直接加到 embedding 上。
  - 证明/解释它具有相对位置依赖、序列长度灵活性、远距离衰减等性质。
  - 在机器翻译、预训练、GLUE、Performer 和中文任务上做验证。
- 后续要验证的 claim：RoPE 是否真的比绝对/相对位置编码更适合长文本；这里第一遍只抓直觉，不把实验结论当作今天重点。

## 章节地图

| Section | 作用 | 首轮是否精读 |
|---|---|---|
| Abstract / Intro | 位置编码为什么重要 | 是 |
| Background | 绝对位置编码、相对位置编码的传统做法 | 快速扫 |
| Proposed approach | rotary position embedding 如何作用到 q/k | 是 |
| Properties | long-term decay、linear attention 兼容性 | 扫核心结论 |
| Experiments | MT / MLM / GLUE / Performer / Chinese long text | 选读 |
| Limitations / Conclusion | 作者承认解释仍不完整 | 看限制 |

## 论文写作骨架

这篇论文的写法是标准方法论文：

```text
1. Introduction:
   self-attention 本身 position-agnostic
   旧 position encoding 有局限
   提出 RoPE

2. Background:
   先写标准 self-attention / qkv
   再回顾 absolute position embedding
   再回顾 relative position embedding
   目的：把 RoPE 放在旧方法的坐标系里

3. Proposed approach:
   先提出形式化目标：
     q_m 和 k_n 的内积应该只通过 m-n 表达相对位置
   再用 2D complex / rotation 推出 RoPE
   再推广到 d 维 block diagonal rotation
   再讲性质：long-term decay / linear attention compatibility

4. Experiments:
   用 MT、MLM pretraining、GLUE、Performer、中文长文本任务证明有效

5. Limitations:
   承认还不能充分解释为什么收敛更快、为什么长文本更好

6. Conclusion:
   总结 RoPE 是一种把 absolute position 和 relative dependency 统一进 q/k attention 的位置编码方法
```

首轮读法：

- `Background` 只看它如何设定旧方法的问题。
- `Proposed approach` 精读 `Formulation -> 2D case -> General form`。
- `Properties` 只抓 long-term decay 和 linear attention 的直觉。
- `Experiments` 只抓验证覆盖面，不逐表深挖。

## 8 问

- 任务是什么？改造 Transformer 的位置编码，让 attention 更自然地表达 token 间相对位置。
- observation 是什么？对 LLM 来说是 token ids 对应的 token embeddings；进入 attention 后是每层的 hidden states。
- action 是什么？不适用；类比到模型内部，是每个 token 的 contextual representation / logits。
- 数据怎么采？论文用通用 NLP 数据集和任务验证，不是数据采集论文。
- policy / model 输出什么？RoFormer 仍是 Transformer/RoFormer 输出 hidden states 或任务 logits；RoPE 只改变 attention 内部的位置注入方式。
- eval 怎么做？机器翻译 BLEU、MLM loss、GLUE、Performer loss、中文长文本任务效果。
- failure mode 是什么？作者承认还没有充分解释为什么 RoPE 收敛更快、为什么长文本效果更好。
- 如果我要产品化，需要什么 software / data / runtime 支撑？需要在 attention kernel / model implementation 中正确生成 sin/cos cache，并在 q/k 上 apply rotary；长上下文扩展时还要处理位置索引、cache 长度和推理显存。

## 方法结构

### 1. 普通 self-attention 为什么缺位置

标准 attention 的核心项是：

```text
score(m, n) = q_m^T k_n
```

如果 `q_m` 和 `k_n` 只来自 token embedding / hidden state，而没有位置注入，那么交换 token 顺序不会被 attention 本身自然区分。

### Background: 论文如何铺垫旧方法

这一节的目的不是重新教 Transformer，而是把所有位置编码方法统一写成：

```text
q_m = f_q(x_m, m)
k_n = f_k(x_n, n)
v_n = f_v(x_n, n)
```

这里：

```text
x_m: 第 m 个 token 的词向量，不含位置
m: 第 m 个位置
f_q/f_k/f_v: 把 token 内容和位置合成 q/k/v 的函数
```

attention 仍然是：

```text
a_mn = softmax(q_m^T k_n / sqrt(d))
o_m = sum_n a_mn v_n
```

所以作者真正关心的是：`f_q/f_k/f_v` 应该怎么设计，才能让位置关系自然进入 `q_m^T k_n`。

### 2. 传统绝对位置编码

常见做法：

```text
x_m = token_embedding_m + position_embedding_m
q_m = W_q x_m
k_m = W_k x_m
```

问题是：位置通过加法混进 token representation，模型要自己学出相对距离关系。

论文里的统一写法是：

```text
f_t(x_i, i) = W_t (x_i + p_i), t in {q,k,v}
```

这说明 absolute PE 的关键是：

```text
先把 token 内容 x_i 和位置 p_i 相加
再投影成 q/k/v
```

这里的 `p_i` 可以是：

- learned positional embedding：一张可训练的位置表。
- sinusoidal positional encoding：用 sin/cos 固定公式生成。

作者给 sinusoidal PE 留了一个伏笔：RoPE 也会用 sin/cos，但不是把 sin/cos 向量加到 `x_i` 上，而是用 sin/cos 对 `q/k` 做旋转。

### 2.5 传统相对位置编码

relative PE 的目标更接近 RoPE：让 attention score 知道 `m-n`。

一种常见形式是：

```text
score(m,n) = q_m^T k_n + bias(m,n)
```

或者更细地把 absolute PE 展开：

```text
(x_m + p_m)^T W_q^T W_k (x_n + p_n)
```

展开后会有四项：

```text
content-content:   x_m^T W_q^T W_k x_n
content-position:  x_m^T W_q^T W_k p_n
position-content:  p_m^T W_q^T W_k x_n
position-position: p_m^T W_q^T W_k p_n
```

Transformer-XL、T5、DeBERTa 等方法都可以理解为：在这些项上做替换、裁剪、加 bias，或把 `p_m/p_n` 换成相对位置 `p_(m-n)`。

作者想表达的批评是：

```text
旧 relative PE 多数是在 additive PE 的展开式上改补丁
RoPE 想从 q/k 的构造函数 f_q/f_k 本身推导出相对位置
```

### 3. RoPE 的核心做法

RoPE 不把位置向量加到 `x` 上，而是对 `q/k` 做旋转：

```text
q_m = R_m W_q x_m
k_n = R_n W_k x_n
score(m, n) = q_m^T k_n
```

其中 `R_m` 是由位置 `m` 决定的旋转矩阵。

关键直觉：

```text
(R_m q)^T (R_n k)
```

因为旋转矩阵的性质，最后的 attention score 会自然依赖 `m-n`，也就是 query token 和 key token 的相对距离。

### 4. 二维直觉

把向量每两个维度看成一个 2D 平面：

```text
[a, b] -> rotate by m * theta
```

位置越靠后，旋转角度越大。query 在位置 `m` 旋转 `mθ`，key 在位置 `n` 旋转 `nθ`；它们相乘时只剩下相对角度 `(m-n)θ` 的影响。

### 5. 高维实现

高维向量会被拆成多组二维子空间，每组用不同频率：

```text
theta_i = 10000^(-2i / d)
```

这和原始 sinusoidal position encoding 的频率设计相近，但 RoPE 是把 sin/cos 用在 `q/k` 的旋转上。

#### 3.2.2 General form 细读

论文从 `d=2` 推广到任意偶数维 `d` 的关键是：

```text
d 维空间 = d/2 个二维子空间的拼接
高维内积 = 每个二维子空间内积的求和
```

因此只要每个二维子空间都满足：

```text
(R(mθ_i) q_i)^T (R(nθ_i) k_i)
= q_i^T R((n-m)θ_i) k_i
```

那么所有二维块加起来后，整体也满足：

```text
(R_m^d q)^T (R_n^d k)
= q^T R_{n-m}^d k
```

高维旋转矩阵 `R^d_{Θ,m}` 是 block diagonal matrix：

```text
R^d_{Θ,m} =
diag(
  R(mθ_1),
  R(mθ_2),
  ...,
  R(mθ_{d/2})
)
```

每个二维 block 都是：

```text
R(mθ_i) =
[ cos(mθ_i)  -sin(mθ_i) ]
[ sin(mθ_i)   cos(mθ_i) ]
```

不同 `θ_i` 的作用是提供多尺度位置频率：

```text
θ 大：短距离变化更敏感
θ 小：长距离变化更稳定
```

所以 3.2.2 的核心表达是：

> 高维 RoPE 不是重新发明一个复杂矩阵，而是把二维旋转在多个频率子空间上并行应用；由于内积可以按维度块相加，每个块的相对位置性质会保留到整体。

#### Figure 1 在说明什么

Figure 1 的本质是 RoPE 实现图：

```text
输入 Query/Key
-> 按维度两两分组
-> 每组匹配一个 θ_i
-> 按 position m 生成 mθ_i
-> 对每个二维块做旋转
-> 得到 position encoded Query/Key
```

上半部分展示 `d=2` 的单个二维旋转；下半部分展示高维时多个二维块并排做同样操作。它想说明实际实现并不需要真的构造一个巨大的 `d x d` 稀疏旋转矩阵，而是用 `cos/sin` 对 q/k 的成对维度做向量化旋转。

### 6. 和 nanoGPT 的连接

nanoGPT 里今天需要区分三件事：

```text
token ids -> token embedding
position index -> position information
attention(q, k, v) -> contextual mixing
```

如果是 learned absolute position embedding，通常会看到：

```text
x = token_embedding + position_embedding
```

如果是 RoPE，位置不会先加到 `x` 上，而是在 attention 计算前 apply 到 `q/k`：

```text
q, k = apply_rotary(q, k, position_ids)
```

这就是为什么 RoPE 更像 attention 内部机制，而不是 tokenizer 或 embedding 层本身的机制。

## 实验与证据

- Baselines: Transformer/BERT/WoBERT/NEZHA/Performer variants 等。
- Metrics: BLEU、MLM loss、GLUE 指标、分类任务指标、loss curve。
- Main results:
  - 作者在多个 NLP 任务中报告 RoFormer/RoPE 优于或接近 baseline。
  - 中文长文本任务中，增大最大输入长度后 RoFormer 相对 WoBERT/BERT 更有优势。
  - Performer 加入 RoPE 后 loss curve 更好，说明 RoPE 可用于 linear attention 场景。
- Ablations: 第一遍不细看。
- Failure / limitations:
  - 作者承认没有充分解释为什么 RoPE 比其他位置策略收敛更快。
  - 对长文本表现更好的理论解释也不完全充分。

## 系统 / 工程启发

- 位置编码不只是“给 token 加个 index”，它会直接影响 attention 如何表达相对位置信息，以及后续 context extension 能不能自然做下去。
- 从工程实现看，RoPE 会影响：
  - attention kernel 前的 q/k transformation；
  - sin/cos cache 生成和长度；
  - KV cache 在推理时如何保持 position id 连续；
  - 长上下文扩展时的位置缩放、插值或 extrapolation 策略。

## 和 Robot Learning / Runtime 的连接

- 对当前路线的价值主要在 runtime 支撑线：理解上下文长度、position encoding 和长上下文外推的工程边界。
- 对 VLA / robot runtime 的间接价值：如果未来 robot policy 使用 VLM/VLA backbone，prompt、视觉 token、action token、history token 都依赖上下文组织；位置编码决定模型如何理解这些 token 的顺序和相对距离。

## 可以转成的实验 Idea

- 把 `RoPE / ALiBi / Position Interpolation` 串成一条 context 线，专门回答“原始位置编码、外推、扩窗”三步。
- 在 nanoGPT 小模型中对比：
  - learned absolute position embedding
  - sinusoidal position encoding
  - RoPE
  - ALiBi
  只看实现差异和 train length / test length 的直觉，不追求大实验。

## 疑问

- RoPE 的 long-term decay 是理论性质，但现代 LLM 长上下文扩展还需要 NTK scaling / position interpolation / YaRN 等工程策略；这篇不是最终答案。
- 为什么 RoPE 在很多现代模型中成为主流，需要结合后续 LLaMA / Qwen / long-context engineering 再看。

## 阅读记录

| 日期 | 阅读模式 | 进度 | 产出 |
|---|---|---|---|
| 2026-06-05 ~ 2026-06-07 | Quick Scan | done | RoPE 核心直觉、二维/高维推导、Figure 1、properties 和 nanoGPT/context 连接 |
