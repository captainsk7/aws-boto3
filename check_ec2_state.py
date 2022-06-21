import boto3

AWS_REGION = "us-west-2"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
INSTANCE_ID = 'i-00979c8fc5667ce79'

instances = EC2_RESOURCE.instances.filter(
    InstanceIds=[
        INSTANCE_ID,
    ],
)

for instance in instances:
    print(f'Instance {instance.id} state is {instance.state["Name"]}')