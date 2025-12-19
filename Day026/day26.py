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
