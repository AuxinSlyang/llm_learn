---
type: upgrade_path
project: SO-ARM101 + LeRobot 首闭环
target: LingBot-VLA / VLA runtime
status: draft
---

# LingBot-VLA Upgrade Path

## 当前定位

`LingBot-VLA` 是本项目的后续升级目标，不是第一闭环的第一训练目标。

第一阶段先用 LeRobot + ACT / 小策略跑通：

```text
real robot -> dataset -> train -> eval -> failure analysis
```

之后再接：

```text
VLA model -> post-training -> open-loop eval -> deployment
```

## 为什么不第一天跑 LingBot-VLA 4B

- 模型是 4B 级别，环境和显存要求高。
- README 要求 Python 3.12、PyTorch 2.8、CUDA 12.8。
- GM-100 数据集很大，不能作为首轮下载目标。
- post-training 配置默认面向多 GPU / FSDP2。
- 如果没有先跑通数据和评估，直接上 VLA 会不知道失败来自哪里。

## 当前资源策略

本项目当前可用资源假设：

- 本地 Mac：适合做文档、数据整理、LeRobot 客户端、teleop、日志、回放、轻量脚本，不作为 LingBot-VLA 4B 推理主力。
- 单张 V100：适合做 ACT / 小模型训练、LeRobot 数据检查、轻量 open-loop 实验；不作为 LingBot-VLA 4B 全量 post-training 依赖。
- 多卡资源：只有进入 LingBot-VLA 4B full post-training 时才需要争取，不能作为第一个月项目的前置条件。

执行规则：

- 第一个月不要求 LingBot-VLA 4B 微调成功。
- 第一个月优先完成 `ACT / BC -> real eval -> failure analysis`。
- LingBot-VLA 阶段的可接受产出包括：schema mapping、open-loop eval 尝试、资源需求报告、blocker list。
- 如果尝试 LingBot-VLA 推理，优先放在远端 CUDA GPU；Mac 只跑 websocket client / robot process / logger。

## 巧客具身 LingBot-VLA 教程定位

资源：`https://ldgl0ghbka.feishu.cn/wiki/MZNSwUT88i8ijokrEMPcgYF5nIb`

该教程和本项目同类，但阶段更后置。它覆盖：

```text
LeRobot 数据采集
-> LeRobot v2.1 / v3.0 数据格式转换
-> robot config / VLA train config
-> norm stats
-> LingBot-VLA 后训练
-> open-loop eval
-> 云端推理 server + 本地 robot WebSocket client
-> 真机部署
```

和当前第一阶段的关系：

- 可复用：数据 schema、robot config、norm stats、open-loop eval、WebSocket server/client 部署结构。
- 暂不直接执行：4B VLA post-training、三路相机、双臂平台、云端训练和真机 VLA 部署。
- 当前正确位置：ACT / LeRobot 首闭环跑通后，作为 `Stage A/B/C` 的 walkthrough 和 checklist。

## 第一阶段与 LingBot-VLA 的连接点

| 首闭环产物 | LingBot-VLA 对应点 |
|---|---|
| LeRobot dataset | VLA data config / feature mapping |
| observation.images | multi-view image tokens |
| observation.state | proprioceptive state |
| action | action expert / action chunk |
| norm stats | normalization config |
| eval table | open-loop / real-robot eval |
| failure taxonomy | post-training data selection |

## 第一次 LingBot-VLA walkthrough

只读这些入口：

- `README.md`
- `configs/vla/robotwin_load20000h.yaml`
- `configs/robot_configs/robotwin.yaml`
- `scripts/open_loop_eval.py`
- `deploy/lingbot_vla_policy.py`
- `lingbotvla/data/vla_data/README.md`

回答 8 个问题：

- 它的 observation 是什么？
- 它的 action 是什么？
- 它如何定义 robot config？
- 它如何做 normalization？
- post-training 入口在哪里？
- open-loop eval 如何跑？
- deployment server 怎么接 action？
- 哪些地方和我们自己的 SO-ARM101 dataset 不一致？

## 升级阶段

### Stage A：Schema Mapping

目标：把自己的 LeRobot dataset 映射到 LingBot-VLA 期望的数据配置。

输出：

- `notes/lingbot_schema_mapping.md`

### Stage B：Open-Loop Eval

目标：尝试用已有 checkpoint 或小数据做 open-loop eval。

输出：

- `experiments/E006_lingbot_open_loop_eval.md`

### Stage C：Tiny Post-Training Feasibility

目标：不是训练成功，而是确认最小 post-training 是否能启动。

输出：

- 环境报告
- 资源需求
- blocker list

### Stage D：Real Deployment

目标：只有在前面三步可控后再考虑。

输出：

- 真机推理记录
- latency / action frequency / failure note

## 进入 LingBot-VLA 的前置条件

- 已完成一次 ACT 首闭环。
- 知道自己的 dataset schema。
- 有明确 eval 任务。
- 有远端 GPU 或可用训练资源。
- 能接受 VLA 阶段先产出 blocker report，而不是立刻成功。
