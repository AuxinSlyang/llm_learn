# Tokenizer Learning Map

## 主问题

- 文本为什么不能直接喂给 Transformer？
- Unicode、UTF-8、byte、token 的边界是什么？
- BPE 为什么是一种压缩和建模折中？
- token id 如何进入 embedding table？
- tokenizer 如何影响 context window 和生成质量？

## 学习顺序

1. Unicode / UTF-8 / bytes
2. byte-level tokenization
3. pair frequency
4. BPE merge table
5. encode / decode
6. special tokens
7. vocab size trade-off
8. token ids -> embedding

## 输出要求

- 一段可复述解释
- 一个最小 BPE 例子
- 一个 encode/decode demo
- 一段接入 nanoGPT 的接口说明

