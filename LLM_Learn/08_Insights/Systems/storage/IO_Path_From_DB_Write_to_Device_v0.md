---
type: systems_note
track: Storage / IO Path
status: draft
created: 2026-07-01
---

# IO Path From DB Write To Device v0

## 要回答的问题

```text
一次 DB write 到底经历了什么？
WAL append 和 fsync 贵在哪里？
LSM 为什么偏爱顺序写？
SSD 为什么也怕随机写和写放大？
HDD / SATA SSD / NVMe SSD 的性能差异来自哪里？
```

## 第一版链路

```text
DB / storage engine
-> write syscall / pwrite / fsync
-> VFS
-> filesystem
-> page cache or direct IO
-> block layer
-> IO scheduler / request queue
-> NVMe / SATA / SCSI driver
-> device queue
-> SSD FTL / NAND or HDD platter/head
-> completion interrupt / polling
```

## 和 mini-lsm 的连接

- WAL append：先保证 crash recovery，再更新 memtable。
- Memtable：把随机更新先留在内存有序结构。
- Flush：把内存数据批量转成 SST，偏向顺序写。
- Compaction：把读放大 / 空间放大 / 写放大之间的 tradeoff 转成后台 IO。

## 和 TokaDB / RocksDB 的连接

- RocksDB WAL / MANIFEST / SST / compaction 最终都落到文件系统和块设备。
- TabletServer tail latency 不只由业务线程决定，也会被 WAL fsync、flush、compaction、page cache、device queue 影响。
- 后续看 brpc / bthread 时，需要把 request scheduling 和 storage IO scheduling 一起看。

## 待补材料

- Linux VFS / page cache / block layer。
- HDD：seek / rotational latency / sequential vs random。
- SSD：NAND page / erase block / FTL / GC / wear leveling / write amplification。
- NVMe：submission queue / completion queue / queue depth / polling。
- SPDK / io_uring：kernel bypass / async IO / polling / userspace driver。
