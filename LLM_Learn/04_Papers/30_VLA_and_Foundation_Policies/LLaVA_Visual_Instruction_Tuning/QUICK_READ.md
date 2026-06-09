---
type: paper_note
title: Visual Instruction Tuning
short_name: LLaVA
arxiv_id: "2304.08485"
url: https://arxiv.org/abs/2304.08485
pdf_url: https://arxiv.org/pdf/2304.08485
local_pdf: ./LLaVA_Visual_Instruction_Tuning.pdf
project_page: https://llava-vl.github.io/
track: VLM instruction tuning
read_mode: Mini Scan
status: downloaded
created: 2026-06-08
---

# LLaVA - QUICK READ

## Position

LLaVA 是从 VLM 表征走向 VLM assistant 的关键入口：它把 vision encoder、projection layer 和 LLM 接起来，并用 visual instruction tuning 让模型能围绕图片进行问答和对话。

```text
image
-> vision encoder
-> projector
-> LLM
-> assistant-style text response
```

## Why Now

RT-2 和后续 VLA 都会继承类似的思想：不是只做分类或检索，而是让模型在图像、语言指令和输出序列之间形成统一接口。

## Tonight's Scan Questions

- LLaVA 如何构造 visual instruction data？
- vision encoder 和 LLM 中间的 projector 做什么？
- instruction tuning 带来的能力是什么？
- 如果把 text response 换成 action response，会遇到什么新问题？

## Rough Takeaway

LLaVA 的关键是 `visual instruction tuning`：让 VLM 不只是对齐图文，而是能按自然语言指令处理图像上下文并生成回答。

## Bridge To Robotics

机器人系统里，instruction tuning 的对应问题是：

```text
image + robot state + task instruction
-> policy context
-> action sequence
```

LLaVA 还不是机器人 policy，但它提供了 `image + instruction -> sequence output` 的范式。

## Tomorrow / Later

- 读 abstract、intro、architecture、data construction。
- 先不深挖 ScienceQA 和所有 benchmark。
