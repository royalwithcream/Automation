import boto3
import time

# initialise a boto3 client
ec2 = boto3.resource('ec2', region_name='eu-west-1')

# function to create and start an EC2 instance
def create_and_start_instance():
    # create a new EC2 instance
    instances = ec2.create_instances(
        ImageId='ami-0905a3c97561e0b69',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='DaveKey'
    )

    instance = instances[0]
    print(f"Instance {instance.id} is being created...")
    instance.wait_until_running()
    instance.reload() # reload the instance attributes

    return instance

# Main function to execute the script
if __name__== "__main__":
    instance = create_and_start_instance()

    # print the SSH connection details
    print(f"instance {instance.id} is ready.")
    print(f"Connect using: ssh -i /path/to/your-key.pem ec2-user@{instance.public_dns_name}")
