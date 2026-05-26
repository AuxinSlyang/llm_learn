# nanogpt-from-scratch：bigram

## 阶段定位

这是 `nanogpt-from-scratch` 项目的第一部分。

这一部分的重点不是模型能力，而是先建立：

```text
token
-> logits
-> probs
-> loss
-> backward / update
-> generate
```

也就是说，`bigram` 在这个项目中的作用，主要是提供一个 **最小训练与生成闭环**。

---

## 今天已经明确的判断

今天看的 `bigram` 部分，本质上已经比较清楚：

> 它最后其实就是在维护一个“当前字符 -> 下一个字符分布”的二维表。

如果用参数矩阵的视角来说，就是：

- 词表大小为 `V`
- 参数矩阵形状可以理解为 `(V, V)`
- 第一个维度表示“当前字符是谁”
- 第二个维度表示“下一个字符候选是谁”

所以它本质上学的是：

\[
P(next\ token \mid current\ token)
\]

这也是为什么会觉得这个模型本质上接近：

- bigram 条件概率表
- 或者词表级别的 next-token 权重矩阵

---

## 代码主线

当前这版 `bigram` 代码主线可以先收口成下面几层：

### 1. 数据准备
- 读入 `input.txt`
- 提取字符表 `chars`
- 建立 `stoi / itos`
- 把全文编码成整数序列 `data`
- 按 9:1 划分 train / val

### 2. batch 构造
通过 `get_batch(split)`：
- 随机采样多个起点
- 取长度为 `block_size` 的上下文片段 `x`
- 对应目标 `y` 是整体右移一位

这里虽然叫 `bigram`，但训练张量已经是 `(B, T)` 的序列形式；只是模型本身对每个位置仍然只看“当前 token 自己”。

### 3. 模型本体
```python
self.token_embedding_table = nn.Embedding(vocab_size, vocab_size)
```

这一句非常关键。

它表示：
- 输入一个 token id
- 直接查出一个长度为 `vocab_size` 的向量
- 这个向量就表示“下一个字符”的 logits

所以这里的 embedding table，本质上不是在学低维语义 embedding，
而更像是在学：

> 每个当前字符，对所有下一字符候选的一整行打分。

### 4. forward
```python
logits = self.token_embedding_table(idx)  # (B, T, C)
```

输出 `logits` 后：
- 如果给了 `targets`，就展平成 `(B*T, C)`
- 再和 `(B*T)` 的标签做 `cross_entropy`

因此训练路径是：

```text
idx -> logits -> loss
```

### 5. generate
生成路径是：

```text
idx
-> logits
-> 取最后一个 time step
-> softmax
-> multinomial sample
-> 拼回上下文
```

这里要特别记住：

> 训练和生成共享同一个前向模型，只是在 forward 之后分叉成 loss 计算或采样。

### 6. 训练循环
训练循环的结构已经是一个很标准的最小 PyTorch 训练框架：

- 定期 `estimate_loss()`
- 取 batch
- forward
- `optimizer.zero_grad()`
- `loss.backward()`
- `optimizer.step()`

所以从工程形式上说，`bigram` 已经把后续很多模型都会复用的训练框架先搭出来了。

---

## 当前最值得记住的点

### 1. `bigram` 的重点不是表达能力，而是闭环
要吃透的不是“它能不能生成好文本”，而是：

- 数据如何组织
- next-token prediction 如何写成监督学习
- logits / loss / sample 是怎么串起来的

### 2. `nn.Embedding(vocab_size, vocab_size)` 的本质很像二维查表
这一步可以理解为：

> 当前 token id -> 取出对应一行 next-token logits

### 3. 这个阶段真正建立的是训练框架直觉
今天这个阶段最重要的收获之一，就是：

> `bigram` 虽然简单，但它已经把一个语言模型训练程序的主框架搭出来了。

包括：
- 数据切分
- batch 构造
- forward
- loss
- backward
- optimizer step
- generate

---

## 和后续 `transformer` 的关系

这里要明确：

- `bigram` 主要负责建立最小闭环
- 后续真正值得重点吃透的是 `transformer`

也就是说，后续升级不是推翻这个框架，而是：

- 把“只根据当前 token 预测下一个 token”
- 升级成“根据上下文序列建模下一个 token”

因此后续看 `transformer` 时，建议一直带着这个问题：

> 它到底是在 `bigram` 这条最小闭环主线上，替换掉了哪一层、增强了哪一层？

---

## 当前一句话收口

`bigram` 在这个项目里的核心价值不是模型复杂度，而是：

> 它先把字符级语言模型的最小训练框架搭清楚；而后续真正的主战场，会是 `transformer` 如何在这个框架上升级出上下文建模能力。
