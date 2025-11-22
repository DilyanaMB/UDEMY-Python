from auction_art import *

print(logo)
print("Welcome to the secret auction")
bidders = {}
is_other_bidders = True

while (is_other_bidders):
    print("What is your name?")
    name = input()
    print("What is your bid?")
    bid = float(input())
    print("Are there any other bidders? Type 'yes' or 'no'.")
    will_continue = input().lower()

    bidders[name] = bid

    if will_continue == "no":
        is_other_bidders = False
    else:
        print("\n" * 100)

highest_bidder_price = -1
highest_bidder_name = ""

for person in bidders:
    if bidders[person] >= highest_bidder_price:
        highest_bidder_name = person
        highest_bidder_price = bidders[person]

print(f"The winner is {highest_bidder_name} with a bid of ${bidders[highest_bidder_name]}")
