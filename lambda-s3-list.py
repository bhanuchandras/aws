import json
import boto3

def lambda_handler(event, context):
    # Initialize S3 client
    s3 = boto3.client('s3')
    
    # Specify the bucket name
    bucket_name = 'your_bucket_name'
    
    # List objects in the bucket
    response = s3.list_objects_v2(Bucket=bucket_name)
    
    # Extract metadata for each object
    file_list = []
    for obj in response['Contents']:
        # Get object metadata
        file_name = obj['Key']
        last_modified = obj['LastModified'].strftime('%Y-%m-%d %H:%M:%S')
        owner = obj['Owner']['DisplayName']
        size = obj['Size']
        
        # Append metadata to the list
        file_list.append({
            'file_name': file_name,
            'last_modified': last_modified,
            'owner': owner,
            'size': size
        })
    
    # Return the list of objects with metadata
    return {
        'statusCode': 200,
        'body': json.dumps(file_list)
    }
