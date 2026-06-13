---
type: concept_note
title: CNN Primer
track: CV foundations / visual backbone
status: active
created: 2026-06-11
---

# CNN Primer

## One-sentence takeaway

CNN 是一种利用图像局部性和空间平移结构的神经网络：它用小卷积核在整张图上滑动，逐层把 raw pixels 变成 edges / textures / parts / objects 等层级视觉特征。

## 为什么先看 CNN

AlexNet、VGG、GoogLeNet、ResNet 都是 CNN family。先理解 CNN，后面读这些论文时就不会只记住模型名字，而能看懂它们分别改了什么：

```text
CNN 基础
-> AlexNet: deep CNN + ImageNet + GPU + ReLU
-> VGG: 更深、更规整的小卷积堆叠
-> Inception: 多尺度分支 + 计算效率
-> ResNet: residual connection 解决深层网络优化问题
-> ViT: 反过来问，能不能少用 CNN inductive bias，直接用 patch token + Transformer
```

## 核心概念

### 1. Local receptive field

图像相邻像素强相关。CNN 不让每个神经元看整张图，而是先看局部小窗口，例如 `3x3` 或 `5x5`。

```text
local patch -> convolution filter -> feature response
```

直觉：边缘、角点、纹理通常是局部模式。

### 2. Weight sharing

同一个卷积核会在整张图上滑动，共享一组参数。

这意味着模型学到的“边缘检测器”可以在左上角用，也可以在右下角用。

```text
same filter + many spatial positions -> feature map
```

### 3. Feature map

卷积核扫完整张图后，输出一张 feature map。不同卷积核学习不同模式：

- vertical edge
- horizontal edge
- texture
- color blob
- object part

### 4. Hierarchical features

浅层特征偏低级，深层特征偏语义：

```text
pixels
-> edges / colors
-> textures / corners
-> parts
-> object-level features
```

这就是 CNN backbone 的基本意义：把图像转成可供分类、检测、VLM、VLA 使用的视觉表示。

### 5. Pooling / downsampling

pooling 或 stride convolution 会降低空间分辨率，扩大感受野，并让表示对小位移更稳定。

代价是丢掉一部分精细空间信息。所以分类任务很合适，检测/分割/机器人操作有时需要保留更多空间细节。

## CNN 的 inductive bias

CNN 对图像做了几个强假设：

- `locality`: 近处像素关系更重要。
- `translation equivariance`: 同一个视觉模式可以出现在不同位置。
- `hierarchy`: 复杂对象可以由简单局部模式逐层组合。

这些假设让 CNN 在数据没那么夸张时也很好训练。ViT 的关键问题则是：如果减少这些图像专用假设，用 Transformer + 大数据能不能学出同样甚至更强的视觉表示？

## 和 robot observation 的连接

机器人相机输入本质是图像流：

```text
camera image
-> CNN / ViT visual encoder
-> visual feature / visual token
-> policy / VLA / planner
-> action
```

第一版 SO-ARM101 + LeRobot 可以先把 raw image 交给 policy。后续如果要解释失败、检测目标物体、做数据筛选或接 VLA，就需要理解 visual encoder 到底在做什么。

## 读完检查

- [ ] 我能解释卷积核为什么要滑动。
- [ ] 我能解释 weight sharing 为什么适合图像。
- [ ] 我能解释 feature map 是什么。
- [ ] 我能解释 CNN 为什么能做视觉 backbone。
- [ ] 我能解释 ViT 和 CNN 的核心差别：ViT 把图像切成 patch token，减少 CNN 的局部卷积假设，用 attention 建模 token 关系。
