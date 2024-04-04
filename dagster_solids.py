from dagster import job, op

@op(config_schema={"message": str})
def custom_message_op(context):
    message = context.op_config["message"]
    context.log.info(f"Returning the message: {message}")
    return message

@op
def dummy_op(context):
    context.log.info("Dummy op executed")
    return "Dummy result"

@op
def bash_date_op(context):
    context.log.info("Executing bash command: date")
    # Here you would include the logic to execute the 'date' command
    return "Executed date command"

@op
def bash_sleep_op(context):
    context.log.info("Executing bash command: sleep 5")
    # Here you would include the logic to execute the 'sleep 5' command
    return "Executed sleep command"

@op(config_schema={"my_param": str})
def bash_custom_op(context):
    my_param = context.op_config["my_param"]
    context.log.info(f"Executing custom bash command with param: {my_param}")
    # Here you would include the logic to execute the custom command with Jinja templating
    return f"Executed custom command with param: {my_param}"

@job
def custom_operator_job():
    custom_message_op()

@job
def example_job():
    dummy_op()

@job
def tutorial_job():
    # Define the execution logic of the tutorial job
    date_result = bash_date_op()
    sleep_result = bash_sleep_op()
    custom_result = bash_custom_op()

    # Define dependencies if needed
    # date_result >> sleep_result
    # date_result >> custom_result

if __name__ == "__main__":
    # Execute the jobs with the appropriate run configuration
    result_custom_operator = custom_operator_job.execute_in_process(run_config={
        "ops": {
            "custom_message_op": {
                "config": {
                    "message": "Here is the message!"
                }
            }
        }
    })

    result_example = example_job.execute_in_process()

    result_tutorial = tutorial_job.execute_in_process(run_config={
        "ops": {
            "bash_custom_op": {
                "config": {
                    "my_param": "Parameter I passed in"
                }
            }
        }
    })
