def format_name(first, last):
    if first == "" or last == "":
        return "You didn't provide a valid input"
    f_name = first.title()
    l_name = last.title()
    return f"{f_name} {l_name}"

print(format_name("DeYa", "bodUROva"))
print(format_name(input("What is your first name? "), input("What is your last name? ")))

def add (a, b):
    return a + b

# storing a function as variable is WITHOUT parentheses
my_favourite_operation = add

print(my_favourite_operation(5, 6))