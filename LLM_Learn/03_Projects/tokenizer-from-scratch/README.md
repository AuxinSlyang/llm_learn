---
type: project
status: active
track: LLM foundation / tokenizer / nanoGPT support
linked_project: [[nanogpt-from-scratch]]
---

# Tokenizer From Scratch

## 定位

这是 `nanoGPT` 主链路的 tokenizer 专题维护目录。

目标不是单独开一条新主线，而是把下面这条链路讲清楚：

```text
raw text
-> Unicode / UTF-8 bytes
-> BPE merge
-> token ids
-> batch
-> embedding
-> logits / loss / generate
```

## 最低完成线

- [ ] 能解释为什么直接按字符建模不够。
- [ ] 能解释 UTF-8 bytes 为什么提供可逆底层表示。
- [ ] 能手写一个最小 BPE merge 过程。
- [ ] 能解释 `vocab_size / sequence length / compression` 的 trade-off。
- [ ] 能把 tokenizer 输出接到 `nanoGPT` 的 embedding 输入。

## 维护方式

- 具体代码和实验可以放 `code/`。
- 概念笔记放 `notes/`。
- 和 `nanoGPT` 主链路连接的总结同步回写到：
  - `/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/nanogpt-from-scratch/notes/nanogpt-mainline-summary-v0.md`

## 目录

- `notes/learning-map.md`：学习地图
- `notes/bpe-mainline.md`：BPE 主链路
- `code/`：后续最小实现

