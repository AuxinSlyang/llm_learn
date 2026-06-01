---
type: career_strategy
time_window: 2026-2030
current_role: DB / Storage Kernel Engineer
target_direction: Embodied AI Systems Builder / Robot Full-Stack Engineer -> Roboticist
updated: 2026-06-01
linked_files:
  - "[[00_North_Star]]"
  - "[[02_Capability_Map]]"
  - "[[03_Annual_Plan_2026]]"
  - "[[04_2026_Monthly_Learning_Materials]]"
  - "[[06_Embodied_AI_Software_Engineer_Learning_Curve]]"
  - "[[07_One_Year_Interview_Roadmap_Embodied_AI_Software]]"
  - "[[08_One_Year_Roadmap_LLM_Inference_to_Robot_Runtime]]"
  - "[[09_One_Year_Robot_Learning_Full_Stack_Roadmap]]"
---

# Career Strategy 2026-2030

> 这份文件回答的问题：**我如何从当前 DB / 存储内核工程师，逐步迁移到 Physical AI / Robotics 方向，并在 3 年内做出清晰职业决策？**

## 当前判断

### 一句话结论

当前不应该裸辞或立刻大跨度跳到纯机器人算法岗位；应该保留字节 DB / 存储内核岗位作为基本盘，同时用未来一年优先建立 `Robot Learning Full-Stack / Policy Runtime / Robot Learning Infra` 的作品证据。`LLM / AI Infra / Runtime` 继续保留，但定位为 VLA / robot policy runtime / edge inference 的支撑线。

### 当前状态

- 职业阶段：工作第一年即将结束。
- 当前岗位：一线大厂 DB / 存储方向研发工程师，偏 kernel / systems。
- 当前优势：系统工程、性能、存储、分布式、底层抽象、长期学习能力。
- 当前不满：DB / 存储薪水满意，但对长期社会 impact 和未来叙事不够满意。
- 长期吸引：机器人 / Physical AI 可能把 AI 带进物理世界，更接近希望产生的 impact。

### 职业定位

目标不是把自己清零成“纯机器人算法研究员”，也不是永久停在通用 LLM Infra，而是分两层迁移：

> 短期成为懂系统工程、机器人软件闭环和 policy runtime 的具身智能系统构建者；长期成长为能打通机器人本体、感知、控制、学习、runtime 和数据闭环的机器人全栈工程师 / roboticist。

更具体的目标角色：

- Embodied AI Software Engineer
- Robot Full-Stack Engineer
- Robot Learning Infra Engineer
- Policy Runtime Engineer
- Simulation / Evaluation Infra Engineer
- Robot Data Infra Engineer
- AI Infra for Robotics Engineer
- GPU Performance / Model Runtime Engineer
- Edge-Cloud Robotics Systems Engineer
- Robotics Runtime / Observability Engineer
- Physical AI Systems Engineer

## 行业判断：机器人会爆发吗？

### Base Case

机器人 / Physical AI 大概率会成为未来 5-10 年的重要技术主线，但它不会像 ChatGPT 一样突然全民爆发。

更可能的节奏是：

- 工业机器人、仓储物流、制造、巡检等结构化场景先增长。
- 机器人学习、VLA、仿真、数据闭环、边云协同成为关键基础设施。
- Humanoid 和家庭通用机器人会有高热度，但商业化更慢、更不均匀。
- 真正稀缺的人不是只会调模型的人，而是能把数据、模型、仿真、评测、部署和真实系统打通的人。

### 证据来源

- International Federation of Robotics 的 World Robotics 2025 显示，2024 年全球工业机器人安装量约 542,000 台，是历史第二高，且过去 10 年全球工厂机器人需求翻倍。
- Goldman Sachs Research 预测 humanoid robots 市场 2035 年可能达到 380 亿美元，且大多数 2030 年前后出货会先用于工业场景。
- McKinsey 对 embodied AI / humanoid robotics 的判断也偏向“长期有机会、结构化场景先落地”，而不是短期全面取代人类。
- Stanford AI Index 2025 已经把 robotics foundation models 作为 AI 进展的一部分追踪，说明主流 AI 研究视野正在把 robotics 纳入 foundation model 叙事。

### 我的判断

这不是一个确定性暴富赛道，但它是一个值得用 3-5 年建立职业期权的方向。

判断标准不是“机器人会不会爆”，而是：

- 即使行业慢，我学到的 AI Infra / Robot Infra / Robotics Systems 能力是否仍有价值？
- 如果行业快，我是否已经站在正确的交叉点上？

答案是：是。

## 总策略

### 核心策略

> Robotics-first, systems-backed.

未来一年以 Robot Learning Full-Stack 为上位主线，因为它最贴近长期目标和 Unitree JD；DB / 存储 / 系统工程背景不丢弃，而是迁移到 policy runtime、robot data/eval infra、低延迟链路、日志回放、可靠性和 edge inference 这些工程问题上。

### 时间预算

在保留当前工作强度和薪资基本盘的前提下：

- 每周 8-14 小时投入长期学习。
- 每季度至少一个可见产物。
- 每半年做一次职业路线复审。
- 2028 年底前做第一次明确职业方向决策。

## 2026：建立 Robot Learning Full-Stack 职业证据

### 年度定位

2026 年不做裸辞或激进跳槽决策，先用 H2 建立具身智能软件 / Robot Learning Infra / Policy Runtime 的能力和作品证据。

核心问题：

- 我能否把 DB / 系统能力迁移到机器人中的 runtime、数据闭环、评测、日志、回放、可靠性和性能问题？
- 我能否跑通最小 Gymnasium/MuJoCo policy 训练-评估闭环，而不是只读 robot learning 论文？
- 我能否讲清机器人状态、动作、感知、policy、eval、runtime 的完整链路？
- 我能否说明 LLM / VLA / AI Infra 如何支撑机器人语言智能和 policy runtime，而不是偏离机器人主线？

### 学习主线

- nanoGPT 收口：保留语言智能基础，建立 `training -> generate -> runtime` 的系统直觉。
- Gymnasium/MuJoCo + PPO：建立最小 policy 训练-评估闭环。
- Modern Robotics：建立机器人本体、坐标系、运动学和控制语言。
- CS231n / perception：理解视觉 observation 如何进入 policy。
- CS285 / Robot Learning：进入 BC、DAgger、PPO、SAC 和 eval harness。
- LLM / AI Infra / Runtime：只保留 VLA / policy runtime / edge inference 需要的支撑能力。
- latency / throughput / jitter / resource usage：建立 policy runtime 与模型 runtime 的性能诊断语言。
- GPU profiling / quantization / compile awareness：作为端侧模型 runtime 优化入口，不扩散成纯云端 LLM serving 主线。

### 关键产物

- `nanoGPT 第一轮总结`
- `Robot Learning Full-Stack 路线 v0`
- `MuJoCo/Gymnasium + PPO 最小闭环 report v0`
- `state/action/trajectory schema v0`
- `Modern Robotics notes v0`
- `control baseline note`
- `robot perception map`
- `dataset schema + eval harness v0`
- `BC/PPO experiment v0`
- `policy runtime mini-stack draft`
- `Capability Map v1`
- `2027 方向草案`

### 2026 年末决策门

到 2026-12-31，满足以下条件则继续强化 Physical AI 方向：

- 有一个可复现的 robot learning / policy runtime 小闭环。
- 能讲清 obs/action/reward/policy/eval/log/replay/data loop 的主链路。
- 能把 DB / 存储经验迁移到机器人 runtime、数据闭环、评测、可靠性和性能诊断。
- 能讲清 LLM / VLA / AI Infra 如何支撑 robot policy runtime，而不是替代机器人系统。
- 仍然愿意把机器人作为 3-5 年长期目标，而不是被通用 LLM Infra 完全吸走。

如果没有满足：

- 不急着否定方向。
- 2027 上半年补一轮，但砍掉过多分支。
- 保持 DB / AI Infra 方向作为主职业安全线。

## 2027：深化 Robot Learning / Runtime，并测试职业第一跳

### 年度定位

2027 年的第一目标是拿到或至少认真测试具身智能软件 / Robot Learning Infra / Policy Runtime 方向机会；第二目标是根据作品证据决定是否继续强化 Robot Learning 算法、ROS2/real robot、Isaac Lab/VLA，或保留 AI Infra 作为工程支撑线。

### 2027-03 第一轮硬检查点

2027-03 设为职业转向的第一轮硬检查点。

到 2027-03，不要求已经完成转岗，但必须达到：

- 有可展示的 `policy runtime mini-stack`、`robot learning infra` 或等价机器人系统作品。
- 能把 Unitree / 具身智能软件 / Robot Learning Infra JD 映射到自己的项目证据和系统经验。
- 已经准备好面试叙事：DB / 存储系统经验如何迁移到机器人数据闭环、runtime、eval、logging、replay、可靠性和性能诊断。
- 开始真实市场测试：内部机会沟通、外部岗位调研、机器人 / AI Infra / Robot Learning 工程师交流。
- 判断是否在 2027-Q2 继续冲具身智能软件 / Robot Learning Infra，还是先通过 AI Infra / Runtime 岗位过渡。

目标不是证明自己会一点机器人，也不是只做通用模型服务，而是证明自己能做：

> policy runtime + robot data / simulation / evaluation / learning infra + VLA/LLM runtime support 的交叉系统。

### 项目方向

优先做一个具有系统含量的项目，而不是只做一个会动的机器人 demo。

候选项目：

- VLA / policy inference latency benchmark
- Robot trajectory 数据格式与回放系统
- MuJoCo / LeRobot eval harness
- Robot episode logging + metrics + failure case index
- Simulation dataset generation pipeline
- Teleop 数据采集、版本管理与质量分析工具
- Edge-cloud robot data sync prototype

### 关键产物

- 一个公开或半公开的 `robot-learning-infra` 项目。
- 一个可展示的 `policy-runtime-mini-stack` 或 robot learning infra 项目总结。
- 至少 3 篇结构化技术文章：
  - Robot data lifecycle
  - Simulation / eval pipeline
  - LLM / VLA runtime in robotics
- 至少 10 次行业对话：
  - 机器人公司工程师
  - 自动驾驶 / 数据闭环平台工程师
  - AI Infra 工程师
  - 机器人实验室 / 开源社区成员

### 2027 年末决策门

到 2027-12-31，做一次强复盘：

| 问题 | 判断 |
|---|---|
| Robotics 是否仍然强吸引？ | 如果只剩概念兴奋，停止大迁移 |
| 是否已有作品能说服外部工程师？ | 如果没有，继续补项目，不急着跳 |
| 当前 DB 工作是否仍能成长？ | 如果能成长且薪资高，保留基本盘 |
| 是否出现合适 AI Infra / Robot Infra 机会？ | 有则开始市场测试 |

如果 `作品 + 兴趣 + 机会` 三者同时成立，2028 年可以开始认真看机会。

## 2028：明确职业切换决策

### 年度定位

2028 年是第一次硬决策窗口。

不要求一定跳槽，但必须明确未来 2-3 年主职业定位。

### 三条路径

| 路径 | 适合条件 | 风险 |
|---|---|---|
| A. 留在 DB / 存储，向 AI Infra 靠 | 当前岗位成长性高，外部机器人机会不成熟 | 离 Physical AI 变远 |
| B. 切到 AI Infra / LLM Infra | 能进入训练、推理、数据、评测平台核心团队 | 可能变成通用 AI Infra，不够 robotics |
| C. 切到 Robot Infra / Physical AI Systems | 有合适团队、作品能匹配、薪资折损可接受 | 行业和团队质量不确定 |

### 决策规则

只有同时满足以下条件，才建议从当前高质量岗位切出去：

- 新岗位不是边缘业务，而是数据、仿真、训练、评测、部署、runtime 中的核心系统。
- 团队有真实机器人 / Physical AI 数据闭环，而不是纯 PPT。
- 薪资折损在可接受范围内，或者成长上限明显更高。
- 你已有作品和知识能在新岗位里直接复用。
- 当前 DB 岗位的成长曲线明显下降，或者新方向机会窗口明显打开。

否则不急着跳。可以先内部转 AI Infra / 数据平台 / 多模态 infra。

## 2029-2030：形成长期职业定位

### 目标定位

到 2030 年，至少形成一个清晰身份：

- Physical AI Systems / Robot Infra 方向的核心工程师
- AI Infra + Robotics Data/Eval 交叉方向的系统 owner
- 或者 DB / 存储 + AI Infra 的强系统工程师，同时保留机器人长期副线

### 2030 年希望具备的证据

- 一个长期维护的 Robot Infra / Robot Learning 项目。
- 能讲清从传感器数据到模型训练、评测、部署、线上反馈的完整闭环。
- 至少一次真实机器人或仿真大规模数据系统经验。
- 在 AI Infra / Robot Infra 社区有可被看到的技术文章、项目或贡献。
- 职业选择不是“追热点”，而是已经站在一个交叉型壁垒上。

## 年度能力栈

| 年份 | 主能力 | 副能力 | 关键证据 |
|---|---|---|---|
| 2026 | Robot Learning Full-Stack + policy runtime | LLM / AI Infra runtime 支撑 | MuJoCo PPO report + robot learning infra evidence |
| 2027 | 具身智能软件 / Robot Learning Infra 岗位匹配 | VLA / policy runtime / Robot Data-Eval Infra | 职业第一跳 + 深化计划 |
| 2028 | AI Infra 到 Robot Infra / Physical AI Systems 的硬决策 | networking / interview / market test | 职业切换决策 |
| 2029 | 深入一个核心系统方向 | robotics product / deployment understanding | 系统 owner 能力 |
| 2030 | Physical AI Systems 身份成型 | open-source / community / impact | 长期定位 |

## 每季度固定动作

- 更新一次 `02_Capability_Map.md`。
- 复盘当前工作是否仍在增强系统能力。
- 输出至少一篇结构化技术笔记或项目总结。
- 和至少 2 位相关方向的人交流。
- 检查是否出现新的内部 / 外部机会。

## 不做事项

- 不因为机器人热度立刻裸辞。
- 不把当前 DB / 存储积累清零。
- 不把自己定位成纯机器人算法新人。
- 不为了追热点去低质量机器人团队。
- 不在没有作品和行业反馈前做大跨度职业跳跃。
- 不把 AI Infra 学成新的无边界主线；未来一年只围绕 inference serving / runtime / GPU profiling / scheduling 建立职业踏板。
- 不因为推理系统更现实，就把机器人长期目标从路线中删掉。

## 一句话回锚

> 保留 DB / 存储基本盘，用 2026-2028 年建立 Physical AI Systems 职业期权；到 2028 年底前，用作品、兴趣、行业机会和岗位质量做第一次硬决策。
