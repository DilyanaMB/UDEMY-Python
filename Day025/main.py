# with open('weather_data.csv') as data:
#     data_list = data.readlines()

# import csv
#
# with open('weather_data.csv') as data:
#     data_list = csv.reader(data)
#     temperature = []
#
#     for row in data_list:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas
data =pandas.read_csv('weather_data.csv')
print(data['temp'])