import requests
from datetime import datetime

MY_LATITUDE = 42.697708
MY_LONGITUDE =23.321867

parameters = {
    'lat': MY_LATITUDE,
    'lng': MY_LONGITUDE,
    'formatted':0
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]

time_now = datetime.now()
print(time_now.hour)


