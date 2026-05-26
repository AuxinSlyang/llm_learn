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
