---
type: reading_track
track: diffusion / flow / action generation
status: active_support_track
created: 2026-06-18
---

# Diffusion / Flow / Action Generation Track

## Position

这条 track 单独维护 diffusion 相关内容，但它不是当前晚间主线。它服务三件事：

```text
generative vision: noise -> denoising -> image
robot action generation: noisy action sequence -> denoising -> action sequence
VLA frontier: flow matching / action expert / action tokenization
```

当前主线仍然是 `OpenVLA -> pi0 -> pi0-FAST -> LeRobot / SO-ARM101 data loop`。Diffusion track 用来解释后续为什么 `Diffusion Policy`、`pi0 flow matching action expert`、`action sequence generation` 会成为机器人策略的重要分支。

## Why Track Separately

Diffusion 容易横跨多个目录：

- `15_CV_Foundations`：DDPM / DDIM / Score SDE / Latent Diffusion，理解生成式视觉。
- `20_Robot_Learning`：Diffusion Policy，理解 action sequence denoising。
- `30_VLA_and_Foundation_Policies`：pi0 / pi0-FAST，理解 flow action expert 和 action tokenization。

单独成 track 的目的不是扩大阅读面，而是统一 review 这些操作：

- forward noising / reverse denoising
- score / SDE / flow matching
- sampling steps / latency / control frequency
- action horizon / action chunk / receding horizon
- multimodal action distribution
- robot runtime 上的 inference cost 和 safety fallback

## First Pass Order

完整扎实版路线见：[[ROADMAP]]

| 顺序 | 材料 | 本地入口 | 读法 | 只回答什么 |
|---|---|---|---|---|
| 1 | DDPM | `DDPM_Denoising_Diffusion_Probabilistic_Models/QUICK_READ.md` | Awareness | forward noising / reverse denoising 是什么 |
| 2 | DDIM | `../15_CV_Foundations/Diffusion_Models_for_Generative_Vision/QUICK_READ.md` | Scan | 为什么 sampling 可以加速 |
| 3 | Score SDE | `../15_CV_Foundations/Diffusion_Models_for_Generative_Vision/QUICK_READ.md` | Awareness | score / continuous-time 视角是什么 |
| 4 | Flow Matching / Rectified Flow | `Flow_Matching_for_Generative_Modeling/QUICK_READ.md` | Bridge | 为什么 pi0 选择 flow matching action expert |
| 5 | Latent Diffusion | `../15_CV_Foundations/Diffusion_Models_for_Generative_Vision/QUICK_READ.md` | Awareness | 为什么 latent space diffusion 更工程可行 |
| 6 | Diffusion Policy | `../20_Robot_Learning/Diffusion_Policy/QUICK_READ.md` | Structured Read | 如何把 observation-conditioned denoising 变成 robot policy |
| 6.5 | 3D Diffusion Policy | `3D_Diffusion_Policy/QUICK_READ.md` | Later Scan | 3D observation 如何接 diffusion action generation |
| 7 | pi0 | `../30_VLA_and_Foundation_Policies/PI0/QUICK_READ.md` | first pass done | flow action expert 和 continuous action horizon；后续配合 Flow Matching / Diffusion Policy 回看 |
| 8 | pi0-FAST | `../30_VLA_and_Foundation_Policies/PI0_FAST/QUICK_READ.md` | Scan | FAST action tokenizer 如何连接 continuous action 与 autoregressive VLA |

## Output Standard

每篇材料读完后必须补 6 个点：

- `one_sentence`: 一句话讲清它。
- `object`: 它生成/建模的是 image、latent、action sequence，还是 trajectory distribution。
- `conditioning`: 条件是什么，如 text、image、robot state、instruction。
- `training`: 学的是 noise prediction、score、velocity/flow，还是 action token。
- `inference_cost`: sampling steps、latency、control frequency 的代价。
- `robot_connection`: 它对 VLA / policy runtime / SO-ARM101 数据闭环有什么意义。

## Boundary

- 不训练 Stable Diffusion。
- 不把 diffusion 扩成完整生成模型全科。
- 不在 OpenVLA / pi0 第一轮未完成前深挖公式。
- 公式只在能解释 `policy runtime` 或 `action generation` 时精读。
