import boto30
client = boto3.client('s3')
response = client.run_instances(
   ImageId='ami-04b6019d38ea93034',
   InstanceType='t2.micro',
   KeyName='devops',
   Maxcount=1,
   MinCount=1
)
