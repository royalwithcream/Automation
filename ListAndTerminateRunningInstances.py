import boto3

def list_and_terminate_running_instances():
    # Create a session using Amazon EC2
    ec2 = boto3.resource('ec2')

    # Filter to select only instances in running state
    instances = ec2.instances.filter(
        Filters = [{'Name': 'instance-state-name', 'Values': ['running']}])
    
    running_instance_ids = [instance.id for instance in instances]

    if running_instance_ids:
        # Printing the IDs of instances to be terminated
        print(f"Terminating the following running instances:")
        for instance_id in running_instance_ids:
            print(f"Instance ID: {instance_id}")

        # Actual termination call
        ec2.instances.filter(InstanceIds=running_instance_ids).terminate()
        print(f"Instances have been terminated.")
    else:
        print(f"No running instances to terminate.")


if __name__== "__main__":
    list_and_terminate_running_instances()
