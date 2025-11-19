from random import random

word_list = ['aardvark','baboon','camel']
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/''')
print("Word to guess: _______")
chosen_word = random.choice(word_list)
print(chosen_word)
letter = input("Guess a letter: ")