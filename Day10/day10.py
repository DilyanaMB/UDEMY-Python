def format_name(first, last):
    if first == "" or last == "":
        return "You didn't provide a valid input"
    f_name = first.title()
    l_name = last.title()
    return f"{f_name} {l_name}"

print(format_name("DeYa", "bodUROva"))
print(format_name(input("What is your first name? "), input("What is your last name? ")))

