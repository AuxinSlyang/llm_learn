---
type: study_note
topic: nanoGPT 主链路总结 v0
status: draft
linked_week: [[2026-W23]]
---

# nanoGPT 主链路总结 v0

> 目标：不用资料，讲清 `get_batch -> model(x, y) -> logits/loss -> backward -> optimizer.step`，以及 `generate` 与 training forward 的共用与分叉。

## 1. 训练闭环（Training Loop）

- 数据：`(x, y)` 的 shape 与含义
- `model(x, y)` 返回什么：`logits` / `loss`
- 反向与更新：`loss.backward()` / `optimizer.step()`

## 2. 模型主链路（Forward）

- token -> embedding（token embedding / positional embedding）
- block：attention + MLP + residual + layernorm
- logits：最终 projection 到 vocab
- loss：cross entropy（targets = `y`）

## 3. Generate / Sampling（推理侧）

- prefill vs decode 的直观区别（先不引入 KV cache 细节）
- `generate` 与 training forward 的共用部分
- `generate` 的分叉：采样策略（greedy / multinomial / temperature / top-k）

## 4. 一张图（草图）

- `token -> embedding -> attention -> block -> logits -> loss/generate`
- training / generate 分叉点标注

## 5. CS336 前置补丁清单（随看随补）

- [ ] cross entropy 公式与 PyTorch 实现
- [ ] Adam / weight decay 的直觉
- [ ] attention 里常见 shape（B, T, C）与 mask
- [ ] GPU memory / KV cache 基本量纲

