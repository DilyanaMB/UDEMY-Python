from calculator_art import *

print(logo)

def add_nums(a, b):
    print(f"{a} + {b} = {a + b}")
    return a + b


def subtract_nums(a, b):
    print(f"{a} - {b} = {a - b}")
    return a - b


def multiply_nums(a, b):
    print(f"{a} * {b} = {a * b}")
    return a * b


def divide_nums(a, b):
    if b == 0:
        print(f"{a} / {b} = NaN")
    print(f"{a} / {b} = {a / b}")
    return a / b

is_continue = 'n'

while True:
    if is_continue == "n":
        first_num = float(input("What's the first number?:"))
        result = first_num
    action = input("Pick an operation:\n+\n-\n*\n/\n")
    second_num = float(input("What's the next number?:"))
    if action == "+":
        result = add_nums(result, second_num)
    elif action == "-":
        result = subtract_nums(result, second_num)
    elif action == "*":
        result = multiply_nums(result, second_num)
    else:
        result = divide_nums(result, second_num)

    is_continue = input(f"Type 'y' to continue calculating with {result}, "
                        f"or type 'n' to start a new calculation:").lower()

