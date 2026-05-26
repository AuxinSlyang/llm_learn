# Reading Index

## 当前 4 周论文队列

> `start-my-day` 默认从这里挑选 paper slot。完成后手动打勾或移动顺序。
> 如果 `04_Papers/99_Overrides/YYYY-MM-DD.md` 存在，指定日期优先读 override，不使用本队列。

- [ ] DAgger: dataset aggregation and covariate shift
- [ ] ACT: action chunking for fine-grained manipulation
- [ ] Diffusion Policy: action generation as conditional denoising
- [ ] RT-1: scalable real-world robot learning with language-conditioned policies
- [ ] RT-2: VLM-to-VLA transfer from web knowledge to robot control
- [ ] Open X-Embodiment: cross-robot data and RT-X style generalization
- [ ] Octo: open generalist robot policy
- [ ] OpenVLA: open vision-language-action model
- [ ] PI0: flow-based general robot policy

## 分类

### 10 AI Foundations

| 材料 | 价值 | 状态 |
|---|---|---|
| The Bitter Lesson | 判断 AI 系统长期趋势，不迷信手工规则 | 已有 insight，可回看 |
| Finding Structure in Time | 理解简单 RNN / Elman network 如何表示时间和记忆 | Transformer 前传 |
| Long Short-Term Memory | 理解 LSTM 如何缓解 RNN 长距离依赖问题 | Transformer 前传 |
| Sequence to Sequence Learning with Neural Networks | 理解 Transformer 前的 encoder-decoder seq2seq 框架 | Transformer 前传 |
| Neural Machine Translation by Jointly Learning to Align and Translate | 理解 attention 如何解决 fixed-length vector 瓶颈 | Transformer 前传 |
| Attention Is All You Need | Transformer / attention 基础 | nanoGPT 收口后可回看 |
| ResNet / ViT | CV 表征基础 | CS231n/CV 入口阶段选读 |

### 20 Robot Learning

| 论文 | 价值 | 建议时间 |
|---|---|---|
| DAgger | 理解 BC 的分布偏移问题 | 2026-08/09 |
| ACT / ALOHA | manipulation imitation learning 入口 | 2026-09 |
| Diffusion Policy | robot action generation 经典路线 | 2026-09/10 |

### 30 VLA And Foundation Policies

| 论文 | 价值 | 建议时间 |
|---|---|---|
| RT-1 | language-conditioned robot policy 早期系统化路线 | 2026-11 |
| RT-2 | VLM knowledge transfer to robotic action | 2026-11 |
| Octo | open generalist robot policy | 2026-11/12 |
| OpenVLA | open VLA model and deployment awareness | 2026-11/12 |
| PI0 | general robot policy frontier awareness | 2026-11/12 |

### 40 Data And Eval

| 材料 | 价值 | 建议时间 |
|---|---|---|
| Open X-Embodiment | robot data scale, heterogeneity, embodiment gap | 2026-10/11 |
| LeRobot | practical dataset / policy / eval stack | 2026-10 |
| RoboMimic / robosuite materials | imitation learning dataset and benchmark awareness | 2026-09/10 |

## 读完后的沉淀标准

每篇论文目录至少保留：

- `QUICK_READ.md`：通读 / 核心思路 / takeaway
- `DEEP_READ.md`：精读 / 公式细节 / 训练推理 / 实验分析
- `README.md`：可选，仅用于目录或论文资源介绍，不作为默认阅读笔记
- `takeaways.md`：真正能迁移到项目里的 idea
- 可选 `links.md`：代码、项目主页、复现资料
