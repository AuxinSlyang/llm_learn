---
type: chapter_notes
project: [[ddia]]
status: in_progress
updated: 2026-07-03
---

# Ch2 Data Models and Query Languages Notes

## Takeaways

- 2026-07-03 first pass：本章核心问题是“数据模型如何塑造你能自然表达的问题”。模型不是中性容器，它会影响应用代码、查询方式、性能和演进成本。
- 数据系统通常是多层模型叠加：现实世界对象 -> 应用对象/API -> 通用数据模型（关系/文档/图）-> 存储引擎的 bytes/records/indexes。每一层都隐藏下一层复杂度，也带来表达能力边界。
- Relational model 的强项是通用、规范化、join 和声明式查询；它让应用少关心底层访问路径。
- Document model 的强项是局部性和对象结构贴合；当数据天然是“一整棵一起读写”的聚合对象时更顺。但它在 many-to-one / many-to-many 关系和 join 上会变复杂。
- Graph model 的强项是关系本身很重要、连接很多且模式灵活的场景；比如社交关系、推荐、依赖图、知识图谱。
- Query language 的关键区别：declarative query 说“要什么”，由系统优化执行；imperative query 说“怎么做”，执行路径更多暴露给程序员。
- 本章和 Ch3 的连接：Ch2 讲逻辑数据模型和查询表达，Ch3 会讲底层存储引擎如何支持这些模型与查询。

## Code / System Mapping

- MiniLSM 当前处在最低层：它不关心 document/relational/graph 语义，只提供 ordered key-value storage、point lookup、range scan 和后续 persistence/compaction。
- RocksDB 也是 KV storage engine：上层数据库/TabletServer 可以把 table row、index entry、metadata、versioned key 编码成 KV，再让 RocksDB 负责有序存储和迭代。
- TokaDB TabletServer 的关键问题之一是：上层 tablet/row/index/事务语义如何编码到底层 Engine 的 key/value、range、write batch 和 snapshot 上。
- DDIA Ch2 提醒后续看 TokaDB/RocksDB 时要分清：
  - logical model：表、行、tablet、index、事务。
  - physical model：key encoding、value bytes、SST、memtable、iterator。
  - query/API model：RPC、scan、get、write、admin operation。
- 对 AI Infra 的连接：KVCache storage 的“数据模型”可能是 request/session/prefix/block/page，而不是传统 table；选错模型会直接影响 reuse、eviction、movement 和 scheduler。

## One Sentence Summary

DDIA Ch2 的核心是：数据模型决定你如何思考问题、表达查询和演进系统；底层 KV/LSM 只是物理基础，上层还必须设计清楚 logical model 和 query/API model。
