import turtle as t
from random import randint, choice

timmy = t.Turtle()
timmy.shape("turtle")
t.colormode(255)

def random_colour():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    random_color= (r,g,b)
    return random_color

directions = [0,90,180,270]
timmy.pensize(5)
timmy.speed(1)

for _ in range(200):
    timmy.forward(30)
    timmy.color(random_colour())
    timmy.setheading(choice(directions))
