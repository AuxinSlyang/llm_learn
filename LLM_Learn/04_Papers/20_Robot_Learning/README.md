# 20 Robot Learning

这里是 2026 H2 最重要的论文线。

阅读顺序：

1. DAgger：理解 BC 为什么会因 covariate shift 失败。
2. ACT：理解 action chunking 和 manipulation imitation learning。
3. Diffusion Policy：理解把动作生成建模成条件扩散的路线。
4. RL for Robot Learning：只作为支撑线，理解 reward-driven improvement、offline data reuse、continuous control 和 world-model RL，不抢当前 VLA 主线。

阅读目标不是追 SOTA，而是把 `observation -> action -> data -> eval -> failure` 结构吃透，并落到 `embodied-ai-mini-stack`。

## Support Maps

- [[RL_For_Robot_Learning_Reading_Map]]：RL / offline RL / robot policy improvement 支撑线。
