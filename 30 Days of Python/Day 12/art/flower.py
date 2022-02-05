from turtle import *
import turtle

def flower():
    for i in range(300):
        circle(190-i,90)
        left(90)
        circle(190-i,90)
        left(18)
    turtle.speed(0)

flower()