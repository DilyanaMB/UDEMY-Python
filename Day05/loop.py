fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

student_scors = [100,99,92,100,94,66,23,45]
total_score = sum(student_scors)
print(total_score)
print(max(student_scors))

new_sum = 0
for score in student_scors:
    new_sum += score
print(new_sum)

max_num = -1
for score in student_scors:
    if score > max_num:
        max_num = score
print(max_num)

# range

for number in range(1,11): #11 is NOT included
    print(number)

for number in range(1,11, 3): #the last is step
    print(number)

sum = 0
for number in range(1,101):
    sum += number
print(sum)
