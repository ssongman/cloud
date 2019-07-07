from __future__ import print_function # Python 2/3 compatibility
from datetime import datetime

import webapp2

import os
import time

import json
import decimal



# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)



# Main
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('this page is log saver which can transfer log to aws dynamodb\n')


# [START gae_python_request_timer]
class TimerHandler(webapp2.RequestHandler):
    def get(self):
        from google.appengine.runtime import DeadlineExceededError

        try:
            time.sleep(3)
            self.response.write('sleep 3 seconds Completed.')
        except DeadlineExceededError:
            self.response.clear()
            self.response.set_status(500)
            self.response.out.write(
                'The request did not complete in time.')
# [END gae_python_request_timer]


# [START gae_python_environment]
class PrintEnvironmentHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        for key, value in os.environ.iteritems():
            self.response.out.write(
                "{} = {}\n".format(key, value))
# [END gae_python_environment]


# [START gae_python_request_ids]
class RequestIdHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        request_id = os.environ.get('REQUEST_LOG_ID')
        self.response.write(
            'REQUEST_LOG_ID={}'.format(request_id))
# [END gae_python_request_ids]


# [START gae_python_sendbox]
class SendboxHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        somevalue = os.environ.get('PATH_TRANSLATED')
        logs_put_item(somevalue)
        self.response.write(
            '1111-PATH_TRANSLATED={}'.format(somevalue))
# [END gae_python_sendbox]



def logs_put_item(message):
    import boto3
    #dynamodb = boto3.resource('dynamodb')
    #dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
    dynamodb = boto3.resource('dynamodb', 
                              region_name='AP_NORTHEAST_2',
                              endpoint_url='https://dynamodb.AP_NORTHEAST_2.amazonaws.com',
                              aws_access_key_id='AKIAZY5WUZS5VIEPXQTZ',
                              aws_secret_access_key='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')
    
    table = dynamodb.Table('GCPlogs')
    
    now = datetime.now()
    time=now.strftime("%Y-%m-%d %H:%M:%S")
    #time="2019-07-06 13:01"
    #message="this is gcplog"
    
    response = table.put_item(
       Item={
            'time': time,
            'message': message,
            'info': {
                'plot':"Nothing happens at all.",
                'rating': decimal.Decimal(0)
            }
        }
    )





app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/timer', TimerHandler),
    ('/environment', PrintEnvironmentHandler),
    ('/requestid', RequestIdHandler),
    ('/sendbox', SendboxHandler)
], debug=True)
