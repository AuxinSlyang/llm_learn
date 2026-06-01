# nanogpt-from-scratch：transformer

## 当前定位

这是 `nanogpt-from-scratch` 项目的第二部分，也是后续最应该重点吃透的部分。

如果说 `bigram` 解决的是：

> 先把最小语言模型训练与生成闭环搭出来

那么 `transformer` 解决的是：

> 怎样让模型不只看当前 token，而是能根据上下文序列去预测下一个 token。

---

## 后续重点问题

后续阅读和分析 `transformer` 部分时，优先围绕下面这些问题：

1. token 是怎样先变成 embedding 的？
2. position information 是怎样加进去的？
3. self-attention 为什么能让当前位置看到上下文？
4. causal mask 为什么必要？
5. multi-head attention 相比单头在增强什么？
6. feed-forward 在 block 里承担什么角色？
7. residual + layernorm 为什么几乎是标配？
8. 多个 transformer block 堆叠后，整体能力是怎样提升的？
9. 最后 logits 是怎样回到词表维度上的？
10. `generate` 时，transformer 和 bigram 的根本差异是什么？

---

## 建议的阅读顺序

建议后续按这个顺序吃透：

1. token embedding
2. positional embedding
3. single head self-attention
4. masked self-attention
5. multi-head attention
6. feed-forward
7. residual connection
8. layer norm
9. transformer block
10. 整体 forward
11. generate 路径

---

## 和 bigram 的升级关系

后续一定要明确 `bigram -> transformer` 的升级到底发生在哪里。

可以先带着下面这条比较框架化的对照去看：

### bigram
- 输入：当前 token
- 建模能力：只看当前位置
- 参数直觉：当前 token 对下一 token 的查表式打分
- 优势：简单、最适合建立训练闭环
- 局限：无法真正利用长上下文

### transformer
- 输入：整个上下文序列
- 建模能力：每个位置都可以聚合历史上下文信息
- 参数直觉：通过 attention 动态决定“应该看上下文里的哪些位置”
- 优势：具备更强的上下文建模能力
- 局限：结构与计算复杂度显著上升

所以后续最重要的问题不是“记住模块名”，而是：

> transformer 到底如何把“当前 token 查表预测”升级成“上下文条件建模”。

---

## 2026-05-13：self-attention 阶段性理解

今天先收口单头 `self-attention` 的核心链路。

当前理解：

```text
x = token embedding + positional embedding
Q = query(x)
K = key(x)
V = value(x)
wei = Q @ K.T
wei = causal mask + softmax
out = wei @ V
```

其中：

- `x` 是每个 token 的当前表示，已经包含 token 内容和位置信息。
- `Q / K` 用来算匹配关系：当前 token 想找什么，以及历史 token 能被什么查询匹配上。
- `causal mask` 保证当前位置只能看自己和过去 token，不能偷看未来。
- `softmax` 把匹配分数变成注意力权重。
- `V` 是每个 token 真正提供出去的内容。
- `wei @ V` 表示按注意力权重，把自己和历史 token 的内容聚合回来，形成当前位置的新表示。

一句话收口：

> `Q/K` 决定看谁，`V` 决定拿什么，`wei @ V` 完成按关系取内容。

当前最重要的理解是：

> attention 让每个 token 不再只携带自己的信息，而是能够从自己和历史 token 中，按学习出来的相关性提取上下文信息。

明天继续：

- 轻量通读 Transformer 原论文中 attention 相关部分
- 把论文里的 `Scaled Dot-Product Attention` 和 nanoGPT 代码对应起来
- 理解 `multi-head attention` 相比单头 attention 到底增加了什么

---

## 当前先不展开的点

现在先不急着写细节结论，后续逐段分析时再补：

- attention 的具体张量形状流动
- Q / K / V 的线性投影含义
- mask 的具体实现
- block 内部前向代码路径
- generate 时上下文裁剪与 block_size 的关系

---

## 当前一句话收口

后续 `nanogpt-from-scratch` 真正最值得深挖的，不是 `bigram` 本身，而是：

> `transformer` 如何在同样的 next-token prediction 框架下，把模型从“查表式预测”升级成“上下文建模”。

---

## 2026-05-28：nanoGPT transformer 代码主链路收口

今天把 Karpathy 风格的 `nanoGPT` transformer 实现从训练角度过了一遍，当前先抓主链路，不急着补完整源码。

### 1. 数据与 batch

字符级 tokenizer 做的是：

```text
text <-> char ids
```

`get_batch(split)` 构造的是 next-token prediction 的监督样本：

```text
x = [t1, t2, ..., t256]
y = [t2, t3, ..., t257]
```

所以 `block_size` 可以理解为每次训练的 sequence length / context window。

### 2. GPTLanguageModel.forward

主链路：

```text
idx: (B, T)
-> token_embedding_table(idx): (B, T, n_embd)
-> position_embedding_table(arange(T)): (T, n_embd)
-> x = tok_emb + pos_emb: (B, T, n_embd)
-> blocks(x): (B, T, n_embd)
-> ln_f(x): (B, T, n_embd)
-> lm_head(x): (B, T, vocab_size)
-> cross_entropy(logits.view(B*T, C), targets.view(B*T))
```

这里的 `lm_head` 是语言模型输出头：把每个位置的 hidden state 映射成整个词表的 logits，用于预测下一个字符。

### 3. Attention Head

单头 attention 的代码主线：

```text
k = key(x)
q = query(x)
v = value(x)
wei = q @ k.T / sqrt(head_size)
wei = causal mask
wei = softmax(wei)
out = wei @ v
```

当前理解：

- `Q/K` 决定当前位置应该看哪些历史位置。
- `V` 是历史位置能提供的内容。
- causal mask 用下三角矩阵保证当前位置不能看到未来。
- softmax 不是 `-log`，而是 `exp / sum(exp)` 的归一化；`-log` 出现在 cross entropy 中。
- dropout 会随机置零部分 attention weight / projection 输出，用于正则化。

### 4. Multi-head / FFN / Block

Multi-head 是多个 head 并行读上下文：

```text
6 个 head * 64 维 = 384 维
concat 后 projection 回 n_embd
```

FFN 是逐 token 的非线性变换：

```text
n_embd -> 4 * n_embd -> n_embd
```

Block 是 pre-norm residual：

```text
x = x + self_attention(LayerNorm(x))
x = x + feed_forward(LayerNorm(x))
```

`LayerNorm` 不是作为参数“传入 attention”，而是先把 `x` 归一化，再送进子模块；原始 `x` 通过 residual 直连加回去。

### 5. 为什么主干维度保持 n_embd

每个 block 的输入输出都保持 `(B, T, n_embd)`，核心原因是 residual add 要求 shape 一致。

内部可以临时扩维或拆 head，但子模块输出前必须回到 `n_embd`：

```text
attention: n_embd -> heads/head_size -> n_embd
FFN: n_embd -> 4*n_embd -> n_embd
```

所以 `n_embd` 是主干 hidden state 宽度，`vocab_size` 只在最后 `lm_head` 出现。

### 6. Train / Generate

训练：

```text
get_batch
-> model(x, y)
-> loss
-> optimizer.zero_grad
-> loss.backward
-> optimizer.step
```

生成：

```text
context
-> crop to last block_size
-> forward
-> take last-step logits
-> softmax
-> multinomial sample
-> append token
```

生成阶段不更新参数；它只是在用训练好的 autoregressive LM 反复续写。

### 今日收口

`nanoGPT` 的核心不是模块名，而是这条 shape 稳定的 hidden-state 加工链：

```text
(B,T) token ids
-> (B,T,n_embd) hidden states
-> repeated transformer blocks
-> (B,T,vocab_size) next-token logits
```

下一步如果继续推进，应优先把本地 `code/transformer.py` 从占位骨架补成“边看边注释”的可运行版本，而不是继续扩论文范围。
