import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC601056324ca57339ab07bce2930786fa"
auth_token = "19e0a9fbc341e6cb4ffe7b3be81a2a9d"
client = Client(account_sid, auth_token)

message = client.messages.create(
  body="Hello from Twilio",
  from_="+17197493329",
  to="+5511941793124"
)

print(message.sid)
