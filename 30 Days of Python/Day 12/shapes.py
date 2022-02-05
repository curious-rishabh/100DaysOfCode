# Turtle Module
# Day 12 of 100DaysOfCode

import random
from turtle import Turtle

tim = Turtle()

colors = ['aqua', 'blue', 'cyan', 'red', 'black', 'purple', 'brown', 'orange']

def shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        tim.right(angle)
        tim.forward(100)

for shapes_side in range(3, 11):
    tim.color(random.choice(colors))
    shape(shapes_side)