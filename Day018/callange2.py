from turtle import Turtle, Screen
import random

def draw():
    timmy.color("red")
    for _ in range(15):
        timmy.forward(10)
        timmy.pendown()
        timmy.forward(10)
        timmy.penup()

screen = Screen()
timmy = Turtle()
timmy.shape("turtle")

draw()
screen.exitonclick()