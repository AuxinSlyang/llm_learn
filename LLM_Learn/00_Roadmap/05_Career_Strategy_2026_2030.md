---
type: career_strategy
time_window: 2026-2030
current_role: DB / Storage Kernel Engineer
target_direction: Embodied AI Software / Physical AI Systems / Robot Learning Infra
updated: 2026-05-18
linked_files:
  - "[[00_North_Star]]"
  - "[[02_Capability_Map]]"
  - "[[03_Annual_Plan_2026]]"
  - "[[04_2026_Monthly_Learning_Materials]]"
  - "[[06_Embodied_AI_Software_Engineer_Learning_Curve]]"
  - "[[07_One_Year_Interview_Roadmap_Embodied_AI_Software]]"
---

# Career Strategy 2026-2030

> 这份文件回答的问题：**我如何从当前 DB / 存储内核工程师，逐步迁移到 Physical AI / Robotics 方向，并在 3 年内做出清晰职业决策？**

## 当前判断

### 一句话结论

当前不应该裸辞或立刻大跨度跳到纯机器人算法岗位；应该保留字节 DB / 存储内核岗位作为基本盘，同时用 2026-2028 年系统建立 `Embodied AI Software / Physical AI Systems / Robot Learning Infra` 方向的职业期权。

### 当前状态

- 职业阶段：工作第一年即将结束。
- 当前岗位：一线大厂 DB / 存储方向研发工程师，偏 kernel / systems。
- 当前优势：系统工程、性能、存储、分布式、底层抽象、长期学习能力。
- 当前不满：DB / 存储薪水满意，但对长期社会 impact 和未来叙事不够满意。
- 长期吸引：机器人 / Physical AI 可能把 AI 带进物理世界，更接近希望产生的 impact。

### 职业定位

目标不是把自己清零成“纯机器人算法研究员”，而是迁移成：

> 懂 DB / 存储 / 分布式系统，理解 LLM / AI Infra，也能做 Robotics / Robot Learning demo 的 Physical AI Systems Builder。

更具体的目标角色：

- Robot Data Infra Engineer
- Robot Learning Infra Engineer
- Simulation / Evaluation Infra Engineer
- AI Infra for Robotics Engineer
- Embodied AI Software Engineer
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

> Robotics-first, Infra-shaped.

学习上以 Robotics / Robot Learning 为主，因为这是当前最大认知缺口；职业上以 AI Infra / Robot Infra 作为切入点，因为这是当前 DB / 存储背景最能迁移的位置。

### 时间预算

在保留当前工作强度和薪资基本盘的前提下：

- 每周 8-14 小时投入长期学习。
- 每季度至少一个可见产物。
- 每半年做一次职业路线复审。
- 2028 年底前做第一次明确职业方向决策。

## 2026：建立方向证据

### 年度定位

2026 年不做跳槽决策，做方向验证和能力打底。

核心问题：

- 我是不是真的愿意长期学 Robotics，而不是只喜欢机器人叙事？
- 我能否把 DB / 系统能力迁移到 Robot Learning / Robot Infra demo 中？
- 我能否做出一个可展示、可复现的机器人学习闭环？

### 学习主线

- Modern Robotics：建立机器人系统底层语言。
- MuJoCo：建立仿真和控制直觉。
- LeRobot / Robot Learning：跑通数据采集、训练、评测闭环。
- AI Infra / LLM Infra：只学 inference / runtime / data / eval 中对机器人有用的部分。

### 关键产物

- `nanoGPT 第一轮总结`
- `Modern Robotics 学习地图`
- `MuJoCo classic-control demo`
- `Behavior Cloning train/eval pipeline`
- `Robot Learning Infra demo v0`
- `Capability Map v1`
- `2027 方向草案`

### 2026 年末决策门

到 2026-12-31，满足以下条件则继续强化 Physical AI 方向：

- 有一个可复现的 MuJoCo manipulation demo。
- 有一个 BC 训练 / eval pipeline。
- 能讲清机器人系统、Robot Learning、AI Infra 的关系。
- 仍然对 Robotics 的慢反馈、工程现实和系统复杂性感兴趣。

如果没有满足：

- 不急着否定方向。
- 2027 上半年补一轮，但砍掉过多分支。
- 保持 DB / AI Infra 方向作为主职业安全线。

## 2027：做出交叉型作品

### 年度定位

2027 年从“学习型 demo”升级到“职业证据型项目”。

目标不是证明自己会一点机器人，而是证明自己能做：

> Robot Data / Simulation / Evaluation / Learning Infra。

### 项目方向

优先做一个具有系统含量的项目，而不是只做一个会动的机器人 demo。

候选项目：

- Robot trajectory 数据格式与回放系统
- MuJoCo / LeRobot eval harness
- Robot episode logging + metrics + failure case index
- Simulation dataset generation pipeline
- Teleop 数据采集、版本管理与质量分析工具
- VLA / policy inference latency benchmark
- Edge-cloud robot data sync prototype

### 关键产物

- 一个公开或半公开的 `robot-learning-infra` 项目。
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
| 2026 | Robotics foundations + MuJoCo + BC | LLM inference / runtime awareness | 可复现 demo |
| 2027 | Robot Data / Eval / Simulation Infra | VLA / policy runtime | 职业证据型项目 |
| 2028 | AI Infra 或 Robot Infra 真实岗位匹配 | networking / interview / market test | 职业切换决策 |
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
- 不把 AI Infra 学成新的无边界主线。

## 一句话回锚

> 保留 DB / 存储基本盘，用 2026-2028 年建立 Physical AI Systems 职业期权；到 2028 年底前，用作品、兴趣、行业机会和岗位质量做第一次硬决策。
