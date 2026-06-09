---
type: paper_note
title: "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control"
short_name: RT-2
arxiv_id: "2307.15818"
url: https://arxiv.org/abs/2307.15818
pdf_url: https://arxiv.org/pdf/2307.15818
local_pdf: ./RT_2_Vision_Language_Action_Models_Transfer_Web_Knowledge_to_Robotic_Control.pdf
project_page: https://robotics-transformer.github.io/
track: VLA foundation
read_mode: Structured Read
status: downloaded
created: 2026-06-08
---

# RT-2 - QUICK READ

## Position

RT-2 是今天这组论文里第一个真正进入 `VLM -> VLA` 的材料。它的题眼是：把 robot actions 表示成模型可以预测的 token/sequence，让同一个模型同时学习 web-scale VLM 任务和机器人轨迹数据。

```text
image + instruction
-> VLM backbone
-> action-as-token output
-> robot control
```

## Why Now

我们买了 SO-ARM101 后，第一阶段不直接训练 RT-2 级别模型，但必须理解：

- action 如何被表示成可学习目标；
- web-scale VLM knowledge 如何迁移到 robot control；
- 高层语义推理和低层动作控制怎么接上；
- VLA 不是“会聊天的模型”，而是 observation-to-action policy。

## Tonight's Scan Questions

- 什么是 Vision-Language-Action model？
- RT-2 如何把自然语言 response 和 robot action 放到同一个输出格式？
- action tokenization 是简单工程 trick，还是 VLA 成立的关键抽象？
- 为什么 web data 能帮助机器人泛化到新物体、新语义、新任务？
- RT-2 的闭环延迟、控制频率和 action granularity 有什么限制？

## Rough Takeaway

RT-2 的关键跃迁是把 action 也纳入“模型输出序列”。这让 VLM 不只是看图说话，而是可以把视觉、语言和机器人轨迹一起训练，输出能执行的动作。

## Bridge To SO-ARM101

SO-ARM101 当前首闭环先做：

```text
observation.images
+ observation.state
+ task
-> simple policy / teleop / ACT baseline
-> action
-> eval / failure log
```

RT-2 明天要帮助我们回答：如果未来把 simple policy 换成 VLA，LeRobot dataset 里的 observation/action schema 应该怎样被理解。

## Tomorrow / Later

- 明天主读 abstract、intro、method/action representation、eval setup。
- 暂时不深挖所有实验表；先抓 `action-as-token` 和 `co-fine-tuning`。
