import requests
import os
from twilio.rest import Client

# Call 5 day / 3 hour forecast data
"""
5 day forecast is available at any location on the globe. It includes weather forecast data with 3-hour step. Forecast is available in JSON or XML format. 

That is, from 0-7 (first day) - (32-39)(last day)
"""

# API request and parameters
OWM_Endpoint = "http://api.openweathermap.org/data/2.5/forecast?"
api_key = "c9b22f1f66f0376eedd0aba4ca79c914"

# Params from Cotia
weather_params = {
    "lat":-23.602669,
    "lon": -46.919468,
    "appid":api_key
}
response = requests.get(OWM_Endpoint, params=weather_params)


# Twilio params
account_sid = "AC601056324ca57339ab07bce2930786fa"
auth_token = "19e0a9fbc341e6cb4ffe7b3be81a2a9d"
client = Client(account_sid, auth_token)

# Organizing information in a dictionary
# TODAY
output_list = []
output_dict = {}
for n in range(0, 8):
    output_list.append(response.json()['list'][n]["weather"][0]['id'])
output_dict['today'] = output_list

# Check if it is going to rain today
if True in [x <= 700 for x in output_dict['today']]:
    message = client.messages.create(
    body="Leve um guarda-chuva, vai chover hoje",
    from_="+17197493329",
    to="+5511941793124"
    )



