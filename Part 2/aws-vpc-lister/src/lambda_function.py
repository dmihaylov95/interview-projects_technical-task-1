import boto3
import os
from datetime import datetime

ec2 = boto3.client('ec2')
dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('DYNAMO_TABLE', 'NetworkResources')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        vpcs = ec2.describe_vpcs()['Vpcs']
        for vpc in vpcs:
            table.put_item(Item={
                'ResourceId': vpc['VpcId'],
                'ResourceType': 'VPC',
                'CidrBlock': vpc['CidrBlock'],
                'Tags': vpc.get('Tags', []),
                'Timestamp': datetime.utcnow().isoformat()
            })

        subnets = ec2.describe_subnets()['Subnets']
        for subnet in subnets:
            table.put_item(Item={
                'ResourceId': subnet['SubnetId'],
                'ResourceType': 'Subnet',
                'VpcId': subnet['VpcId'],
                'AvailabilityZone': subnet['AvailabilityZone'],
                'CidrBlock': subnet['CidrBlock'],
                'Tags': subnet.get('Tags', []),
                'Timestamp': datetime.utcnow().isoformat()
            })

        return {
            'statusCode': 200,
            'body': 'VPCs and Subnets successfully saved to DynamoDB'
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': str(e)
        }