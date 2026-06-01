# nanoGPT gap list（Phase A：5/27-6/30）

> 目标：把 “nanoGPT -> inference/runtime” 这条主链路补齐到能复述、能定位代码、能写最小 benchmark/指标入口的程度。

## 最低完成线（本周）

- 列出 10-20 个“我现在讲不清楚/定位不到代码/不知道如何测”的缺口问题
- 每个缺口给一个“下一步动作”（读哪段笔记/定位哪个符号/写哪个最小脚本）

## 缺口清单（持续维护）

### A. Transformer / GPT 结构与实现

- [ ] 讲清 `encoder-decoder Transformer` 到 `decoder-only GPT` 的结构裁剪：哪些模块被删、哪些被改、为什么合理？
  - 下一步：补 `notes/transformer.md` 的 `cross-attn -> removed` 对照表。
- [ ] causal self-attention 的 mask（`tril`）在代码里如何影响 attention scores？为什么只影响上三角？
  - 下一步：在 `code/transformer.py` 定位 `tril/masked_fill`，画一张 4x4 示例。
- [ ] pre-norm vs post-norm：当前实现是哪一种？训练稳定性为什么不同？
  - 下一步：在 `code/transformer.py` 找 LayerNorm 位置，写 3 行结论。
- [ ] positional encoding：当前实现是 learned position embedding 还是 sinusoidal？对长上下文有什么约束？
  - 下一步：定位 `position_embedding_table`；写“长度上限=block_size”的一句话。

### B. 训练主链路（data -> loss -> update）

- [ ] dataset/tokenizer 的“输入输出契约”是什么：如何从文本到 token ids，再到 batch？
  - 下一步：复读 `Phase 1 总结` + 在代码里标注 `encode/decode` 的调用点。
- [ ] loss 计算的 shape 约束：`(B,T,C)` 如何 reshape 成 `(N,C)`？target 的 dtype/range 约束是什么？
  - 下一步：写一个 10 行的 shape sanity check（可先写在笔记里）。
- [ ] optimizer/grad 的最小闭环：`zero_grad/backward/step` 在训练 loop 中的真实语义（以及常见坑：梯度累积/混合精度/clip）
  - 下一步：补一个“我最容易犯错的 3 点”清单。

### C. 推理链路与指标（inference/runtime bridge）

- [ ] prefill vs decode 的区分在 GPT 推理里到底是什么？在当前最小实现里能否显式拆出来？
  - 下一步：在 `generate()` 里标注第一步 vs 后续循环；写一句类比（prefill=first forward over context）。
- [ ] KV cache：为什么能加速 decode？当前最小实现有没有 cache？如果没有，缺什么结构？
  - 下一步：在笔记里写“KV cache 的数据结构=每层每头的 K/V tensors”，并列出需要改动的函数边界。
- [ ] 指标入口：TTFT / TPOT / throughput 在最小脚本里怎么测（哪怕是粗糙的 wall clock）？
  - 下一步：写一个 `prompt -> generate -> time` 的最小脚本 TODO（后续放到 `03_Projects/` 下）。
- [ ] sampling：temperature/top-k/top-p 各自改变的概率分布是什么？在实现里如何插入？
  - 下一步：在 `generate` 中标注 softmax 前后的位置，写 3 行解释。

## 关联

- `notes/phase1-summary.md`：训练闭环骨架
- `notes/transformer.md`：Transformer->GPT 模块映射（待补齐）

