from turtle import Turtle, Screen
x_coordinate = [0,-20,-40]
segments = []
for _ in range (0,3):
    new_segment = Turtle(shape ='square')
    new_segment.goto(x_coordinate[_],0)
    new_segment.color('white')
    segments.append(new_segment)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.exitonclick()