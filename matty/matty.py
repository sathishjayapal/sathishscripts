import boto3

session = boto3.Session(profile_name='matty');
ec2 = session.resource('ec2')
for instanceData in ec2.instances.all():
    print(instanceData)
for vpcData in ec2.subnets.all():
    print(vpcData)