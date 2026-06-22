---
type: video_plan
project: SO-ARM101 + LeRobot first loop
status: active
created: 2026-06-11
---

# Robotics Video Sidecar

## 定位

这是一条低带宽视频线，用来并发补机器人直觉，但不替代论文、笔记和硬件实操。

规则：

- 每天最多 20-30 分钟。
- 看完必须留下 3 行：`这节讲什么 / 和 SO-ARM101 有什么关系 / 下次要不要继续`。
- 不连续刷课；视频只服务当前项目里的一个接口问题。
- 周末工具到位后，硬件 bring-up 优先于视频。

## P0：当前项目直接相关

| Source | 用法 | 什么时候看 |
|---|---|---|
| 子豪兄 LeRobot / SO-ARM101 教程 | 主教程，指导采购、组装、端口、校准、teleop、record/train/eval | 工具到位前看装配前章节；工具到位后边做边看 |
| LingBot-VLA walkthrough | 后续 VLA upgrade path，不作为第一阶段训练目标 | SO-ARM101 首闭环跑通后再看 |

本地入口：

- `09_Primary_Tutorial_Zihao_AI.md`
- `99_Resources.md`

## P1：机器人基础直觉

| Source | 官方入口 | 先看什么 | 目标 |
|---|---|---|---|
| Modern Robotics | https://modernrobotics.northwestern.edu/ | Introduction / Foundations of Robot Motion / Degrees of Freedom | 建立 configuration、DOF、rigid-body motion 的语言 |
| Modern Robotics YouTube playlist | https://www.youtube.com/playlist?list=PLggLP4f-rq02vX0OQQ5vrCxbJrzamYDfx | 只看前几节短视频 | 不进入完整推导，先补机器人词汇 |
| Stanford CS223A | https://see.stanford.edu/Course/CS223A/33 | Lecture 1 / kinematics overview | 后续补 manipulator kinematics、DH、FK/IK |

## P2：后续控制和系统直觉

| Source | 官方入口 | 什么时候看 |
|---|---|---|
| MIT Underactuated Robotics | https://underactuated.csail.mit.edu/index.html | SO-ARM101 首闭环后，开始关心 dynamics/control/failure recovery 时 |
| MIT OCW Underactuated Robotics | https://ocw.mit.edu/courses/6-832-underactuated-robotics-spring-2022/ | 后续作为 control / dynamics 深水区，不进入 W24 |

## P3：日常消遣 / Robot Learning 旁听

| Source | 定位 | 使用边界 |
|---|---|---|
| CMU 16-831 机器人学习导论 | Robot Learning 概念旁听，作为长期兴趣材料 | 不占用 SO-ARM101 / LeRobot 主体学习时间；不进入 Weekly Top 3；只在碎片时间看，每次最多留 3 行 takeaway |

## W24 建议视频槽

| 日期 | 视频槽 | 输出 |
|---|---|---|
| 2026-06-11 | 子豪兄教程装配前章节 or Modern Robotics Introduction 10-20m | 3 行视频 takeaway |
| 2026-06-12 | Modern Robotics: Foundations / DOF 20m | 解释 configuration / DOF 和机械臂状态 |
| 2026-06-13 | 子豪兄教程里 `组装机械臂` / `查看端口` 章节 | 如果工具到位，直接转硬件 checklist |

## 当前不做

- 不开始完整 MIT Underactuated。
- 不完整刷 Stanford CS223A。
- 不用视频替代真实装配、校准、teleop 和 record。
