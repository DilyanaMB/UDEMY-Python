def greet():
    print("Hello")
    print("How are you today?")
    print("Have a lovely day!")

greet()

# Function that allows input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you today {name}?")
    print(f"Have a lovely day {name}!")

greet_with_name("Deya")
greet_with_name("Victor")

# calculator how many weeks you have until reach 90
def life_in_weeks(age):
    weeks = (90 - age)*52
    print(f"You have {weeks} weeks left.")

age=int(input("Enter your age:\n"))
life_in_weeks(age)

# Function that allows more than one input

def greet_with_name_and_location(name,location):
    print(f"Hello {name}")
    print(f"How are you today {name} in {location}?")
    print(f"Have a lovely day in {location}!")

greet_with_name_and_location("Deya",'Germany')
greet_with_name_and_location("Angola",'Victor')

# Function with keyword positioning

def greet_with_name_and_location_position(name,location):
    print(f"Hello {name}")
    print(f"How are you today {name} in {location}?")
    print(f"Have a lovely day in {location}!")

greet_with_name_and_location_position(name="Deya",location='Germany')
greet_with_name_and_location_position(location="Angola",name='Victor')


def calculate_love_score(name1, name2):
    count_true_first_name = 0
    count_love_first_name = 0
    for i in name1.lower():
        if i == 't' or i == 'r' or i =='u' or i == 'e':
            count_true_first_name += 1
        if i == 'l' or i == 'o' or i =='v' or i == 'e':
            count_love_first_name += 1

    count_true_second_name = 0
    count_love_second_name = 0
    for i in name2.lower():
        if i == 't' or i == 'r' or i =='u' or i == 'e':
            count_true_second_name += 1
        if i == 'l' or i == 'o' or i =='v' or i == 'e':
            count_love_second_name += 1

    sum_true = count_true_second_name + count_true_first_name
    sum_love = count_love_first_name + count_love_second_name
    print(f"{sum_true}{sum_love}")

calculate_love_score("Kanye West","Kim Kardashian")