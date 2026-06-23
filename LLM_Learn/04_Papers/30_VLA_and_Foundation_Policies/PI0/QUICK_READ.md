---
type: paper_note
title: "pi0: A Vision-Language-Action Flow Model for General Robot Control"
short_name: pi0
arxiv_id: "2410.24164"
url: https://arxiv.org/abs/2410.24164
pdf_url: https://arxiv.org/pdf/2410.24164
local_pdf: ./PI0_A_Vision_Language_Action_Flow_Model_for_General_Robot_Control.pdf
track: robot foundation policy frontier
read_mode: Structured Awareness
status: first_pass_done
created: 2026-06-09
---

# pi0 - QUICK READ

## Position

pi0 代表 VLA + flow/action generation 的前沿 robot foundation policy 方向。

## Read Questions

- VLM backbone 和 action expert 如何分工？
- flow matching 如何用于 action generation？
- 如何覆盖多机器人、多任务？
- 端侧 runtime 和控制频率如何处理？

## This Week

W25 短期两篇 VLA 代表材料之一：明天优先读，完成 structured awareness read，但不进源码复现，不训练，不替代 LeRobot 首闭环。

### 为什么选它

- 它代表 `VLM backbone + action expert + flow matching` 的新一代 robot foundation policy 方向。
- 它直接回答连续动作如何生成，和 OpenVLA / RT-2 的 action token 路线形成对照。
- 它后续可以自然连接 `pi0-FAST`，但本周先读 pi0 主文，不把 FAST 单独扩成第三篇。

### Must Answer

- pi0 的 VLM backbone 和 action expert 如何分工？
- flow matching 在这里是如何用于 action generation 的？
- 它如何处理连续动作、action horizon / action chunk，以及多机器人多任务？
- 它和 ACT / Diffusion Policy / RT-2 的 action representation 有什么差别？
- 如果未来接到 SO-ARM101 / LeRobot，最先需要对齐哪些字段：`observation.images`、`observation.state`、`task`、`action`、control frequency、latency？

### Output

- 3-5 条 structured takeaway。
- 一张最小 mental model：

```text
image / state / language
-> VLM backbone
-> action expert / flow matching
-> action sequence
-> robot runtime
```

- 一段 `pi0 -> LeRobot / SO-ARM101` 连接说明：本周只理解接口，不做训练或 deployment。

### Boundary

- 不读 openpi 源码。
- 不训练。
- 不部署。
- `pi0-FAST` 只作为 action tokenization radar：等 pi0 的 flow/action expert 理解后再补。

## 2026-06-23 状态校准

用户确认 `pi0` 已经看过第一轮。当前状态改为 `first_pass_done`。

后续不再把它作为普通待读项重复排队；只在读下面材料时回看它：

- `Flow Matching / Rectified Flow`：补 action expert 背后的 vector field 直觉。
- `Diffusion Policy`：和 diffusion action sequence generation 做对照。
- `pi0-FAST`：对比 continuous flow action expert 与 action tokenizer。
- `SO-ARM101 / LeRobot` 有真实数据后：检查 `observation.images / observation.state / task / action / control frequency / latency` 是否能映射到 pi0 式接口。
