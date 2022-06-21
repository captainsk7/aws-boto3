import boto3

AWS_REGION = "us-west-2"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
INSTANCE_TYPE = 't2.micro'

instances = EC2_RESOURCE.instances.filter(
    Filters=[
        {
            'Name': 'instance-type',
            'Values': [
                INSTANCE_TYPE
            ]
        }
    ]
)

print(f'Instances of type "{INSTANCE_TYPE}":')

for instance in instances:
    print(f'  - Instance ID: {instance.id}')
    print(f'Instance state: {instance.state["Name"]}')
    print(f'Instance AMI: {instance.image.id}')
    print(f'Instance platform: {instance.platform}')
    print(f'Instance type: "{instance.instance_type}')
    print(f'Piblic IPv4 address: {instance.public_ip_address}')
    print('-'*60)