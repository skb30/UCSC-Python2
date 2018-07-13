#!/usr/bin/env python
import boto3

ec2 = boto3.resource('ec2')

def create_instance(ami):
    instance = ec2.create_instances(
        ImageId=ami,
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro')
    return instance

def print_instance():
    for instance in ec2.instances.all():
        print(instance.id, instance.state)

def terminate_instance(id):

    instance = ec2.Instance(id)
    response = instance.terminate()
    print(response)

# create_instance('ami-25110f45')
print_instance()
# terminate_instance('i-0857b694ed013fb75')
#  print_instance()
