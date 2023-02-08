import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "c9b22f1f66f0376eedd0aba4ca79c914"

weather_params = {
    "lat":-23.602669,
    "lon": -46.919468,
    "appid":api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.json())