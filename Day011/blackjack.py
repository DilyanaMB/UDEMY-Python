from blackjack_art import *
from random import randint

print(logo)
should_continue = True

def get_card():
    new_card = randint(1, 13)
    return new_card

def get_score(cards):
    score = 0
    for c in cards:
        score += c
    return score

def get_comp_cards(score, cards):
    while score < 13:
        new_card = get_card()
        cards.append(new_card)
        score = get_score(cards)
    return cards, get_score(cards)

while should_continue:
    user_cards = [get_card(), get_card()]
    user_score = get_score(user_cards)
    is_take_card = 'y'
    computer_cards = [get_card()]

    while is_take_card == 'y':
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer first card: {computer_cards}")

        is_take_card = input("Type 'y' to get another card, type 'n' to pass:").lower()
        if is_take_card == "y":
            user_cards.append(get_card())
            user_score = get_score(user_cards)

    user_score = get_score(user_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")

    computer_score = get_score(computer_cards)

    if user_score <= 21:
        computer_cards, computer_score = get_comp_cards(computer_score, computer_cards)
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    if computer_score < user_score or (computer_score > 21 and user_score <= 21):
        print("You win! :)")
    elif computer_score == user_score:
        print("It's a tie!")
    else:
        print("You lose! :(")

    user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
    if user_input == 'n':
        should_continue = False
