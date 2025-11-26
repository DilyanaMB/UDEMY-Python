from art import *
import random

print(logo)

def set_difficulty(diff):
    lives_left =-1
    if diff == "easy":
        lives_left = 10
    else:
        lives_left = 5
    return lives_left

def check_if_number_guessed(u_guess, ch_number):
    if u_guess == ch_number:
        is_guessed = True
        print(f"You got it! The answer was {ch_number}.")
    else:
        is_guessed = False
        if u_guess > ch_number:
            print("Too high!")
        else:
            print("Too low!")
    return is_guessed

print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
chosen_number = random.randint(1,100)
lives = set_difficulty(difficulty)

is_number_guessed = False
while lives > 0 and not is_number_guessed:
    print(f"You have {lives} attempts remaining to guess the number.")
    lives -= 1
    user_guess = int(input("Make a guess: "))
    is_number_guessed = check_if_number_guessed(user_guess, chosen_number)

if not is_number_guessed:
    print("You've run out of guesses. Refresh the page to run again.")