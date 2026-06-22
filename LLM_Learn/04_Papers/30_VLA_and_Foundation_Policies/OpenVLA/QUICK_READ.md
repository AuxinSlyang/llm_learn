---
type: paper_note
title: "OpenVLA: An Open-Source Vision-Language-Action Model"
short_name: OpenVLA
arxiv_id: "2406.09246"
url: https://arxiv.org/abs/2406.09246
pdf_url: https://arxiv.org/pdf/2406.09246
local_pdf: ./OpenVLA_An_Open_Source_Vision_Language_Action_Model.pdf
track: open VLA
read_mode: Structured Awareness
status: selected_for_2026-06-15
created: 2026-06-09
---

# OpenVLA - QUICK READ

## Position

OpenVLA 是开放 VLA 模型路线的重要入口：pretrained VLM + robot demonstrations -> action generation。

## Read Questions

- VLA input/output contract 是什么？
- action 如何表示？
- fine-tuning 到新任务需要什么数据？
- 推理延迟、显存、量化和端侧部署如何处理？

## This Week

## 2026-06-15 Short-Term Selection

OpenVLA 是短期两篇 VLA 代表材料之一，今晚优先读半篇或一篇。

### 为什么选它

- 它代表 `open-source VLA` 路线：大 VLM + robot demonstration data + action generation。
- 它提供清晰的 open model / fine-tuning / serving / evaluation 入口，适合建立 VLA 工程 contract。
- 它能回答 `camera image + language instruction -> robot action` 这条链路在开放模型中如何组织。

### Tonight Must Answer

- 输入是什么：camera image、language instruction、robot context 如何进入模型？
- 输出是什么：action 如何表示，和 RT-2 的 action-as-token 有什么关系？
- 数据是什么：Open X-Embodiment / robot demonstrations 如何支撑预训练？
- fine-tuning / deployment 做了什么：LoRA/OFT、quantization、serving 的边界在哪里？
- 和 SO-ARM101 / LeRobot 的关系：如果未来只用自己的 record/replay 数据，最先缺什么？

### Boundary

- 不训练。
- 不进源码复现。
- 不追 benchmark 细节。
- 只建立 `VLA input/output contract + data/fine-tune/deploy map`。
