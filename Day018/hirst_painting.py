import random
import colorgram
from turtle import Turtle,Screen

# rgb_colors = []
# colors = colorgram.extract('horizontal-blog-images-1-4.jpeg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))

colours = [ (223, 155, 90), (214, 240, 228), (240, 206, 90), (104, 170, 203), (36, 109, 149), (199, 227, 239), (113, 193, 161), (153, 61, 94), (208, 78, 109), (243, 215, 226), (25, 134, 101), (224, 81, 59), (205, 133, 155), (184, 59, 43), (177, 166, 36), (138, 219, 198), (39, 54, 113), (238, 161, 180), (105, 40, 73), (137, 215, 228), (239, 168, 157), (14, 93, 69), (60, 166, 132), (27, 47, 88), (53, 157, 186), (109, 116, 170), (72, 36, 65), (14, 69, 51), (180, 186, 218)]

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.hideturtle()
tim.penup()
tim.speed("fastest")

dot_size = 20
spacing = 50
start_x = -225
start_y = -225

for row in range(10):
    for col in range(10):
        x = start_x + col * spacing
        y = start_y + row * spacing
        tim.goto(x, y)
        tim.dot(dot_size, random.choice(colours))

screen.exitonclick()