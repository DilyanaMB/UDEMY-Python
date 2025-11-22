programing_dictionary = {
    'bug': 'an error that prevents the program from running as expected.',
    'function': 'a piece of code, that you can easily call over and over again',
}

print(programing_dictionary['bug'])

programing_dictionary['loop'] = 'the action of doing something over and over agin'

print(programing_dictionary)

empty_dictionary = {}
print(empty_dictionary)

# wipe existing dictionary

# programing_dictionary = {}
# print(programing_dictionary)


# edit value
programing_dictionary['loop'] = 'edited the action of doing something over and over agin'
print(programing_dictionary)

# loop through a dictionary

for key in programing_dictionary:
    print(key)
    print(programing_dictionary[key])

# You can have list or dictionary nested as a value in another dictionary
list = ['a', 'b', 'c']
dict = {1: 'apple', 2: 'banana', 3: 'grape'}
nested_dictionary = {'list': list, 'dict': dict}

print(nested_dictionary)

travel_log = {
    "France": ["Lille", 'Paris', 'Dijon'],
    "Germany": ["Stuttgart", "Berlin", 'Cologne']
}

print(travel_log["France"][0])

nested_list = ['A', 'B', ['C', 'D']]

print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visited": ["Lille", 'Paris', 'Dijon'],
        "total_visits": 8
    },
    "Germany": {
        "cities_visited": ["Stuttgart", "Berlin", 'Cologne'],
        "total_visits": 5
    }
}
print(travel_log["Germany"]["cities_visited"][0])
# if you name the dic and then give new values (without specifically relocate to certain key,
# it will just rewrite the dic
print(travel_log)
