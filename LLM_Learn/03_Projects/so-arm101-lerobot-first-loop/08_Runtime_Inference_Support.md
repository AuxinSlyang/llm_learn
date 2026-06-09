---
type: support_note
project: SO-ARM101 + LeRobot 首闭环
track: runtime / inference optimization / VLA support
status: draft
---

# Runtime / Inference Engineering Support

## 当前定位

这条线是 `具身智能软件工程师` 能力的核心支撑线，不是可有可无的边角料。

但它在第一个小项目里的进入方式必须是项目牵引：先通过 `SO-ARM101 + LeRobot` 建立真实 robot runtime / policy runtime 问题，再逐步进入 vLLM、TensorRT-LLM、ONNX/TensorRT、quantization、profiling 等复杂系统。

第一个小项目主线仍然是：

```text
SO-ARM101 + LeRobot
-> teleop
-> dataset
-> train
-> eval
-> failure note
```

推理优化 / runtime 优化作为持续支撑线，后续边做边微调。它要回答的是：

```text
一个 policy / VLA / LLM 模型
如何稳定、低延迟、可观测地接入机器人系统
```

更具体地说，第一阶段不是要成为纯 LLM inference infra 工程师，而是要形成真实具身智能软件能力：

```text
robot data loop
+ policy runtime
+ model inference / serving awareness
+ latency / resource / failure analysis
```

## 算力平台阶梯

后续平台演进按项目规模逐步放大：

```text
Mac / dev1 / 云单卡
-> Jetson Orin
-> Jetson AGX Thor
```

| 阶段 | 平台 | 主要问题 | 不做什么 |
|---|---|---|---|
| Stage 1: dev loop | Mac / dev1 / 便宜云单卡 | LeRobot 数据闭环、训练、离线 eval、基础 runtime log | 不为首闭环采购 Jetson / Thor |
| Stage 2: edge robot runtime | Jetson Orin Nano / Orin NX / AGX Orin | ROS 2、相机、本体侧轻量 policy、TensorRT、低延迟动作循环 | 不强行在 Orin 上跑重 VLA/LLM |
| Stage 3: model-on-robot | Jetson AGX Thor | 本体侧 VLA / VLM / LLM、多相机、多模型、action chunk、fallback | 不把 Thor 当普通 LLM 训练机或高并发服务端 |

采购触发条件：

- `Orin`：当我们已经跑通 SO-ARM101 首闭环，并需要学习 Jetson / ROS 2 / TensorRT / 本体侧 policy runtime 时再买。
- `Thor`：当项目进入 `语言 + 图像/视频 + robot state -> VLA/VLM/LLM -> action`，并且 Orin 或普通 dev 机器的内存、延迟或多模态能力成为真实瓶颈时再买。

## 为什么要保留这条线

- VLA / LLM 推理可能慢，机器人 runtime 需要知道 latency、timeout、fallback。
- policy 推理不是单次函数调用，还涉及 observation preprocessing、action clipping、logging、replay。
- 后续如果上 LingBot-VLA / OpenVLA / SmolVLA，需要理解显存、batch、prefill/decode、KV cache、quantization、server-client 边界。
- 这条线和已有系统工程经验连接很强：日志、回放、延迟预算、资源隔离、failure analysis。
- vLLM / TensorRT-LLM 这类系统不是孤立学习目标；它们应该被放到 `VLA / robot policy runtime 怎么部署、怎么控延迟、怎么控资源、怎么可观测` 这个问题里学习。

## 第一阶段要建立什么

在 `SO-ARM101 + LeRobot` 首闭环阶段，不做复杂优化，但必须建立 runtime / inference 的问题框架。先记录这些事实：

- 每次 policy inference 的输入是什么：image、state、task。
- 输出 action 的 shape、频率、范围。
- 一次 eval episode 中，policy 调用多少次。
- 单次推理耗时是否影响动作频率。
- 失败是否来自模型输出、动作限幅、相机输入、校准、延迟或数据分布。

第一阶段不做的是：

- 不做复杂 serving benchmark。
- 不优化 4B VLA full inference。
- 不把 LLM inference 重新变成主线。

第一阶段要做的是：

- 建立 `runtime_log_schema_v0`。
- 建立 `policy_runtime_interface_v0`。
- 建立 `inference_resource_matrix_v0`。
- 建立 `vLLM / TensorRT-LLM / ONNX-TensorRT` 后续学习问题清单。

## 后续逐步打磨的核心思路

### Stage 0：记录

目标：先让 runtime 可观察。

要记录：

- observation timestamp
- preprocessing time
- policy inference time
- action postprocess time
- action send time
- success/failure label

输出：

- `runtime_log_schema_v0`
- `eval_latency_note_v0`

### Stage 1：接口

目标：把 policy 从脚本变成一个清楚的接口。

接口形状：

```text
obs: image/state/task
-> preprocess
-> policy.forward / policy.generate_action
-> action postprocess
-> send to robot
-> log
```

输出：

- `policy_runtime_interface_v0`

### Stage 2：资源

目标：理解不同模型跑在哪里。

分工：

- Mac：teleop、client、logger、dataset 检查、首轮真机 policy eval。
- dev1 / V100 / 便宜云单卡：ACT/BC 小模型训练、轻量 open-loop eval。
- Jetson Orin：后续本体侧轻量 policy runtime、ROS 2、相机、TensorRT、profiling。
- Jetson AGX Thor：后续重 VLA / VLM / LLM 本体侧 runtime，多相机、多模型、action loop。
- 云 A100/H100/96GB GPU：VLA 4B load / open-loop / tiny post-training feasibility。

输出：

- `inference_resource_matrix_v0`

### Stage 3：优化

目标：只优化真实卡住的点。

优化入口：

- batching / no batching
- FP16 / BF16 / INT8 awareness
- ONNX / TensorRT / torch.compile awareness
- image preprocessing pipeline
- action frequency / timeout / fallback

输出：

- `runtime_bottleneck_report`

### Stage 4：LLM/VLA Serving Systems

目标：进入真实推理系统能力，不停留在“知道名词”。

学习对象：

- vLLM：KV cache 管理、PagedAttention、continuous batching、throughput/latency trade-off。
- TensorRT-LLM：模型编译、kernel/fusion、FP16/INT8/FP8 awareness、engine build/deploy 边界。
- ONNX / TensorRT：端侧或边缘部署里的模型导出、图优化、算子支持、profiling。
- Serving metrics：TTFT、TPOT、tail latency、throughput、显存占用、batch size、并发数。

进入条件：

- 已经能跑通一个真实或模拟 policy eval loop。
- 已经知道 policy/VLA 在 robot loop 里的输入、输出和动作频率要求。
- 已经有 latency / failure log，而不是凭感觉优化。

输出：

- `vllm_serving_note_v0`
- `tensorrt_llm_deploy_note_v0`
- `vla_runtime_latency_report_v0`

## 和 LingBot-VLA 的连接

LingBot-VLA 阶段重点不只是“能不能跑模型”，而是：

- open-loop eval 如何读数据和输出 action。
- deployment server 如何接 robot process。
- action frequency 和 latency 是否适合真机。
- 如果模型太慢，是否需要 action chunk、缓存、降频或 fallback。
- 如果显存不够，是否需要量化、换 GPU 或只做 schema mapping。

## 当前项目原则

- 当前先把真实数据闭环跑通。
- 推理工程能力必须持续打磨，但每次进入都要被真实项目问题牵引。
- 每次新增 runtime 学习，都必须对应一个项目证据：日志字段、接口图、latency 表、资源矩阵或 blocker report。
