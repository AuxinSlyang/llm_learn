---
type: reading_map
track: AI Infra / distributed training
status: queued
created: 2026-06-14
---

# Distributed Training / Parallelism Reading Map

## Why This Matters

This is an AI Infra support line for LLM / VLM / VLA systems. It should help explain why large models require data/model/tensor/pipeline parallelism, how gradients and optimizer state are synchronized or sharded, and why training infrastructure becomes part of the model story.

This should not interrupt the current CV foundation sprint. Read it after AlexNet / ResNet / ViT have built enough visual-backbone context.

## Concept Ladder

```text
data parallelism:
  each GPU has a full copy of the model
  each GPU sees a different batch shard
  gradients are synchronized, often by all-reduce

model parallelism:
  the model itself is split across GPUs
  useful when one GPU cannot fit all parameters / activations

tensor parallelism:
  split large matrix operations or attention / MLP dimensions across GPUs
  common in large Transformer training

pipeline parallelism:
  split layers into stages across GPUs
  send microbatches through the pipeline

ZeRO / FSDP:
  shard optimizer states, gradients, and/or parameters
  reduce memory redundancy in data-parallel training
```

## Reading Order

0. AlexNet Section 3.2 - historical two-GPU model split.
1. Large-scale Deep Unsupervised Learning using Graphics Processors - historical GPU scaling.
2. Flexible, High Performance Convolutional Neural Networks for Image Classification - early GPU CNN context.
3. Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism - tensor/model parallelism for Transformers.
4. GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism - pipeline parallelism and microbatching.
5. ZeRO: Memory Optimizations Toward Training Trillion Parameter Models - optimizer/gradient/parameter memory sharding.
6. Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM - composing tensor, pipeline, and data parallelism at cluster scale.

## Optional Later

- Mesh-TensorFlow / GShard: sharded tensor computation and large sparse Transformer systems.
- PipeDream: pipeline-parallel training schedule tradeoffs.
- Alpa: automatic parallelization strategy search.
- DeepSpeed / FSDP docs: implementation-facing follow-up after the paper concepts are clear.

## First-Pass Questions

- What exactly is replicated?
- What exactly is sharded?
- What communication happens during forward, backward, and optimizer step?
- Is the bottleneck memory, compute, communication, or pipeline bubble?
- How does this map to a future robot/VLA training or fine-tuning workload?
