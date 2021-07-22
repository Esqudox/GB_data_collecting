
import requests
import json
import time


def get_data(service, appid, city):
    while True:
        time.sleep(1)
        url = f'{service}?q={city}&appid={appid}'
        response = requests.get(url)
        if response.status_code == 200:
            print(url)
            break
    return response.json()

service = 'https://samples.openweathermap.org/data/2.5/weather'
appid = 'f8ef6b00f1f6a6cfbd16d1a51f420fe4'
city = 'Moscow'

r = get_data(service, appid, city)

print(r)

with open('data2.json', 'w') as f:
    r_json = json.dump(r, f)