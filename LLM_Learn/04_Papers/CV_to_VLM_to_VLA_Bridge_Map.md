---
type: reading_map
track: CV foundation -> VLM -> VLA -> robot learning
status: active
created: 2026-06-16
linked_project: [[so-arm101-lerobot-first-loop]]
---

# CV to VLM to VLA Bridge Map

## 为什么建这条线

这条线不是为了继续扩论文数量，而是把已经看过或正在看的材料压成一条主干：

```text
image classification
-> visual backbone
-> visual tokens
-> image-text alignment
-> image-to-LLM connector
-> visual instruction following
-> robot imitation learning
-> vision-language-action policy
```

当前目标是服务 `SO-ARM101 + LeRobot`：理解 camera image、language instruction、robot state、action、dataset、policy runtime 之间的接口关系。

## 总链路

```text
LeNet
-> AlexNet
-> VGG
-> ResNet
-> ViT
-> CLIP
-> BLIP-2
-> LLaVA
-> ALOHA / ACT
-> RT-2
-> OpenVLA / pi0
-> LeRobot / SO-ARM101
```

## 本地材料索引

| 顺序 | 材料 | 本地 PDF | QUICK_READ |
|---|---|---|---|
| 1 | LeNet-5 | `15_CV_Foundations/LeNet5_Gradient_Based_Learning_Applied_to_Document_Recognition/LeNet5_Gradient_Based_Learning_Applied_to_Document_Recognition.pdf` | `15_CV_Foundations/LeNet5_Gradient_Based_Learning_Applied_to_Document_Recognition/QUICK_READ.md` |
| 2 | AlexNet | `15_CV_Foundations/AlexNet_ImageNet_Classification_with_Deep_CNNs/AlexNet_ImageNet_Classification_with_Deep_CNNs.pdf` | `15_CV_Foundations/AlexNet_ImageNet_Classification_with_Deep_CNNs/QUICK_READ.md` |
| 3 | VGG | `15_CV_Foundations/VGG_Very_Deep_Convolutional_Networks/VGG_Very_Deep_Convolutional_Networks.pdf` | `15_CV_Foundations/VGG_Very_Deep_Convolutional_Networks/QUICK_READ.md` |
| 4 | ResNet | `15_CV_Foundations/ResNet_Deep_Residual_Learning_for_Image_Recognition/ResNet_Deep_Residual_Learning_for_Image_Recognition.pdf` | `15_CV_Foundations/ResNet_Deep_Residual_Learning_for_Image_Recognition/QUICK_READ.md` |
| 5 | ViT | `15_CV_Foundations/ViT_An_Image_is_Worth_16x16_Words/ViT_An_Image_is_Worth_16x16_Words.pdf` | `15_CV_Foundations/ViT_An_Image_is_Worth_16x16_Words/QUICK_READ.md` |
| 6 | CLIP | `30_VLA_and_Foundation_Policies/CLIP_Learning_Transferable_Visual_Models_From_Natural_Language_Supervision/CLIP_Learning_Transferable_Visual_Models_From_Natural_Language_Supervision.pdf` | `30_VLA_and_Foundation_Policies/CLIP_Learning_Transferable_Visual_Models_From_Natural_Language_Supervision/QUICK_READ.md` |
| 7 | BLIP-2 | `30_VLA_and_Foundation_Policies/BLIP_2_Bootstrapping_Language_Image_Pretraining/BLIP_2_Bootstrapping_Language_Image_Pretraining.pdf` | `30_VLA_and_Foundation_Policies/BLIP_2_Bootstrapping_Language_Image_Pretraining/QUICK_READ.md` |
| 8 | LLaVA | `30_VLA_and_Foundation_Policies/LLaVA_Visual_Instruction_Tuning/LLaVA_Visual_Instruction_Tuning.pdf` | `30_VLA_and_Foundation_Policies/LLaVA_Visual_Instruction_Tuning/QUICK_READ.md` |
| 9 | ALOHA / ACT | `20_Robot_Learning/ACT/ACT_Learning_Fine_Grained_Bimanual_Manipulation_with_Low_Cost_Hardware.pdf` | `20_Robot_Learning/ACT/QUICK_READ.md` |
| 10 | RT-2 | `30_VLA_and_Foundation_Policies/RT_2/RT_2_Vision_Language_Action_Models_Transfer_Web_Knowledge_to_Robotic_Control.pdf` | `30_VLA_and_Foundation_Policies/RT_2/QUICK_READ.md` |

## 每篇只记一个抽象跃迁

| 材料 | 核心抽象 | 为什么对后续重要 |
|---|---|---|
| LeNet-5 | `image -> convolution / subsampling -> classifier` | CNN 的最小完整语法：局部感受野、权重共享、层级特征。 |
| AlexNet | `ImageNet-scale data + GPU + deep CNN -> modern visual backbone` | 证明 CNN 可以从小字符识别扩展到大规模自然图像识别。 |
| VGG | `small conv + depth -> stronger feature hierarchy` | 说明视觉 backbone 可以通过更深、更规则的卷积堆叠提升表征。 |
| ResNet | `y = F(x) + x` | residual path 让很深的 backbone 可优化，是现代视觉编码器的重要基础。 |
| ViT | `image -> patch tokens -> Transformer encoder` | 把图像从 feature map 范式推进到 visual token sequence 范式。 |
| CLIP | `image embedding <-> text embedding` | 图文对齐，让视觉表征进入 open-vocabulary / language grounding。 |
| BLIP-2 | `frozen vision encoder -> Q-Former -> frozen LLM` | 用轻量桥接器把视觉特征接进大语言模型。 |
| LLaVA | `vision encoder + projector + LLM + instruction tuning` | 让 VLM 能按视觉指令对话，形成 instruction-following multimodal assistant。 |
| ALOHA / ACT | `teleop demos -> image/state/action -> action chunk policy` | 回到机器人：真实数据闭环、action chunk、eval/failure，是 SO-ARM101 最近期路径。 |
| RT-2 | `VLM output space -> action-as-token` | 把 VLM 进一步改成 VLA：模型输出不只是文字，而是机器人动作。 |

## 分阶段理解

### 1. CNN backbone 阶段

```text
LeNet -> AlexNet -> VGG -> ResNet
```

这一段回答：

- 图像如何从像素变成局部 / 层级视觉特征？
- 为什么 backbone 是主干特征提取网络？
- 为什么深度、优化和 residual connection 对视觉表征重要？

和机器人连接：

```text
camera image
-> visual backbone
-> feature representation
-> policy input
```

### 2. Visual token 阶段

```text
ResNet -> ViT
```

这一段回答：

- 图像能不能不再只看作 feature map，而是看作 patch token sequence？
- Transformer encoder 如何让 patch token 互相交换局部和全局信息？
- 为什么 ViT 更自然地连接后续 VLM / VLA？

和机器人连接：

```text
observation.images.<camera>
-> patch tokens / visual tokens
-> visual encoder
```

### 3. VLM 阶段

```text
ViT -> CLIP -> BLIP-2 -> LLaVA
```

这一段回答：

- CLIP：图像和文本如何进入同一个语义空间？
- BLIP-2：冻结的 vision encoder 和冻结的 LLM 之间如何桥接？
- LLaVA：visual instruction tuning 如何让 VLM 能按图像和语言指令回答？

和机器人连接：

```text
camera image + language instruction
-> grounded visual-language representation
```

### 4. Robot learning / VLA 阶段

```text
ALOHA / ACT -> RT-2
```

这一段回答：

- ALOHA / ACT：真实机器人数据如何采集，action chunk 如何训练，policy runtime 如何执行？
- RT-2：如何把 robot action 也变成 token，让 VLM 变成 VLA？

和机器人连接：

```text
observation.images
+ observation.state
+ task / language instruction
-> policy / VLA
-> action
-> robot runtime
-> eval / failure log
```

## 当前最重要的判断

- `LeNet -> ResNet` 是视觉特征提取主线。
- `ViT` 是从 CNN feature map 走向 visual tokens 的关键转折。
- `CLIP -> BLIP-2 -> LLaVA` 是从视觉表征走向视觉语言理解。
- `ALOHA / ACT` 是近期最可落地的机器人学习闭环。
- `RT-2` 是从 VLM 走向 VLA 的关键范式：action-as-token。
- `OpenVLA / pi0` 是后续代表模型，用来理解开放 VLA 工程栈和连续动作生成，但不能抢 LeRobot 首闭环。

## 关键架构图

这些图已经从本地 PDF 裁剪成只含架构图的版本，统一放在：`figures/cv_vlm_vla_bridge/architecture_only/`。

| 材料 | 图 | 用途 |
|---|---|---|
| LeNet-5 | `figures/cv_vlm_vla_bridge/architecture_only/lenet_architecture_only.png` | CNN 早期完整形态：convolution / subsampling / classifier。 |
| AlexNet | `figures/cv_vlm_vla_bridge/architecture_only/alexnet_architecture_only.png` | ImageNet-scale deep CNN 架构。 |
| VGG | `figures/cv_vlm_vla_bridge/architecture_only/vgg_config_table_only.png` | 用不同深度配置验证 `depth matters`。 |
| ResNet | `figures/cv_vlm_vla_bridge/architecture_only/resnet_residual_block_only.png` | residual block：用 `F(x) + x` 解决深层 plain net 的优化退化。 |
| ViT | `figures/cv_vlm_vla_bridge/architecture_only/vit_architecture_only.png` | image patch tokens 如何进入 Transformer encoder。 |
| CLIP | `figures/cv_vlm_vla_bridge/architecture_only/clip_architecture_only.png` | image encoder / text encoder 如何通过 contrastive learning 对齐。 |
| BLIP-2 | `figures/cv_vlm_vla_bridge/architecture_only/blip2_qformer_architecture_only.png` | Q-Former 如何用 learnable queries 从 frozen image encoder 抽取视觉表示。 |
| BLIP-2 | `figures/cv_vlm_vla_bridge/architecture_only/blip2_llm_architecture_only.png` | Q-Former 输出如何接入 frozen LLM 做生成。 |
| LLaVA | `figures/cv_vlm_vla_bridge/architecture_only/llava_architecture_only.png` | CLIP vision encoder + projection + LLM 的 visual instruction tuning 架构。 |
| ALOHA / ACT | `figures/cv_vlm_vla_bridge/architecture_only/act_architecture_only.png` | action chunking with Transformers：image/state -> future action sequence。 |
| RT-2 | `figures/cv_vlm_vla_bridge/architecture_only/rt2_architecture_only.png` | 把 robot action 表示成 token，让 VLM 输出动作。 |

## Takeaway Cards

### LeNet-5

- Key idea: `image -> convolution / subsampling -> classifier`，用端到端梯度学习替代手工特征。
- Architecture memory: local receptive field、shared weights、feature map、subsampling、classifier。
- To robotics: camera image 可以先被看作可学习 feature hierarchy 的输入。

### AlexNet

- Key idea: `ImageNet-scale data + GPU + ReLU + augmentation + dropout + deep CNN` 让 CNN 成为大规模自然图像识别主干。
- Architecture memory: convolution / pooling stack + fully connected classifier。
- To robotics: 现代 visual backbone 的工程起点，说明大数据和算力会改变模型上限。

### VGG

- Key idea: 用大量 `3x3 conv` 堆深度，验证 `depth matters`。
- Architecture memory: 规则的 conv3 stack + 5 次 max-pool + classifier。
- To robotics: backbone 可以通过简单模块堆叠形成层级视觉表征。

### ResNet

- Key idea: `y = F(x) + x`，让深层网络学 residual correction，缓解 degradation problem。
- Architecture memory: identity shortcut / residual block / bottleneck block。
- To robotics: 视觉 encoder、Transformer、diffusion、policy network 都会反复用 residual path 维持信息流。

### ViT

- Key idea: `image -> patch tokens -> Transformer encoder`，把图像从 CNN feature map 改写成 token sequence。
- Architecture memory: patchify、linear projection、class token、position embedding、encoder-only Transformer。
- To robotics: `observation.images.<camera>` 后续可以进入 visual encoder，变成 VLA 可用的 visual tokens。

### CLIP

- Key idea: `image embedding <-> text embedding`，用大规模图文对比学习建立共享语义空间。
- Architecture memory: image encoder + text encoder + projection + similarity matrix + symmetric contrastive loss。
- To robotics: 给 VLA 的 language grounding 打地基，但 CLIP 本身不生成回答，也不输出动作。

### BLIP-2

- Key idea: 用 `Q-Former` 把 frozen image encoder 和 frozen LLM 接起来，避免从零训练巨大 VLM。
- Architecture memory: frozen image encoder -> learnable query tokens / Q-Former -> projection -> frozen LLM。
- To robotics: VLA 常见模式也是 `pretrained perception backbone + connector / adapter + language/policy backbone`。

### LLaVA

- Key idea: `vision encoder + projector + LLM + visual instruction tuning`，让模型能围绕图片按指令对话。
- Architecture memory: CLIP ViT-L/14 输出 visual features，线性 projection 到 LLM embedding space，再做 assistant-style response training。
- To robotics: 它提供 `image + instruction -> sequence output` 的范式，但输出还是 text，不是 action。

### ALOHA / ACT

- Key idea: 低成本 teleoperation 采集 demos，ACT 用 `image/state -> future action chunk` 降低长时序 imitation learning 的 compounding error。
- Architecture memory: CVAE style variable `z`、多摄图像 CNN features、joint state、Transformer encoder-decoder、action chunk、temporal ensemble。
- To robotics: 这是 SO-ARM101 / LeRobot 当前最现实的路径：teleop -> record -> replay -> ACT/BC baseline -> eval/failure。

### RT-2

- Key idea: 把 robot action 也表示成 token，让 VLM 变成 `image + instruction -> action-as-token` 的 VLA。
- Architecture memory: web-scale VQA + robot action data co-fine-tuning；VLM 输出 action token，detokenize 成 robot action。
- To robotics: 它解释 VLA 范式，但近期不可直接替代 LeRobot 数据闭环。

## 今天复盘时只问

1. 每篇把什么东西变成了模型可学习的表示？
2. 输入是什么，输出是什么？
3. loss / training target 是什么？
4. 它离真实机器人 action loop 还有多远？
5. 它对 `SO-ARM101 / LeRobot` 的接口有什么启发？
