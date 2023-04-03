#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# Importing libraries
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint

# Retrieving data from the google sheets
sheet_data = DataManager().get_data()

# Checking if iataCode is empty
for city in sheet_data:
    
    if city['iataCode'] == '':
        city['iataCode'] = FlightSearch.get_iatacode(city_name=city)
        DataManager.update_code(city)

    flight_data = FlightSearch.search_price(city)

    if flight_data.price < city['lowestPrice']:
        DataManager.update_lowest_price(city=city, lowest_price=flight_data.price)
        city['lowestPrice'] = flight_data.price
        send_message = f"Hey, look! A flight {flight_data.origin_city}-{flight_data.origin_airport} \
        to: {flight_data.destination_city}{flight_data.destination_airport} for just {flight_data.price}\
        pounds. The inbound/outbound date is {flight_data.out_date} untill {flight_data.return_dates}"

        NotificationManager().send_sms(message=send_message)
