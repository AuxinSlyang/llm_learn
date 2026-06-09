---
type: resources
project: SO-ARM101 + LeRobot 首闭环
status: active
---

# Resources

## 主参考

- 第一阶段主教程（子豪兄 Feishu Wiki）: http://zihao-ai.feishu.cn/wiki/TS6swApHbinx01kHDi5cf5n5n8c
- LingBot-VLA paper: https://arxiv.org/abs/2601.18692
- LingBot-VLA PDF: https://arxiv.org/pdf/2601.18692
- LingBot-VLA project page: https://technology.robbyant.com/lingbot-vla
- LingBot-VLA repo: https://github.com/Robbyant/lingbot-vla
- B站 walkthrough: https://www.bilibili.com/video/BV1sjLx6HE5D/
- 巧客具身 LingBot-VLA 教程（数采 -> 后训练 -> 云端推理部署）: https://ldgl0ghbka.feishu.cn/wiki/MZNSwUT88i8ijokrEMPcgYF5nIb

## Hardware / LeRobot

- LeRobot SO-101 assemble: https://huggingface.co/docs/lerobot/main/assemble_so101
- Seeed SO-ARM100/SO-ARM101 LeRobot full tutorial: https://wiki.seeedstudio.com/lerobot_so100m/
- LeRobot imitation learning on real robots: https://huggingface.co/docs/lerobot/il_robots
- SOARM 中文介绍: https://www.soarm.cn/
- Seeed SO-ARM101 Pro motor kit: https://www.seeedstudio.com/SO-ARM101-Low-Cost-AI-Arm-Kit-Pro-p-6427.html
- SO-ARM101 3D printed skeleton: https://www.seeedstudio.com/SO-ARM101-3D-printed-Enclosure-p-6428.html

## Models / Data

- LingBot-VLA 4B model: https://huggingface.co/robbyant/lingbot-vla-4b
- LingBot-VLA posttrain Robotwin model: https://huggingface.co/robbyant/lingbot-vla-4b-posttrain-robotwin
- GM-100 dataset: https://huggingface.co/datasets/robbyant/gm100
- XLeRobot: https://github.com/Vector-Wangel/XLeRobot
- XLeRobot docs: https://xlerobot.readthedocs.io/
- ACT low-cost robot arm repo: https://github.com/Shaka-Labs/ACT
- ACT paper/project: https://tonyzhaozh.github.io/aloha/
- OpenVLA paper: https://arxiv.org/abs/2406.09246
- OpenVLA repo: https://github.com/openvla/openvla
- SmolVLA blog: https://huggingface.co/blog/smolvla
- PI0 / OpenPI repo: https://github.com/Physical-Intelligence/openpi
- PI0 blog: https://www.physicalintelligence.company/blog/pi0
- PI0-FAST / FAST: https://www.physicalintelligence.company/research/fast
- PI0.5 blog: https://www.pi.website/blog/pi05
- VLA / robotics model radar CSV: https://github.com/epoch-research/robotic-manipulation-compute/blob/main/data/Robotics%20Models.csv

## Cloud GPU

- RunPod pricing: https://www.runpod.io/pricing
- Vast.ai: https://vast.ai/
- OpenBayes pricing: https://openbayes.com/pricing/
- Lambda GPU instances: https://lambda.ai/instances

## 读法

第一次看视频只抓流程：

- 机械臂怎么进入系统
- 摄像头怎么进入 observation
- 示教数据怎么录
- 模型怎么选
- 后训练怎么启动
- open-loop / real eval 分别验证什么

第一次看巧客具身 LingBot-VLA 教程只抓：

- LeRobot v2.1 / v3.0 数据转换与配置
- robot config 中 state / action / images 如何映射
- norm stats 如何计算
- open-loop eval 如何离线评估动作预测
- WebSocket 云端 server / 本地 robot client 如何分离

第一次读论文只抓：

- task
- observation
- action
- model / policy
- data
- training objective
- evaluation
- deployment path
