import random
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0,2)

rock = '''
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)'''
paper = '''
            _______
        ---'   ____)____
                  ______)
                  _______)
                 _______)
        ---.__________)'''
scissors = '''
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)'''

if user == 0:
    print(rock)
    if computer == 0:
        print("Computer chose")
        print(rock)
        print("It's a draw!")
    elif computer == 1:
        print("Computer chose")
        print(paper)
        print("You lose!")
    else:
        print("Computer chose")
        print(scissors)
        print("You win!")
elif user == 1:
    print(paper)
    if computer == 0:
        print("Computer chose")
        print(rock)
        print("You win!")
    elif computer == 1:
        print("Computer chose")
        print(paper)
        print("It's a draw!")
    else:
        print("Computer chose")
        print(scissors)
        print("You lose!")
elif user == 2:
    print(scissors)
    if computer == 0:
        print("Computer chose")
        print(rock)
        print("You lose!")
    elif computer == 1:
        print("Computer chose")
        print(paper)
        print("You win!")
    else:
        print("Computer chose")
        print(scissors)
        print("It's a draw!")