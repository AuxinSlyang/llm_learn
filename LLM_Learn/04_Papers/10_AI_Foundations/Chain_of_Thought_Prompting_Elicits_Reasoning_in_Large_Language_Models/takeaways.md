# Takeaways

## 2026-05-31

- CoT 最值得带走的是一个行为格式 insight：在大模型上，把 few-shot prompt 示例写成 `question -> intermediate reasoning -> answer`，可以诱导模型显式 decode 中间推理过程，并提升多步推理任务表现。
- 它不是后训练论文，也不是完整推理系统；它是一个 prompt-level discovery，说明大模型能力很依赖“如何被问”和“输出格式如何被诱导”。
- CoT prompting 本身不够工程化：任意任务很难总能找到合适示例，prompt 选择有敏感性，小模型收益弱，推理链也不保证真实或正确。
- 后续更重要的方向是把 CoT 变成训练与推理系统的一部分：reasoning SFT、合成 reasoning traces、self-consistency、verifier / process reward model、tool use、reasoning RL。
- 对当前 LLM 主线的定位：CoT 连接 GPT-3 in-context learning 与后来的 reasoning model，是“推理能力可通过显式中间 token 被激发/训练/验证”的入口论文。
