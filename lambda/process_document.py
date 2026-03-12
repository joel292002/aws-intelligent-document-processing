import boto3
import json
import uuid
from datetime import datetime

textract = boto3.client('textract')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('DocumentMetadata')

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    document = event['Records'][0]['s3']['object']['key']

    response = textract.detect_document_text(
        Document={
            'S3Object': {
                'Bucket': bucket,
                'Name': document
            }
        }
    )

    extracted_text = ""

    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            extracted_text += item["Text"] + "\n"

    document_id = str(uuid.uuid4())

    table.put_item(
        Item={
            'document_id': document_id,
            'file_name': document,
            'upload_time': str(datetime.now()),
            'processing_status': 'processed',
            'extracted_text': extracted_text
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Document processed successfully')
    }
