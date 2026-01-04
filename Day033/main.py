import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')
print(response.json())  # actual data

response.raise_for_status()  # raise an error for the specific status if the request doesn't pass

longitude = response.json()['iss_position']['longitude']  # returns specific object from the json
latitude = response.json()['iss_position']['latitude']

iss_position = (longitude, latitude)
print(iss_position)
