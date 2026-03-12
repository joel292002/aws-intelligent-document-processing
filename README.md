# Intelligent Document Processing Engine on AWS

## Overview
The Intelligent Document Processing Engine is a serverless AWS-based system that automatically processes uploaded documents, extracts text, and enables keyword-based search across stored content.

The system demonstrates how multiple AWS services can be integrated to build a scalable document processing pipeline without managing servers. Documents uploaded to cloud storage are automatically analyzed using machine learning-based OCR and indexed for retrieval.

This project showcases practical use of serverless cloud architecture for automated document ingestion and search.

---

## Architecture

The system follows a serverless architecture using AWS services.

Workflow:

1. A user uploads a document to an Amazon S3 bucket.
2. The upload event triggers an AWS Lambda function.
3. The Lambda function sends the document to Amazon Textract for text extraction.
4. Extracted text and metadata are stored in a DynamoDB table.
5. A second Lambda function performs document search.
6. API Gateway exposes an endpoint for querying documents.

---



---

## Technologies Used

- Amazon S3
- AWS Lambda
- Amazon Textract
- Amazon DynamoDB
- Amazon API Gateway
- Python
- Boto3 (AWS SDK for Python)

---


---

## Document Processing Pipeline

1. A document is uploaded to the S3 bucket.
2. The S3 event triggers the `ProcessDocument` Lambda function.
3. The Lambda function calls Amazon Textract to extract text.
4. Extracted text and metadata are stored in DynamoDB.

Example stored attributes:

- document_id
- file_name
- upload_time
- processing_status
- extracted_text

---

## Document Search API

The system provides an API endpoint that allows users to search documents by keyword.

Example request: GET /search?q=data



Example response:  

[
{
"file_name": "uploads/article9.pdf",
"document_id": "630e0f29-e18d-4b10-bc4d-ea741c42097c"
}
]



The search Lambda function scans the DynamoDB table and returns documents that contain the search term in the extracted text.

---

## Setup and Deployment (High-Level)

1. Create an Amazon S3 bucket for document uploads.
2. Create a DynamoDB table for document metadata.
3. Deploy the `ProcessDocument` Lambda function.
4. Configure an S3 trigger for the Lambda function.
5. Deploy the `SearchDocuments` Lambda function.
6. Configure API Gateway to expose the search endpoint.

---

## Example Use Cases

- Legal document indexing
- Compliance and policy analysis
- Financial document processing
- Knowledge base document search
- Automated document ingestion pipelines

---




## Project Structure
