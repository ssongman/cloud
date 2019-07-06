import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Upload a new file
data = open('test.txt', 'rb')
s3.Bucket('userlist.awss3').put_object(Key='test.txt', Body=data)

