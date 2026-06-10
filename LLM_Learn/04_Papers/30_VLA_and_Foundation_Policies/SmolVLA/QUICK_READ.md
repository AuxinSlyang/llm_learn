---
type: paper_note
title: "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics"
short_name: SmolVLA
arxiv_id: "2506.01844"
url: https://arxiv.org/abs/2506.01844
pdf_url: https://arxiv.org/pdf/2506.01844
local_pdf: ./SmolVLA_A_Vision_Language_Action_Model_for_Affordable_and_Efficient_Robotics.pdf
track: efficient VLA / LeRobot
read_mode: Project-Relevant Scan
status: downloaded
created: 2026-06-09
---

# SmolVLA - QUICK READ

## Position

SmolVLA 是当前最贴近我们 SO-ARM101 / LeRobot 路线的 VLA awareness：小模型、低成本、LeRobot community data、可在消费级硬件上训练/部署。

## Read Questions

- 它的 observation 包含哪些 camera / state / instruction？
- action expert 如何生成 action chunk？
- asynchronous inference stack 如何把推理和执行解耦？
- 对 SO-ARM101 / Mac / Orin 的现实启发是什么？

## This Week

如果机械臂装起来，SmolVLA 只读数据格式和 runtime 章节；不下载权重，不训练。

