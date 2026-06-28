---
type: systems_code_map
track: TokaDB / RocksDB / LSM
status: active
created: 2026-06-28
source_code_root: /home/yangshunlei/tokadb/tokadb-blade/tokadb/tokadb
---

# TokaDB / RocksDB Open-Close Map

## 系统问题

Open / Close 不是普通生命周期函数。对 TokaDB 这种 LSM-backed replica 来说，它同时承担：

- 判断这是新 engine 还是已有 engine。
- 恢复 RocksDB / TokaEngine 的本地状态、OPTIONS、MANIFEST、CF handles。
- 把 TokaDB 的 table / tablet / CF metadata 映射回底层 engine。
- 清理 crash 或 DDL 中断留下的 extra / orphan column families。
- 启动或停止 flusher、compactor、dashboard、consensus、snapshot、FSM。
- 给 replica open / close 的 RTO 和 failure case 留 metrics 边界。

W27 不再重复 table / tablet / RG / migration 概念，重点改为：

```text
Open/Close
-> options / manifest / column family descriptors
-> RocksDB/TokaEngine recovery boundary
-> background work shutdown
-> next open 是否可恢复
```

## 代码根路径

外层目录 `/home/yangshunlei/tokadb/tokadb-blade/tokadb` 同时放了 BUILD、脚本和很多可执行 symlink。

真正源码根是：

```text
/home/yangshunlei/tokadb/tokadb-blade/tokadb/tokadb
```

当前分支状态需要注意：`ysl/graceful_exits` 本地 ahead 1、behind 27，且有本地未提交改动；不要直接无脑 pull。

## RocksDBEngine Open

入口：

```text
/home/yangshunlei/tokadb/tokadb-blade/tokadb/tokadb/engine/rocksdb_engine/rocksdb_engine.cc
```

主流程：

```text
RocksdbEngine::Open(db_name, table_opts, engine_opts)
-> table_opts.Sanitize()
-> engine_opts.Sanitize()
-> IsDBExists(db_name + "/CURRENT")
-> if not exists: engine->Create()
-> if exists: engine->Open()
```

关键行：

- `RocksdbEngine::IsDBExists`：`rocksdb_engine.cc:158`
- `RocksdbEngine::Open(db_name, ...)`：`rocksdb_engine.cc:169`
- `RocksdbEngine::Open()`：`rocksdb_engine.cc:200`

已有 DB 的 open 过程：

```text
RocksdbEngine::Open()
-> LockAndFence()
-> LoadColumnFamilyOptions()
-> LoadOptions()
-> fix DBOptions:
   create_if_missing = false
   create_missing_column_families = true
   error_if_exists = false
-> ListColumnFamilies()
-> build default CF descriptor
-> build data CF descriptors from saved CF options
-> detect extra CFs that exist in RocksDB but not in TokaDB CF options
-> load latest options for extra CFs if possible
-> RocksdbWrapper::Open()
-> collect extra CF handles
-> DropColumnFamilies(extra_cfhs)
-> restore max_open_files = -1 if needed
-> Init(rdb_wrapper, cf_handles)
-> dashboard.Start()
-> compactor.Start()
-> flusher.Start()
-> GetPersistedSequenceRange()
-> SetRecovering(true)
```

需要特别盯：

- `LockAndFence()` 在 `rocksdb_engine.cc:203` 前后，是 open 前的 manifest / fencing 边界。
- `LoadColumnFamilyOptions()` 和 `LoadOptions()` 在 `rocksdb_engine.cc:207-217`。
- `ListColumnFamilies()` 在 `rocksdb_engine.cc:231-235`。
- extra CF 识别和 latest options fallback 在 `rocksdb_engine.cc:252-310`。
- `RocksdbWrapper::Open()` 在 `rocksdb_engine.cc:323-330`。
- extra CF drop 在 `rocksdb_engine.cc:372-388`。
- `Init()`、dashboard、compactor、flusher、recovering 在 `rocksdb_engine.cc:398-430`。

底层 wrapper：

```text
RocksdbWrapper::Open()
-> rocksdb::DB::Open(db_opts, db_name, cf_descs, &cfhs, &db)
-> wrap rocksdb::DB*
-> wrap ColumnFamilyHandle*
```

关键行：

- `RocksdbWrapper::Open`：`rocksdb_wrapper.cc:45`
- `rocksdb::DB::Open`：`rocksdb_wrapper.cc:50`
- `RocksdbWrapper::Close`：`rocksdb_wrapper.cc:276`

## RocksDBEngine Close

入口不是一个显式公开 `Close()`，主要在析构链：

```text
RocksdbEngine::~RocksdbEngine()
-> SetStopped / stop background components
-> flusher.Stop()
-> compactor.Stop()
-> rdb_wrapper.CancelAllBackgroundWork(false)
-> compactor.Wait()
-> dashboard.Stop()
-> clear CF maps and default handle
-> rdb_wrapper->Close()
-> rdb_wrapper.reset()
```

关键行：

- stop flusher / compactor：`rocksdb_engine.cc:130-140`
- wrapper close：`rocksdb_engine.cc:144-154`
- `rocksdb::DB::Close()`：`rocksdb_wrapper.cc:279`

阅读重点：

- close 前是否 flush，取决于更上层 replica close 的 prepare 阶段。
- engine close 负责停止后台线程和释放 handles。
- 如果后台 compaction / flush 没处理干净，下一次 open/recovery 的成本和风险会上升。

## TokaDBEngine Open

入口：

```text
/home/yangshunlei/tokadb/tokadb-blade/tokadb/tokadb/engine/tokadb_engine/tokadb_engine.cc
```

主流程：

```text
TokaDBEngine::Open(table_options, engine_options)
-> Sanitize()
-> allow_ingest_bottommost_level option patch
-> new TokaDBEngine
-> SetTimestampProvider()
-> openImpl()
-> if not disable_compaction_and_flush:
   EngineFlusher::Create()
   flusher.Start()
   meta_store.SetBackgroundFlushStrategy()
   data_store.SetBackgroundFlushStrategy()
   compactor.Start()
```

关键行：

- `TokaDBEngine::Open`：`tokadb_engine.cc:118`
- `openImpl()` 调用：`tokadb_engine.cc:136`
- flusher / compactor start：`tokadb_engine.cc:142-161`

`openImpl()` 是真正的恢复入口：

```text
TokaDBEngine::openImpl()
-> create properties/distance collector factories
-> DataStoreOptions shared_store_opts
-> SetupTableOptions()
-> SetupGlobalOptions()
-> openMetaStore(shared_store_opts, &is_new_engine)
-> if is_new_engine: SetState(kRecovering); return
-> meta_store.GetPersistedSequenceRange()
-> if no meta ops: SetState(kRecovering); return
-> openDataStores(shared_store_opts)
-> SetState(kRecovering)
-> GetPersistedSequenceRange()
-> applied_log_index = seq_range.lower
-> applied_real_timestamp = GetFlushedRealTimestamp()
```

关键行：

- shared options 初始化：`tokadb_engine.cc:343-362`
- open metastore：`tokadb_engine.cc:364-371`
- new engine / empty meta early return：`tokadb_engine.cc:373-387`
- open data stores：`tokadb_engine.cc:389-397`
- recovering state and sequence：`tokadb_engine.cc:399-405`

## MetaStore Open

入口：

```text
/home/yangshunlei/tokadb/tokadb-blade/tokadb/tokadb/engine/tokadb_engine/meta_store.cc
```

主流程：

```text
MetaStore::Open(store_name, store_options, is_new)
-> DataStore::DataStoreExists(store_name, env)
-> if not exists:
   meta_store->create({})
   is_new = true
   return
-> open default CF in read-only mode
-> LoadMetaColumnFamilyDescriptors()
-> Close()
-> reopen with meta CF descriptors
-> is_new = false
```

关键行：

- `MetaStore::Open`：`meta_store.cc:32`
- existence check：`meta_store.cc:39-42`
- first read-only open：`meta_store.cc:53`
- load meta CF descriptors：`meta_store.cc:56-64`
- close and reopen with full descriptors：`meta_store.cc:66-71`

系统含义：

- MetaStore 先用 default CF bootstrap 自己的 CF metadata。
- 然后再用完整 meta CF descriptors reopen。
- 这就是 TokaDBEngine 之后能知道 table CF descriptors 和 valid tablets 的基础。

## DataStore Open

入口：

```text
/home/yangshunlei/tokadb/tokadb-blade/tokadb/tokadb/engine/tokadb_engine/data_store.cc
```

主流程：

```text
DataStore::Open(tablet_id, store_name, store_options, table_cf_desc)
-> store_options.Sanitize()
-> DataStoreExists(store_name, env)
-> apply row cache option
-> new DataStore
-> if not exists: create(table_cf_desc)
-> if exists: open(table_cf_desc)
```

关键行：

- `DataStore::Open`：`data_store.cc:762`
- existence check：`data_store.cc:774`
- create/open branch：`data_store.cc:788-797`

已有 DataStore 的 open 过程：

```text
DataStore::open(table_cf_descs)
-> create metrics registry
-> MethodMetricGuard(Open)
-> store_options.Sanitize()
-> fence()
-> set create_if_missing = false
-> set create_missing_column_families = true
-> set error_if_exists = false
-> addFlushEventListener()
-> handle max_open_files == -1
-> generateTokaEngineColumnFamilyDescriptorsForOpen()
-> detect orphan CFs
-> patch options for bottommost ingest / disable compaction
-> toka_engine::DB::Open()
-> dropOrphanColumnFamilies()
-> keep only user-specified CF handles
-> addColumnFamilyDescriptorsAndHandles()
-> metrics CfStatsManager.Start()
-> restore max_open_files = -1
-> log persisted sequence range
```

关键行：

- `DataStore::open`：`data_store.cc:434`
- `fence()`：`data_store.cc:456-458`
- option fixes：`data_store.cc:460-471`
- orphan CF 注释：`data_store.cc:473-482`
- descriptor generation：`data_store.cc:483-487`
- `toka_engine::DB::Open`：`data_store.cc:510-512`
- drop orphan CF：`data_store.cc:520-523`
- handle registration：`data_store.cc:530-533`
- sequence debug：`data_store.cc:546-549`

和 RocksDBEngine 的对照：

| 维度 | RocksDBEngine | TokaDBEngine / DataStore |
|---|---|---|
| DB existence | `db_name/CURRENT` | `store_name/CURRENT` |
| bootstrap metadata | RocksDB OPTIONS + CF options | MetaStore default CF -> meta CF descriptors |
| CF drift | extra CF | orphan CF |
| bottommost ingest | options patch | options patch |
| background work | flusher / compactor / dashboard | flusher / compactor + per-store background strategy |
| recovery state | `SetRecovering(true)` | `SetState(kRecovering)` |

## TokaDBEngine Close

入口主要是析构：

```text
TokaDBEngine::~TokaDBEngine()
-> SetState(kStopped)
-> bytestore_env->Stop()
-> clear background flush strategy
-> flusher.Stop()
-> compactor.Stop()
-> meta_store.CancelAllBackgroundWork(false)
-> data_store.CancelAllBackgroundWork(false)
-> compactor.Wait()
-> notify manual compaction cv
-> join manual_compaction_runner
-> meta_store.Close()
-> data_store.Close()
-> tablet_stores.clear()
```

关键行：

- `TokaDBEngine::~TokaDBEngine`：`tokadb_engine.cc:684`
- stop env / strategy / flusher：`tokadb_engine.cc:688-704`
- stop compactor / cancel background work / wait：`tokadb_engine.cc:706-715`
- close meta store：`tokadb_engine.cc:726-733`
- close tablet stores：`tokadb_engine.cc:735-744`

`DataStore::Close()`：

```text
DataStore::Close()
-> metrics.reset()
-> if !db return
-> resetHandlesAndDescriptors()
-> db_->Close()
-> db_.reset()
-> store_options_.statistics.reset()
```

关键行：

- `DataStore::Close`：`data_store.cc:1316`
- `toka_engine::DB::Close()`：`data_store.cc:1323`
- `CancelAllBackgroundWork`：`data_store.cc:1335`

## Replica Close Control Path

控制面 close 不是直接关闭 engine，而是状态机 + RPC + TS 内部 close：

```text
GroupMaster CloseReplicaRoutine
-> kOnline/kOpening --kCloseReplicaRequest--> kClosing
-> CloseRequestSubroutine sends close RPC
-> TS ReplicaManager::CloseReplica()
-> Replica::CloseWithSpan()
-> Replica::OnPrepareClosing()
-> ReplicaFsm::PrepareClose()
-> engine_->Flush(FlushAllCFStrategy)
-> Replica::OnClosing()
-> Replica::DoClose()
-> stop CDC / consensus / snapshot
-> replica_fsm_.reset()
-> ReplicaFsm::Close()
-> engine_.reset()
-> Engine destructor closes RocksDB/TokaDBEngine
```

关键行：

- GM close state transitions：`close_replica_routine.cc:112-142`
- `CloseRequestSubroutine`：`close_replica_routine.cc:172-214`
- TS `ReplicaManager::CloseReplica`：`replica_manager.cc:787`
- TS `ReplicaManager::InternalCloseReplica`：`replica_manager.cc:819`
- `Replica::DoPrepareClose`：`replica.cc:1431`
- `Replica::DoClose`：`replica.cc:1460`
- `ReplicaFsm::PrepareClose`：`replica_fsm.cc:252`
- `ReplicaFsm::Close`：`replica_fsm.cc:266`

Zero-copy migration 特殊路径：

```text
ZeroCopyBaseMigrationTask::CloseReplica()
-> cache tablet meta / engine_factory / filesystem / metrics / replica_conf
-> replica_manager_->InternalCloseReplica(...)
-> wait old replica destroyed
-> later reopen engine / continue migration
```

关键行：

- `ZeroCopyBaseMigrationTask::CloseReplica`：`global_migration_manager.cc:246`
- `InternalCloseReplica` 调用：`global_migration_manager.cc:278`

这个路径说明 close 的工程要求更高：迁移需要在 close 之前保存 reopen 所需上下文，否则 replica 销毁后很多对象已经不可用。

## Perf Points

`replica.h` 已经把 open / close 的性能点画成了路线图。

Open 关键点：

```text
kRocksDBEngineCheckExist
kRocksDBEngineLoadOptions
kRocksDBEngineOpen
kRocksDBEngineClearExtraCF
kRocksDBEngineInit
kTokaDBEngineOpenMetaStore
kTokaDBEngineOpenDataStores
kFsmRedoLog
kFsmInitMetaCache
kAfterConsensusStart
kFinishCatchUp
```

Close 关键点：

```text
kBeforePrepare
kFlushEngine
kWaitReplicaRef
kBeforeClose
kStopBgThread
kWaitConsensusNoRef
kWaitInflight
kFsmClose
```

关键行：

- open perf graph：`replica.h:105-190`
- close perf enum：`replica.h:195`

W27 看代码时，每看完一个步骤就要问：

- 这个 perf point 是同步等待、IO、CPU、锁竞争，还是后台任务收敛？
- 这个步骤失败后，下一次 open 是继续恢复，还是需要人工修复？
- 这个步骤和 RocksDB WAL replay / MANIFEST / OPTIONS / CF handles 的关系是什么？

## W27 阅读顺序

1. `replica.h`：先看 open / close perf graph，建立全局路径。
2. `rocksdb_engine.cc`：看 RocksDBEngine open/close 的完整生命周期。
3. `rocksdb_wrapper.cc`：确认最终落到 `rocksdb::DB::Open/Close`。
4. `tokadb_engine.cc`：看 TokaDBEngine 如何先 open MetaStore，再 open DataStores。
5. `meta_store.cc`：看 MetaStore 自举：default CF -> meta CF descriptors -> reopen。
6. `data_store.cc`：看 DataStore open 的 fence / orphan CF / `toka_engine::DB::Open`。
7. `replica_fsm.cc` + `replica.cc`：看 close 前 flush、close 时 reset engine。
8. `close_replica_routine.cc` + `replica_manager.cc`：看 GM/TS control path。
9. `global_migration_manager.cc`：看 zero-copy migration 为什么要 internal close。

## 验收问题

本周结束时至少能讲清：

- 一个 existing replica open 时，从 `Replica::DoOpen` 到 RocksDB / TokaEngine `DB::Open` 的路径。
- 为什么 `CURRENT` 文件是 existence / recovery 的关键边界。
- RocksDBEngine 的 extra CF 和 TokaDBEngine 的 orphan CF 分别是什么。
- 为什么 open 时要 `create_missing_column_families = true`，但 `create_if_missing = false`。
- 为什么 `max_open_files == -1` 要先改成 0，open 完再 set 回 -1。
- close 前为什么要 `PrepareClose -> FlushAllCFStrategy`。
- compactor / flusher / background work shutdown 的顺序。
- zero-copy migration close 为什么要先保存 engine_factory、filesystem、replica_conf、metric_registry。

## 和 AI Core Storage 的迁移

这条路径和后续 KVCache / 3FS / inference runtime 的对应关系：

| TokaDB Open/Close | AI Core Storage / KVCache 对应问题 |
|---|---|
| Manifest / CURRENT / OPTIONS | cache metadata / block table / tier metadata 如何恢复 |
| CF descriptors | KV block namespace / tenant / model / prefix metadata |
| extra/orphan CF cleanup | crash 后部分 block / shard / tier metadata 不一致 |
| Flush before close | offload / checkpoint / migration 前的数据边界 |
| Cancel background work | compaction / prefetch / eviction / DMA 任务收敛 |
| replica close state machine | serving worker drain / migration / live rebalancing |
| open perf points | cold start / warm start / recovery RTO |

结论：Open/Close 是理解“存储系统如何恢复和迁移”的入口，也能迁移到 LLM serving worker 的 cold start、KV cache offload、request live migration 和 3FS client/storage recovery。

## 下一步补洞

- RocksDB `DB::Open` 内部具体做了哪些 recovery：LOCK、CURRENT、MANIFEST、VersionSet、WAL replay、memtable rebuild。
- TokaEngine 和 RocksDB 的差异：shared env / BytestoreEnv / file provider / row cache / bottommost ingest。
- `LockAndFence()` 和 `DataStore::fence()` 的具体实现与 failure case。
- open/close 相关单测：extra CF、orphan CF、failpoint、graceful exit。
- 哪些 metrics 可以用于定位 open 慢 / close 慢 / reopen 慢。
