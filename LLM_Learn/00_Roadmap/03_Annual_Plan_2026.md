---
type: annual_plan
year: 2026
target_role: Embodied AI Systems Builder / Robot Full-Stack Engineer -> Roboticist
scenario_anchor: Robot Learning Full-Stack + Robot Runtime + LLM/AI Infra support
time_budget: 8-14h/week (32-56h/month)
active_roadmap: "[[09_One_Year_Robot_Learning_Full_Stack_Roadmap]]"
linked_files:
  - "[[00_North_Star]]"
  - "[[01_Learning_Philosophy]]"
  - "[[02_Capability_Map]]"
  - "[[04_2026_Monthly_Learning_Materials]]"
  - "[[05_Career_Strategy_2026_2030]]"
  - "[[06_Embodied_AI_Software_Engineer_Learning_Curve]]"
  - "[[07_One_Year_Interview_Roadmap_Embodied_AI_Software]]"
  - "[[08_One_Year_Roadmap_LLM_Inference_to_Robot_Runtime]]"
  - "[[09_One_Year_Robot_Learning_Full_Stack_Roadmap]]"
---

# 2026 Annual Plan

> 这份文件回答的问题：**2026 年我具体怎么走？**
> 更新频率：月级；当前权威修订时间：2026-06-01。

## 2026 年定位

短期职业目标：

```text
具身智能系统构建者
-> 具身智能软件 / Robot Learning Infra / Policy Runtime / 机器人全栈工程入口
```

长期能力目标：

```text
机器人全栈工程师 / roboticist
-> 机器人本体 + 感知 + 控制 + 学习 + runtime + 数据闭环 + 语言智能
```

当前执行主线：

```text
Robot Learning Full-Stack 主线
+ LLM / AI Infra / Runtime 支撑线
```

执行含义：

- `Robot Learning Full-Stack` 是 2026-06 起的上位主线。
- `具身智能软件 / Robot Learning Infra / Policy Runtime` 是最现实第一跳。
- `深度强化学习算法 / Robot Learning` 是长期算法目标，需要通过仿真、控制、RL/IL、runtime 和项目证据逐步逼近。
- `LLM / 多模态 / AI Infra` 不再作为独立转岗主叙事，而是作为 VLA、policy runtime、edge inference、语言任务分解和多机器人协作的支撑能力。

## 学习执行原则

- 每个阶段只有一个主课程或主实验，不同时完整刷多门课。
- 每个阶段必须有一个可动手推进的项目；课程、论文和笔记都要服务这个项目的下一个动作。
- 每周至少留下一个可检查证据：笔记、代码、曲线、实验表、失败分析或 JD mapping。
- 论文只作为当前阶段解释器，不随机追热点。
- 实验优先形成闭环：`sim/task -> obs/action -> policy -> train/eval -> log/replay -> runtime -> failure analysis`。
- 看课不是阶段目标本身；看课过程中要同步推进项目里的代码、实验、数据、硬件、日志或报告。
- 月末复盘必须对照月计划，决定下月是继续、降难还是换入口。

## 上半年实际回顾

| 阶段 | 时间 | 实际做了什么 | 结论 |
|---|---|---|---|
| LLM 基础 | 2026-03 ~ 2026-04 | micrograd / makemore / Transformer 基础线推进 | autograd、训练 loop、token 概念有了底座 |
| nanoGPT | 2026-04 ~ 2026-05 | attention、Transformer block、训练/生成主线推进 | LLM 主链路接近收口，但还需要结构化总结 |
| 方向重定义 | 2026-04-27 | 从单一 LLM 工程叙事转向具身智能 / 机器人系统 | 长期目标升级 |
| 职业路径试探 | 2026-05-27 | 曾把 LLM Inference Infra 设为职业第一跳 | 该路径现实但会弱化机器人主线 |
| Unitree JD 校准 | 2026-06-01 | 重新对齐具身智能软件 / Robot Learning Infra / Policy Runtime | 当前权威路线切回 Robot Learning Full-Stack |

H1 的价值不是“已经学完”，而是把语言模型基础、系统工程背景和机器人长期目标重新放到同一条路线里。

## 2026 H2 月度路线

| 月份 | 主模块 | 主资源 | 阶段产出 | 对短期职业目标的帮助 |
|---|---|---|---|---|
| 2026-06 | M1：路线切换 + 实物机器人首闭环预备 | nanoGPT、SO-ARM101、LeRobot、LingBot-VLA walkthrough，Gymnasium/MuJoCo 兜底 | `nanoGPT 主链路总结 v0`、`LLM phase 1 总结 v0`、`SO-ARM101 + LeRobot 首闭环 bring-up 记录`、`robot data schema v0` | 证明能把 LLM 基础收口，并尽早接触真实机器人硬件、示教数据、评估和 failure loop |
| 2026-07 | M2：机器人本体语言 I | Modern Robotics Ch.1-3 | `frame / SO(3) / SE(3) / configuration notes`、`state-action schema v0` | 看懂机器人状态、坐标系和动作表达 |
| 2026-08 | M3：机器人本体语言 II | Modern Robotics Ch.4-6 | `FK/IK/Jacobian demo`、`MR notes v0` | 具备和机器人算法/控制同学沟通的基础语言 |
| 2026-09 | M4：控制 / 动力学入口 | MIT Underactuated 精选、MuJoCo control | `control baseline note`、`latency/jitter/robustness note` | 支撑 policy runtime 的稳定性、低延迟和故障分析 |
| 2026-10 | M5：视觉感知入口 | CS231n 精选 | `robot perception map`、`vision data pipeline note` | 理解视觉 observation 如何进入决策和 policy |
| 2026-11 | M6：感知到 runtime 桥接 | CS231n 精选、policy runtime notes | `perception-to-policy runtime bridge`、`dataset schema v0` | 把感知、数据格式、推理延迟和机器人系统连接起来 |
| 2026-12 | M7：Robot Learning 入口 + 年终作品化 | CS285 精选、BC/PPO/DAgger | `BC/PPO experiment v0`、`policy runtime mini-stack draft`、`2027 plan` | 形成可展示的 robot learning infra / policy runtime 证据 |

## 2026 年度关键产出

- [ ] `nanoGPT 主链路总结 v0`：讲清 `token -> embedding -> attention -> block -> logits -> loss/generate`。
- [ ] `Robot Learning Full-Stack 路线 v0`：明确课程、论文、硬件、实验和 JD 映射。
- [ ] `SO-ARM101 + LeRobot 首闭环 report v0`：包含采购/组装/校准/teleop/record/replay/train/eval/failure note；若硬件阻塞，用 `Gymnasium/MuJoCo + PPO smoke test` 兜底。
- [ ] `state/action/trajectory schema v0`：用机器人系统语言描述 obs/action/reward/log。
- [ ] `Modern Robotics notes v0`：frame、pose、twist、FK、IK、Jacobian。
- [ ] `control baseline note`：PD/LQR/MPC awareness、latency、jitter、stability。
- [ ] `robot perception map`：camera/depth、CNN/ViT、detection/segmentation、数据格式和延迟。
- [ ] `dataset schema + eval harness v0`：episode metadata、seed、metrics、replay、failure category。
- [ ] `BC/PPO experiment v0`：至少一个可复现实验和对比报告。
- [ ] `policy runtime mini-stack draft`：policy load、obs preprocessing、action clipping、timeout、logging、replay。
- [ ] `JD mapping v1`：把具身智能软件 / Robot Learning Infra / Policy Runtime 要求映射到项目证据。
- [ ] `2027 plan`：决定是否进入更强 Robot Learning、ROS2/real robot、Isaac Lab/VLA 或岗位测试阶段。

## 2026 年终自检标准

到 2026-12-31，如果下面这些基本成立，说明 2026 走得稳：

- [ ] 能讲清 robot learning 闭环：`obs -> action -> reward -> policy -> eval -> log/replay -> data loop`。
- [ ] 能讲清机器人状态、坐标系、FK/IK/Jacobian 在系统中的作用。
- [ ] 能跑通至少一个真实或仿真的 robot learning 闭环；优先是真实 SO-ARM101 的 `teleop -> dataset -> replay/train -> eval -> failure note`，硬件阻塞时用 Gymnasium/MuJoCo PPO 兜底。
- [ ] 能解释视觉 observation 如何变成 policy 输入，以及 camera/depth/calibration/data format 的位置。
- [ ] 能解释 policy runtime 的关键工程问题：latency、timeout、action clipping、fallback、watchdog、logging。
- [ ] 能说明 LLM / VLA / 多模态能力如何作为机器人语言智能和高层任务分解模块接入，而不是替代机器人系统。
- [ ] 有一套可展示材料：README、实验脚本、指标图、失败分析、JD mapping。

## 风险与降难策略

| 风险 | 降难策略 |
|---|---|
| 课程开太多 | 每月只保一个主课程，其他只做支撑材料 |
| nanoGPT 收尾拖太久 | 只保主链路总结，不继续展开大规模 LLM 论文 |
| 真实硬件到货或校准卡住 | 先做 LeRobot/LingBot-VLA walkthrough、dataset schema mapping 和 Gymnasium/MuJoCo smoke test，保持项目证据不断档 |
| Modern Robotics 数学推导卡住 | 第一遍不死磕证明，先建立系统直觉和代码 demo |
| CS231n 扩散成纯 CV 路线 | 只看机器人 observation 需要的视觉表示、数据格式和延迟问题 |
| Robot Learning 论文读散 | 每篇只回答 task、obs/action、policy/data/loss/reward、eval/runtime |
| AI Infra 抢回主线 | 只保留与 VLA / policy runtime / edge inference 相关的部分 |
| 机器人目标变成口号 | 每月必须留下一个机器人系统或 robot learning 证据 |

## 与 Roadmap 其他文件的关系

- [[00_North_Star]]：解释**为什么**走机器人全栈 / roboticist 方向。
- [[01_Learning_Philosophy]]：解释**怎么学**。
- [[02_Capability_Map]]：解释**学什么 / 当前 Level**。
- [[05_Career_Strategy_2026_2030]]：解释**职业上怎么在 3-5 年内决策**。
- [[06_Embodied_AI_Software_Engineer_Learning_Curve]]：保留具身智能软件工程师能力曲线。
- [[07_One_Year_Interview_Roadmap_Embodied_AI_Software]]：保留岗位准备材料。
- [[08_One_Year_Roadmap_LLM_Inference_to_Robot_Runtime]]：作为 LLM / AI Infra / runtime 支撑线，不作为当前上位主线。
- [[09_One_Year_Robot_Learning_Full_Stack_Roadmap]]：当前权威的一年 Robot Learning Full-Stack 路线。
- 本文件：解释**2026 年怎么排时间和验收产出**。
- `07_MonthlyPlans/2026/`：每月执行细节。
- `02_WeeklyNotes/`：每周执行。
- `01_DailyNotes/`：每日执行。
