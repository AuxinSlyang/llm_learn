---
type: support_checklist
paper: OpenVLA
track: VLA engineering / AI Infra support
status: queued
created: 2026-06-18
---

# OpenVLA Engineering Support Checklist

## Position

OpenVLA Section 4 暴露了一组 VLA 工程落地能力：

```text
AMP
FlashAttention
FSDP
Open X dataset training support
HuggingFace AutoModel integration
LoRA fine-tuning
quantized model inference
```

这些不是 OpenVLA 的核心模型创新，但它们决定一个 VLA 是否能训练、微调、部署、复现和接入 robot runtime。

## Priority

短期不要一次学完全部。按和 OpenVLA / robot runtime 的距离分层：

| 优先级 | Topic | 为什么学 | 读完要能回答 |
|---|---|---|---|
| P0 | LoRA fine-tuning | OpenVLA 直接用它降低新任务 fine-tuning 成本 | 为什么冻结 base model、只训练低秩 adapter 能省显存和参数？ |
| P0 | quantized model inference | OpenVLA 5.4 直接评估 int8/int4 对 VRAM、速度、success rate 的影响 | 为什么 int4 可能比 int8 更适合某些硬件？量化如何影响控制频率？ |
| P1 | FlashAttention | OpenVLA codebase 支持它，解释 attention IO bottleneck | 为什么 attention 加速不只是减少 FLOPs，还要减少 HBM IO？ |
| P1 | FSDP | OpenVLA 训练 7B VLA 需要多 GPU 显存管理 | FSDP shard 了什么？参数、梯度、optimizer state 如何省显存？ |
| P1 | AMP | 大模型训练/推理基础工程能力 | fp32/bf16/fp16 混合精度如何省显存和提速？有什么数值风险？ |
| P2 | HuggingFace AutoModel integration | 复用 HF 模型加载、权重、配置和 fine-tune 生态 | AutoModel 抽象解决什么工程问题？ |
| P2 | Open X dataset training support | VLA 数据闭环核心，但需要 OpenX/LeRobot 数据格式背景 | robot dataset schema、mixture weight、action space 标准化怎么组织？ |

## Suggested Order

```text
LoRA
-> quantized inference / QLoRA
-> FlashAttention
-> AMP
-> FSDP / ZeRO
-> HuggingFace AutoModel
-> Open X dataset pipeline
```

## OpenVLA Mapping

| OpenVLA 问题 | 工程支撑项 |
|---|---|
| 新机器人任务 fine-tune 太贵 | LoRA / QLoRA |
| 推理显存太大 | quantized inference |
| 推理频率太低 | quantization / FlashAttention / TensorRT-LLM / action chunking |
| 7B VLA 训练显存不够 | FSDP / AMP / FlashAttention |
| 模型生态复用 | HuggingFace AutoModel |
| robot data 组织复杂 | Open X dataset training support / LeRobot dataset schema |

## Section 5.3 Fine-Tuning Techniques

OpenVLA 5.3 比较的是：如果要把 7B VLA 迁移到新机器人/新任务，哪些参数需要训练，代价和性能怎么权衡。

| 方法 | 训练什么 | OpenVLA 结果直觉 | 后续学习重点 |
|---|---|---|---|
| Full FT | 全部参数 | 性能强，但显存和计算成本最高 | 作为上限基准理解 |
| Last layer only | 最后一层和 token embedding | 成本低，但性能明显差 | 为什么只改输出层不够适配视觉/动作域 |
| Frozen vision | 冻结 vision encoder，训练其他部分 | 表现差于 full FT | 为什么机器人控制需要视觉特征适配目标场景 |
| Sandwich | vision encoder + token embedding + last layer | 比 frozen vision 好，低于 full FT / LoRA | 哪些层最影响迁移 |
| LoRA | 在 linear layers 加低秩 adapter | 接近 full FT，只训练约 1.4% 参数 | PEFT 主线入口 |

OpenVLA 数字：

```text
Full FT: 69.7% success, 7188M train params, 163.3GB VRAM
LoRA rank=32: 68.2% success, 97.6M train params, 59.7GB VRAM
```

后续需要补：LoRA / QLoRA / PEFT 的最小原理和 PyTorch/HF 实操。

## Section 5.4 Quantized Inference Trade-Off

OpenVLA 5.4 比较的是：降低权重精度后，显存、推理频率和真实机器人成功率如何变化。

| Precision | VRAM | Success | 关键解释 |
|---|---:|---:|---|
| bf16 | 16.8GB | 71.3% | 默认高精度推理，显存高但稳定 |
| int8 | 10.2GB | 58.1% | 显存下降，但某些 GPU 上量化开销导致推理频率太低 |
| int4 | 7.0GB | 71.9% | 显存更低，memory transfer 减少带来更高吞吐，真实 rollout 接近 bf16 |

机器人 runtime 的关键 takeaway：

```text
offline token accuracy 不等于 robot success rate
precision / latency / control frequency 会共同决定 closed-loop behavior
```

后续需要补：bf16 / fp16 / int8 / int4、weight-only quantization、QLoRA、TensorRT-LLM / vLLM 的 serving trade-off。

## Read Boundaries

- 先理解概念和工程 trade-off，不读大段源码。
- 每个 topic 都要回接 `VLA / policy runtime / SO-ARM101`，不能变成纯 LLM Infra 支线。
- 只有当开始实际 fine-tune / deploy VLA 时，再进入实现细节。

## Output Standard

每个 topic 后续补笔记时至少回答：

- 它解决哪个资源瓶颈：显存、算力、通信、IO、数据格式、部署集成？
- 它作用在 training、fine-tuning、serving 还是 dataset pipeline？
- 它对 robot runtime 的风险是什么：latency、control frequency、accuracy、stability？
- OpenVLA 里对应章节或实验在哪里？
