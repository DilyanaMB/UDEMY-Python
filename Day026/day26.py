list = [1, 2, 3]
# new_list =[new_item for item in list]

new_list = [item + 1 for item in list]

''' This is equivalent to the following:
new_list =[]
for item in list:
    new_item = item + 1
    new_list.append(new_item)
    '''
print(new_list)

numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]

name = 'Deya'
new_list = [letter for letter in name]

range_list = [num * 2 for num in range(1, 5)]

names = ['Beth', 'Alex', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) <= 4]

names = ['Beth', 'Alex', 'Eleanor', 'Freddie', 'Dave', 'Caroline']
upper_case_names = [name.upper() for name in names if len(name) > 5]
