---
type: project_brief
project: SO-ARM101 + LeRobot 首闭环
status: planning
---

# Project Brief

## 项目目标

在 `15-30 天` 内，用 3000 元以内的机器人本体预算，跑通第一个真实 robot learning 闭环：

```text
组装 -> 校准 -> 遥操作 -> 数据采集 -> replay -> 训练 -> 真机评估 -> 失败分析
```

这个项目的价值不在于做出炫技 demo，而在于第一次完整理解机器人学习系统如何从数据进入 policy，再回到真实硬件评估。

## 任务选择

首选任务：`桌面 pick-and-place`

- 物体：小方块、瓶盖、积木、轻量 3D 打印件
- 起点：桌面 A 区
- 终点：桌面 B 区
- 评价：是否在限定时间内把物体移动到 B 区

备选降级任务：`push-to-zone`

- 不要求夹取，只要求把物体推到目标区域。
- 如果夹爪、抓取稳定性或示教质量卡住，先用该任务保住第一闭环。

## 主链路

```text
hardware:
  SO-ARM101 leader/follower + USB camera + desktop task setup

teleoperation:
  leader arm -> follower arm

data:
  LeRobot dataset
  observation.images + observation.state + action + task

policy:
  ACT first
  SmolVLA / LingBot-VLA later

eval:
  10 real episodes
  success rate + failure taxonomy
```

## 验收证据

- 一段真机执行视频
- 一份 LeRobot dataset 结构截图或说明
- 一次训练命令和训练日志
- 一张评估表
- 一份 `first_loop_report_v0.md`

## 风险

| 风险 | 表现 | 降级方式 |
|---|---|---|
| 硬件到货慢 | 无法按周启动 | 先做 LeRobot / LingBot-VLA repo walkthrough |
| 组装和校准卡住 | 端口、电机 ID、方向不对 | 先只完成 teleoperate + replay |
| 抓取不稳定 | 夹不住、夹偏、物体滑动 | 降级到 push-to-zone |
| 训练资源不足 | 本地训练慢或显存不足 | 减少 episode / 降低模型 / 用远端 GPU |
| 数据质量差 | policy 不收敛 | 做 failure taxonomy，再补 10-20 条示教 |
| VLA 模型太重 | LingBot-VLA 跑不动 | 第一阶段只跑 ACT，把 VLA 放到升级路径 |

## 第一阶段不需要完整掌握的知识

- 不需要先完整学完 Modern Robotics。
- 不需要先会 ROS2。
- 不需要理解所有 imitation learning 论文。
- 不需要掌握 VLA 4B 训练系统。
- 不需要自己设计机械臂。

第一阶段只需要知道：

- 机械臂如何接入电脑。
- 示教数据如何记录。
- policy 输入输出是什么。
- eval 为什么会失败。
- 下一轮如何补数据。

