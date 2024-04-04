
from dagster_solids import example_job

if __name__ == "__main__":
    result = example_job.execute_in_process()
    print("Example job executed with result:", result)
