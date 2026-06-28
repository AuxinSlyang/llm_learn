# DeepSeek Storage 面试准备路线 2026Q3

日期：2026-06-28

## 结论

9-10 月开始认真准备 DeepSeek `高性能分布式存储工程师` 面试是合理目标。

更准确的节奏：

```text
2026-07：补齐 JD mapping 和核心知识框架
2026-08：形成 2-3 个可讲深的系统专题
2026-09：开始模拟面试 / 内推沟通 / 简历叙事打磨
2026-10：如果证据足够，正式投递或密集面试
```

9 月可以开始市场测试；10 月更适合作为比较稳的正式面试窗口。

3FS / Fire-Flyer File System 应该成为这 3-4 个月的主样本系统之一。它和 JD 的匹配非常直接：

```text
3FS
-> AI training / inference workload
-> SSD + RDMA + shared storage layer
-> FoundationDB metadata / strong consistency
-> dataloader / checkpoint / KVCache
```

详细研读计划见：[[2026-06-28_DeepSeek_3FS_Study_Plan_2026Q3]]

## JD 反推能力矩阵

### P0：必须能讲深

| JD 要求 | 需要补的内容 | 你已有优势 | 面试证据 |
|---|---|---|---|
| KVCache 高性能存储 | KVCache 生命周期、prefix reuse、eviction、SSD offload、tail latency、failure recovery | DB / cache / storage 直觉 | `KVCache_Storage_System_Map_v0` |
| 分布式文件系统 / 对象存储 | metadata、namespace、replication、placement、consistency、shared storage | 共享存储相关经验 | `Shared_Storage_Design_Review_v0` |
| Rust/C++、多线程、异步 | C++ 并发、async IO、memory ownership、zero-copy data path | 存储内核工程经验 | TokaDB 零拷贝 / data path 复盘 |
| 分布式系统原理 | Raft/Paxos、lease、事务、故障恢复、tail latency | DB / distributed system 背景 | 2-3 个故障恢复案例 |
| 第一性原理设计 | RocksDB、FoundationDB、ClickHouse 设计范式，而不是套概念 | 系统设计经验 | `RocksDB_LSM_Refresh.md` |

### P1：强加分

| 加分项 | 需要补的内容 | 目标证据 |
|---|---|---|
| RDMA / zero-copy | RDMA verbs 基本模型、memory registration、QP/CQ、send/recv/read/write、zero-copy boundary | `RDMA_Zero_Copy_Note_v0` |
| io_uring / SPDK | kernel bypass、submission/completion queue、polling、NVMe path、direct IO | `IO_Path_io_uring_SPDK_RDMA_Note_v0` |
| SSD/HDD 本地引擎 | block layout、WAL、compaction、cache、write amplification、read amplification | RocksDB / toy storage benchmark |
| FUSE / kernel IO stack | VFS、page cache、direct IO、FUSE overhead、性能可维护性 tradeoff | IO stack note |
| 系统会议级思考 | FAST/OSDI/SOSP/VLDB 风格问题拆解 | 1-2 篇系统 paper structured read |

### P2：第二跳提前埋线

| 方向 | 内容 | 为什么现在补 |
|---|---|---|
| vLLM / PagedAttention | block table、KV cache blocks、prefill/decode、scheduler | 连接 KVCache storage 和推理服务 |
| 大规模推理服务 | routing、load balancing、cache hit、tail latency、multi-tenant | 解释存储系统如何影响用户体验 |
| MoE / long context | expert routing、long-context KV pressure | 面向 DeepSeek 模型系统语境 |

## 现有 DB / 存储经验如何保留

这些不是旧方向，而是核心竞争力：

- TokaDB 零拷贝 / data path：可以抽象成 `memory copy elimination / buffer ownership / IO path / CPU efficiency`。
- TokaDB 共享存储：可以抽象成 `shared storage architecture / consistency boundary / failure recovery / metadata design`。
- brpc：可以抽象成 `RPC latency / bthread / connection / serialization / backpressure / observability`。
- ByteStore：可以抽象成 `large-scale storage system / namespace / data placement / replication / availability / performance isolation`。

表达边界：

- 不写内部业务细节、代码、配置、线上数据。
- 只沉淀可迁移抽象、性能问题、设计 tradeoff、失败模式和学习反思。
- 面试叙事要讲“我怎么设计和定位系统问题”，不是讲内部系统流水账。

## 3-4 个月路线

### 2026-07：基础对齐月

目标：把 JD 拆成能力地图，建立 AI storage 语言。

- 写 `DeepSeek_AI_Core_Storage_JD_Mapping_v0`。
- 复盘 RocksDB / LSM：WAL、memtable、SST、compaction、snapshot、iterator、amplification。
- 写 `KVCache_Storage_System_Map_v0`。
- 扫 vLLM / PagedAttention，只抓 KVCache 管理和 storage boundary。
- 开始 3FS first pass：README、Design Notes、USRBIO、metadata / storage service / FUSE 边界。
- 复盘 TokaDB 零拷贝 / 共享存储：只写可迁移抽象。

通过标准：

- 能 20 分钟讲清 DeepSeek storage 岗位为什么匹配自己。
- 能画出 KVCache storage 和传统 storage engine 的相同点 / 不同点。

### 2026-08：系统深水月

目标：形成 2-3 个能讲到实现边界的专题。

- 专题 1：`RocksDB/LSM -> AI Storage`。
- 专题 2：`KVCache storage / SSD offload / tail latency`。
- 专题 3：`IO path: page cache -> direct IO -> io_uring -> SPDK -> RDMA`。
- 专题 4：`3FS architecture -> metadata / storage / client / USRBIO / FUSE / CRAQ`。
- 补 brpc：bthread、RPC latency、serialization、zero-copy、backpressure、bvar/observability。
- 开始一个小 benchmark 或 design sketch：RocksDB microbench、KVCache block metadata toy、或 IO path benchmark。

通过标准：

- 能做一次 45-60 分钟系统设计 mock：`设计一个支撑大模型推理的 KVCache 存储系统`。
- 能解释为什么单纯把 KV 放 RocksDB 里不一定够，以及瓶颈会在哪。

### 2026-09：面试化月

目标：把知识变成可面试叙事。

- 简历重写为 AI Core Storage 叙事。
- 准备 5 个核心故事：
  - 零拷贝 / IO path 优化
  - 共享存储 / 一致性 / 故障恢复
  - RocksDB/LSM 机制与 tradeoff
  - KVCache storage design
  - brpc / RPC / observability / tail latency
- 做 4-6 次 mock interview。
- 开始小范围沟通 / 内推 / 岗位调研。

通过标准：

- 能回答 `为什么不是继续做 DB，而是 AI Core Storage？`
- 能回答 `为什么不是直接去机器人？`
- 能回答 `你对 KVCache 存储系统的设计判断是什么？`

### 2026-10：正式窗口

目标：进入正式投递 / 面试节奏。

- 如果 9 月 mock 反馈合格，开始 DeepSeek 或同类 AI Core Storage 岗位正式投递。
- 同步准备系统设计、C++/Rust、多线程、分布式一致性、性能分析、IO 栈。
- 机器人方向只作为长期动机，不抢主叙事。

通过标准：

- 有一套明确的 AI Core Storage 面试材料。
- 有至少一个可以展示的 benchmark / design sketch / system note。
- 能稳定把个人经历讲成 `DB/storage -> AI storage -> KVCache/inference -> robot/VLA runtime`。

## 需要重点补的具体内容

### 1. TokaDB / 零拷贝 / 共享存储

要补成可迁移材料：

- 数据从网络 / RPC / buffer / storage engine / disk 的路径。
- 哪些 copy 是必要的，哪些可以消除。
- buffer ownership、lifetime、alignment、batching。
- shared storage 下 metadata、cache consistency、failure recovery。
- tail latency 的观测和定位。

### 2. brpc

重点不是“会用 RPC”，而是：

- bthread / worker model / scheduling。
- connection pooling、backup request、timeout、retry。
- serialization / zero-copy attachment。
- bvar / tracing / latency breakdown。
- backpressure 和 overload protection。

### 3. ByteStore / 共享存储系统

重点理解：

- 系统边界：client、metadata、data node、placement、replication。
- 一致性和可用性边界。
- 对象 / 文件 / block 抽象的 tradeoff。
- 性能隔离、热点、恢复、rebalance。
- 如何支撑训练数据读取或 checkpoint。

### 3.5. 3FS / Fire-Flyer File System

重点理解：

- 为什么 AI workload 下传统文件缓存、预读、局部性假设会失效。
- 3FS 如何把 SSD 和 RDMA 聚合成 disaggregated shared storage layer。
- metadata service、FoundationDB、Chain Replication / CRAQ、storage node、client / FUSE / USRBIO 的边界。
- dataloader、checkpoint、KVCache offload 分别如何使用 3FS。
- 3FS 和 ByteStore / TokaDB 共享存储经验之间的可迁移抽象。

### 4. KVCache

必须讲清：

- KVCache 在 prefill / decode 的生成与访问模式。
- cache block / page / sequence 的映射。
- prefix reuse、eviction、offload、hit rate。
- GPU HBM、CPU memory、SSD、remote storage 的层级。
- 为什么 KVCache storage 直接影响推理成本和用户体验。

### 5. RDMA / SPDK / io_uring

目标不是立刻成为 expert，而是能说清：

- 它们分别绕过了什么瓶颈。
- 适合放在 AI storage 链路的哪一层。
- CPU、kernel、copy、interrupt、polling、queue depth、latency 的 tradeoff。
- 和 zero-copy / remote memory / NVMe 的关系。

## 面试 readiness gate

到 2026-09，如果满足这些，可以开始面试测试：

- [ ] 一份 AI Core Storage 简历叙事。
- [ ] 一篇 DeepSeek JD mapping。
- [ ] 一篇 KVCache storage design note。
- [ ] 一篇 RocksDB/LSM refresh note。
- [ ] 一篇 IO path / RDMA / SPDK / io_uring note。
- [ ] 一篇 3FS architecture study note。
- [ ] 一个小 benchmark 或 design sketch。
- [ ] 5 个能讲 10 分钟以上的项目 / 系统故事。

到 2026-10，如果 mock 和材料都稳定，可以正式投递。

## 一句话回锚

> 这 3-4 个月不是泛学 AI Infra，而是把 DB / 存储系统基本盘升级成 DeepSeek AI Core Storage 的面试证据，再把 KVCache 和推理系统作为第二跳入口。
