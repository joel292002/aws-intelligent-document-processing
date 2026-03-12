import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('DocumentMetadata')

def lambda_handler(event, context):

    search_term = event['queryStringParameters']['q']

    response = table.scan()

    results = []

    for item in response['Items']:
        if search_term.lower() in item['extracted_text'].lower():
            results.append({
                "file_name": item['file_name'],
                "document_id": item['document_id']
            })

    return {
        'statusCode': 200,
        'body': json.dumps(results)
    }
