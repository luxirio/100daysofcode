# Importing libraries
import requests
import datetime
from pprint import pprint
from flight_data import FlightData

# DATE VARIABLES
DATE_TODAY = datetime.datetime.now()
FINAL_DATE = DATE_TODAY + datetime.timedelta(days=6*30)
DATE_TODAY_FMT = DATE_TODAY.strftime("%d/%m/%Y")
FINAL_DATE_FMT = FINAL_DATE.strftime("%d/%m/%Y")

# API VARIABLES and parameters
FLIGHT_LOCATION_END =  "https://api.tequila.kiwi.com/locations/query/"
FLIGHT_SEARCH_END = "https://api.tequila.kiwi.com/v2/search/"
FLIGHT_API_KEY = "klLgdoae3sg__C7vx4g0Qdpc0k0gnzu8"
headers = {
    'apikey': FLIGHT_API_KEY
}


class FlightSearch:
    #This class is responsible for talking to the Flight Search API
    # api headers

    # Methods
    # Getting the iata coda if there is none
    def get_iatacode(city_name):
        query = {
            "term": city_name['city'], 
            'location_types':'city'
            }

        response = requests.get(url=FLIGHT_LOCATION_END, params=query, headers=headers).json()
        iata_code =  response['locations'][0]['code']
        return iata_code
    
    # searching the price and other variables
    def search_price(city_to):
        query = {
            "fly_from": "LON",
            "fly_to": city_to['iataCode'],
            "date_from": DATE_TODAY_FMT,
            "date_to": FINAL_DATE_FMT,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": 'round',
            "curr": "GBP"
        }
        response = requests.get(url=FLIGHT_SEARCH_END, params=query, headers=headers).json()
        data = response['data'][0]
        
        flight_data = FlightData(
            price=data['price'],
            origin_city = data['route'][0]['cityFrom'],
            origin_airport=data['route'][0]['flyFrom'],
            destination_city=data['route'][0]['cityTo'],
            destination_airport=data['route'][0]['cityCodeTo'],
            out_date=data['route'][0]['local_departure'].split("T"),
            return_date=data['route'][1]['local_departure'].split("T"),
        )
        # testing the prices
        # print(flight_data.destination_city,":",flight_data.price)
        return flight_data
