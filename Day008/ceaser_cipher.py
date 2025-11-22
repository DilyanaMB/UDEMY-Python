from ceaser_cipher_art import logo
from ceaser_cipher_alphabet import alphabet

print(logo)
is_user_continue = True


def not_letters(msg):
    not_letters = ''
    for letter in msg:
        if letter not in alphabet:
            not_letters += letter
            msg = msg.replace(letter, '')
    return not_letters, msg


def encode(msg, shift, not_letters):
    result = ""

    for i in msg:
        if alphabet.index(i) + shift <= len(alphabet) - 1:
            shifted_position = alphabet.index(i) + shift
            result += alphabet[shifted_position]
        else:
            shift2 = abs(len(alphabet) - alphabet.index(i) - 1)
            result += alphabet[shift2]

    # solution 2:

    # for letter in msg:
    #     shifted_position = alphabet.index(i) - shift
    #     shifted_position %= len(alphabet) ---- 0-25
    #     result += alphabet[shifted_position]

    print("Here's the encoded result: " + result + not_letters)


def decode(msg, shift, not_letters):
    result = ""

    for i in msg:
        if alphabet.index(i) - shift >= 0:
            shifted_position = alphabet.index(i) - shift
            result += alphabet[shifted_position]
        else:
            shift_temp = abs(shift - alphabet.index(i))
            shift2 = alphabet[-shift_temp]
            result += shift2
    # solution 2:

    for letter in msg:
        shifted_position %= len(alphabet) - --- 0 - 25
        result += alphabet[shifted_position]

    print("Here's the encoded result: " + result + not_letters)


while is_user_continue:
    print("Type 'encode' to encrypt, type 'decode' to decrypt:")
    user_input = input()
    print("Type your message:")
    msg = input()  # abc
    print("Type the shift number:")
    shift = int(input())

    not_letters, msg = not_letters(msg)
    if user_input == "encode":
        encode(msg, shift, not_letters)
    else:
        decode(msg, shift, not_letters)

    print("Type 'yes' if you want to go again. Otherwise type 'no'.")
    user_again = input().lower()
    if user_again.lower() == "no":
        is_user_continue = False
        print("Goodbye")
