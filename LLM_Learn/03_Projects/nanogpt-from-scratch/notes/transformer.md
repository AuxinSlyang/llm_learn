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
