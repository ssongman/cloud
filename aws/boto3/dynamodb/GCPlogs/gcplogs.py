from datetime import datetime
import boto3
dynamodb = boto3.resoure('dynamodb')
table = dynamodb.Table('GCPlogs')

now = datetime.now()
time=now.strftime("%Y-%m-%d %H:%M:%S")
#time="2019-07-06 13:01"
message="this is gcplog"

response = table.put_item(
   Item={
        'time': time,
        'message': message,
        'info': {
            'f1':"this is test.",
            'f2':"temp" 
        }
    }
)

