---
type: paper_note
title: "FAST: Efficient Action Tokenization for Vision-Language-Action Models"
short_name: pi0-FAST
arxiv_id: "2501.09747"
url: https://arxiv.org/abs/2501.09747
pdf_url: https://arxiv.org/pdf/2501.09747
project_page: https://www.physicalintelligence.company/research/fast
local_pdf: ./FAST_Efficient_Action_Tokenization_for_Vision_Language_Action_Models.pdf
track: VLA action representation
read_mode: Action Tokenization Scan
status: pdf_downloaded
created: 2026-06-17
---

# pi0-FAST - QUICK READ

## Position

pi0-FAST 是 `pi0` 之后的 action representation 支线：它关注如何把连续机器人动作序列变成更适合 autoregressive VLA 预测的 action tokens。

今天只把它作为 `OpenVLA / pi0 / pi0-FAST` 三件套里的第三个接口视角，不展开 pi0.5，也不进源码。

## Read Questions

- FAST 想解决 pi0 / VLA action output 的什么问题？
- DCT 在 action sequence tokenization 里起什么作用？
- BPE 类 tokenizer 为什么能迁移到连续动作序列？
- 它和 `RT-2 action-as-token`、`OpenVLA action token`、`pi0 flow action expert` 的差别是什么？
- 如果未来接到 SO-ARM101 / LeRobot，最先要对齐哪些字段：`observation.images`、`observation.state`、`task`、`action`、control frequency、latency？

## Today's Output

- 2-3 条 structured takeaway。
- 一句话说明 `continuous action sequence -> action tokens`。
- 一段 `pi0-FAST -> LeRobot / SO-ARM101` 连接说明。

## Boundary

- 不训练。
- 不读源码。
- 不展开 pi0.5。
- 不把 FAST 变成新的 action tokenizer 专题；今天只服务 action representation matrix。
