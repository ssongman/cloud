import boto3

s3 = boto3.client('s3', aws_access_key_id='AKIAxxxx', aws_secret_access_key='d0rJxxxx')

#s3.upload_file( 'FILE_NAME', 'BUCKET_NAME', 'OBJECT_NAME', ExtraArgs={'Metadata': {'mykey': 'myvalue'})
s3.upload_file( 'readme.txt','userlist.awss3', 'gcplogs/readme2.txt' )

# another mode : upload_file
#s3 = boto3.resource('s3', aws_access_key_id='AKIAxxxx', aws_secret_access_key='d0rJxxxx')
#s3.meta.client.upload_file( 'readme.txt','userlist.awss3', 'gcplogs/readme1.txt' )
