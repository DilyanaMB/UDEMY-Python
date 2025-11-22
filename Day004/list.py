fruits = ["apple", "banana", "cherry", "lemon", "grape", "mango"]


print(fruits[1])

# with minus in front of the index, you're getting the value counting from the last one
print(fruits[-2])


fruits[1] = "bananas" # change the value at that index
print(fruits[1])

fruits.append("avocado") # add to the list

print(fruits)
fruits.extend(['pineapple', 'orange', 'pear']) # extend add a whole new list to the previous list
print(fruits)