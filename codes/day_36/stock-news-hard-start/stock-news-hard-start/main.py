#Importing packages
import requests
import datetime
import os
from twilio.rest import Client

# Company info
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# APIs CONFIGS
# Endpoints
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "5IKIOUKPM7QZXSWJ"
NEWS_API = "89f2f4ec3808494eb7f2398a27e50b2a"
#Twillio
account_sid = 'AC601056324ca57339ab07bce2930786fa'
auth_token = '19e0a9fbc341e6cb4ffe7b3be81a2a9d'

#Date values
# Date parameters and values
YESTERDAY = (datetime.date.today() - datetime.timedelta(days = 1))
BEFORE_YESTERDAY = (datetime.date.today() - datetime.timedelta(days = 2))

# API Parameters
stock_parameters = {'function':'TIME_SERIES_DAILY_ADJUSTED', 'symbol':STOCK, 'apikey':STOCK_API_KEY}
news_parameters = {'q':COMPANY_NAME, 'from':str(YESTERDAY), 'sortBy':'popularity', 'apiKey':NEWS_API}

## STEP 1:
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

# Stock retrieve info:
stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_data = stock_response.json()

# Date parameters and values
YESTERDAY_CLOSE = float(stock_data['Time Series (Daily)'][str(YESTERDAY)]['4. close'])
B_YESTERDAY_CLOSE = float(stock_data['Time Series (Daily)'][str(BEFORE_YESTERDAY)]['4. close'])

DIFFERENCE = abs((YESTERDAY_CLOSE) - (B_YESTERDAY_CLOSE))

if ((DIFFERENCE/(B_YESTERDAY_CLOSE))*100) >= 5:
    print('')
else:
    print("Nothing changes significantly")


news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
news_data = news_response.json()
top_articles = news_data['articles'][:4]

# Setting up and sending a message
client = Client(account_sid, auth_token)
## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.
formatted_msg = [f"Head: {x['title']}.\nDescription: {x['description']}\n" for x in top_articles]

for article in formatted_msg:
    client.messages.create(
        body=article,
        from_=+17197493329,
        to=+5511941793124,
    )

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""