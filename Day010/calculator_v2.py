def add_nums(a, b):
    return a + b

def subtract_nums(a, b):
    return a - b

def multiply_nums(a, b):
    return a * b

def divide_nums(a, b):
    if b == 0:
        print(f"{a} / {b} = NaN")
    return a / b

operations = {
    "+": add_nums,
    "-": subtract_nums,
    "*": multiply_nums,
    "/": divide_nums,
}

is_continue = "n"

while True:
    if is_continue == "n":
        first_num = float(input("What's the first number?:"))
        result = first_num

    action = input("Pick an operation:\n+\n-\n*\n/\n")
    second_num = float(input("What's the next number?:"))

    result = operations[action](result, second_num)
    print(f"{first_num} {action} {second_num} = {result}")

    is_continue = input(f"Type 'y' to continue calculating with {result}, "
                        f"or type 'n' to start a new calculation:").lower()
