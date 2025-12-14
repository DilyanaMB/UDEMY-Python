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

data_dict = data.to_dict()
print(data_dict)

temp_list =data['temp'].tolist()
print(temp_list)

average =sum(temp_list) / float(len(temp_list))
print(average)

print(data['temp'].mean()) # do the same as sum()/len() but with pandas