---
type: reading_roadmap
track: diffusion / flow / action generation
status: active
created: 2026-06-28
purpose: "按部就班建立 diffusion -> action generation -> flow action expert 的论文链路"
---

# Diffusion / Flow / Action Generation Roadmap

## 定位

这条线服务机器人动作生成，不做完整图像生成模型全科。

核心问题：

```text
noise / latent / action chunk
-> denoising / score / flow / tokenization
-> image sample or robot action sequence
```

最终要回到：

```text
SO-ARM101 / LeRobot:
observation.images + observation.state + task
-> future action chunk
-> replay / eval / failure taxonomy
```

## 主路线

### Stage 0：最小预备

目标：知道 diffusion 在解决什么生成问题。

| 顺序 | 论文 / 材料 | 本地入口 | 读法 | 只回答什么 |
|---|---|---|---|---|
| 0.1 | Diffusion Models 概念预备 | `README.md` + 本文件 | 20m concept scan | 为什么从 noise 生成 data 可以被看成逐步变换 |

输出标准：

- 能说清 `data -> noise` 和 `noise -> data` 是两条相反方向。
- 暂时不追 ELBO / score matching 公式。

### Stage 1：DDPM 基础

目标：理解 diffusion 最经典的离散时间链路。

| 顺序 | 论文 | arXiv | 本地入口 | 读法 |
|---|---|---|---|---|
| 1 | Denoising Diffusion Probabilistic Models | `2006.11239` | `DDPM_Denoising_Diffusion_Probabilistic_Models/QUICK_READ.md` | Structured Awareness |

必须回答：

- forward process：如何逐步给 clean data 加噪。
- reverse process：模型如何学会从 noisy sample 去噪。
- training target：预测 noise / denoised sample 的直觉。
- sampling cost：为什么通常需要很多步。
- robot connection：把 image sample 换成 action chunk 后，哪些概念能迁移。

完成标准：

- 写出一句：`DDPM = train denoiser on noisy data; sample by repeated denoising from noise`。

### Stage 2：采样加速与连续时间视角

目标：不深挖公式，但理解为什么后续会出现 DDIM、Score SDE、Flow Matching。

| 顺序 | 论文 | arXiv | 读法 | 只回答什么 |
|---|---|---|---|---|
| 2.1 | Denoising Diffusion Implicit Models | `2010.02502` | `DDIM_Denoising_Diffusion_Implicit_Models/QUICK_READ.md` | Scan | 为什么同一个训练目标可以更快采样 |
| 2.2 | Score-Based Generative Modeling through Stochastic Differential Equations | `2011.13456` | `Score_Based_Generative_Modeling_through_SDEs/QUICK_READ.md` | Awareness | score / continuous-time SDE 视角是什么 |

完成标准：

- 能解释 DDIM 是为了解决 sampling steps / latency。
- 能解释 Score SDE 把 diffusion 推到 continuous-time，连接 ODE/SDE 和后续 flow 视角。
- 不要求会推导 SDE。

### Stage 3：机器人动作生成主论文

目标：从 image generation 迁移到 robot action sequence generation。

| 顺序 | 论文 | arXiv | 本地入口 | 读法 |
|---|---|---|---|---|
| 3 | Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | `2303.04137` | `../20_Robot_Learning/Diffusion_Policy/QUICK_READ.md` | Structured Read |

必须回答：

- policy 生成的是 single action 还是 future action sequence。
- condition 是什么：image、state、observation history。
- conditional denoising 如何变成 robot policy。
- receding horizon control 如何执行动作。
- diffusion 为什么适合 multimodal action distribution。
- 对 LeRobot / SO-ARM101 的字段要求是什么。

完成标准：

- 写出 `observation + noisy future action sequence -> denoised action sequence -> receding horizon execution`。
- 写出 `ACT vs Diffusion Policy` 三行对照。

### Stage 4：Flow / Rectified Flow / Flow Matching

目标：理解 pi0 的 flow action expert 为什么不是普通 DDPM 复刻。

| 顺序 | 论文 | arXiv | 本地入口 | 读法 |
|---|---|---|---|---|
| 4.1 | Flow Matching for Generative Modeling | `2210.02747` | `Flow_Matching_for_Generative_Modeling/QUICK_READ.md` | Bridge |
| 4.2 | Flow Straight and Fast: Learning to Generate and Transfer Data with Rectified Flow | `2209.03003` | `Rectified_Flow_Flow_Straight_and_Fast/QUICK_READ.md` | Optional Bridge |

必须回答：

- probability path 是什么。
- vector field 是什么。
- Flow Matching 学的是 noise-to-data 的什么量。
- 它和 DDPM / Diffusion Policy 的区别是什么。
- 为什么它适合 continuous action chunk generation。

完成标准：

- 写出 `Flow Matching = regress a vector field along a probability path; sample by following the learned field`。
- 写出 `Diffusion Policy vs Flow Matching vs pi0` 三行对照。

### Stage 5：工程可行性和视觉生成支线

目标：理解 latent diffusion 为什么能工程化，但不把 Stable Diffusion 作为主线。

| 顺序 | 论文 | arXiv | 读法 | 只回答什么 |
|---|---|---|---|---|
| 5 | High-Resolution Image Synthesis with Latent Diffusion Models | `2112.10752` | `Latent_Diffusion_High_Resolution_Image_Synthesis/QUICK_READ.md` | Awareness | 为什么在 latent space 做 diffusion 能降成本 |

完成标准：

- 能解释 pixel diffusion 和 latent diffusion 的计算差异。
- 只作为 VLA / perception / generative vision 支撑，不训练 Stable Diffusion。

### Stage 6：Robot observation 升级

目标：看 diffusion action generation 如何接 3D observation。

| 顺序 | 论文 | 本地入口 | 读法 |
|---|---|---|---|
| 6 | 3D Diffusion Policy | `3D_Diffusion_Policy/QUICK_READ.md` | Later Scan |

必须回答：

- 3D representation 给 action generation 带来什么信息。
- 它解决的是视觉表征问题、动作生成问题，还是泛化问题。
- 对 SO-ARM101 当前单摄像头 first loop 是否必要。

完成标准：

- 多数情况下标为 later，不抢 DDPM / Diffusion Policy / Flow Matching 主线。

### Stage 7：VLA / foundation policy 回接

目标：把 diffusion/flow 直觉接回 pi0 / pi0-FAST。

| 顺序 | 论文 / 材料 | arXiv | 本地入口 | 读法 |
|---|---|---|---|---|
| 7.1 | pi0: A Vision-Language-Action Flow Model for General Robot Control | `2410.24164` | `../30_VLA_and_Foundation_Policies/PI0/QUICK_READ.md` | Revisit |
| 7.2 | FAST: Efficient Action Tokenization for Vision-Language-Action Models | `2501.09747` | `../30_VLA_and_Foundation_Policies/PI0_FAST/QUICK_READ.md` | Revisit |

必须回答：

- pi0 的 action expert 和 Flow Matching / Diffusion Policy 的关系。
- pi0-FAST 为什么走 action tokenization，而不是 continuous flow action expert。
- 对 Unitree / LeRobot-style runtime，action horizon、control frequency、latency、action clipping 如何记录。

完成标准：

- 写出 `Diffusion Policy / Flow Matching / pi0 / pi0-FAST / ACT` action representation matrix。

## 推荐节奏

### 扎实版：6 个 session

| Session | 内容 | 产出 |
|---|---|---|
| S1 | DDPM | `forward / reverse / training target / sampling steps` |
| S2 | DDIM + Score SDE | `sampling acceleration / continuous-time view` |
| S3 | Diffusion Policy Part 1 | `observation-conditioned action denoising` |
| S4 | Diffusion Policy Part 2 | `receding horizon / multimodality / eval` |
| S5 | Flow Matching | `probability path / vector field / CFM` |
| S6 | pi0 / pi0-FAST 回接 | `action generation matrix` |

### 最小实用版：3 个 session

| Session | 内容 | 产出 |
|---|---|---|
| S1 | DDPM awareness | 一页 noising / denoising 直觉 |
| S2 | Diffusion Policy structured read | robot action sequence denoising |
| S3 | Flow Matching + pi0 回接 | flow action expert 直觉 |

当前建议采用扎实版，但每个 session 控制在 40-70 分钟，不影响 SO-ARM101 晚间硬件主线。

## 每篇论文统一输出

每篇只填这 6 个字段，避免笔记发散：

- `object`: 生成的是 image、latent、action sequence、trajectory，还是 vector field。
- `conditioning`: 条件是什么。
- `training_target`: 学 noise、score、denoised sample、velocity/flow，还是 action token。
- `inference`: 怎么采样 / 推理；需要多少步；是否有 latency 风险。
- `robot_connection`: 和 LeRobot / Unitree / SO-ARM101 的关系。
- `one_sentence`: 一句话 takeaway。

## 当前下一步

下一次 paper session 从 `DDPM` 开始，不直接读 Flow Matching。

具体顺序：

1. `DDPM`：Abstract + Intro + method overview。
2. 写 `DDPM_Denoising_Diffusion_Probabilistic_Models/QUICK_READ.md` 的 5 个空项。
3. 再进入 `Diffusion Policy`。
