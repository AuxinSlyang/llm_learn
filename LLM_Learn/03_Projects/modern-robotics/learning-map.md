# Modern Robotics 学习地图（v0.1）

> 目标：把《Modern Robotics》变成“机器人系统最小闭环”里可调用的知识模块，而不是抽象读书笔记。

## 章节顺序（第一轮：Ch.1-6 优先）

- Ch.1：Introduction / 为什么需要统一语言
- Ch.2：Rigid Body Motions（SO(3)/SE(3) 直觉 + 表示）
- Ch.3：Forward Kinematics（从关节到末端位姿）
- Ch.4：Velocity Kinematics and Statics（Jacobian / wrench）
- Ch.5：Inverse Kinematics（求解策略 + 数值法直觉）
- Ch.6：Dynamics of Open Chains（动力学模型的“用途感”）

## 每章解决什么问题（写给“系统设计”）

- Ch.2 解决：坐标系/位姿/旋转怎么统一表示与组合（系统里：state / frames / calibration 的语言）
- Ch.3 解决：给定关节状态，末端/身体在空间中的位姿怎么得到（系统里：kinematics module）
- Ch.4 解决：速度关系与力的映射怎么写（系统里：control / estimation 的接口）
- Ch.5 解决：目标位姿怎么反推出关节（系统里：planning->control 的桥）
- Ch.6 解决：为什么控制需要动力学 awareness（系统里：torque/accel/constraints）

## 对“机器人系统最小闭环”的对应关系（v0.1）

- state / frames：Ch.2（SE(3) 表示、变换链）
- kinematics：Ch.3-5（FK/IK/Jacobian 作为 planning/control 的底层）
- control（先不深）：Ch.4-6（速度/力/动力学直觉先建立）
- planning / strategy：暂不在 MR 主线里（后续接入）

## 先学的 3 个概念（今晚必须写清）

1. `SE(3)` 是什么、为什么需要它（和机器人系统里“坐标/位姿”一一对应）
2. Jacobian 的直觉（速度映射、奇异性意味着什么）
3. IK 的数值求解套路（不是求闭式解，而是知道怎么迭代）

## 卡点问题（留作后续查证）

- 我现在对 SO(3)/SE(3) 的“最小可用直觉”是什么？
- 奇异性在系统层面如何表现（控制不稳定/不可达/对噪声敏感）？
- 在机器人系统里，哪些模块最先会真正用到 MR（locomotion / arm / vision-head）？

## 下一步（v0.2）

- 把 Ch.1-6 每章拆成一页 `notes/chXX.md`（先不要求完整推导，只写“系统视角”）
- 选 1 个最小例子（2D/3D 刚体 + FK），用 Python 做一次数值验证（后续在 dev1 做）
