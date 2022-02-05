# Turtle Module
# Day 12 of 100DaysOfCode

from turtle import Screen, Turtle
import turtle

# create object named timmy
timmy = Turtle()

# change it shape
timmy.shape('turtle')
# modify action color
timmy.color('red')
# color change of turtle
timmy.fillcolor('cyan')

# draw a square
for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

timmy.shape('arrow')
timmy.color('black')
timmy.left(90)
timmy.hideturtle()

# dash line
for _ in range(11):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

turtle.hideturtle()

# Exit when user click
screen = Screen()
screen.exitonclick()