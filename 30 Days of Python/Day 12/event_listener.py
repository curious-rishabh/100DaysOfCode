# Turtle Module
# Day 12 of 100DaysOfCode

from turtle import Screen, Turtle
import turtle

tim = Turtle()
screen = Screen()

def move():
    tim.forward(20)

screen.listen()
screen.onkey(key='space', fun=move)

screen.exitonclick()