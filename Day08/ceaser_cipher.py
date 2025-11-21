from ceaser_cipher_art import logo
from ceaser_cipher_alphabet import alphabet

print(logo)
is_user_continue = True

def encode(msg, shift):
    result = ""

    for i in msg:
        if alphabet.index(i)+shift<= len(alphabet)-1:
            shifted_position = alphabet.index(i) + shift
            result += alphabet[shifted_position]
        else:
            shift2 =  abs(len(alphabet)- alphabet.index(i)-1)
            result += alphabet[shift2]

    # solution 2:
    # for letter in msg:
    #     shifted_position %= len(alphabet) ---- 0-25
    #     result += alphabet[shifted_position]

    print("Here's the encoded result: " + result)

def decode(msg, shift):
    result = ""

    for i in msg:
        if alphabet.index(i)-shift>=0:
            shifted_position = alphabet.index(i) - shift
            result += alphabet[shifted_position]
        else:
            shift_temp = abs(shift -alphabet.index(i))
            shift2=alphabet[-shift_temp]
            result += shift2


    print("Here's the encoded result: " + result)

while is_user_continue:
    print("Type 'encode' to encrypt, type 'decode' to decrypt:")
    user_input = input()
    print("Type your message:")
    msg = input()  # abc
    print("Type the shift number:")
    shift = int(input())

    if user_input == "encode":
        encode(msg, shift)
    else:
        decode(msg, shift)

    print("Type 'yes' if you want to go again. Otherwise type 'no'.")
    user_again = input()
    if user_again.lower() == "no":
        is_user_continue = False
        print("Goodbye")

