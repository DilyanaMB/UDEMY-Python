from turtle import Turtle, Screen
import random as r # make alias
import heroes

print(heroes.gen())

screen = Screen()
def turn_right_and_move():
    timmy.forward(100)
    timmy.right(90)

timmy = Turtle()
timmy.shape("turtle")
timmy.color("DeepSkyBlue2")

for _ in range(4):
    turn_right_and_move()

num = r.randint(0,100)

screen.exitonclick()