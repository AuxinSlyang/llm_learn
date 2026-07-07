---
type: chapter_notes
project: [[ddia]]
status: in_progress
updated: 2026-07-03
---

# Ch1 Reliable, Scalable and Maintainable Applications Notes

## Takeaways

- 2026-07-03 first pass：本章不是讲某个具体数据库，而是建立 data-intensive system 的三个评价维度：reliability、scalability、maintainability。
- Data-intensive application 的瓶颈通常不是 CPU 算力，而是数据量、数据复杂度、数据变化速度，以及多个数据系统组件之间的一致性和接口边界。
- Ch1 开头列出的五类 building blocks 是现代 data systems 的基础词表：
  - database：保存数据，之后能正确找回。
  - cache：保存昂贵计算或读取的结果，加速后续 read。
  - search index：按关键词或过滤条件高效检索数据。
  - stream processing / message queue：把事件交给另一个进程异步处理。
  - batch processing：周期性处理大量累积数据。
- 这些组件的共同点是都在管理数据：保存、读取、移动、变换、对外提供某种保证。它们的差异不只是名字不同，而是围绕不同 access pattern、performance target 和 correctness guarantee 做优化。
- 用户理解校准：这五类系统“核心差不多”是指它们都处理数据；但系统设计上必须区分它们承诺什么。例如 DB 承诺 durable/correct state，cache 可以丢失后重算，queue 更强调顺序消费和 delivery semantics，search index 更强调 term/filter/ranking，batch 更强调大规模吞吐和失败恢复。
- Reliability：系统在硬件故障、软件 bug、人为操作错误等情况下，仍尽量保持正确服务。它关注的不只是“不挂”，还包括数据正确、完整、可恢复。
- Scalability：负载增长时，系统如何描述 load、衡量 performance，并通过架构/资源/算法调整保持服务质量。关键不是一句“能扩展”，而是先说清 workload 和指标。
- Maintainability：系统长期被不同人维护时，是否容易运维、理解和演进。复杂性本身就是系统风险，好的抽象和清晰 API 是长期资产。
- DDIA 的第一章给后续章节定了方法论：看任何存储、数据库、缓存、索引、消息队列，都要问它在 reliability / scalability / maintainability 上做了什么 tradeoff。

## Code / System Mapping

- MiniLSM：当前只做 toy storage engine，但也能映射三件事：
  - Reliability：WAL / manifest / recovery 后续解决 crash 后数据恢复。
  - Scalability：memtable + SST + compaction 用顺序写和批量 merge 应对写入规模。
  - Maintainability：清晰拆分 `MemTable`、iterator、block、SST、compaction，比一坨 map/file 代码更容易演进。
- RocksDB：Ch1 三个词可以转成面试语言：高可靠依赖 WAL/recovery/checksum；可扩展依赖 LSM、compaction、Bloom/filter、cache；可维护依赖 options、observability、明确的 read/write path。
- TokaDB / TabletServer：一个请求从 RPC 进入 Replica/FSM/Engine，本质上也是数据系统组合；要同时关注正确性、tail latency、故障恢复、运维可观测性和接口简化。
- AI Infra / KVCache：未来看 KVCache storage/offload 时也不能只看吞吐；还要看失败恢复、延迟分位数、调度复杂度、数据一致性和运维成本。

## One Sentence Summary

DDIA Ch1 的核心不是“分布式系统很复杂”，而是给出评价所有数据系统的统一坐标系：可靠、可扩展、可维护；后续每个技术选择都应回到这三个维度看 tradeoff。

## 2026-07-03 Guided Reading Log

### Opening / data-intensive applications

- 当前已理解：现代应用常由 DB / cache / search index / stream processing / batch processing 组合而成。
- 关键修正：这些系统都属于 data systems，但不能粗略认为只是“同一类东西稍微改改”。真正的差异来自：
  - access pattern：按 key 查、全文搜、顺序消费、批量扫描、热点读。
  - performance target：低延迟、高吞吐、tail latency、离线吞吐。
  - correctness guarantee：durability、consistency、cache freshness、delivery semantics、failure recovery。
- 和 MiniLSM 的连接：MiniLSM 只覆盖 DB/storage engine 这一块，优化大量小随机写到 MemTable/WAL，再后台 flush/compact 成 SST。
- 和 TokaDB 的连接：TabletServer 是组合系统，不只要看 RocksDB/LSM，还要看 RPC/API、Replica/FSM、Engine、后台任务、admin/metrics/recovery 如何共同提供对外语义。

### Reliability

- 本节核心问题：系统出问题是常态，可靠性不是“没有故障”，而是发生某些故障时，系统仍能继续正确工作。
- `working correctly` 至少包括：功能符合用户预期、能容忍用户误用、在预期负载下性能足够、阻止未授权访问和滥用。
- 关键区分：
  - fault：系统某个组件偏离预期，例如磁盘坏、进程崩、依赖服务返回脏数据。
  - failure：整个系统对用户不再提供承诺的服务。
- 可靠系统的目标不是把 fault 概率降到 0，而是设计 fault-tolerance 机制，阻止 fault 传播成 user-visible failure。
- 三类 fault：
  - hardware faults：磁盘、内存、电源、网络、机器不可用。传统解法是冗余；云和大规模集群更强调能容忍整机丢失。
  - software errors：系统性 bug、资源耗尽、依赖服务异常、级联故障。它们往往跨节点相关，比随机硬件故障更危险。
  - human errors：配置错误、误操作、错误发布。可靠系统需要好的抽象/API、sandbox、测试、渐进发布、rollback、监控和培训。
- 和 MiniLSM 的连接：WAL / manifest / checksum / recovery 是把 crash fault 阻止为 data loss failure 的机制。
- 和 TokaDB 的连接：TabletServer 的 reliability 要看 RPC 超时/重试、Replica/FSM 状态恢复、Engine 写入语义、监控告警、配置/发布回滚等整条链路，而不是只看 RocksDB 是否可靠。

### Scalability

- 当前理解：Scalability 不是简单“能横向扩展”，而是当负载以某种明确方式增长时，系统有没有可解释、可执行的扩展路径，并保持可接受性能。
- 需要先描述 load parameter，再讨论 scalability。例如：QPS、数据量、读写比例、fan-out、热点 key、单请求扫描范围、cache hit rate。
- 系统应对增长的方式不只有加机器，也包括分片、多副本、cache、index、precompute、异步化、batch、改变数据结构和读写路径。
- 和 MiniLSM 的连接：随机写增多时，MiniLSM/LSM 不每次直接随机写盘，而是 `WAL + MemTable -> flush SST -> compaction`，通过改变写路径和数据结构来承受更多写入。
- 和 TokaDB 的连接：TabletServer 的 scalability 要看 tablet 数量、request QPS、range scan、热点 tablet、replica/follower 负载、tail latency 和资源扩展方式。

### Maintainability

- 用户总结：Maintainability = 可维护性，包含可运维、复杂度控制、可迭代。
- Operability：making life easy for operations。系统要有 metrics/logs/tracing/alerts/admin tools/runbook，出问题能观察、诊断、恢复。
- Simplicity：不是功能少，而是复杂度被控制住；模块边界清楚，数据流和状态流容易理解，API 不制造额外认知负担。
- Evolvability：需求、规模、业务和架构变化时，系统还能继续改；支持迁移、升级、灰度、扩展新功能。
- 和 MiniLSM 的连接：把系统拆成 `MemTable / Iterator / Block / SST / Compaction / WAL / Manifest`，就是用模块化控制复杂度，让后续学习和演进可持续。
- 和 TokaDB 的连接：RPC -> TabletServer -> Replica/FSM -> Engine 的请求路径如果清楚、可观测、可回滚、可定位，才是 maintainable。

### Ch1 overall understanding

- 当前总结：Ch1 是概念性章节，用来建立 data systems 的主体内容和评价框架。
- 先说明现代应用由 DB / cache / search index / stream processing / batch processing 等组件组合而成；这些组件共同构成 data systems。
- 再给出评价 data system 的三条主线：
  - Reliability：发生 fault 时不要轻易变成用户可见 failure。
  - Scalability：负载增长时有明确扩展路径和性能指标。
  - Maintainability：系统长期可运维、复杂度可控、可以继续迭代。
- 后续 Ch2/Ch3/replication/partitioning/transaction 都会回到这三条主线看 tradeoff。
