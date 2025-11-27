from art import *
from game_data import *
import random

user_score = 0

def choose_random_player():
    return data[random.randint(0, len(data) - 1)]

def choose_second_player(playerA):
    new_player= data[random.randint(0, len(data) - 1)]
    while new_player["name"] == playerA["name"]:
        new_player = data[random.randint(0, len(data) - 1)]
    return new_player


def check_if_more_followers(a, b):
    if a["follower_count"] > b["follower_count"]:
        return True
    return False


def game(score, player1):
    player2 = choose_second_player(player1)
    print(f'Compare B: {player2["name"]}, a {player2["description"]}, from {player2["country"]}')
    print('Who has more followers? Type \'A\' or \'B\': ')
    user_guess = input().lower()
    if user_guess == 'a':
        is_user_correct = check_if_more_followers(player1, player2)
    else:
        is_user_correct = check_if_more_followers(player2, player1)
        player1 = player2

    if is_user_correct:
        score += 1
        print(f'You\'re right! Current score: {score}')
        return True, player1, score

    else:
        print(f'Sorry, that\'s wrong. Final score: {score}')
        return False, player1, score


is_user_right = True
is_first_player = True

while is_user_right:
    if is_first_player:
        print(logo)
        first_player = choose_random_player()
        is_first_player = False

    print(f'Compare A: {first_player["name"]}, a {first_player["description"]}, from {first_player["country"]}')
    print(vs_logo)
    is_user_right, first_player, user_score = game(user_score, first_player)
    print(logo)
