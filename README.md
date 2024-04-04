# Migration from Airflow to Dagster

This repository documents the process of migrating an Airflow project to Dagster, using Dagster's latest APIs for data orchestration and pipeline management. The original Airflow project is located at [soggycactus/airflow-repo-template](https://github.com/soggycactus/airflow-repo-template).

## Overview

The migration involves translating Airflow DAGs and custom operators into Dagster jobs and resources, ensuring that the original project's functionality is maintained in the Dagster implementation.

## Prerequisites

- Python 3.7+
- Dagster and Dagit

## Installation

Install Dagster and Dagit using pip:

```bash
pip install dagster dagit
```

## Running Dagster Jobs

The Airflow DAGs have been translated into the following Dagster jobs:

- `custom_operator_job`: Mimics the Airflow custom operator functionality.
- `example_job`: Equivalent to the Airflow example DAG.
- `tutorial_job`: Translates the Airflow tutorial DAG.

To execute a Dagster job, run the corresponding Python script:

```bash
python3 execute_custom_operator_job.py
python3 execute_example_job.py
python3 execute_tutorial_job.py
```

Each script is configured to execute its respective job in the Dagster environment.

## Dagit Interface

To visualize and interact with the Dagster jobs, use the Dagit UI:

```bash
dagit -f dagster_solids.py
```

This command will start the Dagit web server, allowing you to execute and monitor jobs through a web interface.

## Resources

The `dagster_solids.py` file includes a resource `example_hook_resource` that replicates the functionality of the Airflow `ExampleHook`.

## Documentation

For detailed information on the migration process and how to work with the new Dagster setup, refer to the [Dagster documentation](https://docs.dagster.io/).

## Contributing

Contributions are welcome. Please follow the guidelines provided in the original Airflow project repository.

## License

This project is licensed under the terms of the MIT license.
