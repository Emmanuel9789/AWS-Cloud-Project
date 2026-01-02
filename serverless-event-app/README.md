# Project 2: Serverless Event-Driven Application on AWS

## Overview
This project demonstrates an event-driven architecture on AWS using S3, Lambda, and DynamoDB

- Users upload files to an S3 bucket
- A Lambda function is triggered automatically on each upload
- The Lambda function writes the file metadata (file name, bucket name) to DynamoDB

## Architecture
- **S3**: Stores uploaded files
- **Lambda**: Processes S3 events and updates DynamoDB
- **DynamoDB**: Stores metadata of uploaded files

## How to Test
1. Upload a new file to the configured S3 bucket
2. Wait 2–5 seconds
3. Check the DynamoDB table `FileTable`. A new item with the uploaded file name should appear

## Optional
- Screenshots showing S3, Lambda, and DynamoDB setup are included in `screenshots`

## Key Learnings
- Configured S3 event notifications to trigger Lambda
- Dynamically processed S3 event data in Lambda
- Wrote items to DynamoDB using Boto3
- Learned how AWS event-driven serverless architectures work
