# 机器人系统最小闭环拆解（v0）

> 目标：用最少的结构把“机器人系统最小闭环是什么”说清楚，并且能映射到后续学习顺序（Modern Robotics / 控制 / ROS2 / 仿真 / 感知 / 多机器人协作）。

## 1. 系统边界（先定范围）

- 场景：通用机器人系统（短期先做单机闭环；中长期扩展到多机器人协作）
- 最小闭环：能在场上自主移动、感知球与门、做基础决策、执行控制，并持续记录可复盘数据

## 2. 单机器人闭环（最小）

用一条数据流先把模块关系钉死：

`Sense -> State (Estimation) -> Decision/Plan -> Control -> Act -> Log`

- Sense（传感器）：camera / IMU / joint encoders / (optional) lidar
- State（状态估计）：机器人位姿、速度、球的位置与速度、对手/队友相对位置（从 observation 到 state）
- Decision/Plan（决策/规划）：角色（进攻/防守/守门）、目标点、路径/速度指令、踢球时机
- Control（控制）：将高层目标转成可执行控制量（关节/速度/力矩/步态）
- Act（执行）：电机/步态/踢球机构
- Log（日志）：用于 replay、debug、训练与评估的统一记录（时间戳、frame、state、action、reward/metrics、事件）

## 3. 多机器人系统增量（在单机闭环之上加什么）

`Comm -> Roles -> Coordination -> Team Eval`

- Comm（通信）：状态广播、意图/角色同步、时钟/时间戳对齐（哪怕先做最弱一致）
- Roles（角色分工）：前锋/后卫/守门；角色切换条件（球权、距离、视野置信度）
- Coordination（协作）：避免冲突、传球/掩护、区域覆盖（先定义规则，再考虑学习）
- Team Eval（队级评估）：控球率、射门次数、进球、失误类型统计、协作效率

## 4. 本周要补的 3 个知识缺口（先列出来）

- 缺口 1：
- 缺口 2：
- 缺口 3：

## 5. 未来实验入口（只写入口，不展开）

- 仿真：MuJoCo step loop -> 读写 state/action -> episode logger
- 控制：先 joint PD / 速度控制闭环，再谈复杂步态/轨迹
- 感知：先 ball detection / localization 的最小 pipeline（可从 OpenCV 起步）
- 多机器人：先“通信+规则协作”做 baseline，再逐步引入学习方法
