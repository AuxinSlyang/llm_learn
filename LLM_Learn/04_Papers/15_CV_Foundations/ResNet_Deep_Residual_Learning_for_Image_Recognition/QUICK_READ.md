---
type: paper_note
title: Deep Residual Learning for Image Recognition
short_name: ResNet
arxiv_id: "1512.03385"
url: https://arxiv.org/abs/1512.03385
pdf_url: https://arxiv.org/pdf/1512.03385
local_pdf: ./ResNet_Deep_Residual_Learning_for_Image_Recognition.pdf
track: CV foundation
read_mode: Structured Read
status: guided_read_done
created: 2026-06-09
completed: 2026-06-15
---

# ResNet - QUICK READ

## Position

ResNet 是 VGG 之后的关键一步：VGG 说明 `depth matters`，ResNet 解决“深度继续增加以后怎么还能训得动”的优化问题。它也是 CNN backbone 的核心基础之一，CLIP 论文里 image encoder 就可以使用 ResNet 变体。

## Core Question

为什么网络变深后，训练误差反而可能变差？如何让很深的网络更容易优化？

这篇文章的真正问题不是“更深一定更好”，而是：

```text
如果一个深层网络理论上至少可以复制浅层网络，
为什么实际训练时更深的 plain net 反而训练误差更高？
```

作者把这个现象叫做 `degradation problem`。它不是普通 overfitting，因为不是 test error 单独变差，而是 training error 也变差。

## Key Idea

残差连接：

```text
y = F(x) + x
```

模型不必直接学习完整映射 `H(x)`，可以学习残差 `F(x) = H(x) - x`。如果某层不需要改变表示，残差分支可以接近 0，identity path 保留信息。

等价理解：

```text
plain block:    x -> H(x)
residual block: x -> x + F(x)
```

如果最优操作接近“不改动输入”，plain block 需要一堆 conv + ReLU 学出 identity；ResNet 只需要让 residual branch 学到接近 0，shortcut 直接把 `x` 传过去。

这不是严格理论证明，而是一个 optimization reformulation / preconditioning：把“学完整函数”改成“在 identity 附近学一个 delta”。

## Method

### Residual Block

普通 ResNet-18/34 block 是两层 `3x3 conv`：

```text
x -> 3x3 conv -> ReLU -> 3x3 conv -> + x -> ReLU
```

如果 feature map 尺寸和 channel 数相同，shortcut 直接是 identity，不引入参数。

如果维度不一致，例如 spatial size 减半或 channel 增加，论文讨论三种做法：

- `A`: identity shortcut + zero padding，完全无额外参数。
- `B`: 只在维度变化处用 `1x1 projection`。
- `C`: 所有 shortcut 都用 projection。

实验结论：A/B/C 都明显好于 plain net；projection 不是解决 degradation 的本质，identity shortcut 才是关键。

### Bottleneck Block

ResNet-50/101/152 使用 bottleneck：

```text
1x1 conv reduce -> 3x3 conv -> 1x1 conv restore
```

核心目的是控制计算量。`1x1` 先降维，让中间的 `3x3` 在更小 channel 上计算，然后再升回高维。这样 152 层 ResNet 仍然比 VGG-16/19 计算量更低。

## Experiments

### ImageNet: Plain Net vs ResNet

最关键的对照是 18-layer 和 34-layer：

| Model | Top-1 error |
| --- | ---: |
| plain-18 | 27.94 |
| plain-34 | 28.54 |
| ResNet-18 | 27.88 |
| ResNet-34 | 25.03 |

解读：

- plain net 直接加深到 34 层反而更差，并且训练误差也更高。
- ResNet 加到 34 层后明显更好，说明 residual connection 解决了主要优化障碍。
- 18 层时 plain/residual 接近，说明浅一点的时候 SGD 还能训；深了以后 residual 的价值变大。

### Deeper ResNet

ImageNet 10-crop validation：

| Model | Top-1 error | Top-5 error |
| --- | ---: | ---: |
| ResNet-34 B | 24.52 | 7.46 |
| ResNet-50 | 22.85 | 6.71 |
| ResNet-101 | 21.75 | 6.05 |
| ResNet-152 | 21.43 | 5.71 |

Single-model multi-scale validation：

| Model | Top-1 error | Top-5 error |
| --- | ---: | ---: |
| ResNet-50 | 20.74 | 5.25 |
| ResNet-101 | 19.87 | 4.60 |
| ResNet-152 | 19.38 | 4.49 |

Ensemble 在 ImageNet test 上 top-5 error 达到 `3.57%`，拿到 ILSVRC 2015 classification 第一。

### CIFAR-10

CIFAR 实验说明这个现象不只是 ImageNet 特例：

- plain nets 继续加深也出现 training error 变高。
- ResNet-20/32/44/56/110 随深度增加整体受益。
- ResNet-1202 能优化到极低训练误差，但 test error 比 ResNet-110 差，作者认为是 small dataset 上 overfitting。

这点很重要：ResNet 让很深网络更可优化，但不等于“无限堆深永远更好”。

### Transfer To Detection

论文还把 ResNet-101 放进 Faster R-CNN，对比 VGG-16：

- PASCAL VOC 2007 mAP: `73.2 -> 76.4`
- PASCAL VOC 2012 mAP: `70.4 -> 73.8`
- COCO mAP@[.5, .95]: `21.2 -> 27.2`

作者强调实现基本相同，主要增益来自更好的 learned representations。这也是为什么 ResNet 会变成后续 detection / segmentation / robot perception 的常用 backbone。

## Why For VLM/VLA

ResNet 帮助理解 CNN vision encoder 如何稳定训练成深层特征提取器。对 CLIP 来说：

```text
image -> ResNet -> image feature -> projection -> image embedding
```

对机器人/VLA方向，ResNet 的价值不是“今天还一定要用 ResNet”，而是理解 backbone 设计里的几个基本问题：

- 视觉 encoder 如何从 local feature 逐层形成高级语义。
- 为什么深层网络需要更好的 optimization path。
- 为什么 skip/shortcut/residual 这种结构后来在 CNN、Transformer、diffusion、policy network 里都反复出现。
- ViT 把图像转成 patch tokens，但深层表示、信息流、可优化性这些问题仍然存在。

## 2026-06-15 Half-Hour Quick Read

### Minimum Output

- `degradation problem`: 网络变深后，不只是泛化变差，而是训练误差也可能变高，说明 plain deep net 的优化变难。
- `F(x) + x`: shortcut 提供 identity path，让 block 只学习相对于输入的 residual/delta；如果不需要改变表示，residual branch 接近 0 即可。
- `ResNet vs ViT`: ResNet 仍是 CNN 层级局部特征范式，ViT 是 patch token + self-attention 范式；二者都要处理深层表示的信息流和优化问题。

### One-Sentence Takeaway

ResNet 的历史意义是把 VGG 的“深度有用”推进到“深度可以继续扩展并稳定优化”：用 identity shortcut 让新增层学习 residual，而不是强迫一串非线性层从零学习完整映射。

## 2026-06-15 Guided Read Recap

### Introduction

Introduction 的论证链非常完整：

```text
VGG / Inception 等工作说明 depth matters
-> 直接堆更深 plain network 不一定更好
-> 旧问题 vanishing / exploding gradients 已被 initialization / BN 部分缓解
-> 新问题是 degradation problem：更深 plain net 的 training error 也变高
-> 理论上深网可以复制浅网并让新增层做 identity
-> 如果实际更差，说明不是表达能力问题，而是 optimization / learnability 问题
-> residual learning 让 identity 解更容易被 SGD 找到
```

这里的关键理解是：

```text
existence != learnability
```

一个好解在数学上存在，不代表 plain deep net 的优化器容易找到它。

### Identity / Residual / Shortcut

`identity` 在 ResNet 里不是一种图像特征，而是固定映射：

```text
I(x) = x
```

其中 `x` 是当前 block 的 feature representation / feature map，不一定是原始图片。identity shortcut 的意义是让已有 feature 原样通过。

`residual` 是相对当前输入还需要补上的差值：

```text
F(x) = H(x) - x
H(x) = x + F(x)
```

所以一个 ResNet block 可以直接理解为：

```text
ResNet block = x + CNN_block(x)
```

更严格地说：

```text
y = F(x, {W_i}) + x
```

其中 `F(x, {W_i})` 是可训练的 residual branch，`x` 是 parameter-free / always-open identity shortcut。

### Why It Helps

plain deep net 的新增层如果想“不做事”，需要一串 `conv + BN + ReLU` 学出：

```text
H(x) = x
```

这理论上可表达，但训练上不一定容易。

ResNet 里新增层如果没用，只需：

```text
F(x) = 0
y = x
```

所以 ResNet 的核心不是增加表达能力，而是让“新增层至少不伤害已有 representation”更容易。

可以把深层 ResNet 看成：

```text
x_{l+1} = x_l + F_l(x_l)
```

也就是从 layer-by-layer rewriting 变成 identity-centered iterative refinement。

### Section 3 Core

Section 3 的骨架：

- `3.1 Residual Learning`：如果能学 `H(x)`，也能学 `H(x)-x`；二者表达能力相近，但 ease of learning 不同。
- `3.2 Identity Mapping by Shortcuts`：用 `y = F(x, {W_i}) + x` 实现 residual block；shortcut 不增加参数和主要计算量。
- `3.3 Network Architectures`：用 VGG-style `3x3 conv` plain net 做 baseline，再插入 shortcuts 得到 residual net。
- `3.4 Implementation`：ImageNet 训练细节沿用 AlexNet/VGG 范式，使用 BN、SGD、scale augmentation、crop / flip。

Figure 3 的读法：

```text
VGG-19: reference
34-layer plain: 直接堆深的 baseline
34-layer residual: 同一个 plain baseline + shortcuts
```

ResNet 不是重建一个完全不同的网络，而是在 plain CNN 上系统性加入 residual shortcut。

### Shortcut Options

维度一致时：

```text
y = F(x) + x
```

维度不一致时，论文比较三种 shortcut：

- `A`: identity shortcut + zero padding。最省、无参数，但新增 channel 没有 shortcut 信息。
- `B`: 只在维度变化处用 `1x1 projection`。实用选择，ResNet-50/101/152 采用。
- `C`: 所有 shortcut 都用 projection。参数更多，效果只略好。

结论：

```text
identity / residual mechanism 是关键；
projection 主要用于 shape matching，不是 degradation problem 的本质解法。
```

### Section 4 Core Evidence

实验主要证明四件事：

- plain network 直接加深会出现 degradation problem。
- ResNet 避免 degradation：ResNet-34 优于 plain-34，也优于 ResNet-18。
- ResNet 在 ImageNet 上能继续扩展到 50/101/152 层并持续受益。
- ResNet-101 替换 Faster R-CNN 的 VGG-16 backbone 后，detection 也提升，说明它学到的是更强 visual representation。

最终 takeaway：

```text
ResNet 让 depth 从“有用但难训”变成“可以大规模稳定扩展”。
```

## Follow-Up

后续精读如果需要，只需要补两件事：

- 手画一次 `ResNet-34` 和 `ResNet-50 bottleneck` 的 tensor shape。
- 对照 PyTorch/timm/LeRobot 里的 ResNet 或视觉 encoder 实现，看 residual block 在代码里如何落地。
