#This is a script for Lambda that runs once per hour, checks if any of the EC2 instances have stopped and restarts them
#It is ran in  AWS Lambda

import boto3

def lambda_handler(event, context){
    #create EC2 client
    ec2 = boto3.resource("ec2")

    for instance in ec2.isinstances.all():
        state = instance.state["Name"]
        if state == "stopped":
            try:
                isinstance.start()
            except:
                print("something went wrong")
}

