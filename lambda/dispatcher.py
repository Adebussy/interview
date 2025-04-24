#MAIN LOGIC(OR.JS)

import json
import boto3
import os

sqs = boto3.client('sqs')
queue_url = os.environ['SQS_QUEUE_URL']

def handler(event, context):
    body = json.loads(event['body'])
    message = {
        'userId': body.get('userId'),
        'channel': body.get('channel'),
        'subject': body.get('subject'),
        'message': body.get('message')
    }
    
    sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(message)
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'status': 'queued'})
    }
