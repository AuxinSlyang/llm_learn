---
type: roadmap_material_index
year: 2026
target_role: Embodied AI / Robotics Systems Builder
linked_roadmap: [[03_Annual_Plan_2026]]
updated: 2026-05-18
---

# 2026 Monthly Learning Materials

> 这份文件回答的问题：**2026 年剩余每个月具体学什么、看什么材料、产出什么？**
> 使用方式：每月计划负责节奏；本文件负责把课程、文档、论文和项目内容展开成可执行学习清单。

## 总原则

- 2026 H2 主线不是“同时完整学完多门课”，而是围绕一个可见 demo 建能力：`Modern Robotics -> MuJoCo -> Robot Learning -> manipulation demo`。
- `CS231n` 是视觉辅助线，只取与机器人视觉相关的核心内容。
- `CS336` 是语言智能 / runtime 支撑线，只做精选，不完整做 project。
- 每个月都必须有可见产物：笔记、代码、实验记录、视频、demo 或决策文档。

## 材料池

| 材料 | 用途 | 今年使用方式 |
|---|---|---|
| [Karpathy nn-zero-to-hero](https://github.com/karpathy/nn-zero-to-hero) | GPT / training loop / tokenizer / nanoGPT 收口 | 5-6 月收口，不再无限延展 |
| [Stanford CS336: Language Modeling from Scratch](https://cs336.stanford.edu/) | 语言模型从数据、tokenizer、Transformer、训练到评估的系统视角 | 6 月和 11 月精选；不完整做作业 |
| [Modern Robotics official materials](https://hades.mech.northwestern.edu/index.php/Modern_Robotics) | Classical Robotics 主教材与视频入口 | 6-8 月主教材 |
| [Modern Robotics video supplements](https://modernrobotics.northwestern.edu/) | 配合 MR 章节建立运动学 / 动力学直觉 | 6-8 月配套看 |
| [MuJoCo](https://mujoco.org/) / [MuJoCo Python docs](https://mujoco.readthedocs.io/en/stable/python.html) | 仿真与控制主环境 | 7-11 月主实验环境 |
| [Stanford CS231n 2026](https://cs231n.stanford.edu/2026/index.html) | 深度视觉基础、分类、检测、训练工程直觉 | 7-10 月精选视觉相关内容 |
| [OpenCV Get Started](https://opencv.org/get-started/) | 图像读取、相机、tracking、pose 入口 | 7-10 月工具线 |
| [Sutton & Barto: Reinforcement Learning](https://incompleteideas.net/book/the-book-2nd.html) | RL 概念底座 | 8 月只读 MDP / value / policy 基本章节 |
| [OpenAI Spinning Up](https://spinningup.openai.com/en/latest/spinningup/spinningup.html) | Deep RL 术语、算法地图、debug 直觉 | 8 月精选概念，不完整跑算法 |
| [LeRobot GitHub](https://github.com/huggingface/lerobot) / [LeRobot docs](https://huggingface.co/docs/lerobot) | Robot Learning 数据、训练、eval pipeline | 10-12 月主框架候选 |
| [LeRobot SO-100 docs](https://huggingface.co/docs/lerobot/so100) | 低成本实物机械臂入口 | 11-12 月做采购 / 实物决策参考 |
| [Diffusion Policy](https://diffusion-policy.cs.columbia.edu/) | 现代 visuomotor policy 范式 | 9 月精读候选 |
| [ACT paper: Learning Fine-Grained Bimanual Manipulation](https://arxiv.org/abs/2304.13705) | Imitation Learning / action chunking 入口 | 9 月精读候选 |
| [OpenVLA GitHub](https://github.com/openvla/openvla) | VLA 概念与系统规模认知 | 11 月 awareness |
| [PI-0 paper](https://www.physicalintelligence.company/download/pi0.pdf) | robot foundation model 概念 | 11 月 awareness |

## 本月目标：2026-05

### 本月定位

5 月是转向前的收口月：不急着全面切机器人，先把 `nanoGPT / GPT 基础理解` 压成自己的解释，再把 6-8 月机器人入口排稳。

### 5/18-5/31 最低完成线

- 完成 `nanoGPT 第一轮总结`。
- 写出 `tokenizer / nanoGPT / GPT-2 主线映射`。
- 写出 `makemore -> nanoGPT -> inference / runtime` 过渡说明。
- 建立 `机器人 + CV + LLM` 并存路线说明。
- 完成 `Modern Robotics` 入口材料确认，写出 6-8 月进入顺序草案。

### 5 月学习材料

- Karpathy `nn-zero-to-hero`：`nanogpt from scratch`、`tokenizer`、`GPT-2` 相关内容。
- 本地已有项目笔记：`03_Projects/nanogpt-from-scratch/`、`03_Projects/makemore/`。
- Modern Robotics：先只看目录、Ch.1-3 的问题域、视频入口。
- CS336：只作为对照材料，看课程总结构和 tokenizer / Transformer / training loop 的位置，不做作业。

### 5 月学习内容

- GPT 最小训练闭环：`token ids -> embedding -> attention -> block -> logits -> loss`。
- 生成闭环：`prompt -> tokenization -> model forward -> decode`。
- 从 `makemore` 到 `nanoGPT` 的升级：从字符模型 / MLP 直觉升级到 Transformer block。
- 从 `nanoGPT` 到 runtime 的桥：为什么未来会出现 KV cache、decode latency、inference/runtime 问题。
- 机器人入口：MR、MuJoCo、CV、Robot Learning 各自解决什么问题。

### 5 月不做

- 不展开 vLLM / SGLang。
- 不完整学 CS336。
- 不提前做 MuJoCo 复杂 demo。
- 不同时开太多机器人细分方向。

## 2026-06：Phase B Robotics + AI Fundamentals 入口

| 项 | 内容 |
|---|---|
| 月主题 | `nanoGPT 收口 + Modern Robotics Ch.1-3 入门` |
| 主材料 | Karpathy nn-zero-to-hero；Modern Robotics Ch.1-3；MR video supplements；CS336 tokenizer / Transformer / training loop 结构对照 |
| 学习内容 | nanoGPT 主链路；tokenizer 位置；configuration space；刚体运动；SO(3) / SE(3) / se(3) 直觉 |
| 实验内容 | nanoGPT 只补小验证；MR 以推导、图解和 Python 小函数为主 |
| 关键产出 | `LLM phase 1 总结`；`makemore -> nanoGPT -> inference_runtime 映射`；`Modern Robotics 学习地图`；`机器人系统总图 v0` |
| 月末自检 | 能不用资料讲清 nanoGPT 训练 / 生成链路；能解释为什么刚体运动表示是机器人底层语言 |

## 2026-07：Phase B 运动学 + 仿真启动

| 项 | 内容 |
|---|---|
| 月主题 | `Modern Robotics 运动学 + MuJoCo 入门 + CV hello-world` |
| 主材料 | Modern Robotics Ch.4-6；MR Course 2 / video supplements；MuJoCo docs；CS231n 视觉任务 overview；OpenCV Get Started |
| 学习内容 | Forward Kinematics；PoE 公式；space/body frame；Jacobian；Inverse Kinematics；MuJoCo model/data/step loop；OpenCV 读图 / 相机 / 简单检测 |
| 实验内容 | MuJoCo hello-world；加载机械臂模型；读取关节状态；简单 joint target / PD 控制；OpenCV hello-world |
| 关键产出 | `MR Ch4-6 运动学笔记`；`PoE/Jacobian/IK 最小解释`；`MuJoCo Python hello-world 记录`；`机械臂关节控制最小实验` |
| 月末自检 | 能讲清末端位姿如何由关节角决定；能在 MuJoCo 里跑 step loop 并控制一个关节 |

## 2026-08：Phase C 动力学 / 控制 + Robot Learning 地图

| 项 | 内容 |
|---|---|
| 月主题 | `MR 动力学 / 控制入口 + MuJoCo 单臂控制 + RL 概念地图` |
| 主材料 | Modern Robotics Ch.8/9/11 选读；MuJoCo Python docs；Sutton & Barto Ch.3-6 选读；OpenAI Spinning Up overview |
| 学习内容 | 动力学直觉；轨迹生成；控制器边界；MDP / value / policy；Q-learning / policy gradient / PPO 的位置 |
| 实验内容 | MuJoCo 关节 PD 控制；末端目标控制；FK / IK / controller / simulation step loop 关系图 |
| 关键产出 | `MR 动力学 / 控制入口笔记`；`MuJoCo 单臂控制最小实验`；`Robot Learning 概念地图 v1`；`9 月 demo 任务定义` |
| 月末自检 | 能讲清运动学、动力学、控制的边界；能定义 9 月 classic-control demo 的最小闭环 |

## 2026-09：Phase D 仿真闭环 v1 + IL 概念

| 项 | 内容 |
|---|---|
| 月主题 | `MuJoCo pick-place / reach 经典控制 demo + Imitation Learning 概念入口` |
| 主材料 | MuJoCo docs；Modern Robotics Ch.11/12 选读；ACT paper；Diffusion Policy project/paper；OpenCV tracking / pose 入口 |
| 学习内容 | classic control demo 系统拆解；状态、目标、控制、成功判据、失败模式；BC / DAgger；data collection；eval；ACT / Diffusion Policy 的问题定义 |
| 实验内容 | MuJoCo 机械臂 + 桌面 + 物体；reach / push / pick-place 三选一；目标位置 -> IK -> 控制器 -> 仿真结果 |
| 关键产出 | `MuJoCo pick-place/reach 经典控制 demo`；`demo 系统拆解与失败模式记录`；`IL 概念笔记`；`ACT 或 Diffusion Policy 精读笔记` |
| 月末自检 | 有一个可复现仿真 demo；能说清 classic control demo 和后续 BC demo 的边界 |

## 2026-10：Phase D Robot Learning 第一次动手

| 项 | 内容 |
|---|---|
| 月主题 | `Behavior Cloning 最小项目（LeRobot + MuJoCo）` |
| 主材料 | LeRobot docs / examples；MuJoCo docs；CS231n 训练工程与视觉模型精选；OpenCV camera / tracking / pose |
| 学习内容 | dataset format；teleop / scripted policy；Behavior Cloning；policy train/eval；success rate；failure mode；视觉输入与状态输入的取舍 |
| 实验内容 | 选定 reach / push / pick-place；scripted 或 teleop 采少量数据；训练 BC policy；仿真 eval；保存视频和 metrics |
| 关键产出 | `BC 数据采集记录`；`BC 训练脚本/配置`；`BC eval 记录与视频`；`LeRobot/MuJoCo pipeline 笔记` |
| 月末自检 | 跑通第一个 Robot Learning 训练 / eval 闭环；能解释 BC 为什么失败以及数据分布如何影响 policy |

## 2026-11：Phase E 算法产品化 + runtime / TensorRT / 量化入口

| 项 | 内容 |
|---|---|
| 月主题 | `policy runtime + latency / fallback + ONNX / TensorRT / 量化入口` |
| 主材料 | LeRobot；MuJoCo；ONNX / TensorRT 入门材料；OpenVLA；PI-0；RT-2；CS336 deployment/inference/runtime 精选 |
| 学习内容 | policy runtime；latency budget；TTFT / TPOT；ONNX export；TensorRT 基础概念；FP16 / INT8 量化 awareness；VLM / VLA / LLM 的边界 |
| 实验内容 | 基于 10 月 pipeline 写 `policy_runtime v0`；记录 inference / sim step / end-to-end latency；做最小 ONNX export + latency measurement；实现 observation missing / policy timeout / action out-of-bound 处理 |
| 关键产出 | `policy_runtime v0`；`latency_report v0`；`fault_injection_tests v0`；`ONNX / TensorRT / quantization awareness note`；`VLA 概念笔记` |
| 月末自检 | 能把 Robot Learning demo 讲成可部署软件组件；能解释 TensorRT / 量化解决什么问题、不解决什么问题；知道 VLA 今年只需要 awareness 到什么程度 |

## 2026-12：Phase F 作品化 + 多传感器融合入口 + 2027 决策

| 项 | 内容 |
|---|---|
| 月主题 | `Embodied AI mini-stack README + 多传感器融合入口 + Capability Map v1` |
| 主材料 | 全年笔记、demo、代码、视频、实验记录；LeRobot SO-100/SO-101 文档；2027 候选材料清单 |
| 学习内容 | 能力地图重打 Level；全年 deliverable 索引；JD mapping；多传感器融合基本问题：time sync、coordinate frame、calibration、noise、missing data；2027 真机 / ROS2 / edge deployment 计划 |
| 实验内容 | 补齐最小 demo 复现实验；整理视频和 metrics；整理 replay / eval / failure analysis；如有 camera 数据，做 camera frame + qpos/qvel 同步记录 |
| 关键产出 | `Embodied AI mini-stack README`；`Capability Map v1`；`2026 年终复盘`；`2026 deliverable 索引`；`sensor_fusion_note v0`；`JD mapping`；`2027 方向草案`；`实物平台决策记录` |
| 月末自检 | 能用 mini-stack 解释具身智能软件工程师 JD 四块能力；能讲清多传感器融合的基本问题但不扩散成完整 SLAM 主线；2027 不是泛泛继续学，而是有明确主攻方向 |

## 课程取舍规则

### CS231n

今年使用方式：`精选 + 工具化`。

- 必看：视觉任务总览、classification / detection / segmentation 的基本问题形态、CNN / ViT 直觉、训练与 fine-tuning 工程经验。
- 可跳：完整大作业、无关视觉方向的深挖、和机器人 demo 无关的长尾 topic。
- 落点：OpenCV / camera / detection / pose / tracking 能服务 manipulation demo。

### CS336

今年使用方式：`精选 + 桥接`。

- 必看：tokenization、Transformer architecture、training loop、optimizer / eval / scaling 的基本结构。
- 选看：inference / deployment / systems / distributed training。
- 不做：完整 assignment、大规模训练、Triton / FlashAttention / 多机多卡 project。
- 落点：帮助理解机器人语言智能未来需要的 runtime / inference / agent 底座。

### Modern Robotics

今年使用方式：`主教材 + 章节制推进`。

- 6 月：Ch.1-3，系统总图与刚体运动表示。
- 7 月：Ch.4-6，FK / Jacobian / IK。
- 8 月：Ch.8/9/11 选读，动力学 / 轨迹 / 控制入口。
- 9 月之后：按 demo 卡点回查，不再整本线性推进。

### MuJoCo / LeRobot

今年使用方式：`以 demo 驱动`。

- MuJoCo：先本地 GUI + 远端 headless rollout，逐步从 step loop 到 control demo。
- LeRobot：先作为 BC pipeline 框架候选，10 月开始真正使用。
- 实物平台：11-12 月决策，只有仿真 demo 和 pipeline 跑通后再进入。

## 年底量化目标

最低目标：

- 一个可复现的 MuJoCo manipulation demo。
- 一个 Behavior Cloning 训练 / eval pipeline。
- 一组可展示的视频 / metrics / 失败模式记录。
- 一份 `Capability Map v1` 和 2027 方向草案。

拉伸目标：

- 用 SO-100 / SO-101 或等价低成本硬件完成一个最小实物 robot learning demo。
- 任务不追复杂：`reach` / `push` / `pick-place` 三选一。
- 重点不是成功率多高，而是完成 `采集 -> 训练 -> eval -> 部署/复现 -> 记录` 的闭环。
