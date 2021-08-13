import json
import pandas as pd
import requests
import urllib3

from secrets import user_payloads

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

data = []

for user in user_payloads:
    print("Requesting Token...\n")
    print(user)
    res = requests.post(auth_url, data=user, params=user)
    print(res)
    access_token = res.json()['access_token']
    print("Access Token = {}\n".format(access_token))
    header = {'Authorization': 'Bearer ' + access_token}

    data_still_out_there = True
    page = 1

    while data_still_out_there == True:
        param = {'per_page': 200, 'page': page}
        my_dataset = requests.get(
            activites_url, headers=header, params=param).json()

        jsonFile_filepath = 'data_test.json'

        jsonFile = open(jsonFile_filepath, "w")
        jsonFile.write(json.dumps(my_dataset))
        jsonFile.close()

        my_df = pd.read_json(jsonFile_filepath)

        if len(my_dataset) == 0:
            data_still_out_there = False

            print(f'found all the data on this user')
        else:
            data.append(my_df)
            print(f'the length of data object is {len(data)}')
            page = page + 1

df = pd.concat(data)

print(df.info())
df.to_csv('big_data.csv', index=False)
