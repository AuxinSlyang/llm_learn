# Embodied AI Mini-Stack

## 定位

这个项目是面向 `具身智能软件工程师 / Physical AI Systems Engineer` 目标岗位的一年作品主线。

目标不是做一个炫技 demo，而是做出一条可解释、可运行、可评测、可复盘的机器人 AI 软件闭环：

```text
task config
-> simulation / real robot
-> perception / state
-> control or policy
-> data logging
-> training
-> runtime
-> evaluation
-> replay
-> failure analysis
```

## 对齐的 JD 能力

| JD 模块 | 本项目对应证据 |
|---|---|
| 算法产品化 | `policy_runner`、`policy_runtime`、接口边界、配置与版本管理 |
| 模型部署与优化 | ONNX / TensorRT / 量化 awareness、latency report、edge deployment notes |
| 数据闭环迭代 | trajectory schema、episode logger、dataset、metadata、eval harness、failure replay |
| 鲁棒性与可靠性 | timeout、watchdog、action clipping、fault injection、long-run eval |

## 目录规划

```text
embodied-ai-mini-stack/
├── README.md
├── architecture.md
├── jd-mapping.md
├── backlog.md
├── notes/
│   ├── data-schema.md
│   ├── runtime-latency.md
│   ├── sensor-fusion.md
│   └── robot-learning-reading.md
├── experiments/
│   └── README.md
└── reports/
    └── README.md
```

## 2026 年阶段目标

| 阶段 | 时间 | 目标 |
|---|---|---|
| Phase A | 2026-05 | LLM / nanoGPT 收口，明确 runtime 支撑线 |
| Phase B | 2026-06 ~ 2026-07 | Modern Robotics Ch.1-6 + MuJoCo step loop + episode logger |
| Phase C | 2026-08 | 控制闭环 + trajectory schema + RL/IL 概念地图 |
| Phase D | 2026-09 ~ 2026-10 | classic-control demo + Behavior Cloning train/eval |
| Phase E | 2026-11 | policy runtime + latency report + ONNX/TensorRT/量化 awareness |
| Phase F | 2026-12 | mini-stack README + sensor fusion note + JD mapping |

## 当前最低下一步

- [ ] 完成 `nanoGPT 第一轮总结`
- [ ] 完成 `makemore -> nanoGPT -> inference_runtime` 映射
- [ ] 写出 `architecture.md` v0：具身智能软件闭环总图
- [ ] 写出 `jd-mapping.md` v0：当前能力、缺口和项目证据
- [ ] 进入 Modern Robotics Ch.1-3 前，明确它们在机器人系统中的位置

## 不做什么

- 不在 2026 年直接追完整 VLA 训练。
- 不把项目做成普通后端数据平台。
- 不只写论文笔记，必须逐步落到可运行系统。
- 不在仿真和数据闭环跑通前上复杂真机。
- 不把多传感器融合扩展成完整 SLAM 主线。
