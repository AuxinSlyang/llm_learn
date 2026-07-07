---
type: chapter_questions
project: [[ddia]]
status: in_progress
updated: 2026-07-03
---

# Ch2 Data Models and Query Languages Questions

## Questions

- 关系模型、文档模型、图模型分别让什么问题变得自然？又让什么问题变得困难？
- 为什么 document model 在一对多聚合对象上舒服，但在 many-to-many 关系上会变痛苦？
- Declarative query 和 imperative query 的差别是什么？为什么 SQL 这种声明式语言能给优化器空间？
- MiniLSM / RocksDB 这种 ordered KV engine 属于 Ch2 里的哪一层？它和 table/document/graph 模型是什么关系？
- TokaDB 如果把 row/index/tablet 编码成 KV，需要解决哪些 key design 问题？
- KVCache storage 如果用 Ch2 的视角看，它的 logical data model 应该是什么？

## Follow-ups

- 读 Ch3 `Storage and Retrieval` 时，重点看 SSTable、LSM、B-tree 如何服务 Ch2 的查询模型。
- 后续写 TabletServer read/write path 时，单独补一节：logical model -> physical key/value encoding。
- 后续看 KVCache / PagedAttention 时，用 Ch2 视角分析 block/page/prefix/session 是否是好的数据模型。
