---
type: paper_note
title: "3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations"
short_name: 3D Diffusion Policy / DP3
arxiv_id: "2403.03954"
url: https://arxiv.org/abs/2403.03954
pdf_url: https://arxiv.org/pdf/2403.03954
project_page: https://3d-diffusion-policy.github.io/
local_pdf: ./3D_Diffusion_Policy_Generalizable_Visuomotor_Policy_Learning_via_Simple_3D_Representations.pdf
track: robot learning / 3D perception / diffusion policy
read_mode: Later Scan
status: downloaded
created: 2026-06-22
---

# 3D Diffusion Policy - QUICK READ

## Why later

DP3 不是今天主线。它用于后续理解 3D observation 如何接入 diffusion action generation。

## 本轮只回答

- 3D representation 是什么：point cloud / compact 3D representation。
- 它如何作为 condition 输入 diffusion policy？
- 相比 2D image-conditioned Diffusion Policy，它解决什么泛化问题？
- 对 SO-ARM101 是否必要？当前结论：不是首闭环前置。

## 一句话预期 takeaway

3D Diffusion Policy 把 3D 视觉表征作为条件，结合 diffusion policy 生成连续动作序列，以提升跨任务和跨场景泛化。

## 待读后填充

- 3D observation:
- action generation:
- generalization claim:
- robot connection:
