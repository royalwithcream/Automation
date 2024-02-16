import boto3

def list_running_instances():
    # Create a session using Amazon EC2
    ec2 = boto3.resource('ec2')

    # Filter to select only instances in running state
    instances = ec2.instances.filter(
        Filters = [{'Name': 'instance-state-name', 'Values': ['running']}])
    
    for instance in instances:
        #print ({instance.id})
        print (f"Instance ID: {instance.id}")
        print (f"Instance Type: {instance.instance_type}")
        print (f"Public IP Address: {instance.public_ip_address}")
        print (f"Public DNS name: {instance.public_dns_name}")
        print (f"State: {instance.state['Name']}\n")
        


if __name__== "__main__":
    list_running_instances()
