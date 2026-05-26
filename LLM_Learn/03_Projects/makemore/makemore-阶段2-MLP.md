# makemore 阶段二：MLP

## 阶段定位

这是 `makemore` 学习主线里的第二阶段，重点不是再重复 `Bigram`，而是回答下面这几个问题：

1. 为什么 `Bigram` 不够
2. 为什么会出现 `embedding + MLP` 这种神经语言模型
3. `Bengio et al. 2003` 这篇论文到底解决了什么问题
4. `makemore` 里的 `MLP` 结构和论文思想是怎么对应起来的
5. 训练和推理在这个阶段分别是怎么实现的

这一阶段的核心，不是把所有公式都推完，而是把：

> `Bigram -> MLP`

这次模型升级的逻辑讲清楚。

---

## 这一阶段到底在解决什么问题

`Bigram` 的最小闭环已经讲清了：

- 给定前一个 token
- 预测下一个 token 的分布
- 通过训练让正确 token 的概率变高
- 在生成时按概率不断采样下一个 token

但 `Bigram` 有两个根本限制：

1. **上下文太短**：只能看一个 token
2. **泛化能力弱**：更像查表或统计计数，没法很好利用“相似上下文”

因此，`MLP` 阶段要解决的是：

> 能不能看更长的固定窗口上下文，并且不要只靠离散计数，而是通过可训练参数学出泛化能力？

这就是 `Bengio et al. 2003, A Neural Probabilistic Language Model` 的核心出发点。

---

## 这一阶段最重要的结论

### 1. `MLP` 比 `Bigram` 的关键升级，不只是“网络更深”

真正的升级是：

- 从只看一个 token，变成看固定长度上下文
- 从离散计数，变成连续表示 + 参数共享
- 从“查表式条件概率”，变成“学习一个从 context 到 next-token 分布的函数”

所以这一步的本质是：

> `Bigram` 更偏“记忆”，`MLP` 开始有“泛化”。

---

### 2. embedding 是模型参数的一部分，不是固定编码

这一阶段最关键的认知升级之一是：

> embedding 不是预先写死的表示，而是训练中被不断更新的一组参数。

更准确地说：

- token id 本身是离散的，不可导
- embedding table 是一个可训练矩阵
- lookup 的本质是“按 token id 选出 embedding matrix 的某一行”
- 反向传播时，不只是 `MLP` 权重更新，embedding table 也会更新

因此，“token 有了连续表示”的意思不是 token 本身连续了，而是：

> token 被映射到了一个可训练的实数向量空间里。

---

### 3. `hidden layer + 非线性` 的作用，是让模型具备非线性函数拟合能力

这一阶段另一个关键点是理解：

- 只有线性层时，本质上仍然只是线性映射
- 多个线性层叠起来，仍然等价于一个线性层
- 真正让模型表达能力升级的是：`hidden layer + 非线性`

这一步的意义是：

> 模型不再只是做简单线性打分，而开始能学更复杂的上下文模式。

也可以这样理解：

- `hidden layer` 提供中间特征空间
- 非线性让这些中间特征的组合不再退化为单层线性变换

所以 `MLP` 在这里真正学的是：

> 从固定窗口上下文到 next-token 分布的非线性映射。

---

### 4. hidden neuron 可以理解成“模式探测器”

对这一阶段来说，一个很有价值的直觉是：

> 每个 hidden neuron 都像是在问：“当前上下文里有没有我关心的某种模式？”

它做的事情可以理解成：

1. 对输入做加权和，得到某种“匹配分数”
2. 通过非线性得到激活值
3. 激活值越高，表示它越认为某种模式出现了

在名字生成这种任务里，这些模式可能包括：

- 某类字符位置模式
- 某个常见前缀 / 后缀
- 某种局部拼写组合
- 某类相似字符群的出现

因此，整个 hidden layer 输出的向量，可以理解成：

> 当前上下文在一组 learned features 上的激活画像。

---

### 5. `softmax` 是把 logits 变成概率分布的桥

模型最后输出的是 logits，不是概率。

`softmax` 的作用是：

- 把任意实数分数变成 `0~1` 之间的值
- 所有类别概率加起来等于 `1`
- 让输出可以解释成“下一个 token 的概率分布”

在语言模型里，这意味着：

> `softmax(logits)` 给出的就是 `P(next token | context)`。

---

## `Bengio 2003` 的最小理解框架

这篇论文的最小主线可以压成下面这几句：

1. 传统 `n-gram` 语言模型存在严重稀疏性问题
2. 单纯靠离散计数，泛化能力很弱
3. 把词映射成 embedding 后，模型可以在连续空间里共享统计强度
4. 把固定窗口上下文的 embedding 拼接后送进 `MLP`
5. `MLP` 输出整个词表上的 logits，再经 softmax 得到下一个词的分布

因此，这篇论文的核心意义不是“有一个老的神经网络结构”，而是：

> 它标志着语言模型开始从离散统计方法，转向连续表示 + 神经网络建模。

---

## `MLP` 语言模型的真实结构

假设：

- vocab size = `V`
- block size = `n`
- embedding dim = `d`
- hidden dim = `h`

那么模型参数可以写成：

| 参数 | 形状 | 含义 |
|---|---:|---|
| `E` | `(V, d)` | embedding table |
| `W1` | `(n*d, h)` | 从拼接后的上下文到 hidden |
| `b1` | `(h,)` | hidden bias |
| `W2` | `(h, V)` | 从 hidden 到 vocab logits |
| `b2` | `(V,)` | output bias |

前向路径是：

```text
context token ids
-> embedding lookup
-> flatten / concatenate
-> hidden layer + tanh
-> logits over vocab
-> softmax
```

这个结构为什么这么设计，可以压成四点：

1. **embedding**：把离散 token 映射成低维连续向量
2. **concatenate**：保留上下文里的位置信息与顺序
3. **hidden layer + 非线性**：学习复杂上下文模式
4. **output over vocab**：输出 next-token 分类分布

---

## 训练和推理的最小闭环

这一阶段已经比较清楚的一点是：

> 训练和推理使用的是同一个前向网络。

区别只在于前向之后怎么处理结果。

### 训练

训练时：

```text
context
-> embedding
-> MLP
-> logits
-> 与真实 target 计算 cross entropy loss
-> backward
-> 更新 embedding / MLP 权重
```

训练的目标是：

> 让真实下一个 token 的概率变高，让错误 token 的概率变低。

---

### 推理 / 生成

推理时：

```text
context
-> embedding
-> MLP
-> logits
-> softmax
-> 选出 / 采样下一个 token
-> 更新上下文
-> 循环生成
```

推理不再：

- 算 loss
- backward
- 更新参数

它做的事情只是：

> 使用已经学到的条件概率分布，逐步生成序列。

---

## 当前阶段最值得记住的 8 句话

1. `Bigram` 只能看一个 token，本质更接近查表。
2. `MLP` 阶段开始看固定长度上下文。
3. embedding 是可训练参数，不是固定编码。
4. token 的“连续表示”指的是 token 被映射到实数向量空间。
5. `hidden layer + 非线性` 让模型具备非线性函数拟合能力。
6. hidden neuron 可以粗略理解成某种上下文模式探测器。
7. `softmax` 把 logits 变成 next-token 概率分布。
8. 训练是在学习条件分布，推理是在使用条件分布生成序列。

---

## 和 `makemore` 主线的关系

这一阶段在 `makemore` 总体模型演进线中的位置可以写成：

```text
阶段一：Bigram
阶段二：MLP
阶段三：CNN / WaveNet
阶段四：RNN
阶段五：LSTM / GRU
阶段六：Transformer
```

因此，阶段二的任务不是孤立地学一个 `MLP`，而是建立下面这条升级逻辑：

```text
Bigram
-> 看一个 token，泛化弱

MLP
-> 看固定窗口上下文
-> embedding + 参数共享
-> 非线性函数拟合

后续模型
-> 继续解决更长上下文、更强表达能力、更灵活建模的问题
```

---

## 当前阶段已经吃到的内容

基于这次学习，当前阶段已经明确吃到的点包括：

- `Bigram -> MLP` 的升级逻辑
- `Bengio 2003` 的核心问题意识与最小结构
- embedding 是可训练参数这一点
- `hidden layer + 非线性` 为什么必要
- hidden neuron / hidden features 的直觉解释
- `softmax` 在语言模型中的作用
- 训练和推理共用前向，但前向后的处理不同

---

## 代码级最小理解记录：训练 + 推理闭环

下面这部分不再停留在概念层，而是直接对应当前这版 `makemore` 的 `MLP` 初版代码。

### 1. 字表构造：`stoi / itos`

```python
chars = sorted(list(set(''.join(words))))
stoi = {s:i+1 for i,s in enumerate(chars)}
stoi['.'] = 0
itos = {i:s for s,i in stoi.items()}
```

这里做了两件事：

1. 建立字符到整数 id 的映射 `stoi`
2. 建立整数 id 到字符的反向映射 `itos`

其中 `.` 被设为 `0`，它在这份代码里同时承担：

- **起始 padding**：初始 context 里全是 `.`
- **结束符**：生成到 `.` 就停止

因此，`MLP` 阶段的名字生成并不是直接从空开始，而是从 `...` 这样的初始上下文开始。

---

### 2. 数据集构造：核心是 `(context, next_char)`

```python
block_size = 3

def build_dataset(words): 
    X, Y = [], []
    for w in words:
        context = [0] * block_size
        for ch in w + '.':
            ix = stoi[ch]
            X.append(context)
            Y.append(ix)
            context = context[1:] + [ix]
    X = torch.tensor(X)
    Y = torch.tensor(Y)
    return X, Y
```

这段代码的本质是：

> 用长度为 `block_size` 的上下文，预测下一个字符。

如果 `block_size = 3`，那么对任意单词，样本形式就是：

```text
[., ., .] -> ch1
[., ., ch1] -> ch2
[., ch1, ch2] -> ch3
[ch1, ch2, ch3] -> ch4
...
```

如果最后一个字符也处理完，还会再补一个：

```text
[..., last_chars] -> .
```

所以 `X` 存的是长度为 3 的 context，`Y` 存的是“下一个字符”的 id。

这一步非常关键，因为它把语言模型问题转成了一个监督学习问题：

> 输入是上下文，标签是下一个 token。

---

### 3. 数据切分：train / dev / test

```python
random.seed(42)
random.shuffle(words)
n1 = int(0.8*len(words))
n2 = int(0.9*len(words))

Xtr, Ytr = build_dataset(words[:n1])
Xdev, Ydev = build_dataset(words[n1:n2])
Xte, Yte = build_dataset(words[n2:])
```

这里是标准切分：

- `80%` 训练集
- `10%` 开发集
- `10%` 测试集

当前这版代码真正参与训练的是 `Xtr / Ytr`。  
`Xdev / Ydev / Xte / Yte` 已经切出来了，但还没有被用来做完整评估，这也是后续可以补的一步。

---

### 4. 模型参数：这版 MLP 到底长什么样

```python
C = torch.randn((27, 10), generator=g)
W1 = torch.randn((30, 200), generator=g)
b1 = torch.randn(200, generator=g)
W2 = torch.randn((200, 27), generator=g)
b2 = torch.randn(27, generator=g)
```

如果按形状解释：

| 参数 | 形状 | 含义 |
|---|---:|---|
| `C` | `(27, 10)` | embedding table，27 个字符，每个字符 10 维 |
| `W1` | `(30, 200)` | 第一层线性层，把 `3*10=30` 维输入映射到 200 维 hidden |
| `b1` | `(200,)` | hidden bias |
| `W2` | `(200, 27)` | 第二层线性层，把 hidden 映射到 27 个字符 logits |
| `b2` | `(27,)` | output bias |

这里要明确：

- `C` 是可训练的 embedding table，不是固定编码
- `block_size = 3`，所以一个样本有 3 个字符
- 每个字符 embedding 是 10 维，所以拼接后输入维度是 `3 * 10 = 30`

因此这版 MLP 可以概括成：

```text
3 个字符上下文
-> embedding lookup
-> 拼接成 30 维
-> hidden 200 维 + tanh
-> 27 维 logits
```

---

### 5. 前向计算：每个 tensor 的 shape 怎么流动

训练循环里的前向部分是：

```python
ix = torch.randint(0, Xtr.shape[0], (32,))
emb = C[Xtr[ix]]              # (32, 3, 10)
h = torch.tanh(emb.view(-1, 30) @ W1 + b1)  # (32, 200)
logits = h @ W2 + b2          # (32, 27)
loss = F.cross_entropy(logits, Ytr[ix])
```

逐步拆开：

#### `(1) Xtr[ix]`

- `ix.shape = (32,)`
- 从训练集随机采样 32 个样本
- `Xtr[ix].shape = (32, 3)`

表示：

- batch size = 32
- 每个样本由 3 个 token id 组成

#### `(2) emb = C[Xtr[ix]]`

- `C.shape = (27, 10)`
- `Xtr[ix].shape = (32, 3)`
- 所以 `emb.shape = (32, 3, 10)`

这一步不是普通矩阵乘法，而是 **embedding lookup**：

> 对 batch 中每个 token id，到 embedding table 里取对应的一行向量。

#### `(3) emb.view(-1, 30)`

把：

- `(32, 3, 10)`

变成：

- `(32, 30)`

本质就是把 3 个字符的 10 维 embedding 拼接起来，形成一个 30 维输入向量。

#### `(4) hidden`

```python
h = torch.tanh(emb.view(-1, 30) @ W1 + b1)
```

shape 变化：

- `(32, 30) @ (30, 200)` -> `(32, 200)`
- 加上 `b1` 后仍是 `(32, 200)`
- 过 `tanh` 后还是 `(32, 200)`

这里 `tanh` 的意义是：

> 给模型引入非线性，否则多层线性层叠加仍等价于一个线性层。

#### `(5) logits`

```python
logits = h @ W2 + b2
```

shape 变化：

- `(32, 200) @ (200, 27)` -> `(32, 27)`

意思是：

- batch 中每个样本
- 对 27 个字符类别
- 都得到一个未归一化分数

注意这里是 **logits**，不是概率。

---

### 6. `cross_entropy` 到底在算什么

```python
loss = F.cross_entropy(logits, Ytr[ix])
```

这里输入必须是 `logits`，因为模型最后一层给出的还只是原始分数，还没有归一化成概率。

`cross_entropy` 本质上做的是：

1. 对 logits 做 `softmax`，得到概率分布
2. 找到目标类别 `y` 的概率 `p_y`
3. 计算 `-log(p_y)`
4. 对 batch 求平均

也就是：

```text
cross entropy = mean( -log P(target | context) )
```

这里的 `log` 默认是 **自然对数 `ln`**，不是 `log10`。

#### softmax 的数值稳定性

softmax 定义是：

```text
softmax(z_i) = exp(z_i) / sum_j exp(z_j)
```

实现里通常会先减去最大值：

```text
softmax(z_i) = exp(z_i - max(z)) / sum_j exp(z_j - max(z))
```

这样做不是改变数学定义，而是为了避免 `exp` 数值溢出。

#### 为什么要取负对数

- 如果目标类别概率高，loss 就小
- 如果目标类别概率低，loss 就大
- 对非常离谱的错误，惩罚会更重

所以交叉熵的训练目标可以直观理解成：

> 不断提高正确下一个字符的概率。

---

### 7. 反向传播和参数更新

```python
for p in parameters:
    p.grad = None
loss.backward()

lr = 0.1 if i < 100000 else 0.01
for p in parameters:
    p.data += -lr * p.grad
```

这段代码的逻辑是：

1. 先把旧梯度清掉
2. 从 loss 开始 backward
3. 自动计算所有参数的梯度
4. 用最简单的 SGD 更新参数

也就是：

```text
p <- p - lr * grad
```

这里还有一个值得注意的小点：

- 当前训练循环是 `for i in range(20000)`
- 但学习率条件写的是 `i < 100000`

所以这版代码里，实际学习率一直都是 `0.1`，后面的 `0.01` 根本不会触发。  
如果想做前后两段学习率，就应该把阈值改到 20000 以内，比如 `10000`。

---

### 8. 补充：完整训练过程、softmax / cross entropy 与 logits 梯度直觉

如果把这一版 `MLP` 的一次训练 step 再细拆一层，可以写成：

```text
Xb
-> embedding lookup
-> flatten / concatenate
-> linear 1
-> BatchNorm
-> tanh
-> linear 2
-> logits
-> softmax
-> cross entropy loss
-> backward
-> SGD update
```

对应到代码级的张量流动，大致是：

- `Xb: [32, 3]`
- `C: [27, 10]`
- `emb = C[Xb] -> [32, 3, 10]`
- `embcat -> [32, 30]`
- `hprebn = embcat @ W1 + b1 -> [32, 64]`（或在早期版本里是 hidden=200）
- `BatchNorm` 之后仍是 `[32, hidden_dim]`
- `h = tanh(...) -> [32, hidden_dim]`
- `logits = h @ W2 + b2 -> [32, 27]`

这里可以把整个 forward 理解成三段：

1. **输入表示阶段**：token id 先经过 embedding，变成连续向量
2. **特征变换阶段**：拼接、线性层、BatchNorm、tanh 得到 hidden features
3. **分类输出阶段**：hidden features 映射成 vocab 上的 logits，再转成概率并计算 loss

#### softmax 在哪里

下面这段：

```python
logit_maxes = logits.max(1, keepdim=True).values
norm_logits = logits - logit_maxes
counts = norm_logits.exp()
counts_sum = counts.sum(1, keepdims=True)
counts_sum_inv = counts_sum**-1
probs = counts * counts_sum_inv
```

本质就是 **softmax**。

其中：

- `logits - logit_maxes` 是数值稳定处理
- `exp` 把每个类别分数变成正数
- 再除以一行内所有类别的总和
- 最终得到每个样本对 27 个字符的概率分布 `probs`

也就是：

```text
logits -> softmax -> probs
```

#### cross entropy 在哪里

下面这段：

```python
logprobs = probs.log()
loss = -logprobs[range(n), Yb].mean()
```

是在做 **cross entropy loss**（更细说，是 softmax 后接 NLL）。

它的含义是：

1. 先找到真实标签对应的概率
2. 对这个概率取 `log`
3. 加上负号
4. 对 batch 做平均

所以可以写成：

```text
probs + target -> cross entropy -> loss
```

合在一起就是训练里常说的：

```text
logits -> softmax -> probs -> cross entropy -> loss
```

#### 当前阶段对 backward 的最小理解

反向传播本质上没有新模块，它只是把 forward 里每一步倒过来，沿着计算图按链式法则传梯度。

当前阶段最重要的不是把所有局部导数公式死背下来，而是先建立下面几个稳定认知：

1. **梯度的 shape 必须和对应变量的 shape 一致**
2. **广播在 backward 时通常会对应求和**
3. **矩阵乘法 backward 有固定模式**
4. **BatchNorm 的难点在于它依赖 batch 内的 mean / var，因此一个样本的梯度会和其他样本耦合**

#### `dlogits` 的核心直觉

对 `softmax + cross entropy` 来说，最关键的结论是：

```text
dlogits = probs - one_hot(target)
```

如果 loss 对 batch 做了 `mean`，那还要再除以 batch size。

这条式子的直觉很重要：

- **错误类别位置**：梯度等于它当前的 softmax 概率
- **正确类别位置**：梯度等于 `p_correct - 1`

所以在梯度下降更新时：

- 错误类别 logit 会被压低
- 正确类别 logit 会被抬高

也可以换一种更直觉的说法：

> logits 层上的梯度像是在类别之间重新分配分数。  
> 错误类别拿到正梯度，会在更新时被减弱；正确类别拿到负梯度，会在更新时被增强。

这里还有一个很值得记住的性质：

```text
sum(dlogits) = 0
```

原因是：

- `softmax` 输出的概率和等于 1
- `one_hot(target)` 的和也等于 1

所以每个样本上所有类别的 logits 梯度之和恒为 0。  
这说明这不是“整体抬高或整体压低”，而更像是类别之间的相互作用与重新分配。

对正确类别而言，被增强的力度其实不是“等于 softmax 概率本身”，而是：

```text
1 - p_correct
```

所以：

- 如果正确类别概率已经很高，梯度就小，说明模型已经比较确定
- 如果正确类别概率很低，梯度就大，说明这次错得比较厉害，需要更强修正

这也是 `softmax + cross entropy` 很优雅的一点：

> 模型会按自己当前的置信度，自动决定修正强度。

---

### 9. 训练闭环：这版代码每一步在做什么

整个训练循环可以压缩成：

```text
sample batch
-> embedding lookup
-> flatten
-> hidden + tanh
-> logits
-> cross entropy loss
-> backward
-> SGD update
```

它学到的目标是：

> 给定长度为 3 的 context，让正确下一个字符的 logits 更高、概率更大。

这就是最小的字符级语言模型训练闭环。

---

### 9. 推理 / 生成闭环：训练好的模型怎么用来生成名字

推理部分代码：

```python
g = torch.Generator().manual_seed(2147483647 + 10)
for _ in range(20):
    out = []
    context = [0] * block_size
    while True:
        emb = C[torch.tensor([context])]
        h = torch.tanh(emb.view(1, -1) @ W1 + b1)
        logits = h @ W2 + b2
        probs = F.softmax(logits, dim=1)
        ix = torch.multinomial(probs, num_samples=1, generator=g).item()
        context = context[1:] + [ix]
        out.append(ix)
        if ix == 0:
            break
    print(''.join(itos[i] for i in out))
```

推理流程和训练前向是同一个网络，只是后处理不同：

```text
context
-> embedding
-> MLP
-> logits
-> softmax
-> sample next token
-> 更新 context
-> 循环
```

#### 为什么从 `[0, 0, 0]` 开始

因为 `0` 对应 `.`，所以一开始 context 是 `...`。  
模型要从“名字起点”开始预测第一个字符。

#### 为什么用 `multinomial` 而不是 `argmax`

```python
ix = torch.multinomial(probs, num_samples=1, generator=g).item()
```

这是按概率采样，而不是每次都选概率最大的字符。  
这样生成会更多样，也更符合“从模型学到的分布里抽样”的语义。

如果一直 `argmax`，生成会非常死板、容易重复。

#### 为什么遇到 `0` 就结束

因为 `0` 对应结束符 `.`。  
当模型预测到 `.`，就表示这个名字已经生成完成。

---

### 10. embedding 可视化在看什么

```python
plt.scatter(C[:,0].data, C[:,1].data, s=200)
for i in range(C.shape[0]):
    plt.text(C[i,0].item(), C[i,1].item(), itos[i], ...)
```

这里不是在“重新计算 embedding”，而是在：

> 观察训练后的 embedding matrix `C` 在前两个维度上的分布。

每个字符本来是 10 维向量，这里只画前两维。  
它的价值主要是直觉性的：

- 看字符有没有在向量空间里形成某种结构
- 看相似角色的字符是否可能更接近

它不是严格分析，只是辅助观察。

---

### 11. 这版 MLP 相比 `Bigram`，到底升级了什么

如果用一句话概括：

> `Bigram` 更像查表统计，`MLP` 开始真正学习“从上下文到下一个字符分布”的非线性函数。

更具体地说，它新增了三层升级：

1. **更长上下文**：从只看 1 个 token，变成看 3 个 token
2. **连续表示**：字符先进入 embedding 空间，而不是只作为离散 id
3. **非线性组合**：通过 hidden layer + tanh 学更复杂的局部模式

因此，`MLP` 阶段是从离散统计语言模型，迈向神经语言模型的最小台阶。

---

### 12. 这版 MLP 的局限：为什么后面还要去看 CNN / WaveNet

这版模型虽然已经比 `Bigram` 强很多，但它仍有明显局限：

1. **固定窗口**：只能看 `block_size=3` 个字符
2. **参数量会随窗口变大而快速增加**
3. **没有更强的局部结构归纳偏置**
4. **对更长上下文不灵活**

所以后面进入 `CNN / WaveNet` 时，核心问题就变成：

> 能不能比固定窗口 MLP 更高效地扩大感受野，并保留更强的局部模式建模能力？

这也说明：

- `MLP` 是必要的一步
- 但它不是最终可扩展的序列建模结构

---

## 当前还没彻底展开的点

这一阶段已经搭起主线，而且训练 / 推理 / `cross entropy` / tensor shape 已经基本讲顺。  
后续仍值得继续展开的是：

1. `logits -> softmax -> loss` 的梯度直觉
2. 参数量为什么会随着 `block_size` 和 `hidden dim` 快速变大
3. `fixed-window MLP` 和后续 `CNN / RNN / Transformer` 的结构差异
4. 为什么 `MLP` 的上下文建模能力会自然卡在固定窗口上
5. 如何把当前这版代码理解进一步映射到 `Bengio 2003` 的原论文表达

---

## 下一步建议

对阶段二，下一步建议优先做两类沉淀：

### 1. 代码映射版理解

补一份“论文结构 -> `makemore` 代码实现”的映射笔记，重点关注：

- 输入数据集如何构造 `(context, target)`
- embedding lookup 后 tensor shape 如何变化
- flatten / concatenate 在代码里怎么写
- hidden / logits / loss 的形状与意义

### 2. 阶段收口版总结

把阶段二最终收口成一个更短的复述版本，要求自己能不用看资料讲清：

- 为什么 `Bigram` 不够
- `MLP` 的结构长什么样
- embedding / hidden layer / softmax 各自做什么
- 训练和生成分别怎么走
- 这一阶段为什么是后续 `RNN / Transformer` 的前置台阶

---

## 一句话收口

阶段二 `MLP` 最重要的，不是记住一堆层名，而是明确：

> 语言模型从这一阶段开始，真正从离散统计计数，进入了连续表示学习与神经网络建模。
