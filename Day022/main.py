from turtle import Screen, Turtle
import time
from ball import Ball
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)
ball = Ball()

r_paddle = Paddle(370,0)
l_paddle = Paddle(-370,0)

screen.listen()
screen.onkey(r_paddle.go_up,'Up')
screen.onkey(r_paddle.go_down,'Down')

screen.onkey(l_paddle.go_up,'w')
screen.onkey(l_paddle.go_down,'s')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    elif ball.xcor() > 390:
        ball.reset_position()
    elif ball.xcor() < -390:
        ball.reset_position()

screen.exitonclick()
