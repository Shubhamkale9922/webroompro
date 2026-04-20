import boto3

s3 = boto3.client('s3')

bucket_name = 'my-static-web-123456'

s3.upload_file('index.html', bucket_name, 'index.html')

print("Deployment Successful!")