# Importing libraries
import requests
from pprint import pprint

# Sheet API
## Info
GET_SHEET_URL = "https://api.sheety.co/350d5e8fc7a69a08e3f7c6d3de3b111e/flightDeals/prices"
PUT_URL_END = "https://api.sheety.co/350d5e8fc7a69a08e3f7c6d3de3b111e/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
    ## Retrieve the data
    def get_data(self):
        sheet_info = requests.get(GET_SHEET_URL).json()
        self.destination_data = sheet_info['prices']
        return self.destination_data
    def update_code(city):
        new_data = {
            'price':{
                'iataCode': city['iataCode']
            }
        }
        response = requests.put(
        url=f"{PUT_URL_END}/{city['id']}",
        json=new_data)
    
    def update_lowest_price(city,lowest_price):
        new_data = {
            'price':{
                'lowestPrice': lowest_price
            }
        }
        response = requests.put(
            url=f"{PUT_URL_END}/{city['id']}",
            json=new_data
        )







