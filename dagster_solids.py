from dagster import job, op, resource, Field, String
import subprocess

# Define a resource that mimics the Airflow ExampleHook
@resource(config_schema={"conn_message": Field(String, is_required=False, default_value="I got your connection")})
def example_hook_resource(context):
    def get_conn():
        context.log.info(context.resource_config["conn_message"])
    return get_conn

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
    result = subprocess.run(["date"], capture_output=True, text=True)
    date_output = result.stdout.strip()
    context.log.info(f"Date command output: {date_output}")
    return date_output

@op
def bash_sleep_op(context):
    context.log.info("Executing bash command: sleep 5")
    subprocess.run(["sleep", "5"])
    return "Executed sleep command"

@op(config_schema={"my_param": str})
def bash_custom_op(context):
    my_param = context.op_config["my_param"]
    context.log.info(f"Executing custom bash command with param: {my_param}")
    result = subprocess.run(my_param, shell=True, capture_output=True, text=True)
    custom_command_output = result.stdout.strip()
    context.log.info(f"Custom command output: {custom_command_output}")
    return custom_command_output

@job(resource_defs={"example_hook": example_hook_resource})
def custom_operator_job():
    custom_message_op()

@job
def example_job():
    dummy_op()

@job
def tutorial_job():
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
        },
        "resources": {
            "example_hook": {
                "config": {
                    "conn_message": "Custom connection message"
                }
            }
        }
    })

    result_example = example_job.execute_in_process()

    result_tutorial = tutorial_job.execute_in_process(run_config={
        "ops": {
            "bash_custom_op": {
                "config": {
                    "my_param": "echo Parameter I passed in"
                }
            }
        }
    })
