# Mini MDS

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
python pipelines/elt.py
```

Visualize data:

```bash
python visualize/app.py
```

## Project Structure

```
mini-mds
├── data/                   # DuckDB warehouse
├── pipelines/              # Prefect workflows
├── scripts/                # Scripts
├── transform/              # dbt project
├── visualize/              # Dash application
├── .gitignore              # Untracked files to ignore
├── LICENSE                 # MIT license
├── README.md               # Documentation
└── requirements.txt        # Python dependencies
```
