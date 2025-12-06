from turtle import Screen, Turtle

tim = Turtle()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.back(10)

def move_left():
    tim.left(10)

def move_right():
    new_heading = tim.heading() - 10  # heading + 10 for left = those 2 lines are equivalent to .left()/.right()
    tim.setheading(new_heading)

def clean_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

tim.shape("turtle")
tim.color('aquamarine')
screen = Screen()
screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clean_screen, "c")

screen.exitonclick()
