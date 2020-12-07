import boto3
import json
import os

# initialize boto3 resources
dynamo = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamo.Table(os.environ['tablename'])


def lambda_handler(event, context):

    try:
        # get current value from ddb
        resp = table.get_item(Key={'id': 1})
        current = resp['Item']['visitors']

        # add 1
        current += 1

        # update ddb
        table.update_item(
            Key={'id': 1},
            UpdateExpression='SET visitors = :val1',
            ExpressionAttributeValues={':val1': current}
        )

        # return to website
        return {
            "body": json.dumps({
                'count': current, }),
            'statusCode': 200,
            "headers": {
                "Access-Control-Allow-Origin": "https://*.hdsouza.com",
                "Access-Control-Allow-Headers": "application/json",
                'Access-Control-Allow-Methods': 'OPTIONS,POST',
                "Access-Control-Allow-Credentials": 'true'
            },
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'error': str(e)
        }
