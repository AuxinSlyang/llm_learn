# nanogpt-from-scratch：项目结构

## 项目目标

围绕 `nanogpt from scratch` 建一个可持续沉淀的学习项目，而不是把理解散落在 daily note 里。

当前项目拆成两个核心部分：

1. `bigram`
2. `transformer`

这个拆分的含义不是简单按代码文件划分，而是按学习职责划分：

- `bigram`：建立最小训练闭环
- `transformer`：建立上下文建模能力理解

---

## 当前目录

```text
LLM_Learn/03_Projects/nanogpt-from-scratch/
├── README.md
├── notes/
│   ├── bigram.md
│   ├── transformer.md
│   └── project-structure.md
└── code/
    ├── bigram.py
    └── transformer.py
```

---

## 目录职责说明

### `README.md`
项目入口说明：
- 为什么新增这个项目
- 当前学到哪
- 后续重点在哪

### `notes/bigram.md`
记录：
- bigram 本质
- 训练框架
- forward / loss / generate 主线
- 它在整个项目里的定位

### `notes/transformer.md`
记录：
- transformer 后续重点问题
- 阅读拆解顺序
- 它相对 bigram 的核心升级

### `notes/project-structure.md`
记录项目结构本身，防止后续内容继续散掉。

### `code/bigram.py`
放最小 bigram 代码：
- 可以先放跟读版
- 后续再整理成自己的复述版

### `code/transformer.py`
放 transformer 部分代码：
- 可以先保留骨架
- 后续边读边补

---

## 当前学习主线

当前主线不是“把全部代码一股脑跑完”，而是：

1. 先确认 bigram 已经讲清楚什么
2. 再把 transformer 变成后续主要分析对象
3. 每看完一个模块，就往 notes 里落结构化结论
4. 代码与笔记同步推进，不只停在阅读印象

---

## 当前一句话总结

这个项目结构的目标是：

> 用 `project + notes + code` 的方式，把 `nanogpt from scratch` 从一次性阅读，变成可持续复盘和迭代的学习资产。
