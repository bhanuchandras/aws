import boto3

# Set your AWS access key and secret key
access_key = 'YOUR_ACCESS_KEY'
secret_key = 'YOUR_SECRET_KEY'

# Create an S3 client with your credentials
s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)

# Set the name of the S3 bucket you want to query
bucket_name = 'your-bucket-name'

# Use the S3 client to list all objects in the bucket
response = s3.list_objects_v2(Bucket=bucket_name)

# Loop through each object in the response and print its key (file name),
# last modified time, and full path (including the bucket name)
for obj in response['Contents']:
    file_name = obj['Key']
    full_path = 's3://' + bucket_name + '/' + file_name
    last_modified = obj['LastModified']
    print(f'File name: {file_name}, Full path: {full_path}, Last modified: {last_modified}')
