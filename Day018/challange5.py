from turtle import Screen,Turtle
from random import  choice

screen = Screen()
timmy = Turtle()
timmy.shape("turtle")
colours = ['chartreuse','DarkOrange','DeepPink','purple','yellow','SlateBlue1','red','turquoise1']
timmy.speed('fastest')

# circle with radius of 100
for _ in range(40):
    timmy.color(choice(colours))
    timmy.circle(100)
    timmy.forward(1)
    timmy.right(10)
screen.exitonclick()