# Turtle Module
# Day 12 of 100DaysOfCode

from turtle import Screen, Turtle
import turtle

tim = Turtle()
screen = Screen()

def forward():
    tim.forward(25)

def backward():
    tim.backward(25)

def left():
    tim.left(10)
    # Or
    # new_heading = tim.heading + 10
    # tim.setheading(new_heading)

def right():
    tim.right(10)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key='w', fun=forward)
screen.onkey(key='s', fun=backward)
screen.onkey(key='a', fun=left)
screen.onkey(key='d', fun=right)
screen.onkey(key='c', fun=clear_drawing)


screen.exitonclick()