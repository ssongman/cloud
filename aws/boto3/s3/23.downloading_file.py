import boto3

s3 = boto3.client('s3')
#s3.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')
s3.download_file('userlist.awss3', 'test1.txt', 'test_local.txt')

