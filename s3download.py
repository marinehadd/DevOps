import boto3

s3 = boto3.client('s3')
s3.download_file(Bucket = 'marniebucket',Key='downfile.txt',Filename='downfile.txt')
