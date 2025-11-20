import random
from  hangman_art import *
from hangman_words import word_list

print(hangman_logo)

chosen_word = random.choice(word_list)
letters_count = len(chosen_word)
guessed_letters = []
presented_word = []


for i in range(letters_count):
    presented_word.append("_")
presented_word_str = "".join(presented_word)
print("Word to guess: " + presented_word_str)

lives = 6
is_user_win = False

def print_left_lives(lives):
    print(f"**************************** {lives}/6 LIVES LEFT****************************")

while lives > 0 and not is_user_win:
    letter = input("Guess a letter: ").lower()
    if letter in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue
    else:
        if letter in chosen_word:
            temp_index = 0
            for i in chosen_word:
                if i == letter:
                    presented_word[temp_index]=letter
                temp_index +=1
            presented_word_str = "".join(presented_word)
            print(presented_word_str)
            print(hangman[lives])
        else:
            lives = lives - 1
            guessed_letters.append(letter)
            print(f"You guessed {letter}, that's not in the word. You lose a life.")
            print(hangman[lives])
            print_left_lives(lives)
    is_user_win =not any(x == "_" for x in presented_word)

if is_user_win:
    print("**************************** You win! ****************************")
