import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('chess')

def lambda_handler(event,context):
    response = table.get_item(
        Key = {
            'id':'queen'
        }
    )
    print(response)
    return {
        'statuscode':200,
        'body':'response'
    }
