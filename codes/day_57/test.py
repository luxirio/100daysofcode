import requests

# Endpoints
AGE_ENDPOINT = "https://api.agify.io?name="
GENDER_ENDPOINT = "https://api.genderize.io?name="

age_response = requests.get(AGE_ENDPOINT+"micheal")
gender_response = requests.get(GENDER_ENDPOINT+"micheal")
print(gender_response.json())