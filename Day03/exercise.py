print("Welcome to Treasure Island.\nYour mission is to find the treasure.\n"
      "You're at a cross road. Where do you want to go?")
side = input("      Type \"left\" or \"right\"\n")
if side == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    action=input("  Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
    if action == "swim":
        print("You get attacked by an angry trout. Game Over.")
    else:
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        colour = input("  One red, one yellow and one blue. Which colour do you choose?\n")
        if colour == "red":
            print("It's a room full of fire. Game Over.")
        elif colour == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You enter a room of beasts. Game Over.")
else:
    print("You fell into a hole. Game Over.")