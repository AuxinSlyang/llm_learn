---
type: paper_note
title: "FAST: Efficient Action Tokenization for Vision-Language-Action Models"
short_name: pi0-FAST
arxiv_id: "2501.09747"
url: https://arxiv.org/abs/2501.09747
pdf_url: https://arxiv.org/pdf/2501.09747
project_page: https://www.physicalintelligence.company/research/fast
local_pdf: ./FAST_Efficient_Action_Tokenization_for_Vision_Language_Action_Models.pdf
authors: Karl Pertsch; Kyle Stachowicz; Brian Ichter; Danny Driess; Suraj Nair; Quan Vuong; Oier Mees; Chelsea Finn; Sergey Levine
submitted: 2025-01-16
subjects: Robotics (cs.RO); Machine Learning (cs.LG)
track: VLA action representation
read_mode: Structured Read
status: active_2026-06-24
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

## Official arXiv Metadata

- arXiv ID：`2501.09747`
- Title：`FAST: Efficient Action Tokenization for Vision-Language-Action Models`
- Authors：Karl Pertsch, Kyle Stachowicz, Brian Ichter, Danny Driess, Suraj Nair, Quan Vuong, Oier Mees, Chelsea Finn, Sergey Levine
- Submitted：`2025-01-16`
- Subjects：`Robotics (cs.RO); Machine Learning (cs.LG)`
- Source：`https://arxiv.org/abs/2501.09747`
- PDF：`https://arxiv.org/pdf/2501.09747`
- Abstract summary：论文指出 autoregressive VLA 需要把连续机器人动作离散化；常见逐维逐时刻 binning 在高频灵巧数据上效果差。FAST 用 DCT 视角压缩动作序列，并释放 FAST+ 作为通用 action tokenizer，目标是在保持 autoregressive VLA 训练方式的同时更好处理高频连续动作。

## 2026-06-23 Quick Scan

### 一句话 takeaway

FAST 的核心不是再提出一个完整 VLA，而是把连续高频机器人动作序列先变成更适合 autoregressive VLA 预测的离散 action tokens：`continuous action sequence -> DCT compression -> BPE-like action tokens -> autoregressive prediction -> decode back to continuous actions`。

### 和 RT-2 / OpenVLA / pi0 的区别

- `RT-2`：把 robot action 放进 token 输出空间，重点是 `VLM -> VLA` 的 action-as-token 抽象。
- `OpenVLA`：开放 7B VLA contract，重点是 image/language 输入、Open X 数据、fine-tune / deploy。
- `pi0`：走 continuous action / flow action expert，重点是生成连续 action sequence。
- `pi0-FAST`：把连续 action sequence 压成 action tokens，让 autoregressive VLA 也能处理高频、灵巧、连续动作。

### 和 SO-ARM101 / LeRobot 的连接

- 当前阶段不需要训练 FAST，但它提醒我们：`action` 不只是单步关节位置，也可能是一段高频轨迹的可压缩序列。
- 录 `push-to-zone` 或后续 ACT/BC 数据时，至少要把 control frequency、action dim、action horizon、episode boundary、latency 记录清楚，否则后续无法判断 action tokenization 或 action chunk 是否合理。
- 第一阶段仍以 LeRobot / ACT 的 action chunk 直觉为主；FAST 暂时作为 action representation radar。
