---
type: reading_plan
track: VLA / robot learning / SO-ARM101
status: active
created: 2026-06-10
linked_project: [[so-arm101-lerobot-first-loop]]
---

# VLA First Stage Reading Plan

## 判断

当前清单作为 VLA 第一阶段已经足够，不需要再盲目扩论文数量。

真正的问题不是论文不够，而是要把论文分层：

```text
P0: 直接服务 SO-ARM101 首闭环
P1: 解释 VLA 主流范式
P2: 前沿雷达和后续扩展
Reference: 大清单，只用于查漏补缺
```

## P0：本周必须围绕实物闭环读

| 材料 | 作用 | 读法 |
|---|---|---|
| LeRobot docs | 先跑通 SO-ARM101 的 teleop / record / replay / ACT | 跟做，不精读 |
| ACT | 第一阶段最现实的 imitation learning policy | first pass done；ACT/BC v0 训练前回看 method / ablation |
| XLeRobot | 双臂 / 移动底盘 / SO101 社区工程参考 | 先扫硬件和 bring-up 流程 |
| LingBot-VLA | 看 LeRobot dataset/config/eval/deploy 如何接 VLA | 项目 walkthrough，暂不训练 4B |
| SmolVLA | affordable robotics / 小 VLA / LeRobot 生态 | 重点看 runtime、数据、异步推理 |

## P1：VLA 主线必读

| 材料 | 为什么必须读 | 当前状态 |
|---|---|---|
| RT-1 | language-conditioned robot policy 的早期系统化路线 | 待读 |
| RT-2 | action-as-token，把 VLM 变成 VLA | 已完成第一轮 |
| Open X-Embodiment / RT-X | 多机器人数据规模化和 embodiment gap | 待读 |
| OpenVLA | 开源 VLA，理解 7B VLA、Open X 数据、fine-tune/deploy | 已下载，待结构化读 |
| π0 | flow matching action expert，理解连续动作 VLA | first pass done；配合 Flow Matching / Diffusion Policy / pi0-FAST 回看 |
| π0-FAST | action tokenizer，从离散 token 化走向更高效动作序列 | 待读 |
| π0.5 | open-world generalization，异构数据 co-training | 待读 |

## P2：补充但不抢主线

| 材料 | 作用 | 触发条件 |
|---|---|---|
| PaLM-E | embodied multimodal LM，理解视觉/语言/机器人状态统一输入 | VLM->VLA 谱系补全 |
| Octo | open generalist robot policy | OpenVLA 后 |
| Diffusion Policy | 连续动作生成和 action distribution 基础 | ACT 跑通后 |
| DAgger | BC 分布偏移和 dataset aggregation | 发现 policy drift 后 |
| Mobile ALOHA | 双臂移动操作系统参考 | 进入双臂/移动底盘阶段 |
| Agile But Safe | safe + agile legged locomotion / reach-avoid value / recovery policy | sim2real / safe RL 专题时读 |
| CMU 16-831 Reading Map | Robot Learning 系统课程阅读地图 | 长期课程队列，不抢 SO-ARM101 |

## Reference：大清单的定位

Epoch robotic manipulation compute CSV 是雷达库，不是阅读队列。

使用方式：

- 每月 review 一次，看是否有新的关键范式。
- 只把能解释当前项目问题的论文提升到 P0/P1。
- 不用为了“读得多”去扫 400+ 条模型表。

## 2026-06-11 用户补充资源分层

这些材料都值得保留，但不能同一天全部精读。按和 `SO-ARM101 + LeRobot` 首闭环的距离分层：

| 层级 | 材料 | 链接 | 当前读法 |
|---|---|---|---|
| P0 | XLeRobot | https://github.com/Vector-Wangel/XLeRobot | 社区工程参考：先看硬件、bring-up、teleop/sim/VR/VLA tutorial，不作为本月新硬件项目 |
| P0 | SmolVLA | https://huggingface.co/blog/smolvla | 贴近 LeRobot / affordable robotics：重点看数据格式、action chunk、async inference 和 consumer hardware |
| P0/P1 | LingBot-VLA | https://arxiv.org/abs/2601.18692 | LeRobot-style VLA 工程栈：dataset/config/eval/deploy，对齐 SO-ARM101 数据闭环 |
| P1 | OpenVLA | https://arxiv.org/abs/2406.09246 / https://github.com/openvla/openvla | 开放 VLA 模型：理解 Open X 数据、7B VLA、fine-tune/deploy；SO-ARM101 record/replay 前不训练 |
| P2 | pi0 / openpi | https://github.com/Physical-Intelligence/openpi | 前沿模型与工程实现：只看 action interface、LeRobot dataset conversion、policy server / remote inference |
| P2 | pi0-FAST | https://huggingface.co/blog/pi0 | FAST action tokenizer / autoregressive VLA，作为 action representation 对照 |
| P2 | pi0.5 | https://www.pi.website/blog/pi05 | open-world generalization / 异构数据 co-training，后续 awareness |
| Reference | Robotics Models CSV | https://github.com/epoch-research/robotic-manipulation-compute/blob/main/data/Robotics%20Models.csv | 雷达库：每月 review，不变成逐篇阅读队列 |
| Reference | ACT repo | https://github.com/Shaka-Labs/ACT | 只在训练 ACT v0 时查实现，不再作为今天阅读任务 |

## 2026-06-15 用户补充 VLA 队列二次分层

用户给出的资源都保留，但本周不能全部精读。按和当前 `SO-ARM101 + LeRobot` 首闭环的距离重新分层：

| 层级 | 资源 | 本周读法 | 只回答什么 |
|---|---|---|---|
| Today P0 | `ViT` | 白天 structured read | `camera image -> patch tokens -> visual encoder -> VLA visual input` |
| Today P0 | XLeRobot：`https://github.com/Vector-Wangel/XLeRobot` | 30-45m repo triage | 低成本双臂/移动底盘如何复用 LeRobot / SO100/SO101；有哪些 hardware / software / simulation / web control 入口 |
| Today P0 / Week P0 | ACT repo：`https://github.com/Shaka-Labs/ACT` | 20-30m repo triage；record/replay 后再细读 | action chunking 如何接到 low-cost robot train/evaluate 流程 |
| Week P1 | SmolVLA：`https://huggingface.co/blog/smolvla` | structured awareness | 450M 小 VLA、LeRobot community data、SO100/SO101、flow matching action expert、async inference |
| Week P1 | pi0 / openpi：`https://github.com/Physical-Intelligence/openpi` | structured awareness | VLM backbone + action expert + flow matching action sequence；需要什么 GPU / runtime 边界 |
| Week P1 | pi0-FAST：`https://huggingface.co/blog/pi0` | action representation scan | FAST action tokenizer：DCT + BPE 如何把连续动作序列 tokenized |
| Later P2 | OpenVLA：`https://arxiv.org/abs/2406.09246` / `https://github.com/openvla/openvla` | 30-45m awareness，record/replay 后再读 | 7B VLA、Open X 数据、LoRA/OFT fine-tune、REST serving；本周不训练 |
| Later P2 | pi0.5：`https://www.pi.website/blog/pi05` | 20-30m awareness | open-world generalization；等 pi0 理解后再看 |
| Reference | Robotics Models CSV：`https://github.com/epoch-research/robotic-manipulation-compute/blob/main/data/Robotics%20Models.csv` | 每月 radar review | 看 VLA / manipulation model 生态，不进入逐篇阅读 |

### 今日顺序

```text
1. ViT structured read
2. XLeRobot repo triage
3. ACT repo triage
4. 回到 E001 / LeRobot 硬件证据
```

今天不读：

- OpenVLA full paper / repo
- pi0 / pi0-FAST / pi0.5 full read
- Robotics Models CSV 逐行 review

### 本周顺序

```text
ViT
-> XLeRobot / ACT repo triage
-> SmolVLA
-> pi0
-> pi0-FAST
-> OpenVLA awareness
-> pi0.5 awareness
-> Robotics Models CSV monthly radar
```

关键约束：

- 每读一个 VLA 材料，都必须写清：
  - observation 是什么；
  - action / output 是什么；
  - data / training 是什么；
  - eval / deployment 是什么；
  - 和 SO-ARM101 / LeRobot 当前首闭环有什么关系。
- 如果当天没有 E001/E002/E003 新证据，VLA 只能读 20-40m。
- 本周 VLA 学习目标是建立 action representation 和 deployment map，不做训练。

## 2026-06-15 短期两篇 VLA 选择

用户校准：今天、明天最多看两篇 VLA 代表材料；后续论文只放白天或碎片时间，晚间主线回 `Robot / LeRobot / SO-ARM101`。

短期只选：

| 顺序 | 材料 | 为什么代表 | 读法 |
|---|---|---|---|
| 1 | `OpenVLA` | open-source 7B VLA，覆盖 VLA input/output contract、Open X robot demonstrations、fine-tuning、quantization / serving | 今晚读半篇或一篇，重点看 abstract / intro / model / data / deployment，不训练 |
| 2 | `pi0` | VLM backbone + action expert + flow matching，代表连续动作生成的 robot foundation policy 路线 | 明天读，重点看 action expert、flow matching、action horizon、runtime/control frequency |

暂时不读、只进 radar：

- `SmolVLA`：更贴近 LeRobot / affordable robotics，但等 OpenVLA + pi0 建立范式后再作为工程化补充。
- `pi0-FAST / FAST`：重要，但它是 action tokenization 支线；等 pi0 主文理解后再看。
- `pi0.5`：open-world generalization 后续 awareness。

两篇读完后的收束输出：

```text
ViT / CLIP / BLIP-2 / LLaVA
-> DINOv2 / SigLIP: OpenVLA fused visual encoder support
-> OpenVLA: open VLA contract and deployment
-> pi0: flow/action expert and continuous action generation
-> LeRobot / SO-ARM101: record/replay data, action schema, runtime gaps
```

## 2026-06-17 今日聚焦校准

用户校准：今天目标聚焦在 `OpenVLA / pi0 / pi0-FAST`，如果时间有余再看 `DAgger`。这次校准只改变今天的阅读目标，不改变本周 `SO-ARM101 + LeRobot` 首闭环主线。

| 顺序 | 材料 | 今天只回答什么 | 输出 |
|---|---|---|---|
| 1 | OpenVLA | open VLA input/output contract、Open X data、fine-tune / quantization / serving | `OpenVLA/QUICK_READ.md` 3-5 条 takeaway |
| 2 | pi0 | VLM backbone、action expert、flow matching、continuous action / action horizon | `PI0/QUICK_READ.md` 3-5 条 takeaway |
| 3 | pi0-FAST | DCT + BPE / FAST action tokenizer 如何把 continuous action sequence 变成 action tokens | `PI0_FAST/QUICK_READ.md` 2-3 条 takeaway |
| Optional | DAgger | BC covariate shift 和 dataset aggregation 为什么服务 failure-driven data loop | `DAgger/QUICK_READ.md` 一句话定位 |

今日边界：

- 不训练 OpenVLA / pi0。
- 不读 OpenVLA / openpi / FAST 源码。
- 不展开 SmolVLA、pi0.5、Robotics Models CSV。
- DAgger 只在前三项完成后看，不进入最低完成线。

## 第一阶段阅读顺序

```text
1. ACT
2. LeRobot ACT training / dataset flow
3. LingBot-VLA project walkthrough
4. SmolVLA
5. OpenVLA
6. π0
7. π0-FAST
8. π0.5
```

这条顺序和 SO-ARM101 的工程进度对齐：

```text
assemble/calibrate
-> teleop
-> record/replay
-> train ACT
-> understand small VLA
-> understand OpenVLA / π family
```

## 现阶段不要做的事

- 不要把 VLA 论文阅读变成纯 survey。
- 不要在 SO-ARM101 没有 record/replay 前训练大 VLA。
- 不要跳到 Thor/Orin runtime，除非本地数据闭环已经跑通。
- 不要把 World Model、Dexterous Hand、Humanoid、Navigation 全部同时打开。

## 当前缺口

| 缺口 | 补法 |
|---|---|
| 数据闭环经验不足 | 先用 LeRobot record/replay 和 ACT 补 |
| action representation 还不稳定 | 对比 ACT action chunk / RT-2 token / π0 flow matching / π0-FAST tokenizer |
| VLA 工程部署经验不足 | LingBot-VLA / SmolVLA / OpenPI 只看 deployment path |
| OpenVLA Section 4 工程项未补 | 看 `OpenVLA/OpenVLA_Engineering_Support_Checklist.md`，按 LoRA / quantization / FlashAttention / AMP / FSDP 顺序补 |
| OpenVLA visual encoder 还没拆开 | 补 DINOv2 / SigLIP structured quick read：分别理解 spatial/dense visual features 和 language-aligned semantic features |
| CV 基础较薄 | 在 SO-ARM101 首闭环后补 ResNet / ViT / CLIP / DINO/SAM/Vision Banana |
| sim2real / real2sim / safe deployment 缺口 | 新增 [[20_Robot_Learning/CMU_16_831_Robot_Learning_Reading_Map]]，从 Agile But Safe、Domain Randomization、Real2Sim or Sim2Real 开始 |
