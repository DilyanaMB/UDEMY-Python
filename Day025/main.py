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

print(data['temp'].max())

# print(data['condition'])
print(data.condition) # pandas automatically collect into a series all columns,
# e.g. if in the file there is column Emo then you can call data.Emo


# Get data in row
print(data[data.day == 'Monday'])

print(data[data.temp==data.temp.max()])

# Extract particular value from row

monday = data[data.day == 'Monday']

print(monday.condition)

monday_temp = monday.temp[0]
monday_fahrenheit = monday_temp * 9/5 + 32
print(monday_fahrenheit)

# Create a dataFrame from scratch

data_dict = {
    'students': ['Emo', 'Victor', 'Deya'],
    'scores': [90, 80, 70],
}

data_dict_from_scratch = pandas.DataFrame(data_dict)
print(data_dict_from_scratch)

data_dict_from_scratch.to_csv('students.csv')