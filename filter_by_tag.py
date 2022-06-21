import boto3

AWS_REGION = "us-west-2"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
INSTANCE_NAME_TAG_VALUE = 'face-detection-anime-pg'

instances = EC2_RESOURCE.instances.filter(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                INSTANCE_NAME_TAG_VALUE
            ]
        }
    ]
)

print(f'Instances with Tag "Name={INSTANCE_NAME_TAG_VALUE}":')

for instance in instances:
    print(f'  - Instance ID: {instance.id}')