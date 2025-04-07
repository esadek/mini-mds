# Mini MDS

[![Build](https://img.shields.io/github/actions/workflow/status/esadek/mini-mds/ci.yml)](https://github.com/esadek/mini-mds/actions/workflows/ci.yml)
[![Supported Python Versions](https://img.shields.io/badge/python-3.9_|_3.10_|_3.11_|_3.12_|_3.13-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/github/license/esadek/mini-mds)](https://github.com/esadek/mini-mds/blob/main/LICENSE)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Lightweight, open source, locally-hosted Modern Data Stack

- Extract and Load: [Polars](https://pola.rs/) and [dlt](https://dlthub.com/)
- Data Quality: [Pandera](https://www.union.ai/pandera/)
- Storage: [DuckDB](https://duckdb.org/)
- Transformation: [dbt](https://www.getdbt.com/)
- Orchestration: [Prefect](https://www.prefect.io/)
- Visualization: [Dash](https://dash.plotly.com/)

## Installation

Prerequisites: Install [git](https://git-scm.com/) and [uv](https://docs.astral.sh/uv/).

Clone repository and change directory:

```bash
git clone https://github.com/esadek/mini-mds.git
cd mini-mds
```

## Usage

Extract, validate, load and transform data:

```bash
uv run prefect/elt.py
```

Visualize data:

```bash
uv run dash/app.py
```

## Architecture

```mermaid
flowchart LR
    A(CSV) --> B[Polars]
    subgraph Prefect
        B --> C[Pandera]
        C --> D[dlt]
        E[dbt Core]
    end
    D --> F[(DuckDB)]
    E <--> F
    F --> G[Dash]
```

## Project Structure

```
mini-mds
├── .github/                # GitHub workflows
├── dash/                   # Dash application
├── dbt/                    # dbt project
├── duckdb/                 # DuckDB warehouse
├── prefect/                # Prefect workflows
├── .editorconfig           # Editor configuration
├── .gitignore              # Untracked files to ignore
├── .python-version         # Default Python version
├── LICENSE                 # MIT license
├── pyproject.toml          # Project metadata
├── README.md               # Documentation
└── uv.lock                 # Dependency lockfile
```
