from turtle import Turtle, Screen
from random import randint, choice,random

screen = Screen()
timmy = Turtle()
timmy.shape("turtle")
colours = ['aquamarine','DarkSlateGray1','CadetBlue1','DarkSeaGreen1','LightBlue',
           'LightGreen','PaleGreen','PaleTurquoise1','turquoise1','turquoise2']
directions = ['left','right','up','down']
timmy.pensize(5)
timmy.speed(1)

def move_left():
    timmy.color(choice(colours))
    timmy.left(randint(10,50))

def move_right():
    timmy.color(choice(colours))
    timmy.right(randint(10,50))

def move_up():
    timmy.color(choice(colours))
    timmy.forward(randint(10,50))

def move_down():
    timmy.color(choice(colours))
    timmy.back(randint(10, 50))

for _ in range(200):
    direction = choice(directions)
    if direction == 'left':
        move_left()
    elif direction == 'right':
        move_right()
    elif direction == 'up':
        move_up()
    elif direction == 'down':
        move_down()


screen.exitonclick()