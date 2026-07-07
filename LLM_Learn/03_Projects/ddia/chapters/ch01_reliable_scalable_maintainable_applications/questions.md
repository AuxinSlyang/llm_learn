---
type: chapter_questions
project: [[ddia]]
status: in_progress
updated: 2026-07-03
---

# Ch1 Reliable, Scalable and Maintainable Applications Questions

## Questions

- 什么是 data-intensive application？它和 compute-intensive application 的主要瓶颈差异是什么？
- Reliability 只等于 availability 吗？它还包括哪些“数据正确性”要求？
- 为什么描述 scalability 之前必须先描述 load？MiniLSM / RocksDB 的 load 可以怎么描述？
- 性能指标为什么不能只看 average latency？后续读 serving / storage 时应该关注哪些分位数或 tail 指标？
- Maintainability 为什么是系统设计问题，而不是“代码风格问题”？
- 如果把 TokaDB TabletServer 看成一个 data system，它的 reliability / scalability / maintainability 分别应该看哪些证据？

## Follow-ups

- 后续读 Ch3 时，把 storage engine 设计映射回 Ch1 三个维度。
- 后续读 Ch5/Ch6 时，把 replication / partitioning 映射回 reliability / scalability。
- 写 `TabletServer_Request_Path_Index` 时，用 Ch1 三个词作为评估字段。
