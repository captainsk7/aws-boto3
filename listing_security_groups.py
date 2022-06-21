import boto3

AWS_REGION = "us-west-2"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)

security_groups = EC2_RESOURCE.security_groups.all()

print('Security Groups:')
for security_group in security_groups:
    print(f'  - Security Group {security_group.id}')