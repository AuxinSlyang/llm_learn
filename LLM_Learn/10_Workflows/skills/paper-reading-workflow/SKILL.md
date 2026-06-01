---
name: paper-reading-workflow
description: Guide a structured English research paper reading session for AI, robot learning, embodied AI, systems, USENIX/OSDI/SOSP-style systems papers, or Hugging Face/arXiv papers. Use when the user asks to read, explain, translate, deep-read, quick-read, summarize, or build notes for a paper.
---

# Paper Reading Workflow

## Overview

Do not rush directly into a final summary. Guide the user through the paper in passes, then write notes only after the user has understood the core idea or asks to record.

## Source Order

When metadata is needed:

1. Official arXiv page or PDF
2. Hugging Face paper page when available
3. Official conference page, such as USENIX / OSDI / SOSP / CoRL / RSS / ICRA / NeurIPS
4. Official project page / GitHub
5. Secondary blogs only as explanation support, never as the authority

Preserve title, authors, date, arXiv/DOI/URL, PDF URL, code URL, and venue when available.

## Reading Passes

### Pass 0: Metadata and Position

- What is the paper?
- Which field does it belong to?
- Why read it now in the current roadmap?
- What prior concepts are needed?
- Recommended read mode: `Scan`, `Structured Read`, `Deep Read`, or `Reproduce`.

### Pass 1: Abstract + Introduction

Explain in Chinese, but preserve important English terms.

Answer:

- The problem the paper claims to solve
- Why existing methods are insufficient
- The key insight
- The claimed contributions
- What the reader should watch for in later sections

For the user, teach rather than compress. Translate meaning paragraph by paragraph when needed.

### Pass 2: Structure Map

Build a section map:

- Section title
- What this section is trying to prove
- Which figures/tables matter
- What can be skipped on first pass

### Pass 3: Method

For AI / robot learning papers:

- Task
- Observation
- Action
- Data collection
- Model / policy
- Objective: loss, reward, or optimization target
- Training pipeline
- Inference / deployment path

For systems papers:

- Workload and assumptions
- System architecture
- Key abstraction / data structure / protocol
- Scheduling/resource-management decisions
- Failure handling
- Evaluation setup

### Pass 4: Experiments

Explain:

- What hypotheses are tested
- Baselines
- Metrics
- Main results
- Ablations
- Failure cases or limitations
- Whether the evidence actually supports the claims

### Pass 5: Synthesis

Produce:

- One-sentence takeaway
- 3-5 core ideas
- What changed in the field
- What this means for the user's Robot Learning / VLA / runtime roadmap
- Follow-up papers or experiments

## Note Output

Only write to files when the user asks to record, or when the current workflow explicitly requests note write-back.

Default files:

- `QUICK_READ.md` for Scan / Structured Read
- `DEEP_READ.md` for Deep Read
- `takeaways.md` only when the user explicitly asks for takeaway-only notes

Default paper note sections:

- Metadata
- Why now
- Abstract + Introduction understanding
- Section map
- Method
- Experiments
- Takeaway
- Robot Learning / runtime connection
- Open questions

## Teaching Rules

- If the user says they do not understand, slow down and explain the local concept before moving on.
- Avoid dumping a long summary before the user has the structure.
- Do not overquote copyrighted text; paraphrase and use short excerpts only when necessary.
- Keep formulas tied to intuition and implementation.
- For robotics papers, always map back to `observation -> action -> policy -> eval -> failure -> runtime/data loop`.
