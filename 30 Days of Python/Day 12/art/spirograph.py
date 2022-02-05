# Turtle Module
# Day 12 of 100DaysOfCode

from turtle import Screen, Turtle
import turtle
import random


view = Turtle()
view.speed("fastest")
turtle.colormode(255)

view.pensize(2)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    coloring = (r,g,b)
    return coloring

def spirograph(size_graph):
    for _ in range(int(360/ size_graph)):
        view.color(random_color())
        view.circle(100)
        current_heading = view.heading()
        view.setheading(current_heading + size_graph)

spirograph(5)

screen = Screen()
screen.exitonclick()