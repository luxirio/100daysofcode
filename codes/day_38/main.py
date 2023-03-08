import requests
import datetime

# GLOBAL VARIABLES
GENDER = 'male'
MY_WEIGHT = 78
MY_HEIGHT = 179
MY_AGE = 26 
TODAY = datetime.datetime.now()
APP_ID = '3a730fe6'
API_KEY = 'e8ab61289a2742a3653c8349509bd3aa'
ENDPOINT_EXERCISE = 'https://trackapi.nutritionix.com/v2/natural/exercise'
ENDPOINT_SHEET = 'https://api.sheety.co/350d5e8fc7a69a08e3f7c6d3de3b111e/myWorkouts/workouts'

# User input info for retrieving exercise info
query = input('Which exercises you did?: ')

# Exercise info
exercise_headers = {
    'x-app-id':APP_ID,
    'x-app-key':API_KEY,
}

query_params_exercise = {
    "query":query,
    "gender":GENDER,
    "weight_kg":MY_WEIGHT,
    "height_cm":MY_HEIGHT,
    "age":MY_AGE
}

# Retrieving exercise response
exercise_response = requests.post(url=ENDPOINT_EXERCISE, headers=exercise_headers, json=query_params_exercise)
# Working with google sheets


query_params_sheet = {}
sheet_header = {
    'Authorization':'Basic bHV4aXJpb3g6bHV4aXJpbzE0Nw'
}

for exercise in exercise_response.json()['exercises']:
    query_params_sheet ={
        'workout':{
            'date':TODAY.strftime(('%d/%m/%Y')),
            'time': TODAY.strftime(('%H:%M:%S')),
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }
    requests.post(url=ENDPOINT_SHEET, json=query_params_sheet, headers= sheet_header)
