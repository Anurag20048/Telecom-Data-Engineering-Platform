# Production Architecture

Sources -> Batch Ingestion -> Bronze -> Quality Gate -> Customer 360 Gold -> PostgreSQL / BI.

Streaming: Kafka -> PySpark Structured Streaming -> event-time windows -> operational metrics.

Airflow coordinates the batch workflow. dbt provides warehouse-level modeling. Prometheus and Grafana provide monitoring configuration. Docker provides local infrastructure.

Production extensions would include cloud object storage, CDC, secrets management, alerting, partitioning, schema evolution, and workload-scale testing.
