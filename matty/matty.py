import sys

import boto3
import click
import mattysall
session = boto3.Session(profile_name='matty');
ec2 = session.resource('ec2')
s3 = boto3.client('s3')


def getInstances(project):
    if project:
        filters = [{'Name': 'tag:aws:cloudformation:stack-name', 'Values': ["ssathishkeypair"]}]
        ec2instances = ec2.instances.filter(Filters=filters)
    else:
        ec2instances = ec2.instances.all()
    return ec2instances


@cli.group("instances")
def instances():
    """Commands for instances"""


@instances.command('list')
@click.option('--project', default=None, help="Only instances for project (tag Project:<name>")
def list_instances(project):
    """List all my EC2 instances"""
    instances = getInstances(project)
    for instanceData in instances:
        print(','.join((instanceData.id, instanceData.instance_type, instanceData.state['Name'])))
    return


@instances.command('stop')
@click.option('--project', default=None, help='Only stop EC2 instances')
def stop_instances(project):
    """Stop the EC@ instances of specified project"""
    ec2instances = getInstances(project)
    for oneInstance in ec2instances:
        print("Stopping {0} ..".format(oneInstance.id))
        oneInstance.stop()
    return


@instances.command('start')
@click.option('--project', default=None, help='Only stop EC2 instances')
def stop_instances(project):
    """Stop the EC@ instances of specified project"""
    ec2instances = getInstances(project)
    for oneInstance in ec2instances:
        print("starting {0} ..".format(oneInstance.id))
        oneInstance.start()
    return

@click.command()
def list_alls3():
    """List all S3 buckets"""
    assert isinstance(s3.list_buckets, object)
    allBuckets = s3.list_buckets()
    print("Comming to get the buckets")
    for s3Instance in allBuckets['Buckets']:
        print(s3Instance["Name"])


def list_ec2instance_vpcs():
    for vpcData in ec2.subnets.all():
        print(vpcData)


if __name__ == '__main__':
    print(sys.argv)
    instances()
