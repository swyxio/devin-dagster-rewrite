from dagster_solids import custom_operator_job

if __name__ == "__main__":
    result = custom_operator_job.execute_in_process(run_config={
        "ops": {
            "custom_message_op": {
                "config": {
                    "message": "This is a custom message"
                }
            }
        }
    })
    print("Custom operator job executed with result:", result)
