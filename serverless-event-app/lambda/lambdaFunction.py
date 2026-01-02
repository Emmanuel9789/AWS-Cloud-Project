import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('FileTable')

def lambda_handler(event, context):
    # Get the first record from the event
    record = event['Records'][0]
    
    # Extract bucket name and file name
    bucket_name = record['s3']['bucket']['name']
    file_key = record['s3']['object']['key']
    
    # Put item in DynamoDB
    table.put_item(
        Item={
            'FieldID': file_key,
            'BucketName': bucket_name
        }
    )
    
    return {
        'statusCode': 200,
        'body': 'File metadata stored'
    }
