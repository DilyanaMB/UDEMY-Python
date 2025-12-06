from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

x_coordinate = [0, -20, -40]
segments = []
for _ in range(0, 3):
    new_segment = Turtle(shape='square')
    new_segment.goto(x_coordinate[_], 0)
    new_segment.color('white')
    segments.append(new_segment)
    new_segment.penup()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for s in range(len(segments)-1, 0, -1):
        new_x = segments[s - 1].xcor()
        new_y = segments[s - 1].ycor()
        segments[s].goto(new_x, new_y)
    segments[0].forward(20)


screen.exitonclick()
