# Telecom Data Engineering Platform

End-to-end telecom data engineering project demonstrating batch ingestion, real-time event streaming, data quality validation, Customer 360 transformation, PostgreSQL warehousing, Airflow orchestration, dbt modeling, monitoring, and Docker infrastructure.

## Architecture

```text
Telecom Sources -> Batch Ingestion -> Bronze -> Quality Gate -> Customer 360 Gold -> PostgreSQL / BI
                         |
                         +-> Kafka -> PySpark Structured Streaming -> Windowed Metrics

Airflow: orchestration | dbt: warehouse modeling | Prometheus/Grafana: monitoring | GitHub Actions: CI
```

## Features
- Reproducible synthetic source generation: 1,000 customers, 10,000 recharges, 30,000 usage records, 5,000 complaints.
- Quality gate for schema, nulls, duplicate keys, and referential integrity.
- Customer 360 gold transformation and PostgreSQL loading.
- Kafka producer/consumer and PySpark Structured Streaming with event-time windows.
- Airflow DAG for ingestion -> quality -> transformation -> PostgreSQL loading.
- dbt Customer 360 mart and source definitions.
- Prometheus/Grafana monitoring configuration and Docker infrastructure.
- Pytest and GitHub Actions CI.

## Run

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python scripts/generate_data.py
python -m src.quality.validate
python -m src.transform.build_gold
pytest -q
```

Infrastructure: `docker compose -f docker-compose.full.yml up -d`

Generated data is excluded from GitHub through `.gitignore`.

## Structure
`airflow/` orchestration, `dbt/` warehouse models, `spark/` streaming, `streaming/` Kafka, `src/` ingestion/quality/gold, `monitoring/` observability, `tests/` validation.

## Technology Stack
Python, Apache Kafka, Apache Spark, Apache Airflow, dbt, PostgreSQL, Docker, Prometheus, Grafana, Pytest, GitHub Actions

## Scope
Separated from the telecom customer churn analytics project. This repository contains the **data engineering project only**.

## Author
Anurag Pareek - https://github.com/Anurag20048
