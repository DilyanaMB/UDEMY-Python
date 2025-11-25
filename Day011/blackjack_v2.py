from blackjack_art import *
import random
from cards import *


def deal_cards():
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(2):
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif u_score ==0:
        return "Win with a Blackjack"
    elif c_score == 0:
        return "Lose, opponent has Blackjack"
    elif u_score >21:
        return "You went over 21. You lose"
    elif c_score > 21:
        return "Opponent went over 21. You win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    print(logo)
    is_game_over = False
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1

    while not is_game_over:
        for i in range(2):
            user_cards.append(deal_cards())
            computer_cards.append(deal_cards())

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score == 21:
            is_game_over = True
        else:
            is_take_card = input("Type 'y' to get another card, type 'n' to pass:").lower()
            if is_take_card == "y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? (y/n) ").lower() == "y":
    print("\n" * 20)
    play_game()