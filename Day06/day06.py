def my_function(): # define new function (method)
    print("Hello")
    print("Bye")

my_function()

# hurdle - https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# # for i in range(6):
# #    jump()
#
# number_of_hurdles = 6
#
# while number_of_hurdles > 0:
#     jump()
#     number_of_hurdles -= 1
#       if at_goal():
#           number_of_hurdles = 0

# hurdle 3

# def jump():          # remove the 1st move, or else will hit the wall
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()


# hurdle 4

# def jump():
#     turn_left()
#     while not right_is_clear():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
#
#
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

# hurdle 5

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# while front_is_clear():
#     move()
# turn_left()
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
