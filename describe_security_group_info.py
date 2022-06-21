import json
import boto3

AWS_REGION = "us-west-2"
EC2_CLIENT = boto3.client('ec2', region_name=AWS_REGION)
SECURITY_GROUP_ID = 'sg-02f3ffb0621a9dae2'

response = EC2_CLIENT.describe_security_groups(
    GroupIds=[
        SECURITY_GROUP_ID,
    ],
)

print(f'Security Group {SECURITY_GROUP_ID} attributes:')

for security_group in response['SecurityGroups']:
    print(json.dumps(
            security_group,
            indent=4
        )
    )