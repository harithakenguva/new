import boto3
client = boto3.client('ec2')
response = client.run_instances(
   ImageId='ami-04b6019d38ea93034',
   InstanceType='t2.medium',
   KeyName='git',
   Maxcount=1,
   MinCount=1
)
