from dagster_solids import tutorial_job

if __name__ == "__main__":
    result = tutorial_job.execute_in_process(run_config={
        "ops": {
            "bash_custom_op": {
                "config": {
                    "my_param": "echo Hello, Dagster!"
                }
            }
        }
    })
    print("Tutorial job executed with result:", result)
