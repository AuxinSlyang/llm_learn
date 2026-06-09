---
type: paper_note
title: A Pragmatic VLA Foundation Model
short_name: LingBot-VLA
arxiv_id: "2601.18692"
url: https://arxiv.org/abs/2601.18692
pdf_url: https://arxiv.org/pdf/2601.18692
local_pdf: ./LingBot_VLA_A_Pragmatic_VLA_Foundation_Model.pdf
project_page: https://technology.robbyant.com/lingbot-vla/
code: https://github.com/Robbyant/lingbot-vla
benchmark_data: https://huggingface.co/datasets/robbyant/lingbot-GM-100
track: VLA engineering stack
read_mode: Project Walkthrough
status: downloaded
created: 2026-06-08
---

# LingBot-VLA - QUICK READ

## Position

LingBot-VLA 不是今晚精读的论文，而是后续 VLA 工程栈入口。它关注的关键词是 pragmatic：真实双臂数据、跨平台泛化、post-training、LeRobot 数据格式、open-loop eval、real-robot deployment 和训练/推理效率。

```text
real robot data
-> LeRobot-style dataset / robot config / norm stats
-> VLA post-training
-> open-loop eval
-> real-robot deployment
```

## Why Now

我们第一阶段买 SO-ARM101 的目的不是立刻训练 4B VLA，而是建立真实机器人数据闭环。LingBot-VLA 的价值在于提前告诉我们后续工程能力要长什么样：

- 数据要能转成标准 robot dataset；
- state/action/image feature mapping 要清楚；
- normalization statistics 是 policy runtime 的一部分；
- eval 要先有 open-loop，再谈 real-robot closed-loop；
- 推理部署不是论文附录，而是工程主线。

## Tonight's Scan Questions

- LingBot-VLA 的输入 observation 包含什么？
- 它如何定义 robot config / feature mapping？
- post-training 最小需要哪些数据准备？
- open-loop eval 和 real-robot deployment 各自验证什么？
- 它和 LeRobot v3.0 的关系是什么？
- 哪些部分未来适合 dev1，哪些部分适合 Orin/Thor？

## Rough Takeaway

LingBot-VLA 对我们最重要的不是“今天能不能跑 4B 模型”，而是它把 VLA 变成了一套工程流程：数据格式、配置、归一化、训练、评估、部署、推理效率。

## Bridge To SO-ARM101

到货后第一阶段要从 LingBot 的视角反推我们的记录方式：

```text
camera placement
motor state
teleop action
task label
episode success/failure
normalization-ready action/state logs
```

这会让首闭环不只是“机械臂动了”，而是为未来 policy/VLA 训练留下可复用数据资产。

## Tomorrow / Later

- 明天只 walkthrough README、dataset format、post-training example、open-loop eval、real-robot deployment。
- 暂时不下载 4B 权重，不启动多卡训练，不把 SO-ARM101 首闭环改成 LingBot 项目。
