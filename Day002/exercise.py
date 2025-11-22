print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percent = float(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
your_bill = bill//people

if tip_percent == 10:
    your_bill += your_bill * 0.1
elif tip_percent == 12:
    your_bill += your_bill * 0.12
else:
    your_bill +=  your_bill * 0.15

print(f"Each person should pay: ${your_bill:.2f}")
