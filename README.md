# Mini MDS

[![Build](https://img.shields.io/github/actions/workflow/status/esadek/mini-mds/ci.yml)](https://github.com/esadek/mini-mds/actions/workflows/ci.yml)
[![Supported Python Versions](https://img.shields.io/badge/python-3.9_%7C_3.10_%7C_3.11_%7C_3.12-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/github/license/esadek/mini-mds)](https://github.com/esadek/mini-mds/blob/main/LICENSE)

Lightweight, open source, locally-hosted Modern Data Stack

- Extract & Load: [dlt](https://dlthub.com/)
- Data Quality: [Great Expectations](https://greatexpectations.io/)
- Storage: [DuckDB](https://duckdb.org/)
- Transformation: [dbt](https://www.getdbt.com/)
- Orchestration: [Prefect](https://www.prefect.io/)
- Visualization: [Dash](https://dash.plotly.com/)

## Installation

Clone repository and change directory:

```bash
git clone https://github.com/esadek/mini-mds.git
cd mini-mds
```

Install required packages:

```bash
pip install -r requirements.txt
```

Add dbt connection profile:

```bash
python scripts/add_profile.py
```

## Usage

Extract, validate, load and transform data:

```bash
python prefect/elt.py
```

Visualize data:

```bash
python dash/app.py
```

## Project Structure

```
mini-mds
├── .github/                # GitHub workflows
├── dash/                   # Dash application
├── dbt/                    # dbt project
├── duckdb/                 # DuckDB warehouse
├── prefect/                # Prefect workflows
├── scripts/                # Scripts
├── .gitignore              # Untracked files to ignore
├── LICENSE                 # MIT license
├── README.md               # Documentation
└── requirements.txt        # Python dependencies
```
