# Turtle Module
# Day 12 of 100DaysOfCode

import random
from turtle import Screen, Turtle,colormode
import turtle

directions = [0, 90, 180, 270]

tim = Turtle()
tim.shape('turtle')

# to use rgb color
turtle.colormode(255)

def random_color():
    """Generate random rgb color"""
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    coloring = (r,g,b)
    return coloring

# tim.turtlesize(5)
tim.pensize(15)
tim.speed(6)
for _ in range(500):
    tim.color(random_color())
    tim.forward(40)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()