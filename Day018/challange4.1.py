from turtle import Screen,Turtle
from random import  choice

screen = Screen()
timmy = Turtle()
timmy.shape("turtle")
colours = ['aquamarine','DarkSlateGray1','CadetBlue1','DarkSeaGreen1','LightBlue',
           'LightGreen','PaleGreen','PaleTurquoise1','turquoise1','turquoise2']
directions = [0,90,180,270]
timmy.pensize(5)
timmy.speed(1)

for _ in range(200):
    timmy.forward(30)
    timmy.color(choice(colours))
    timmy.setheading(choice(directions))

screen.exitonclick()