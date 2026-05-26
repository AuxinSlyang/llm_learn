---
name: llm-learn-devbox
description: Work with the dedicated LLM learning development machine and remote experiment repos used alongside the LLM_Learn workspace. Use when the task involves ssh dev1, remote environment discovery, GPU/CUDA/Python/PyTorch setup, inference-serving experiments, or coordinating local notes with remote experiment code and runs.
---

# LLM Learn Devbox

Use this skill when work spans the local `LLM_Learn/` note workspace and the remote experiment machine.

## Known entry point
- Login: `ssh dev1`
- Hostname: `n37-194-122`
- User: `yangshunlei`
- Home symlink: `/home/yangshunlei -> /data00/home/yangshunlei`

## Known remote learning repo root
- `~/llm_learn`

Currently observed projects:
- `~/llm_learn/micrograd`
- `~/llm_learn/makemore`
- `~/llm_learn/nanogpt`
- `~/llm_learn/nano-vllm`

## Confirmed environment facts
- System python: `/usr/bin/python3`
- System Python version: `3.11.2`
- Known venv: `~/venvs/llm-cu124-py311`
- Shell alias: `llm` → `source ~/venvs/llm-cu124-py311/bin/activate`
- GPU: `Tesla V100-SXM2-32GB`
- Driver: `550.54.15`
- CUDA in active LLM venv: `torch 2.6.0+cu124`, `torch.cuda.is_available() = True`, `cuda 12.4`

Observed package set in the active LLM venv includes at least:
- `torch==2.6.0+cu124`
- `transformers==4.57.3`
- `accelerate==1.13.0`
- `triton==3.2.0`
- `datasets==4.6.1`
- `sentencepiece==0.2.1`
- `tokenizers==0.22.2`
- `safetensors==0.7.0`

## Use this skill to
- reconnect note plans to the remote experiment machine
- inspect environment facts before proposing commands
- map local learning goals to concrete remote experiments
- keep environment notes and repo notes from drifting apart
- choose the right repo on dev1 for the current topic

## Default first moves on dev1
When entering a new dev1 task, prefer:
1. confirm host / user / cwd
2. decide whether the task is note-side or experiment-side
3. if experiment-side, activate `llm` first unless there is a reason not to
4. locate the relevant repo under `~/llm_learn`
5. inspect repo-specific entry files before proposing commands
6. sync conclusions back into the local notes workspace

## Repo-level guidance
- `micrograd`: early autograd / foundational learning
- `makemore`: small language-model learning exercises
- `nanogpt`: model/training-oriented learning repo
- `nano-vllm`: inference/serving oriented repo, especially relevant to the current main line

When the user is focused on inference / serving, prefer starting from:
- `~/llm_learn/nano-vllm`
- then `~/llm_learn/nanogpt` only when model internals matter to the current question

## Keep the boundary clear
- `LLM_Learn/` is the planning and note workspace
- `dev1` is the execution and experiment workspace
- Prefer syncing conclusions back into notes instead of letting knowledge remain only on the remote machine

## Read more context if needed
If the current task depends on environment details or remote layout, read:
- `references/dev1-context.md`
- `references/dev1-first-probe.md`
