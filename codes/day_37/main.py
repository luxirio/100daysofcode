import requests
import datetime


PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
USERNAME = 'gutavobobo'
TOKEN = 'hashmydi'
TODAY = datetime.datetime.now()
user_params = {
    'token':TOKEN, 
    'username':USERNAME,
    'agreeTermsOfService':'yes',
    'notMinor':'yes'
    }

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

headers = {
    'X-USER-TOKEN':TOKEN
}

graph_params = {
    'id':'graph1',
    'name':'Days of Workout',
    'unit':'days',
    'type':'int',
    'color':'ichou'
}


response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
#print(response.text)


post_params = {
    'date':TODAY.strftime('%Y%m%d'),
    'quantity':'01'

}
POST_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_params['id']}"
post = requests.post(url=POST_ENDPOINT, json=post_params, headers=headers)
print(post.text)

