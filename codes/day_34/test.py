import requests 

api_params = {
    "amount":10,
    "type":"boolean"
}

quiz_request = requests.get("https://opentdb.com/api.php", api_params)
print(quiz_request.json()['results'][0])