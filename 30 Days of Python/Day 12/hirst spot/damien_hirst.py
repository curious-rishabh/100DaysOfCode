# $1.5 Million Art
# Day 12 of 100DaysOfCode

# import colorgram
# # extract colors from image
# rgb_colors = []
# colors = colorgram.extract('100 Minor Projects in Python/Day 12/hirst spot/image.jpg', 20)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r, g, b)
#     rgb_colors.append(new_colors)
# print(rgb_colors)

import random
import turtle
from turtle import Screen, Turtle
turtle.colormode(255)

turtle.title("$1.5 Million Painting </RB>")
colors_list = [(233, 239, 246), (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71)]

tim = Turtle()

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
tim.hideturtle()
tim.speed(0)
for _ in range(10):
    for _ in range(10): 
        tim.dot(20, random.choice(colors_list))
        tim.penup()
        tim.forward(50)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

screen = Screen()
screen.exitonclick()