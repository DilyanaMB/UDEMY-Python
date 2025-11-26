def my_func():
    for i in range(1, 21):
        if i == 20:
            print("You've got it")


my_func()

from random import randint

dice_images = ['1', '2', '3', '4', '5', '6']
dice_num = randint(0, 5)
print(dice_images[dice_num])

year = int(input("What's your year of birth?"))

if 1980 < year < 1994:
    print("You are millennial.")
elif year >= 1994:
    print("You are a Gen Z.")
