---
type: support_roadmap
time_window: 2026-06-01_to_2027-05-31
target_role: LLM / AI Infra Runtime Support -> Robot Runtime / VLA Runtime
current_role: DB / Storage Kernel Engineer
updated: 2026-06-01
linked_files:
  - "[[00_North_Star]]"
  - "[[02_Capability_Map]]"
  - "[[03_Annual_Plan_2026]]"
  - "[[05_Career_Strategy_2026_2030]]"
  - "[[07_One_Year_Interview_Roadmap_Embodied_AI_Software]]"
  - "[[09_One_Year_Robot_Learning_Full_Stack_Roadmap]]"
---

# Runtime Support Roadmap: LLM / AI Infra to Robot Runtime

> 2026-06-01 状态：本文件从“当前上位主线”降级为 `LLM / AI Infra / Runtime 支撑线`。当前权威路线见 [[09_One_Year_Robot_Learning_Full_Stack_Roadmap]]。

## 一句话定位

这条线回答的问题不是“如何转成纯 LLM Inference Infra 工程师”，而是：

```text
LLM / AI Infra / Runtime 能力
-> 支撑 VLA runtime / robot policy runtime / edge inference / 多机器人语言协作
```

## 支撑线价值

- Transformer 推理链路帮助理解 VLA / 多模态模型如何接入机器人系统。
- KV cache、prefill/decode、batching、latency 指标帮助分析 robot runtime 中的推理延迟和资源风险。
- ONNX / TensorRT / quantization / profiling 帮助未来端侧部署和 policy inference 优化。
- DB / 存储 / 系统工程经验可以迁移到 robot data loop、logging、replay、eval harness、observability 和 reliability。
- vLLM / TensorRT-LLM 代表真实推理工程能力：KV cache、batching、kernel/graph 优化、显存、吞吐、延迟和部署边界。它们后续必须学习，但学习入口应来自 VLA / robot runtime 的实际部署问题。

## 学习边界

- 不把 vLLM / SGLang / TensorRT-LLM 源码阅读作为独立上位主线，但要把它们作为 `VLA / robot policy runtime` 的核心工程能力逐步打磨。
- 不构建独立 `LLM inference mini-stack` 作为年度主作品。
- 不因为 LLM Infra 更熟悉就抢走 Robot Learning Full-Stack 主线。
- 需要时只取服务 VLA / policy runtime / edge inference 的最小知识。
- 推理优化采用项目牵引方式：先记录真实 robot policy/VLA runtime 的 latency、资源、接口和 failure，再决定是否补 batching、KV cache、quantization、ONNX/TensorRT 或 serving 细节。

## 支撑线材料节奏

| 时间 | 材料 | 只取什么 | 输出 |
|---|---|---|---|
| 2026-06 | nanoGPT | `training -> generate -> runtime` 主链路 | `nanoGPT 主链路总结 v0` |
| 2026-06 ~ 2026-07 | SO-ARM101 + LeRobot | policy inference 输入/输出、动作频率、日志、eval latency | `runtime_log_schema_v0`、`policy_runtime_interface_v0` |
| 2026-H2 | CS336 精选 | language model system map、training/inference 边界 | `CS336 支撑线 checklist` |
| 2026-H2 | vLLM / serving 精选 | prefill、decode、KV cache、PagedAttention、continuous batching、latency/throughput trade-off | `vllm_serving_note_v0`、`VLA/policy runtime latency note` |
| 2026-H2 | TensorRT-LLM / ONNX / TensorRT / quantization | engine build、graph/kernel optimization、模型导出、端侧/边缘部署、profiling | `tensorrt_llm_deploy_note_v0`、`edge inference support note` |
| 2027-H1 | VLA runtime papers | action interface、推理延迟、数据闭环 | `VLA -> policy runtime mapping` |

## 必须掌握的问题

- Transformer inference 和 training loop 的差异。
- Prefill / decode 的计算和显存特征。
- KV cache 为什么会影响长上下文和多模态推理。
- vLLM 为什么要做 PagedAttention / continuous batching，它解决的是吞吐、显存碎片还是并发调度问题。
- TensorRT-LLM / TensorRT 的核心价值在哪里：图优化、kernel fusion、低精度、engine build、部署约束。
- TTFT / TPOT / throughput / latency / tail latency 如何定义。
- ONNX Runtime / TensorRT / FP16 / INT8 在端侧部署中的位置。
- VLA / LLM 作为高层任务理解与规划模块时，如何与低层 policy runtime 分层。
- 高层慢推理和低层高频控制如何通过 timeout、fallback、watchdog 和 action boundary 接起来。

## 与机器人主线的接口

| 机器人问题 | Runtime 支撑 |
|---|---|
| VLA 推理太慢 | latency 指标、profiling、prefill/decode 分析 |
| policy 部署不稳定 | timeout、fallback、watchdog、action clipping |
| edge 设备资源有限 | ONNX / TensorRT / quantization awareness |
| 多机器人语言协作 | LLM task decomposition、communication protocol awareness |
| 数据闭环难复盘 | logging、replay、metrics、observability |

## 一句话回锚

> LLM / AI Infra 是机器人全栈中的语言智能与 runtime 支撑层；当前上位目标仍是 Robot Learning Full-Stack / 机器人全栈工程师 / roboticist。
