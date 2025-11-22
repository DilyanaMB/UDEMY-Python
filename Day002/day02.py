print("Hello"[0])  # take from the zero character - count to the right

print("Hello"[-1])  # take from the last character - count to the left

print(123_345_567)  # ignores underscore - it can be placed for humans to easily read big numbers

print(type("Hello"))  # return the type
print(type(124))
print(type(3.5))
print(type(True))

print("123" + "456")
print(int("123") + int("456"))

print("Numbers of letters in your name: " + str(len(input("Enter your name:"))))

print(5 / 3)  # it will add the numbers for not whole division, so 5 /3 will return 1.66666...

print(5 // 3)  # it will NOT add the numbers for not whole division , so 5//3 will return only 1

print(9**2) # give a number of the power of... so it returns 81

# the order of execution of operation is PEMDAS:
# ()
# **
# *
# /
# +
# -


height = 1.62
weight = 54

# bmi is equal to the person's weight divided by the person's height squared.
# Calculate the bmi using weight and height.
bmi = weight /(height**2)

print(bmi)
print(int(bmi))
print(round(bmi))
print(round(bmi,2))