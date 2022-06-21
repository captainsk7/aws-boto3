import boto3

AWS_REGION = "us-west-2"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
INSTANCE_ID = 'i-04091b10d2cdc86aa'
SECURITY_GROUP_ID = 'sg-6dbc5f1b'

instance = EC2_RESOURCE.Instance(INSTANCE_ID)

instance_sgs = [
    sg['GroupId'] for sg in instance.security_groups
]

if SECURITY_GROUP_ID in instance_sgs:
    instance_sgs.remove(SECURITY_GROUP_ID)

instance.modify_attribute(
    Groups=instance_sgs
)

print(f'Security Group {SECURITY_GROUP_ID} has been detached from the instance {INSTANCE_ID}')