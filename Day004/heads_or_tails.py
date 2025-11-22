import random

user = int(input("Enter 0 for heads and 1 for tails: \n"))
actual = random.randint(0,1)

if user == 0:
    if actual == 0:
        print("It's heads. You win!")
    else:
        print("It's tails. You lose!")
elif user == 1:
    if actual == 1:
        print("It's tails. You win!")
    else:
        print("It's heads. You lose!")