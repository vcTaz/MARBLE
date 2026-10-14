<div align= "center">
    <h1> <img src="assets/marble.jpg" height=40 align="texttop">MARBLE</h1>
</div>


**M**ulti-**A**gent Coo**R**dination **B**ackbone with **L**LM **E**ngine


**MultiAgentBench** is a modular and extensible framework designed to facilitate the development, testing, and evaluation of multi-agent systems leveraging Large Language Models (LLMs). It provides a structured environment where agents can interact within various simulated environments, utilizing cognitive abilities and communication mechanisms to perform tasks collaboratively or competitively.

<div style="display: flex; justify-content: center;">
  <div style="width: 100; transform: scale(1.0);">
    <img src="assets/benchmark.png" style="width: 100%;" alt="marble">
  </div>
</div>

---

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
  - [Folder Structure](#folder-structure)
  - [Key Components](#key-components)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setup Steps](#setup-steps)
- [Usage](#usage)
  - [Running the Simulation](#running-the-simulation)
  - [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features

- **Modular Design**: Easily extend or replace components like agents, environments, and LLM integrations.
- **Multi-Agent Support**: Model complex interactions between multiple agents with hierarchical or cooperative execution modes.
- **LLM Integration**: Interface with various LLM providers (OpenAI, etc.) through a unified API.
- **Shared Memory**: Implement shared memory mechanisms for agent communication and collaboration.
- **Flexible Environments**: Support for different simulated environments like web-based tasks.
- **Metrics and Evaluation**: Built-in evaluation metrics to assess agent performance on tasks.
- **Industrial Coding Standards**: High-quality, well-documented code adhering to industry best practices.
- **Docker Support**: Containerized setup for consistent deployment and easy experimentation.

<div style="display: flex; justify-content: center;">
  <div style="width: 100; transform: scale(1.0);">
    <img src="assets/engine.jpg" style="width: 100%;" alt="marble">
  </div>
</div>


---


### Install from scratch

MARBLE requires Python 3.9, 3.10 or 3.11. Use a virtual environment, e.g. with anaconda3:

```bash
conda create -n marble python=3.10
conda activate marble
curl -sSL https://install.python-poetry.org | python3
export PATH="$HOME/.local/bin:$PATH"
poetry install
```

Alternatively, with [uv](https://docs.astral.sh/uv/):

```bash
uv venv -p 3.11 .venv
uv pip install -p .venv -e . pytest pytest-asyncio
source .venv/bin/activate
```

### Configure environment variables
Environment variables such as `OPENAI_API_KEY` and `Together_API_KEY` related configs are required to run the code. The recommended way to set all the required variable is
1. Copy the `.env.template` file into the project root with the name `.env`.
```bash
cp .env.template .env
```
2. Fill the required environment variables in the `.env` file. `marble/main.py` loads it automatically.

### Using local or other models
Model calls in the research, database, coding and world scenarios go through [LiteLLM](https://docs.litellm.ai/docs/providers), so any LiteLLM model name works in a config's `llm` field. Models that a config does not name (memory summaries, embeddings, coding tools, planner and evaluator defaults) are read from `MARBLE_DEFAULT_LLM` and `MARBLE_EMBEDDING_MODEL`. For example, with [Ollama](https://ollama.com):

```bash
ollama pull qwen2.5:7b
ollama pull nomic-embed-text
export MARBLE_DEFAULT_LLM="ollama_chat/qwen2.5:7b"
export MARBLE_EMBEDDING_MODEL="ollama/nomic-embed-text"
```

Then set `llm: ollama_chat/qwen2.5:7b` (and `evaluate_llm` under `metrics`) in the scenario config. Agents act through tool calls, so small local models may produce weak or malformed actions.

The werewolf scenario uses the OpenAI client directly. To run it on a local model, set `base_url: http://localhost:11434/v1` and `model_name: qwen2.5:7b` under `villager_config` and `werewolf_config` in its config.

### Running the examples
Each scenario has a run script in `scripts/`. The scripts can be run from any directory:

```bash
bash scripts/research/run_simulation.sh   # research collaboration
bash scripts/database/run_simulation.sh   # database root-cause analysis
bash scripts/werewolf/run_simulation.sh   # werewolf game
bash marble/run_demo.sh                   # coding
```

To run a single config directly, run `python main.py --config_path <config.yaml>` from the `marble/` directory.

#### New branch for each feature

`git checkout -b feature/feature-name` and PR to `main` branch.

#### Before committing

Run `poetry run pytest` to make sure all tests pass (this will ensure dynamic typing passed with beartype) and `poetry run mypy --config-file pyproject.toml .` to check static typing. (You can also run `pre-commit run --all-files` to run all checks)

#### Check github action result

Check the github action result to make sure all tests pass. If not, fix the errors and push again.

## Citation
Please cite the following paper if you find Marble helpful!
```bibtex
@misc{zhu2025multiagentbenchevaluatingcollaborationcompetition,
      title={MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents},
      author={Kunlun Zhu and Hongyi Du and Zhaochen Hong and Xiaocheng Yang and Shuyi Guo and Zhe Wang and Zhenhailong Wang and Cheng Qian and Xiangru Tang and Heng Ji and Jiaxuan You},
      year={2025},
      eprint={2503.01935},
      archivePrefix={arXiv},
      primaryClass={cs.MA},
      url={https://arxiv.org/abs/2503.01935},
}
```

<p align="center">
<a href="https://star-history.com/#Significant-Gravitas/AutoGPT">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=ulab-uiuc/MARBLE&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=ulab-uiuc/MARBLE&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=Significant-Gravitas/AutoGPT&type=Date" />
  </picture>
</a>
</p>
