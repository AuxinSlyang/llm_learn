# Hugging Face Text Generation 章节笔记（2026-03-08）

## 关联

- 来源：`Transformers LLM tutorial / Text generation`
- 关联 DailyNote：[[2026-03-08]]
- 学习主线：`LLM Inference / Serving`

## 原文链接

- Text generation（本节主链接）：https://huggingface.co/docs/transformers/llm_tutorial
- Chat templating（配套阅读）：https://huggingface.co/docs/transformers/chat_templating

## 本文目标

- 搞清最小推理链路：`tokenizer -> model -> generate -> decode`
- 搞清 `chat template` 在 chat 模型中的作用
- 为后续 `TTFT / TPOT / prefill / decode` 指标映射打基础

## 最小代码链路（你今天的实验）

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

quantization_config = BitsAndBytesConfig(load_in_4bit=True)
model = AutoModelForCausalLM.from_pretrained(
    "mistralai/Mistral-7B-v0.1",
    device_map="auto",
    quantization_config=quantization_config
)

tokenizer = AutoTokenizer.from_pretrained(
    "mistralai/Mistral-7B-v0.1",
    padding_side="left"
)
model_inputs = tokenizer(
    ["A list of colors: red, blue"],
    return_tensors="pt"
).to(model.device)

generated_ids = model.generate(**model_inputs)
text = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
```

## 这段代码在做什么（你的理解整理版）

1. 用 `from_pretrained` 加载 base causal LM（这里是 `Mistral-7B-v0.1`）。
2. 用 `BitsAndBytesConfig(load_in_4bit=True)` 在加载时做 4bit 量化，核心目的是降低显存占用。
3. 用 `tokenizer(...)` 把输入文本转成 token ids（张量形式）。
4. 用 `model.generate(...)` 做自回归生成。
5. 用 `batch_decode(...)` 把 token ids 还原成可读文本。

## 3-5 条摘记（Text generation）

- `generate()` 是推理主入口，最小闭环先跑通比先调参更重要。
- 量化（如 4bit）是显存和可部署性的关键抓手，但会有精度/输出质量权衡。
- prompt 文本先经过 tokenizer 变成张量输入，模型输出 token ids 后再 decode 成文本。
- 对 inference 学习早期，先固定参数拿到可复现输出，再谈性能优化更稳。
- 先建立“能稳定生成一次”的闭环，再进入 `TTFT/TPOT` 指标和 cache 视角。

## 你的本章 Takeaway（当前阶段）

1. 先跑通黑盒最小链路：`tokenizer -> model -> generate -> decode`。
2. `generate()` 的行为由参数决定，至少要能控制：`max_new_tokens`、`do_sample`、`temperature`。
3. `GenerationConfig` 保存的是“生成策略模板”，不是模型权重。
4. chat 模型需要 `chat template`，否则输入格式可能不匹配训练分布，输出会劣化。
5. 这周不深挖高级解码技巧，目标是可复现、可解释、可复盘。

## 常见坑（简版）

- 不设 `max_new_tokens`：输出经常过短，容易误判模型效果。
- 默认 greedy：在创意/对话场景可能显得呆板。
- 批量输入长度不一时：decoder-only 模型通常要 `padding_side="left"`。
- chat 模型喂裸 prompt：可能得到次优输出，优先使用 chat template。

## chat template 要点

- 问题：为什么 chat 模型不应直接喂裸 prompt？
- 结论：
  - chat 模型训练时依赖特定对话格式（`system/user/assistant`）。
  - `apply_chat_template` 会把消息列表转成模型预期的 token 序列。
  - 不用模板时，输出常见问题是角色错乱、指令跟随变差、风格漂移。

## `apply_chat_template` 最小示例

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "Qwen/Qwen2.5-1.5B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")

messages = [
    {"role": "system", "content": "You are a concise assistant."},
    {"role": "user", "content": "用两句话解释 TTFT 和 TPOT。"},
]

inputs = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

outputs = model.generate(inputs, max_new_tokens=128, do_sample=False)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## 裸 prompt vs chat template（结论）

- 裸 prompt：有时也能生成，但结果不稳定，容易偏离“对话助手”行为。
- chat template：更贴近模型训练分布，回答风格与指令跟随通常更稳定。

## 你当前该用哪种输入格式

- `Mistral-7B-v0.1`（base model）：可先用普通字符串 prompt 跑最小闭环。
- `Qwen2.5-1.5B-Instruct`（chat/instruct）：优先使用 `messages + apply_chat_template`。

## `add_generation_prompt` vs `continue_final_message`

- 常规问答：`add_generation_prompt=True`，显式告诉模型“现在轮到 assistant 回答”。
- 续写/prefill：`continue_final_message=True`，让模型接着最后一条消息继续写。
- 两者不能同时开；一个是“新开回复”，一个是“继续上一条”。

## 实验结论（2026-03-08）

- `1_normal.py` 跑通：`tokenizer -> model -> generate -> decode` 闭环成立。
- `2_saving.py` 跑通：`GenerationConfig` 可保存/加载并参与生成。
- `3_chat_format.py` 跑通：`apply_chat_template` 会按模型格式插入控制 token（如 `[INST]`）。
- `4_chat_tokenizer.py` 问题与修复：
  - 问题：输入 tensor 在 CPU，模型在 CUDA，导致 device mismatch。
  - 修复：`inputs = inputs.to(model.device)`，并用 `model.generate(**inputs)` 传入完整输入（含 `attention_mask`）。

## 训练场景的一句结论

- chat template 不只用于推理，也用于训练前数据预处理；训练时通常用 `add_generation_prompt=False`。

## 对今天主线的连接

- 这页完成后，你应该能直接回答：
  - `tokenizer -> model -> generate -> decode` 每一步在干什么
  - `chat template` 为什么是 chat 模型推理前的必要步骤
  - 这些步骤后续如何映射到 `prefill/decode` 与 `TTFT/TPOT`
