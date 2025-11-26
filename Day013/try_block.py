try:
    age = int(input("What's your age?"))
except ValueError:
    print("That's not a number. Try again with a numerical value such as 15.")
    age = int(input("What's your age?"))
if age > 18:
    print(f"You can drive at age {age}")