# JD Mapping v0

## 目标 JD

目标岗位：`具身智能软件工程师 / Embodied AI Software Engineer`

岗位核心是把具身智能算法、模型和 policy 接入真实机器人系统，使其具备可部署、可评测、可回放、可持续迭代的工程形态。

## 能力映射

| JD 要求 | 当前状态 | 一年内项目证据 |
|---|---|---|
| C++ / Python / 软件架构 | DB / 存储工程背景较强；机器人项目代码待建立 | 清晰项目结构、接口边界、config、logging、README |
| 多进程 / 多线程 / 通信 / 时延 | 系统工程基础较强；ROS2 / DDS 待补 | ROS2 map、latency report、policy runtime |
| TensorRT / ONNX Runtime / 量化 | 目前 awareness 不足 | ONNX export + latency measurement；TensorRT / FP16 / INT8 笔记或最小验证 |
| DL / CV / LLM 原理 | micrograd / makemore / nanoGPT 进行中；CV 待补 | nanoGPT 总结、CS231n/CV 入口、VLA awareness |
| 传感器物理特性 / 失效模式 | 待补 | sensor_fusion_note v0、camera frame + qpos/qvel 同步记录 |
| 多传感器融合 | 待补 | time sync / frame / calibration / noise / missing data 笔记 |
| 机器人运动学 / 动力学 | 待补 | Modern Robotics Ch.1-6 + 控制入口笔记 |
| 算法产品化 | 待通过项目建立证据 | policy_runner、policy_runtime、fallback、version/config |
| 数据闭环 | DB / 存储背景有迁移优势；机器人语义待补 | trajectory schema、episode logger、dataset、eval harness、replay |
| 鲁棒性与可靠性 | 系统可靠性意识较强；机器人 failure mode 待补 | fault injection、timeout、action clipping、failure taxonomy |

## 2027-05 面试合格线

- 能讲清一个端到端 mini-stack。
- 能把项目映射到 JD 四块：算法产品化、模型部署优化、数据闭环、鲁棒性可靠性。
- 能回答 Robot Learning 基本问题：BC、DAgger、covariate shift、observation/action、eval。
- 能解释 runtime latency、TensorRT / 量化 awareness 和 fallback。
- 能承认短板：真机经验不足、复杂控制不足、完整 VLA 训练不足。

## 简历表达草案

> Embodied AI Mini-Stack: built a MuJoCo/LeRobot-based robot learning software stack covering task configuration, control/policy loop, trajectory logging, BC training/evaluation, replay, failure analysis, latency measurement, and fault handling. The project maps DB/storage systems experience to robot data lifecycle and policy runtime reliability.
