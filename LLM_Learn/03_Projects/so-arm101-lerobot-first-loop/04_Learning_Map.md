---
type: learning_map
project: SO-ARM101 + LeRobot 首闭环
status: draft
---

# Learning Map

## 项目最小知识图

```text
robot hardware
  -> ports / motors / calibration / safety

teleoperation
  -> leader-follower / action recording

dataset
  -> observation / state / action / task / episode

policy
  -> imitation learning / ACT / action chunk

eval
  -> success rate / failure taxonomy /补数据

runtime
  -> latency / camera stability / action frequency / watchdog
```

## 先学什么

### 1. LeRobot 基本工作流

问题：

- 怎么找端口？
- 怎么校准？
- 怎么 record / replay？
- dataset 存在哪里？
- 如何从 dataset 进入 train？

输出：

- 能画出 `record -> dataset -> train -> eval`。

### 2. SO-ARM101 硬件直觉

问题：

- leader 和 follower 分别是什么？
- 电机 ID 为什么重要？
- 关节状态和动作维度怎么对应？
- 为什么电源、线材、固定会影响学习结果？

输出：

- 能写出一页硬件 bring-up checklist。

### 3. Imitation Learning 最小直觉

问题：

- behavior cloning 是什么？
- ACT 为什么预测 action chunk？
- 为什么示教数据分布很重要？
- policy 为什么会在分布外失败？

输出：

- 能用自己的任务解释 `observation -> action`。

### 4. Evaluation 和 Failure Analysis

问题：

- 什么叫成功？
- 失败类型有哪些？
- 补数据应该补什么？
- 成功率低时先怀疑硬件、数据还是模型？

输出：

- 10 次 eval 表 + failure taxonomy。

## 暂时不用完整学

- 完整刚体运动学证明
- ROS2 全套
- VLA 4B 训练系统
- Isaac Lab 高保真仿真
- Diffusion Policy 公式细节
- LingBot-VLA depth distillation

这些可以在首闭环后补。

## 推荐阅读顺序

1. LeRobot SO-101 assemble / getting started
2. LeRobot imitation learning on real robots
3. ACT 概念和 LeRobot 示例
4. 同济子豪兄 `LeRobot + LingBot-VLA` 视频
5. LingBot-VLA 技术报告 first scan
6. LingBot-VLA repo walkthrough

## 和长期路线的连接

| 首闭环模块 | 长期能力 |
|---|---|
| 端口 / 校准 / 电机 | 机器人本体与硬件 bring-up |
| 示教数据 | robot data loop |
| ACT 训练 | robot learning / imitation learning |
| 真机 eval | evaluation harness |
| failure taxonomy | deployment robustness |
| LingBot-VLA schema mapping | VLA / policy runtime |

