import random
import hangman_lost_lives

word_list = ['aardvark', 'baboon', 'camel']
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/''')

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

while lives > 0 and not is_user_win:
    letter = input("Guess a letter: ").lower()
    if letter in guessed_letters:
        print("You already guessed that letter. Try.")
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
            print(hangman_lost_lives.hangman)
        else:
            lives = lives - 1
            guessed_letters.append(letter)
            print(f"You guessed {letter}, that's not in the word. You lose a life.")
            if lives == 0:
                print(hangman_lost_lives.hangman_minus_six)
            elif lives ==1:
                print(hangman_lost_lives.hangman_minus_five)
                print(f"****************************{lives}/6 LIVES LEFT****************************")
            elif lives == 2:
                print(hangman_lost_lives.hangman_minus_four)
                print(f"****************************{lives}/6 LIVES LEFT****************************")
            elif lives == 3:
                print(hangman_lost_lives.hangman_minus_three)
                print(f"****************************{lives}/6 LIVES LEFT****************************")
            elif lives == 4:
                print(hangman_lost_lives.hangman_minus_two)
                print(f"****************************{lives}/6 LIVES LEFT****************************")
            elif lives == 5:
                print(hangman_lost_lives.hangman_minus_one)
                print(f"****************************{lives}/6 LIVES LEFT****************************")
    is_user_win =not any(x == "_" for x in presented_word)

if is_user_win:
    print("You win!")