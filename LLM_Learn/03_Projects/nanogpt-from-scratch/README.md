# nanogpt-from-scratch

## 项目定位

这是 2026-05 新增的一个项目化学习对象，用来承接：

- `Zero to Hero`
- `nanoGPT from scratch`
- 从 `bigram` 走向 `transformer`
- 从最小语言模型训练闭环走向更完整的 GPT 结构理解

这个项目当前不追求“大而全复现”，而是围绕 **最小可讲清主线** 来组织：

1. `bigram`
2. `transformer`

也就是先把最简单的字符级 next-token prediction 讲清，再进入 `nanoGPT` 中真正值得吃透的 `transformer` 部分。

---

## 当前阶段拆分

### Part 1: Bigram

目标：
- 讲清最小语言模型训练闭环
- 讲清 `token -> logits -> probs -> loss / generate`
- 理解它本质上是在学习一个“当前字符 -> 下一个字符分布”的映射

当前状态：
- 已新增 `notes/bigram.md`
- 已新增 `notes/bigram-code-flow.md`
- 已新增 `notes/phase1-summary.md`
- 已记录今天对 bigram 训练框架、代码流程和模型本质的第一轮总结

### Part 2: Transformer

目标：
- 进入 `nanoGPT from scratch` 真正的核心
- 理解 embedding / positional encoding / self-attention / multi-head / feed-forward / residual / layernorm
- 理解 `block_size` 为什么重要
- 理解从 `bigram` 到 `transformer` 的升级到底升级了什么

当前状态：
- 已新增 `notes/transformer.md` 作为后续主战场
- 目前仍是待补充状态

---

## 建议目录结构

```text
nanogpt-from-scratch/
├── README.md
├── notes/
│   ├── bigram.md
│   ├── bigram-code-flow.md
│   ├── phase1-summary.md
│   ├── transformer.md
│   └── project-structure.md
└── code/
    ├── bigram.py
    └── transformer.py
```

说明：
- `notes/` 放结构化学习记录
- `code/` 放最小实现或跟读版代码
- 当前先把项目骨架搭起来，后续再逐步补全实现与笔记

---

## 当前最重要的学习顺序

1. 先收口 `bigram`
2. 再逐段吃透 `transformer`
3. 最后再回到“为什么这叫 nanoGPT from scratch”

这里最关键的判断是：

> `bigram` 主要建立训练闭环直觉；`transformer` 才是这个项目后续最值得重点吃透的主体。

---

## 后续推荐沉淀物

建议这个项目后续优先沉淀下面几类内容：

1. `bigram` 最小训练闭环说明
2. `transformer` 代码结构拆解
3. `from bigram to transformer` 升级逻辑说明
4. `nanoGPT from scratch` 主线总结
5. 如果后续推进顺利，再补：
   - `generate` 路径说明
   - `loss` 计算路径说明
   - `block_size / context window` 解释

---

## 当前一句话总结

这个项目的目标不是机械抄代码，而是：

> 通过 `bigram -> transformer` 这条路径，把 `nanoGPT from scratch` 的最小语言模型主线真正讲清楚。

---

## 2026-05-28 项目核心总结

今天把 `GPT-1/2/3` 的演化和 `nanoGPT from scratch` 代码主线对齐后，当前项目可以收口成一句话：

> `nanoGPT from scratch` 是 GPT pretraining 主链路的最小可运行版本：`text -> token ids -> batch x/y -> embedding -> decoder-only transformer blocks -> lm_head -> next-token loss -> AdamW -> generate`。

### 1. 这个项目到底在学什么

不是在学“一个玩具字符模型”，而是在学 GPT 系列最核心的训练范式：

```text
给前文 tokens
-> 预测下一个 token 的概率分布
-> 用 cross entropy 逼近真实下一个 token
-> 通过反向传播更新 embedding / transformer blocks / lm_head
```

字符级 tokenizer、Tiny Shakespeare、小模型参数只是教学降维；主链路和 GPT-1/2/3 的 autoregressive LM 是同构的。

### 2. bigram 到 transformer 升级了什么

`bigram` 阶段建立的是最小训练闭环：

```text
current token -> lookup logits -> next-token loss -> generate
```

`transformer` 阶段升级的是上下文建模能力：

```text
token + position
-> masked self-attention 聚合历史上下文
-> FFN 做逐位置非线性变换
-> residual + layernorm 稳定深层堆叠
-> 多层 block 反复加工 hidden state
```

核心差异不是 loss 变了，而是 hidden state 从“当前 token 查表”变成了“上下文条件表示”。

### 3. 当前已经讲清的代码主链路

- `batch_size`：一次并行训练多少段独立序列。
- `block_size`：每个位置最多能利用的上下文窗口，也是 position embedding / causal mask 的最大长度。
- `n_embd`：主干 hidden state 宽度；block 与 block 之间传递的 shape 固定为 `(B, T, n_embd)`。
- `n_head`：把 `n_embd` 拆成多个 attention head 并行读上下文，最后 concat + projection 回 `n_embd`。
- `n_layer`：重复堆叠多少个 transformer block。
- `get_batch`：构造 `x` 和右移一位的 `y`，把语言模型训练变成监督学习。
- `Head`：`Q/K` 决定看谁，`V` 决定拿什么，`wei @ V` 完成上下文聚合。
- `Block`：采用 pre-norm residual 形式 `x + module(LN(x))`，保持 shape 不变并稳定训练。
- `lm_head`：把最后 hidden state 从 `n_embd` 映射到 `vocab_size`，得到每个位置的 next-token logits。
- `generate`：不更新参数，只反复取最后位置 logits，softmax 后采样下一个 token 并拼回上下文。

### 4. 当前最重要的理解

Transformer block 内部可以临时改变维度，例如：

```text
FFN: n_embd -> 4 * n_embd -> n_embd
attention: n_embd -> heads * head_size -> n_embd
```

但每个 block 的入口和出口通常必须保持 `n_embd`，因为 residual add 要求 shape 一致：

```text
x = x + self_attention(LayerNorm(x))
x = x + feed_forward(LayerNorm(x))
```

所以 `n_embd` 是主干表示宽度，`lm_head` 才是把这个主干表示翻译回词表输出空间的出口。

### 5. 和 GPT-1/2/3 的连接

- GPT-1：`nanoGPT` 对应它的 pretraining 主链路；GPT-1 额外讨论 task head / supervised fine-tuning。
- GPT-2：`generate` 路径对应 zero-shot task framing 的底层机制，本质仍然是续写。
- GPT-3：in-context learning 仍然建立在同一个 autoregressive LM 机制上，只是 prompt 中包含任务说明和示例。

当前阶段先不追更多论文，下一步优先把本项目的 transformer code path 真正写清楚。
