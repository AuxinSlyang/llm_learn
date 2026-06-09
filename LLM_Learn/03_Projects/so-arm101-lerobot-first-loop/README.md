---
type: project
status: planning
track: Robot Learning Full-Stack / LeRobot / SO-ARM101
time_window: 2026-06_to_2026-07
budget_scope: robot_first_loop_under_3000_rmb
optional_infra: 3d_printer_separate_budget
linked_roadmap: [[09_One_Year_Robot_Learning_Full_Stack_Roadmap]]
---

# SO-ARM101 + LeRobot 首闭环

## 一句话定位

这是第一个真实机器人学习闭环项目：

```text
SO-ARM101 leader/follower
-> 组装 / 校准
-> 遥操作
-> 录制示教数据
-> replay 验证
-> 训练 ACT / SmolVLA 小策略
-> 真机评估
-> failure note
```

这个项目不以复现 `LingBot-VLA 4B` 为第一目标。`LingBot-VLA` 和同济子豪兄视频作为工程 walkthrough 与后续升级路线；第一阶段先跑通 LeRobot 生态内的最小真实闭环。

## 为什么现在做

- 它直接对应当前上位目标：`Robot Learning Full-Stack / policy runtime / data loop`。
- 它比纯仿真更早暴露机器人系统问题：端口、校准、摄像头、示教数据、动作噪声、失败模式。
- 它能把后续 `LingBot-VLA / OpenVLA / ACT / Diffusion Policy / policy runtime` 的概念放到真实硬件语境里。
- 它不要求一开始掌握完整机器人学、控制理论、VLA 训练系统；先跑通闭环，再反查知识缺口。

## 项目边界

### 第一阶段要做

- 买一套 `SO-ARM101 Pro leader/follower` 或等价套件。
- 使用现成 3D 打印骨架，不把 3D 打印机作为首闭环依赖。
- 完成一个桌面任务：`pick-and-place` 或 `push-to-zone`。
- 录制 30-50 条示教，训练一个小策略，做 10 次真机评估。
- 输出一份 `first_loop_report_v0.md`。

### 第一阶段不做

- 不做 `LingBot-VLA 4B` 全量后训练。
- 不买 Jetson / Orin / Thor / RealSense / 多摄高端设备作为首轮依赖。
- 不追求复杂任务，如衣物折叠、插接、装配、双臂协同。
- 不把 3D 打印、CAD、夹爪改型变成第一周主线。

## 算力平台演进

本项目后续的规模扩展采用 `dev -> Orin -> Thor` 的阶梯，不在第一阶段一次性买满。

| 阶段 | 平台 | 目标 |
|---|---|---|
| Stage 1 | Mac / dev1 / 云单卡 | 跑通 LeRobot 数据闭环、ACT/BC 训练、离线 eval、基础 latency 记录 |
| Stage 2 | Jetson Orin Nano / Orin NX / AGX Orin | 学 Jetson / ROS 2 / TensorRT / 相机接入，把轻量 policy 放到机器人旁边跑 |
| Stage 3 | Jetson AGX Thor | 承接本体侧 VLA / VLM / LLM runtime，多相机、多模型、低延迟 action loop |

采购原则：先让真实任务暴露瓶颈，再买对应平台。Orin 是后续本体 runtime 的低成本入口；Thor 是“大模型上机器人”阶段的高端平台，不是首闭环依赖。

## 成功标准

### 最低完成线

- 机械臂完成组装、端口识别、校准。
- 能遥操作 follower，并录制至少 10 条有效 episode。
- 能 replay 至少 1 条 episode。
- 能解释 LeRobot 数据里 `observation.images / observation.state / action / task` 的含义。
- 写出一次 failure note。

### 标准完成线

- 录制 30-50 条同一任务示教。
- 训练 `ACT` 或同类小策略。
- 真机评估 10 次，记录成功率与失败类型。
- 写出 `first_loop_report_v0.md`。

### 拉伸目标

- 做一次补数据迭代：根据失败类型新增 10-20 条示教。
- 对比 `before补数据 / after补数据` 的评估结果。
- 尝试 `SmolVLA` 或 LingBot-VLA open-loop schema mapping。

## 目录

- [[01_Project_Brief]]：项目定义、验收、风险
- [[02_Budget_And_BOM]]：3000 元以内项目本体预算与采购顺序
- [[03_2_to_4_Week_Roadmap]]：半个月到一个月执行路线
- [[04_Learning_Map]]：需要补哪些知识，哪些先不用学
- [[05_Experiment_Log]]：实验记录模板
- [[06_LingBot_VLA_Upgrade_Path]]：LingBot-VLA 后续升级路径
- [[07_Cloud_GPU_Strategy]]：云 GPU 预算、平台和阶段用卡策略
- [[08_Runtime_Inference_Support]]：推理优化 / runtime 支撑线，后续边做边微调
- [[09_Primary_Tutorial_Zihao_AI]]：第一阶段主教程入口，子豪兄 LeRobot / SO-ARM101 飞书目录
- [[10_Robotics_Video_Sidecar]]：低带宽机器人视频线，服务 SO-ARM101 / Modern Robotics 基础直觉
- [[lerobot_code_map]]：LeRobot 官方源码整体地图，串起 robot / teleop / record / replay / train / eval
- [[99_Resources]]：资料、视频、论文、仓库链接
