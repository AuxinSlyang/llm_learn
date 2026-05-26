---
type: annual_plan
year: 2026
target_role: Embodied AI / Robotics Systems Builder
scenario_anchor: Robot Soccer (long-term) + Manipulation (2026 H2 first demo)
time_budget: 8-14h/week (32-56h/month)
linked_files:
  - "[[00_North_Star]]"
  - "[[01_Learning_Philosophy]]"
  - "[[02_Capability_Map]]"
  - "[[04_2026_Monthly_Learning_Materials]]"
  - "[[05_Career_Strategy_2026_2030]]"
  - "[[06_Embodied_AI_Software_Engineer_Learning_Curve]]"
  - "[[07_One_Year_Interview_Roadmap_Embodied_AI_Software]]"
---

# 2026 Annual Plan

> 这份文件回答的问题：**今年我具体怎么走？**
> 更新频率：月级（每月复盘后微调下个月 Phase 细节）；写于 2026-05-17。

## 2026 年定位（一句话）

> 把通用机器人 + AI + Robot Learning 三大 Pillar 都推到 **L1 概念深度**，至少 1-2 条到 **L2 实现层**，并在仿真里跑出至少一个 anchor 项目原型作为整合验证。

## 上半年（H1）实际回顾

| 阶段 | 时间 | 实际做了什么 | Level 变化 |
|---|---|---|---|
| 早期 | 2026-03 ~ 2026-04 | 在原 LLM / AI Infra 学习框架下推进 micrograd / makemore 基础线 | autograd / 训练 loop: L0 → L1 |
| 中期 | 2026-04 ~ 2026-05 | nanoGPT 主线推进；attention / transformer 收口中 | Transformer: L0 → L1 |
| 转向 | 2026-04-27 | 目标升级：从单一 LLM 工程线叙事 → 具身智能主线 | 方向重定义 |
| 收敛 | 2026-05-17 | 仓库梳理 + 目标再确认：通用机器人 + 三大 Pillar | Roadmap reframe |

**H1 实际投入**：节奏不稳，过去几周低于预算。H2 起回到 8-14h/周稳定节奏。

## 下半年（H2）：Phase A-F 总览

| Phase | 时间窗 | 主推 | 副推 | Month-end Deliverable |
|---|---|---|---|---|
| **A** | 5/18 - 5/31 | LLM 收口（nanoGPT） | CS336 结构对照 | nanoGPT 总结 + GPT 到 runtime 桥接 |
| **B** | 6/1 - 7/31 | Modern Robotics 大部分内容（Ch.1-6） | CS231n/CV 入口 + MuJoCo step loop + CS336 runtime awareness | MR 笔记 + 机器人系统图 + MuJoCo 最小循环 |
| **C** | 8/1 - 8/31 | MR 动力学 / 控制入口 | RL 基本概念 + trajectory schema | 控制闭环 + RL/IL 概念地图 |
| **D** | 9/1 - 10/31 | IL 概念 + MuJoCo 仿真闭环 + BC 第一次动手 | ACT/Diffusion paper + eval harness | classic-control demo + BC train/eval |
| **E** | 11/1 - 11/30 | 算法产品化 + runtime / TensorRT / 量化入口 | VLA awareness + robustness | policy runtime + latency report + fault tests |
| **F** | 12/1 - 12/31 | 作品化 + 年终复盘 | 多传感器融合入口 + 2027 真机/edge plan | mini-stack README + Capability Map v1 + 2027 plan |

## 每个 Phase 详细

### Phase A（5/18 - 5/31，2 周）—— LLM 收口

**主推：LLM phase 1 收口到 5 月底**
- W21（5/18-24）：Zero-to-Hero 收口（nanoGPT + tokenizer + GPT-2），写 nanoGPT 第一轮总结
- W22（5/25-31）：写 `makemore → nanoGPT → inference/runtime` 映射；确认 Modern Robotics / CS231n / CS336 的进入边界

**副推：CS336 只做结构对照**（tokenization / Transformer / training loop / deployment 的位置）

**Deliverable**：
- `LLM phase 1 总结.md`（nanogpt-from-scratch/ 下）
- `makemore -> nanoGPT -> inference_runtime 映射`
- `具身智能软件岗位能力图`

**Level 目标**：Transformer L1→L2 / LLM runtime awareness L0→L1

### Phase B（6 月 - 7 月，8 周）—— MR 大部分内容 + AI fundamentals / perception 入口

**主推：Modern Robotics Ch.1-6**
- 6 月：Ch.1-3，configuration space、刚体运动、SO(3) / SE(3)
- 7 月：Ch.4-6，FK / Jacobian / IK
- 第一轮不追完整证明，先建立机器人系统底层语言

**副推 1：MuJoCo 最小软件循环**
- 安装 + hello-world
- Python step loop
- 读 `qpos/qvel`
- 写 `state/action schema v0`
- 写 `episode_logger v0`

**副推 2：CS231n / CV 入口**
- 只看视觉任务形态：classification / detection / segmentation
- OpenCV 读图、相机、简单检测
- 目标是理解视觉 observation 如何进入机器人系统，不完整刷 CS231n

**副推 3：CS336 runtime awareness**
- deployment / inference / runtime 概念位置
- 不做完整 assignment，不做 distributed training project

**Deliverable**：MR Ch.1-6 笔记 + 机器人系统图 v0 + MuJoCo step loop + CV hello-world

**Level 目标**：刚体表示 / FK / IK / Jacobian L0→L1+ / MuJoCo L0→L1 / OpenCV L0→L1

### Phase C（8 月，4 周）—— MR 动力学/控制 + RL 概念

**主推**：MR 动力学 / 轨迹 / 控制入口

**副推 1**：MuJoCo 控制闭环
- joint PD control
- optional simple IK
- `trajectory schema v1`
- `metrics v0`

**副推 2**：RL / IL 概念地图
- MDP / policy / reward / value
- Q-learning / PPO 的位置
- BC / DAgger / covariate shift 预热

**Deliverable**：控制入口笔记 + MuJoCo 控制实验 + RL/IL 概念地图 + trajectory schema

**Level 目标**：动力学/控制 L0→L1 / RL&IL 概念 L0→L1 / data schema L0→L1

### Phase D（9 月 - 10 月，8 周）—— IL + MuJoCo 仿真闭环

**主推 1：classic-control demo**
- reach / push / pick-place 三选一，默认从 reach 或 push 起步
- 一键跑 N 个 episode
- 输出 eval report、failure categories、sample videos
- replay 失败 episode

**主推 2：Behavior Cloning 第一次动手**
- scripted policy 或 teleop 采数据
- `BC dataset v0`
- train/eval pipeline
- `policy_runner v0`
- 同一套 eval harness 对比 classic-control baseline 和 BC policy

**副推**：ACT / Diffusion Policy 论文精读，只看 observation / action / data / eval / system structure

**Deliverable**：classic-control demo + eval harness + BC train/eval + Robot Learning 第一次动手总结

**Level 目标**：MuJoCo L1→L2- / BC L0→L1+ / eval harness L0→L1+

### Phase E（11 月，4 周）—— 算法产品化 + Runtime / TensorRT / 量化入口

**主推：policy runtime**
- `policy_runtime v0`
- latency report：inference latency / simulation step latency / end-to-end latency / jitter
- timeout / action clipping / fallback / watchdog

**副推 1：模型部署与优化 awareness**
- ONNX export
- TensorRT 基础概念
- quantization awareness：FP16 / INT8
- 如果环境允许，做一个最小 ONNX/TensorRT latency demo；如果环境不允许，写清理论路径和缺口

**副推 2：VLA awareness**
- RT-2 / OpenVLA / PI-0 / Octo 中选 2-3 个建立地图
- 不做完整 VLA 训练

**Deliverable**：policy runtime + latency report + fault injection tests + VLA 概念笔记

**Level 目标**：runtime L0→L1+ / TensorRT&量化 awareness L0→L1 / robustness L0→L1

### Phase F（12 月，4 周）—— 作品化 + 多传感器融合入口 + 年终复盘

**主推：Embodied AI mini-stack 作品化**
- README
- 架构图
- demo video
- eval report
- failure analysis
- JD mapping

**副推：多传感器融合入口**
- 今年不追完整 SLAM / EKF / factor graph
- 只建立软件系统视角：time synchronization、coordinate frames、calibration、noise、missing data
- 最小实践：camera frame + qpos/qvel 同步记录，在 replay 中同时展示视觉帧和 robot state

**Deliverable**：Embodied AI mini-stack README + Capability Map v1 + sensor fusion note v0 + 2027 real-robot / edge-deployment plan

**Level 目标**：mini-stack L1+ / sensor fusion awareness L0→L1 / career readiness 进入 2027 H1


## 年度产出清单（年底应该有的可见证据）

- [ ] nanoGPT 第一轮总结（Phase A）
- [ ] `makemore -> nanoGPT -> inference_runtime` 映射（Phase A）
- [ ] Modern Robotics Ch.1-6 + 动力学/控制入口笔记（Phase B-C）
- [ ] 机器人系统图：`sensor -> state -> perception -> decision -> action -> log -> train -> eval`（Phase B）
- [ ] MuJoCo step loop + `episode_logger v0` + `state/action schema v0`（Phase B）
- [ ] CV / CS231n perception 入口笔记（Phase B）
- [ ] RL / IL 能力地图（Phase C）
- [ ] `trajectory schema v1` + `metrics v0`（Phase C）
- [ ] 1 篇 ACT / Diffusion Policy 精读笔记（Phase D）
- [ ] reach / push / pick-place classic-control demo + eval harness（Phase D）
- [ ] BC 训练 + eval 完整 pipeline + `policy_runner v0`（Phase D）
- [ ] `policy_runtime v0` + latency report + fault injection tests（Phase E）
- [ ] ONNX / TensorRT / 量化 awareness 笔记或最小验证（Phase E）
- [ ] VLA Models 概念笔记（Phase E）
- [ ] 多传感器融合入口笔记：time sync / frame / calibration / missing data（Phase F）
- [ ] Embodied AI mini-stack README + demo video + JD mapping（Phase F）
- [ ] Capability Map v1（Phase F）
- [ ] 年终复盘 + 2027 real-robot / edge-deployment plan（Phase F）

## 年终自检标准

到 2026-12-31，如果下面这些基本成立，说明这一年走得稳：

- [ ] 三大 Pillar 都至少到 L1（概念深度）
- [ ] 至少 1-2 条 Pillar 子方向到 L2-（实现层），重点候选：MuJoCo / BC / data loop / eval harness
- [ ] 有一个端到端 `Embodied AI mini-stack` 能 demo 给别人看
- [ ] 我能讲清"通用机器人由哪些能力组成、我当前在哪、下一年要去哪"
- [ ] 我能讲清具身智能软件工程师 JD 四块：算法产品化、模型部署优化、数据闭环、鲁棒性可靠性
- [ ] 对 2027 方向有清楚选择（不是泛泛"继续学"）
- [ ] 实物平台是否入手有明确决定

## 风险与降难策略

| 风险 | 降难策略 |
|---|---|
| MR 卡在 SE(3) / 李代数推导 | 第一遍不死磕证明，先建直觉；Ch.4-6 卡的地方留 issue，第二遍再补 |
| MuJoCo 环境问题 | 本地 Mac + CPU server 双备份；不要等到 Phase B 才装 |
| Phase D classic-control demo 做不出 | 降难：从 reach 起步，不急着 pick-place |
| Phase D BC 训不出来 | 降难：从 LeRobot 的现成 example 改一改先跑通 |
| TensorRT / 量化环境卡住 | 降难：先做 ONNX export + latency measurement，TensorRT 写清理论路径和环境缺口 |
| 多传感器融合扩散成 SLAM 主线 | 降难：今年只做 time sync / frame / calibration / missing data awareness |
| Phase F mini-stack 包装不完整 | 砍掉真机，只保留 sim + data + eval + runtime + replay |
| 时间预算长期低于 50% | 触发月计划复审，砍副推线 |
| LLM 分心想继续深 | 6 月起 LLM 降为副推；不再主导日程 |

## 与 Roadmap 其他文件的关系

- [[00_North_Star]]：解释**为什么**走这条路
- [[01_Learning_Philosophy]]：解释**怎么学**
- [[02_Capability_Map]]：解释**学什么 / 当前 Level**
- [[05_Career_Strategy_2026_2030]]：解释**职业上怎么在 3-5 年内决策**
- [[06_Embodied_AI_Software_Engineer_Learning_Curve]]：解释**按具身智能软件工程师岗位画像怎么安排学习曲线**
- [[07_One_Year_Interview_Roadmap_Embodied_AI_Software]]：解释**一年内怎么准备到可以认真聊相关岗位**
- 本文件：解释**今年怎么排时间**
- `07_MonthlyPlans/2026/`：每月细节（按 Phase 拆解）
- `02_WeeklyNotes/`：每周执行
- `01_DailyNotes/`：每日执行
