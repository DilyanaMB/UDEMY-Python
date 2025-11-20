import random

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

while lives > 0 or is_user_win:
    letter = input("Guess a letter: ").lower()
    if letter in guessed_letters:
        continue
    else:
        if letter in chosen_word:
            for i in chosen_word:
                if i == letter:
                    guessed_letters.append(letter[i])