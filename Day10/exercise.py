def is_leap_year(year):
    """Take a first and last name and format it to return the
    title case version of the name"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    else:
        return False

print(is_leap_year(int(input("Enter the year: "))))
