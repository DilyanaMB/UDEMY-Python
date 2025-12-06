from turtle import Turtle,Screen

tim = Turtle()

def move_forwards():
    tim.forward(10)
screen = Screen()
screen.listen()
screen.onkey(move_forwards, "space")

screen.exitonclick()
