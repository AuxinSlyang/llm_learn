---
type: cloud_gpu_strategy
project: SO-ARM101 + LeRobot 首闭环
status: draft
updated: 2026-06-05
---

# Cloud GPU Strategy

## 一句话结论

可以租便宜云 GPU，但第一阶段不租 8 卡。

当前策略：

```text
local Mac:
  robot client / teleop / logger / replay / docs

local V100:
  ACT / BC 小模型训练
  LeRobot 数据检查
  轻量 open-loop smoke test

cheap cloud single GPU:
  环境 smoke test
  4090/5090/A6000/A40/RTX PRO 6000 级别短时验证

cloud A100/H100/96GB GPU:
  LingBot-VLA 4B 推理或 open-loop 可行性验证

8x A100/H100:
  只用于后续 full post-training，不作为首月目标
```

## 阶段用卡规则

| 阶段 | 目标 | 推荐资源 | 不建议 |
|---|---|---|---|
| 首月首闭环 | LeRobot dataset / ACT / BC / eval | 本地 V100 或 1x 4090/5090 | 为 ACT 上 8 卡 |
| LingBot-VLA walkthrough | schema / config / websocket runtime | 本地 Mac + V100 | 直接 full fine-tune |
| LingBot-VLA open-loop | 加载 checkpoint，跑 fake/real observation | 1x A100 80GB / H100 / RTX PRO 6000 96GB | 24GB 卡硬塞 4B VLA |
| Full post-training | 多任务 VLA 后训练 | 8x A100/H100 或同等级集群 | 用单 V100 硬训 |

## 当前平台候选

价格会变，以下只作为 2026-06-05 的选型快照。

### RunPod

定位：海外按小时 GPU，适合短时实验和 notebook/pod。

当前页面可见价格：

- RTX A5000 24GB: $0.27/h
- L4 24GB: $0.39/h
- RTX 3090 24GB: $0.46/h
- RTX 4090 24GB: $0.69/h
- RTX 5090 32GB: $0.99/h
- A40 48GB: $0.44/h
- RTX A6000 48GB: $0.49/h
- L40S 48GB: $0.86/h
- RTX 6000 Ada 48GB: $0.77/h
- A100 PCIe 80GB: $1.39/h
- A100 SXM 80GB: $1.49/h
- H100 PCIe 80GB: $2.89/h
- H100 SXM 80GB: $3.29/h
- RTX Pro 6000 96GB: $2.09/h

适合：

- 1-3 小时 smoke test。
- 尝试 A100/H100 加载 LingBot-VLA。
- 4090/5090 跑小模型训练和推理。

注意：

- Community Cloud 便宜但可用性波动。
- 一定设置预算上限，实验结束立刻关机。
- 大模型和数据放 persistent volume，避免重复下载。

### Vast.ai

定位：GPU marketplace，通常便宜，但机器质量、网络和可用性波动更大。

适合：

- 低成本 4090/3090/A6000 短跑。
- 不敏感数据的 smoke test。
- 可失败、可重试的实验。

不适合：

- 首次搭复杂环境。
- 长时间无人值守训练。
- 带隐私数据或强稳定性要求的实验。

### OpenBayes

定位：国内可访问的按小时 GPU 平台之一。

当前页面可见价格：

- RTX 5090 32GB: 2.9 元/h
- RTX PRO 6000 96GB: 8 元/h 起

适合：

- 国内网络环境更顺的短时实验。
- 5090 / 96GB 显存机器可用性验证。
- 支付宝/微信支付场景。

注意：

- 训练环境、CUDA、镜像和数据下载速度需要单独验证。
- 具体可用 GPU 和价格以登录后实时页面为准。

### Lambda

定位：更稳定的海外 GPU instance，价格通常比 marketplace 高，但环境和机器形态清晰。

当前页面可见价格：

- V100 16GB: $0.79/h
- A6000 48GB: $1.09/h
- A100 40GB: $1.99/h
- H100 PCIe 80GB: $3.29/h
- H100 SXM 80GB: $3.99-$4.29/h
- B200: $6.69/h 起

适合：

- 需要稳定环境和多 GPU instance 时。
- 后续认真做 LingBot-VLA 资源评估。

不适合：

- 首月便宜试错。

## 首月预算建议

不要一开始充值太多。

建议预算：

- 0 元：只用本地 V100 跑 ACT / BC。
- 100-300 元：租 1x 4090/5090/A6000 做 2-6 小时短测。
- 300-800 元：租 1x A100/H100/96GB 卡做 LingBot-VLA load / fake inference / open-loop 可行性。
- 不建议首月花 3000+ 元跑 8 卡 VLA full post-training。

## 第一次云 GPU smoke test

目标不是训练成功，而是判断平台是否可用。

检查项：

- `nvidia-smi`
- CUDA / PyTorch 版本
- `torch.cuda.is_available()`
- clone repo / install deps
- 下载小模型或 checkpoint 是否顺畅
- 跑 LeRobot / ACT toy command
- 跑 LingBot-VLA websocket server 的最小启动或记录 blocker

必须记录：

- 平台
- GPU 型号
- 单价
- 租用时长
- CUDA / driver / PyTorch
- 安装命令
- 成功项
- blocker
- 是否值得下次继续用

## Stop Rule

出现以下情况，停止烧钱：

- 环境安装超过 2 小时仍无法进入训练或推理。
- 模型无法加载且 blocker 是显存/架构，不是简单依赖问题。
- 单次实验没有明确验收项。
- 数据还没准备好，却在云上等待。
- 只是为了“感觉在推进”而开着 GPU。

