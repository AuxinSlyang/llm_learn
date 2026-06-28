# DeepSeek 3FS 研读计划 2026Q3

日期：2026-06-28

## 定位

3FS / Fire-Flyer File System 是准备 DeepSeek `高性能分布式存储工程师` 的主样本系统之一。

它直接覆盖 JD 里的几个关键词：

- 大模型训练 / 推理的数据底座
- 分布式文件系统 / 共享存储层
- SSD / NVMe / RDMA / zero-copy
- metadata / strong consistency / fault tolerance
- dataloader / checkpoint / KVCache offload
- FUSE / kernel I/O stack / user-space I/O path

公开入口：

- GitHub：`https://github.com/deepseek-ai/3FS`
- Paper：`https://arxiv.org/abs/2507.10551`

## 研读目标

不是把 3FS 当普通开源项目浏览，而是用它反推 DeepSeek Storage 岗位能力：

```text
AI workload
-> storage abstraction
-> metadata / consistency
-> IO path / RDMA / SSD
-> client / FUSE / USRBIO
-> dataloader / checkpoint / KVCache
-> 面试系统设计语言
```

## 第一轮：Architecture First Pass

要回答：

- 3FS 要解决的 AI storage 问题是什么？
- 为什么普通本地盘 / NFS / 对象存储不够？
- 它的核心组件有哪些：client、metadata service、storage service、FoundationDB、FUSE、USRBIO。
- 它如何支持训练 dataloader、checkpoint、KVCache。
- 它和传统分布式文件系统、对象存储、shared storage 的区别。

输出：

- `3FS_Architecture_First_Pass.md`
- 一张组件图：client / metadata / storage / network / SSD / GPU workload。

## 第二轮：Consistency / Metadata / Failure

要回答：

- metadata 为什么放在 FoundationDB。
- namespace / inode / chunk / placement 的抽象是什么。
- Chain Replication / CRAQ 解决什么一致性和读扩展问题。
- 节点故障、网络抖动、数据恢复、rebalance 如何影响 tail latency。
- 和 TokaDB / ByteStore 共享存储里的 metadata / recovery 经验怎么对齐。

输出：

- `3FS_Metadata_Consistency_Note.md`
- 面试故事：`如何设计 AI 共享存储的 metadata 和一致性边界`。

## 第三轮：IO Path / RDMA / SSD

要回答：

- 3FS 的读写路径经过哪些层。
- RDMA 在这里绕过了什么瓶颈。
- USRBIO / FUSE / kernel I/O path 的 tradeoff 是什么。
- SSD / NVMe / queue depth / polling / CPU usage 的性能边界在哪里。
- 和 io_uring / SPDK 的关系是什么：相同目标、不同栈位。

输出：

- `3FS_IO_Path_RDMA_SSD_Note.md`
- 面试故事：`如何从 CPU copy / syscall / interrupt / network / SSD 维度优化 IO path`。

## 第四轮：KVCache / Inference Connection

要回答：

- KVCache 为什么可能需要外部存储或 SSD offload。
- 3FS / LMCache 类方案如何让 KVCache 在 HBM / DRAM / SSD / distributed storage 间移动。
- KVCache hit rate、eviction、prefix reuse、tail latency 如何影响推理成本和用户体验。
- 它和 vLLM PagedAttention 的接口在哪里：block/page 管理、offload、remote fetch。

输出：

- `3FS_KVCache_Offload_Note.md`
- 面试系统设计题：`设计一个支撑大模型推理的 KVCache 存储系统`。

## 和现有经验的回接

### TokaDB

- 零拷贝经验 -> 3FS IO path / USRBIO / RDMA / buffer ownership。
- 共享存储经验 -> metadata、consistency、failure recovery、cache invalidation。
- 性能分析经验 -> tail latency、CPU profile、IO profile。

### brpc

- RPC latency / backpressure / bthread / observability -> storage service 和 client 交互。
- zero-copy attachment / serialization -> data path copy 消除。

### ByteStore

- shared storage / placement / replication / recovery -> 3FS 的 storage layer 对照。
- namespace / metadata / availability -> 3FS metadata service 对照。

## 时间安排

```text
2026-W27：README + design overview + 组件图
2026-W28：metadata / consistency / FoundationDB / CRAQ
2026-W29：IO path / RDMA / SSD / FUSE / USRBIO
2026-W30：KVCache / LMCache / vLLM / 面试系统设计题
```

## 面试化产出

到 2026-09，至少形成：

- 一篇 `3FS architecture first pass`。
- 一篇 `3FS IO path / RDMA / SSD`。
- 一篇 `3FS KVCache offload`。
- 一个系统设计讲稿：`设计一个 AI 推理 KVCache 存储系统`。
- 一个对照讲稿：`3FS 和我已有 DB / 共享存储经验如何连接`。

## 一句话回锚

> 3FS 是 DeepSeek Storage 路线的最佳公开样本：用它把 DB / 存储基本盘、RDMA/SSD IO path、KVCache 推理存储和未来机器人/VLA runtime 串成同一条系统能力链。
