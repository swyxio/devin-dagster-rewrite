# Migration from Airflow to Dagster

This repository contains the result of migrating an Airflow project to Dagster, utilizing Dagster's latest APIs and features for data orchestration and pipeline management. The original Airflow project can be found at [soggycactus/airflow-repo-template](https://github.com/soggycactus/airflow-repo-template).

## Why Dagster?

Dagster offers a modern approach to data pipeline orchestration, with an emphasis on development productivity, operational robustness, and observability. This migration aims to leverage Dagster's advantages, such as its strong typing system, flexible execution, and powerful tooling.

## Getting Started with Dagster

To get started with the migrated project:

1. Ensure you have Dagster and Dagit installed. You can install them using pip:

   ```
   pip install dagster dagit
   ```

2. The Airflow DAGs have been translated into Dagster jobs and can be found in the `dagster_solids.py` file.

3. To run a Dagster job, execute:

   ```
   dagit -f dagster_solids.py
   ```

   This will open the Dagit UI where you can execute and monitor your jobs.

## Contributing

Contributions to this project are welcome. Please refer to the original Airflow project for guidelines on contributing to the DAGs and operators.

## Further Documentation

For more information on working with Dagster, visit the [Dagster documentation](https://docs.dagster.io/).
