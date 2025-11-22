print("Welcome to the rollercoaster.")
height = int(input("What's the height?\n"))

if height > 120:
    print("You can ride.")
    age = int(input("What's the age? "))
    ticket_price = 0
    if age > 18:
        ticket_price = 12
    elif age > 11:
        ticket_price = 7
    elif 45 <= age <= 55:
        ticket_price = 0
    else:
        ticket_price = 5

    wants_photo = input("Do you want a picture? (y/n): ")
    if wants_photo == "y":
        ticket_price += 3

    print(f"Your ticket is ${ticket_price:.2f}")
else:
    print("You are not tall enough")
