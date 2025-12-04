from turtle import Turtle, Screen

def draw_triangle():
    timmy.color("green3")
    angle = 360 / 3
    for i in range(3):
        timmy.forward(50)
        timmy.right(angle)

def draw_square():
    timmy.color("green")
    angle = 360 / 4
    for i in range(4):
        timmy.forward(50)
        timmy.right(angle)

def draw_pentagon():
    timmy.color("lawngreen")
    angle = 360 / 5
    for i in range(5):
        timmy.forward(50)
        timmy.right(angle)

def draw_hexagon():
    timmy.color("DarkGreen")
    angle = 360 / 6
    for i in range(6):
        timmy.forward(50)
        timmy.right(angle)

def draw_heptagon():
    timmy.color("GreenYellow")
    angle = 360 / 7
    for i in range(7):
        timmy.forward(50)
        timmy.right(angle)

def draw_octagon():
    timmy.color("OliveDrab3")
    angle = 360 / 8
    for i in range(8):
        timmy.forward(50)
        timmy.right(angle)

def draw_nonagon():
    timmy.color("OliveDrab1")
    angle = 360 / 9
    for i in range(9):
        timmy.forward(50)
        timmy.right(angle)

def draw_decagon():
    timmy.color("LimeGreen")
    angle = 360 / 10
    for i in range(10):
        timmy.forward(50)
        timmy.right(angle)


screen = Screen()
timmy = Turtle()
timmy.shape("turtle")

draw_triangle()
draw_square()
draw_pentagon()
draw_hexagon()
draw_heptagon()
draw_octagon()
draw_nonagon()

screen.exitonclick()