# WaveNet 论文最小阅读笔记

## 论文信息
- 标题：`WaveNet: A Generative Model for Raw Audio`
- 位置：`LLM_Learn/03_Projects/makemore/paper/1609.03499v2.pdf`

---

## 这篇论文对我当前学习的意义

这篇论文虽然原始任务是 **raw audio generation**，但对我当前的 `makemore` 学习来说，重点不是语音任务本身，而是：

> **它展示了如何从 fixed-window MLP 走向更结构化的卷积式长序列建模。**

我现在读它，主要是从 `NLP / 序列建模` 的角度理解：

- 为什么 `MLP` 不够
- 为什么会出现 `CNN`
- 为什么普通 `CNN` 还不够
- 为什么 `WaveNet` 要引入 `causal convolution` 和 `dilated convolution`

---

## 背景：为什么 `MLP` 不够

`MLP` 已经比 `Bigram` 更强：

- 能看固定长度上下文
- 有 `embedding`
- 有 `hidden layer + nonlinearity`
- 不再只是简单计数

但它仍然有几个问题：

1. **上下文是固定窗口**
   - 想看更长历史，通常只能直接增大 `block size`

2. **输入组织方式比较僵硬**
   - 把上下文 embedding `concat` 成一个长向量，再整体处理

3. **扩展长上下文不自然**
   - 上下文长度一变，输入维度和参数规模也会变

4. **不是层次化建模**
   - 更像“整块看”，不是先抓局部模式再逐层组合

一句话：

> `MLP` 的问题不只是 fixed input，而是 `fixed window + flatten + 整体处理` 这套方式在长序列上比较僵硬。

---

## `CNN` 的核心直觉

`CNN` 也是神经网络，但和 `MLP` 的输入处理方式不同。

### `MLP`
- 把上下文摊平
- 一次性整体处理

### `CNN`
- 保留序列结构
- 先在局部窗口里找模式
- 再通过多层把小模式组合成更大模式

我现在对 `CNN` 的最简理解是：

> **把长上下文化整为零，先学子模式，再逐层组合。**

---

## 感受野（Receptive Field）

目前我的最简理解：

> **感受野 = 当前预测最多能看到多长的历史上下文。**

也可以理解成：

> 某个位置的输出，最终会受到多大范围输入的影响。

`CNN` 层数越多，通常感受野越大。  
因为更高层看到的是低层提取出来的局部特征组合。

---

## 普通 `CNN` 的问题

普通 `CNN` 比 `MLP` 更结构化，但还有一个问题：

> **感受野扩张太慢。**

如果是普通连续卷积：

- 每一层通常只在连续近邻上建模
- 每加一层，感受野只扩大一点点
- 想看到很远历史，就需要很多层

这会导致：

- 网络变深
- 训练更难
- 长序列建模效率不高

一句话：

> 普通 `CNN` 解决了 `MLP` 的僵硬问题，但在长序列上感受野长得太慢。

---

## `WaveNet` 的核心贡献

我当前理解，这篇论文最核心的贡献有两个：

### 1. `causal convolution`
作用：

> **保证预测当前位置时不能偷看未来，只能看历史。**

意义：

- 让卷积网络也能用于 autoregressive generation
- 相当于把卷积改造成符合语言模型因果约束的结构

---

### 2. `dilated convolution`
作用：

> **通过跳步连接更远位置，让感受野更快扩大。**

直觉：

- 普通卷积：紧邻地看，像小步挪
- dilated convolution：隔着步长看，像跳步前进

意义：

- 不是不要近邻
- 而是避免每一层都只在近邻附近慢慢扩张
- 在保留近邻信息的前提下，更快接入远距离历史

一句话：

> `dilation` 的核心不是减少一切重复，而是更高效地扩大感受野。

---

## 从 `MLP -> CNN / WaveNet` 的升级逻辑

### `MLP`
- 固定窗口
- embedding + MLP
- 摊平后整体处理
- 扩长上下文比较僵硬

### `CNN`
- 局部模式提取
- 多层组合
- 比 `MLP` 更结构化

### `WaveNet`
- 保留卷积思路
- 用 `causal convolution` 保证生成合法
- 用 `dilated convolution` 更快扩大感受野
- 更适合长序列自回归建模

---

## 我现在对这篇论文的一句话总结

> **WaveNet 这篇论文的核心，不是单纯提出一个音频模型，而是展示了：在自回归序列建模中，可以用 causal convolution 保证因果约束，用 dilated convolution 更快扩大感受野，从而比 fixed-window MLP 和普通 CNN 更高效地利用长历史上下文。**

---

## 当前已经理解的点
- `MLP` 为什么不够
- `CNN` 为什么是自然升级
- `CNN` 的核心是局部模式 + 多层组合
- 什么是感受野
- 为什么普通 `CNN` 感受野扩张太慢
- `WaveNet` 为什么要用 `causal convolution`
- `WaveNet` 为什么要用 `dilated convolution`

---

## 目前还没彻底展开的点
- `causal convolution` 的更细实现方式
- `dilation=1,2,4,8...` 叠加时为什么效果好
- 论文里 residual / skip connection 的具体作用
- 这套结构如何映射回 `makemore` 的代码实现
- 音频任务细节和 NLP 任务之间的差异边界

---

## 下一步补充方向
1. 回到论文原文，补 `Abstract / Introduction / 方法部分` 的结构化理解
2. 补一份 `WaveNet` 结构图的口语化解释
3. 补 `CNN / WaveNet` 和 `RNN` 的对比
4. 补 `makemore` 中这一阶段的实现映射
5. 最后补一版“我自己的复述稿”