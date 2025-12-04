import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
colours = [(223, 155, 90), (214, 240, 228), (240, 206, 90), (104, 170, 203), (36, 109, 149), (199, 227, 239),
           (113, 193, 161), (153, 61, 94), (208, 78, 109), (243, 215, 226), (25, 134, 101), (224, 81, 59),
           (205, 133, 155), (184, 59, 43), (177, 166, 36), (138, 219, 198), (39, 54, 113), (238, 161, 180),
           (105, 40, 73), (137, 215, 228), (239, 168, 157), (14, 93, 69), (60, 166, 132), (27, 47, 88), (53, 157, 186),
           (109, 116, 170), (72, 36, 65), (14, 69, 51), (180, 186, 218)]

tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
tim.hideturtle()

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colours))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
