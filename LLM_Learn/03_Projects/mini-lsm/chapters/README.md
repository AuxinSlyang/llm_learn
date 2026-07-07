---
type: chapter_index
project: mini-lsm
source_pdf: ../materials/LSM in a Week.pdf
created: 2026-07-01
---

# MiniLSM Chapters

This directory splits `LSM in a Week.pdf` into one learning directory per chapter.
Each chapter keeps `chapter.pdf`, `README.md`, `notes.md`, and `questions.md`.

## Current Course

- [Preface: What is LSM and Why LSM](00_preface/README.md) - `p1-p5`
- [Mini-LSM Course Overview](01_course_overview/README.md) - `p6-p8`
- [Environment Setup](02_environment_setup/README.md) - `p9-p10`
- [Week 1 Overview: Mini-LSM](03_week1_overview/README.md) - `p11-p12`

## Week 1

- [Week 1 Day 1: Memtables](w1d1_memtables/README.md) - `p13-p19`
- [Week 1 Day 2: Merge Iterators](w1d2_merge_iterators/README.md) - `p20-p25`
- [Week 1 Day 3: Block Encoding](w1d3_block_encoding/README.md) - `p26-p29`
- [Week 1 Day 4: SST Encoding](w1d4_sst_encoding/README.md) - `p30-p33`
- [Week 1 Day 5: Read Path](w1d5_read_path/README.md) - `p34-p37`
- [Week 1 Day 6: Write Path](w1d6_write_path/README.md) - `p38-p41`
- [Week 1 Day 7: SST Optimizations](w1d7_sst_optimizations/README.md) - `p42-p45`

## Week 2

- [Week 2 Overview: Compaction and Persistence](04_week2_overview/README.md) - `p46-p52`
- [Week 2 Day 1: Compaction Implementation](w2d1_compaction_implementation/README.md) - `p53-p56`
- [Week 2 Day 2: Simple Compaction Strategy](w2d2_simple_compaction_strategy/README.md) - `p57-p61`
- [Week 2 Day 3: Tiered Compaction Strategy](w2d3_tiered_compaction_strategy/README.md) - `p62-p69`
- [Week 2 Day 4: Leveled Compaction Strategy](w2d4_leveled_compaction_strategy/README.md) - `p70-p75`
- [Week 2 Day 5: Manifest](w2d5_manifest/README.md) - `p76-p79`
- [Week 2 Day 6: Write-Ahead Log](w2d6_wal/README.md) - `p80-p82`
- [Week 2 Day 7: Batch Write and Checksums](w2d7_batch_write_and_checksums/README.md) - `p83-p86`

## Week 3

- [Week 3 Overview: Multi-Version Concurrency Control](05_week3_overview/README.md) - `p87-p88`
- [Week 3 Day 1: Timestamp Key Encoding and Refactor](w3d1_timestamp_key_refactor/README.md) - `p89-p92`
- [Week 3 Day 2: Snapshot Read - Memtables and Timestamps](w3d2_snapshot_read_memtables_timestamps/README.md) - `p93-p97`
- [Week 3 Day 3: Snapshot Read - Engine Read Path and Transaction API](w3d3_snapshot_read_engine_transaction_api/README.md) - `p98-p101`
- [Week 3 Day 4: Watermark and Garbage Collection](w3d4_watermark_gc/README.md) - `p102-p104`
- [Week 3 Day 5: Transaction and Optimistic Concurrency Control](w3d5_transaction_occ/README.md) - `p105-p107`
- [Week 3 Day 6: Partial Serializable Snapshot Isolation](w3d6_partial_serializable_snapshot_isolation/README.md) - `p108-p111`
- [Week 3 Day 7: Compaction Filters](w3d7_compaction_filters/README.md) - `p112-p113`

## Appendix

- [The Rest of Your Life (TBD)](06_rest_of_your_life_tbd/README.md) - `p114`

## Legacy v1

- [Legacy v1: Course Overview](z_legacy_v1_overview/README.md) - `p115`
- [Legacy v1: Block Builder and Block Iterator](z_legacy_v1_block_builder_iterator/README.md) - `p116-p118`
- [Legacy v1: SST Builder and SST Iterator](z_legacy_v1_sst_builder_iterator/README.md) - `p119-p121`
- [Legacy v1: Mem Table and Merge Iterators](z_legacy_v1_memtable_merge_iterators/README.md) - `p122-p125`
- [Legacy v1: Storage Engine and Block Cache](z_legacy_v1_storage_engine_block_cache/README.md) - `p126-p128`
- [Legacy v1: Leveled Compaction](z_legacy_v1_leveled_compaction/README.md) - `p129`
- [Legacy v1: Write-Ahead Log for Recovery](z_legacy_v1_wal_recovery/README.md) - `p130`
- [Legacy v1: Bloom Filters](z_legacy_v1_bloom_filters/README.md) - `p131`
- [Legacy v1: Key Compression](z_legacy_v1_key_compression/README.md) - `p132`
- [Legacy v1: What's Next](z_legacy_v1_whats_next/README.md) - `p133`
