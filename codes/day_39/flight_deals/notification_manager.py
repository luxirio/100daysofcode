import os 
from twilio.rest import Client

ACCOUNT_SID = "AC601056324ca57339ab07bce2930786fa"
AUTH_TOKEN = "d22ff04c2fc795d1678a1d1cb6689d2b"

class NotificationManager():
    def __init__(self):
        self.client = Client(ACCOUNT_SID,AUTH_TOKEN)
    
    def send_sms(self, message):
    #This class is responsible for sending notifications with the deal flight details.
        message = self.client.messages.create(
                        body=message,
                        from_='+17197493329',
                        to='+5511941793124'
                    )
        print(message.sid)