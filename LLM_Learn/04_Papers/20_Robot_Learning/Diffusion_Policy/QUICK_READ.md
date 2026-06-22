---
type: paper_note
title: Diffusion Policy: Visuomotor Policy Learning via Action Diffusion
short_name: Diffusion Policy
authors:
  - Cheng Chi
  - Zhenjia Xu
  - Siyuan Feng
  - Eric Cousineau
  - Yilun Du
  - Benjamin Burchfiel
  - Russ Tedrake
  - Shuran Song
arxiv_id: "2303.04137"
url: https://arxiv.org/abs/2303.04137
project_page: https://diffusion-policy.cs.columbia.edu/
local_pdf: ./Diffusion_Policy_Visuomotor_Policy_Learning_via_Action_Diffusion.pdf
track: robot learning / imitation learning / diffusion action generation
read_mode: Structured Read
status: downloaded
created: 2026-06-22
---

# Diffusion Policy - QUICK READ

## Why now

Diffusion Policy 是把 diffusion 从 image generation 迁移到 robot action sequence generation 的核心论文，用来解释 pi0 为什么要关注 continuous action generation。

## 本轮只回答

- policy 生成的对象是什么：single action 还是 future action sequence？
- condition 是什么：image / state / observation history？
- conditional denoising 具体如何变成 robot policy？
- receding horizon control 怎么避免一次性执行整段动作？
- 为什么 diffusion 能处理 multimodal action distribution？

## 一句话预期 takeaway

Diffusion Policy 把 visuomotor policy 表示成条件去噪过程：给定 observation，把 noisy future action sequence 逐步去噪成可执行的 action sequence。

## 和 pi0 的连接

```text
Diffusion Policy:
  observation + noisy action sequence
  -> denoising
  -> clean action sequence

pi0:
  image + language + state + noisy action chunk
  -> flow/action expert
  -> continuous action chunk
```

## 待读后填充

- observation:
- action representation:
- denoising target:
- receding horizon:
- multimodal action distribution:
- SO-ARM101 / LeRobot connection:
