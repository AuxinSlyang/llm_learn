# nanogpt-from-scratch：bigram 代码流程拆解

## 当前目标

把 `bigram.py` 的代码流程按“程序结构 + 张量流动 + 训练/生成主线”拆清楚。

这个阶段先不追求把所有数学细节推到极致，而是先把：

- 程序分成哪几块
- 每一块在干什么
- 张量形状怎么变
- 训练和生成分别怎么走

讲顺。

---

## 代码整体可以分成 7 部分

### 1. 超参数区

```python
batch_size = 32
block_size = 8
max_iters = 3000
eval_interval = 300
learning_rate = 1e-2
device = 'cuda' if torch.cuda.is_available() else 'cpu'
eval_iters = 200
```

这一段定义的是整个最小训练程序的控制参数。

可以先按职责理解：

- `batch_size`：一次并行处理多少条序列
- `block_size`：每条序列的上下文长度
- `max_iters`：训练多少步
- `eval_interval`：每隔多少步评估一次
- `learning_rate`：优化器学习率
- `device`：放在 CPU 还是 GPU 上跑
- `eval_iters`：评估 loss 时采样多少个 batch 求平均

这里虽然模型叫 `bigram`，但训练程序已经按“序列批处理”的形式组织了，所以会同时出现 `batch_size` 和 `block_size`。

---

### 2. 数据读入 + 字符表建立

```python
with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

chars = sorted(list(set(text)))
vocab_size = len(chars)
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }
encode = lambda s: [stoi[c] for c in s]
decode = lambda l: ''.join([itos[i] for i in l])
```

这一段在做 4 件事：

1. 读入原始文本
2. 对文本里出现过的字符去重，得到字符表 `chars`
3. 建立字符到整数 id 的映射 `stoi`
4. 建立整数 id 回字符的映射 `itos`

这里最关键的是：

> 神经网络不能直接处理字符，所以要先把字符离散化成 token id。

因此：
- `encode`：字符串 -> 整数序列
- `decode`：整数序列 -> 字符串

你前面的理解是对的：

> 这里先对 data 做 `set` 去重，然后建立 encoder / decoder。

---

### 3. train / val 划分

```python
data = torch.tensor(encode(text), dtype=torch.long)
n = int(0.9 * len(data))
train_data = data[:n]
val_data = data[n:]
```

这一段把整篇文本先编码成一个长的一维 token 序列，然后直接按 9:1 切分：

- 前 90% 当训练集
- 后 10% 当验证集

这里和 `makemore` 里按样本随机拆分不完全一样。

当前这个版本更像：

> 把一整条长文本按时间顺序切一刀。

这是字符级语言模型里很常见的最小做法。

---

### 4. data loading：`get_batch(split)`

```python
def get_batch(split):
    data = train_data if split == 'train' else val_data
    ix = torch.randint(len(data) - block_size, (batch_size,))
    x = torch.stack([data[i:i+block_size] for i in ix])
    y = torch.stack([data[i+1:i+block_size+1] for i in ix])
    x, y = x.to(device), y.to(device)
    return x, y
```

这是训练程序里非常关键的一段。

### 它到底干了什么？

它会：
1. 从 train 或 val 中选数据源
2. 随机采样 `batch_size` 个起点
3. 每个起点截一个长度为 `block_size` 的片段作为 `x`
4. 再取整体右移一位的片段作为 `y`

所以：

- `x.shape = (B, T)`
- `y.shape = (B, T)`

其中：
- `B = batch_size`
- `T = block_size`

### `x` 和 `y` 的关系

如果 `x` 是：

```text
[a, b, c, d]
```

那么 `y` 就是：

```text
[b, c, d, e]
```

也就是：

> 每个位置都在做 next-token prediction。

这一步非常重要，因为它把“语言模型问题”转成了标准监督学习格式。

---

### 5. `estimate_loss()`

```python
@torch.no_grad()
def estimate_loss():
    out = {}
    model.eval()
    for split in ['train', 'val']:
        losses = torch.zeros(eval_iters)
        for k in range(eval_iters):
            X, Y = get_batch(split)
            logits, loss = model(X, Y)
            losses[k] = loss.item()
        out[split] = losses.mean()
    model.train()
    return out
```

这部分的作用是：

> 在不更新梯度的情况下，估计当前模型在 train 和 val 上的平均 loss。

关键点：

- `@torch.no_grad()`：评估时不保留梯度图，节省显存和计算
- `model.eval()`：切到评估模式
- 多采样 `eval_iters` 个 batch 做平均，避免单个 batch 波动太大
- 最后 `model.train()`：再切回训练模式

所以你说：

> 一个 `estimate_loss`，对应的就是没有 grad 的情况下，计算出对应的 losses

这个理解是对的。

---

### 6. `BigramLanguageModel`

这是整个最小模型本体。

#### 6.1 初始化

```python
self.token_embedding_table = nn.Embedding(vocab_size, vocab_size)
```

这一句是整个 bigram 的核心。

它可以理解成一个大小为：

```text
(vocab_size, vocab_size)
```

的参数表。

含义是：

- 行：当前 token 是谁
- 列：下一个 token 的候选是谁

所以它本质上就是：

> 给定当前字符，直接查出一整行“下一个字符 logits”。

这也是你说的“最后就是维护一个二维数组”的更精确表达。

---

#### 6.2 `forward(idx, targets=None)`

```python
logits = self.token_embedding_table(idx)  # (B, T, C)
```

如果：
- `idx.shape = (B, T)`
- 词表大小是 `C`

那么查表后：

- `logits.shape = (B, T, C)`

意思是：

> 对 batch 中每条序列的每个位置，都给出一个对“下一个 token”的词表打分。

这是很关键的张量含义。

---

#### 6.3 为什么要 reshape？

```python
B, T, C = logits.shape
logits = logits.view(B*T, C)
targets = targets.view(B*T)
loss = F.cross_entropy(logits, targets)
```

这里要纠正一个小点：

不是变成 `(32, 1)` 的 cross entropy，
而是：

- `logits` 从 `(B, T, C)` 变成 `(B*T, C)`
- `targets` 从 `(B, T)` 变成 `(B*T)`

例如如果：
- `B = 32`
- `T = 8`
- `C = vocab_size`

那么：
- `logits` 变成 `(256, C)`
- `targets` 变成 `(256,)`

这是因为 `cross_entropy` 期望的输入格式是：

- 预测：`(N, C)`
- 标签：`(N,)`

这里的 `N = B * T`，表示把所有时间步上的预测样本摊平后一起算 loss。

所以本质上是：

> 一个 batch 中所有位置的 next-token prediction，一次性合并起来做分类损失。

---

### 7. 训练循环

```python
optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)

for iter in range(max_iters):
    if iter % eval_interval == 0:
        losses = estimate_loss()
        print(...)

    xb, yb = get_batch('train')
    logits, loss = model(xb, yb)
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    optimizer.step()
```

这是标准的 PyTorch 训练主线：

1. 定期评估
2. 取一个训练 batch
3. forward 得到 `logits, loss`
4. 梯度清零
5. 反向传播
6. 参数更新

这一段最值得记住的是：

> `bigram` 虽然模型极简，但训练程序已经是完整的神经网络训练框架。

也就是说，后面换成更复杂的 `transformer`，训练外壳并不会根本改变，主要变化在模型内部的 forward。

---

## generate 流程

```python
def generate(self, idx, max_new_tokens):
    for _ in range(max_new_tokens):
        logits, loss = self(idx)
        logits = logits[:, -1, :]
        probs = F.softmax(logits, dim=-1)
        idx_next = torch.multinomial(probs, num_samples=1)
        idx = torch.cat((idx, idx_next), dim=1)
    return idx
```

这段的主线是：

1. 输入当前上下文 `idx`
2. forward 得到每个位置的 logits
3. 只取最后一个位置的 logits
4. softmax 变成概率分布
5. multinomial 按分布采样下一个 token
6. 拼接回原序列
7. 继续循环

---

## 你当前关于 generate 的判断

你说得很对：

> 这是一种比较通用的实现；对 bigram 来说其实不需要整个 prefix，只需要前一个字母就够了。

这个判断非常重要。

因为当前 `generate` 写法是为后面更通用的 autoregressive language model 结构服务的：

- 对 `bigram`：只看最后一个 token 就够
- 对 `transformer`：必须看整个上下文（至少看裁剪后的 context window）

所以现在这份 `generate`：

> 对 bigram 来说有点“算多了”，但它保留了后续 GPT 类模型会继续沿用的统一接口。

这也是为什么它是个“common implementation”。

---

## 当前最核心的 5 个结论

### 1. `bigram` 模型本体非常简单
它本质上就是：

> 当前 token -> 查出一行 next-token logits

### 2. 难点不在模型，而在训练程序主线要讲顺
当前更值得吃透的是：
- batch 如何构造
- next-token label 如何对齐
- logits 如何变成 loss
- generate 如何循环展开

### 3. `block_size` 在 bigram 阶段更多是训练张量组织方式
虽然 bigram 每个位置只看自己，但程序仍然按 `(B, T)` 序列批量来处理，
这为后续 transformer 做了接口铺垫。

### 4. reshape 是为了满足 `cross_entropy` 的输入要求
不是随便改形状，而是为了把每个时间步都当成分类样本统一计算损失。

### 5. `generate` 当前是“面向后续通用自回归模型”的写法
对 bigram 有点冗余，但对后续 transformer / GPT 非常自然。

---

## 当前一句话收口

这份 `bigram` 代码最值得学到的，不是模型本身多强，而是：

> 它用一个极简模型，把字符级语言模型从数据编码、batch 构造、forward、loss、训练到 generate 的完整最小程序骨架先搭了出来；而这个骨架，后续会被 transformer 继承下来。
