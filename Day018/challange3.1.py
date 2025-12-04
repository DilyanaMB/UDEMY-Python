from turtle import Turtle, Screen
from random import choice

screen = Screen()
timmy = Turtle()
timmy.shape("turtle")

colours = ['aquamarine','DarkSlateGray1','CadetBlue1','DarkSeaGreen1','LightBlue',
           'LightGreen','PaleGreen','PaleTurquoise1','turquoise1','turquoise2']

def draw_shape(num_sides):
    angle = 360/num_sides
    for i in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for shape_side in range(3,11):
    timmy.color(choice(colours))
    draw_shape(shape_side)

screen.exitonclick()