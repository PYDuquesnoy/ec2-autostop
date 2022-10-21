import boto3

region = 'eu-west-1'

#ec2 = boto3.client('ec2', region_name=region)
ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    # create filter for instances in running state
    filters = [
        {
            'Name': 'instance-state-name', 
            'Values': ['running']
        }
    ]
    
    # filter the instances based on filters() above
    instances = ec2.instances.filter(Filters=filters)

    # instantiate empty array
    RunningInstances = []

    for instance in instances:
        # for each instance, append to array and print instance id
        RunningInstances.append(instance.id)
        print(instance.id)

    ec2.stop_instances(InstanceIds=RunningInstances)  
    print('stopped the EC2 instances: ' + str(instances))