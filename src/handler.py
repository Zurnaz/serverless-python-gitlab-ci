import json
# https://stackoverflow.com/a/50034121
# import boto3
# from datetime import datetime


def post_request(event, context):
    # TODO add error handling for invalid inputs
    body = json.loads(event['body'])
    result = body
    return {
        'statusCode': 200,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps(result)
    }


def get_request(event, context):
    return {
        'statusCode': 200,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps("This is a get request")
    }
