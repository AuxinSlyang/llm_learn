# nanogpt-from-scratch：Phase 1 总结（Bigram）

## Phase 1 定位

`nanogpt-from-scratch` 的第一阶段是 `bigram`。

这一阶段的目标，不是追求模型能力，而是先把字符级语言模型最小闭环真正讲清楚。

也就是先建立下面这条主线：

```text
data
-> token ids
-> batch
-> logits
-> loss
-> backward / update
-> generate
```

如果这条线不清楚，后面进入 `transformer` 就容易只剩模块名，而没有主干。

---

## Phase 1 到底解决了什么问题

这一阶段要解决的核心问题是：

> 给定当前 token，怎样预测下一个 token？

在 bigram 的设定里，本质上学的是：

\[
P(next\ token \mid current\ token)
\]

也就是说：
- 当前字符是谁
- 下一个字符在整个词表里的概率分布是什么

所以这个阶段最重要的，不是文本生成质量，而是：

1. 把 next-token prediction 问题形式化
2. 把它写成标准监督学习
3. 看清训练和生成分别怎么走

---

## Phase 1 的代码结构

当前这份最小 bigram 程序，已经可以稳定拆成下面几部分：

1. 超参数
2. 数据读入
3. 字符表建立：`chars / stoi / itos / encode / decode`
4. train / val 切分
5. `get_batch(split)`
6. `estimate_loss()`
7. `BigramLanguageModel`
8. optimizer + 训练循环
9. `generate()`

这个结构本身就很重要，因为后续换成 `transformer` 时，外层程序骨架大体不会变，变的主要是模型内部 forward。

---

## Phase 1 的最核心模型理解

### 1. bigram 本质上是一个二维 next-token 表

`BigramLanguageModel` 里最核心的一句是：

```python
self.token_embedding_table = nn.Embedding(vocab_size, vocab_size)
```

它可以理解成一个大小为 `(V, V)` 的参数表：

- 行：当前 token
- 列：下一个 token 候选

因此它本质上就是：

> 给定当前 token，查出一整行下一个 token 的 logits。

所以 bigram 的模型本体非常简单，本质接近：

- 条件概率表
- 或者词表级别的 next-token 权重矩阵

这就是为什么会感觉它最后像“维护一个二维数组”。

---

### 2. `forward` 输出的是 logits，不是概率

`forward` 中：

```python
logits = self.token_embedding_table(idx)  # (B, T, C)
```

这里：
- `B`：batch size
- `T`：block size
- `C`：vocab size

输出的是 logits，也就是每个位置对整个词表的原始打分，而不是归一化后的概率。

这一点很关键：

> 模型直接输出的是 logits；概率是后续 softmax 后才得到的。

---

### 3. 为什么要 reshape 才能算 cross entropy

当前模型输出：

- `logits.shape = (B, T, C)`
- `targets.shape = (B, T)`

而最常见的 `cross_entropy` 输入形式是：

- `input: (N, C)`
- `target: (N,)`

因此代码里要做：

```python
logits = logits.view(B*T, C)
targets = targets.view(B*T)
loss = F.cross_entropy(logits, targets)
```

这里的本质是：

> 把一个 batch 里所有时间步的 next-token prediction，摊平成 `B*T` 个分类样本统一计算损失。

同时也要明确：

- target 比 input 少一个类别维
- target 里的值必须是合法类别 id，即在 `[0, C-1]` 范围内

---

## Phase 1 的训练框架理解

### 1. 数据如何变成训练样本

`get_batch(split)` 的作用是：

- 随机选 `batch_size` 个起点
- 每个起点截一段长度为 `block_size` 的序列作为 `x`
- 再取整体右移一位的序列作为 `y`

因此：

```text
x = 当前 token 序列
y = 下一个 token 序列
```

例如：

```text
x: [a, b, c, d]
y: [b, c, d, e]
```

这一步把语言模型问题改写成了标准监督学习任务。

---

### 2. 训练循环的最小主线

训练循环的结构是：

```text
get_batch
-> model(xb, yb)
-> loss
-> zero_grad
-> backward
-> optimizer.step
```

这就是一个完整的最小 PyTorch 训练闭环。

因此这一阶段非常重要的一点是：

> bigram 不只是一个简单模型，它已经把语言模型训练程序的基本骨架搭出来了。

---

### 3. `estimate_loss()` 的作用

`estimate_loss()` 在 `torch.no_grad()` 下运行，作用是：

- 不更新参数
- 在 train / val 上各采样多个 batch
- 求平均 loss
- 用于观察当前模型训练状态

它的意义不在模型本体，而在训练过程的监控。

---

## Phase 1 的生成框架理解

`generate()` 的流程是：

```text
当前上下文 idx
-> forward 得到 logits
-> 取最后一个 time step 的 logits
-> softmax 得到 probs
-> multinomial 采样下一个 token
-> 拼回序列
-> 循环
```

这里要建立一个很重要的判断：

> 训练和生成共享同一个前向模型，只是在 forward 之后分叉：
> - 训练走 loss
> - 生成走 sample

---

## 当前一个很好的判断：generate 对 bigram 来说偏通用

当前 `generate()` 是一个比较通用的 autoregressive LM 写法。

对 bigram 来说：
- 真正决定下一个 token 的只需要最后一个 token
- 不需要整个 prefix 的全部信息

但当前实现仍然把整个 `idx` 丢进去，再取最后一个位置的 logits。

这说明：

> 这份代码虽然现在是 bigram，但接口设计已经在为后面的 transformer / GPT 类模型做铺垫。

这个判断非常重要，因为它帮助区分：

- 哪些实现是“bigram 本质要求的”
- 哪些实现是“为了后续通用自回归模型接口保留的”

---

## Phase 1 最值得明确的边界

这一阶段已经足够收口，后面没必要继续在以下问题上过深停留：

- 死磕 bigram 的表达能力
- 在 bigram 上纠结长上下文建模
- 把后续 transformer 才该解决的问题留在 bigram 里硬想

因为 Phase 1 的职责已经完成了：

- 讲清 language model 的最小训练闭环
- 讲清 next-token prediction 的最小实现
- 讲清 logits / loss / sample 的基本关系

后面的重点应该自然切到：

> transformer 到底怎样把“只看当前 token 的查表式预测”，升级成“基于上下文的序列建模”。

---

## Phase 1 最终结论

Phase 1 `bigram` 最核心的收获，可以压缩成下面几条：

1. 语言模型的基本任务是 next-token prediction。
2. bigram 学的是 `P(next token | current token)`。
3. `nn.Embedding(vocab_size, vocab_size)` 本质上像一个二维 next-token logits 表。
4. 模型输出的是 logits，不是概率。
5. `cross_entropy` 需要把 `(B, T, C)` / `(B, T)` 处理成标准分类接口形式。
6. 训练和生成共享同一个 forward，只是在 forward 后分叉。
7. bigram 的最大价值不是模型能力，而是把字符级语言模型的最小程序骨架搭出来。
8. 后续真正的主战场是 transformer，而不是继续深挖 bigram。

---

## 一句话收口

Phase 1 的本质不是“学会一个简单模型”，而是：

> 用 bigram 把字符级语言模型从数据编码、batch 构造、logits、loss、训练到 generate 的完整最小闭环真正讲清楚，并为后续进入 transformer 建立稳定起点。
