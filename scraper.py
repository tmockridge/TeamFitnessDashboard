import json
import pandas as pd
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

payload = {
    'client_id': "68613",
    'client_secret': '550f55fa6771596280712d36140be833c370b8b5',
    'refresh_token': '898bc1f877c426da235138fc1124316f23afd29c',
    'grant_type': "refresh_token",
    'f': 'json'
}


print("Requesting Token...\n")
res = requests.post(auth_url, params=payload)
print(res)
access_token = res.json()['access_token']
print("Access Token = {}\n".format(access_token))

pages = [1,2,3,4,5,6,7,8]
for page in pages:
    
    header = {'Authorization': 'Bearer ' + access_token}
    param = {'per_page': 200, 'page': page}
    my_dataset = requests.get(activites_url, headers=header, params=param).json()
    
    
    jsonFile = open(f"data{page}.json", "w")
    jsonFile.write(json.dumps(my_dataset))
    jsonFile.close()
