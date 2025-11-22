print("Welcome to the Pizza Pythong Delivery")
size = input("What size do you want? S, M or L\n")
pepperoni = input("Do you want pepperoni on your pizza? Y or N\n")
extra_chees = input("Do you want extra cheese on your pizza? Y or N\n")

price = 0
if size == "S":
    price = 15
    if pepperoni == "Y":
        price += 2
    if extra_chees == "Y":
        price += 1
elif size == "M":
    price = 20
    if pepperoni == "Y":
        price += 3
    if extra_chees == "Y":
        price += 1
else:
    price = 25
    if pepperoni == "Y":
        price += 3
    if extra_chees == "Y":
        price += 1

print(f"Your final price is ${price:.2f}.")
