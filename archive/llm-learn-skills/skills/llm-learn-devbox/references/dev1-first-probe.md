# dev1 first probe

## Base environment
- hostname: `n37-194-122`
- user: `yangshunlei`
- home actual path: `/data00/home/yangshunlei`
- system python: `/usr/bin/python3`
- system python version: `3.11.2`
- system pip: `/usr/bin/pip3`

## Virtual environments
Known venv:
- `~/venvs/llm-cu124-py311`

Shell alias from `.zshrc`:
- `llm` -> `source ~/venvs/llm-cu124-py311/bin/activate`

## GPU / CUDA / torch facts
- GPU: `Tesla V100-SXM2-32GB`
- driver: `550.54.15`
- `nvidia-smi` present
- in the `llm` venv:
  - `torch==2.6.0+cu124`
  - `torch.cuda.is_available() == True`
  - `torch.version.cuda == 12.4`
  - device count = `1`

## Observed package set in the active LLM venv
- `accelerate==1.13.0`
- `datasets==4.6.1`
- `numpy==2.3.5`
- `pandas==3.0.1`
- `safetensors==0.7.0`
- `sentencepiece==0.2.1`
- `tokenizers==0.22.2`
- `torch==2.6.0+cu124`
- `transformers==4.57.3`
- `triton==3.2.0`

## Repo hints
- `~/llm_learn/nano-vllm` is likely the most directly relevant repo for inference / serving learning
- `~/llm_learn/nanogpt` is useful when model internals or training-side intuition matters
- `~/llm_learn/micrograd` and `~/llm_learn/makemore` are more foundational / pedagogical

## Practical default move
If the task is about inference / serving and needs remote execution:
1. `ssh dev1`
2. `llm`
3. `cd ~/llm_learn/nano-vllm`
4. inspect repo entry files before running anything
