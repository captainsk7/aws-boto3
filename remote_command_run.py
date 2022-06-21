import boto3
import os
import json
import time

AWS_REGION = "us-west-2"
INSTANCE_ID = 'i-00979c8fc5667ce79'

ssm_client = boto3.client('ssm')
response = ssm_client.send_command(
            InstanceIds=[INSTANCE_ID],
            DocumentName="AWS-RunShellScript",
            Parameters={'commands': ['docker images']}, )

command_id = response['Command']['CommandId']
output = ssm_client.get_command_invocation(
      CommandId=command_id,
      InstanceId=INSTANCE_ID,
    )
print(output)