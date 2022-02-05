# Turtle Module
# Day 12 of 100DaysOfCode

from random import randint, random
from turtle import Screen, Turtle
import turtle

race_stat = False
colors = ['red', 'orange', 'yellow', 'green', 'blue','purple']
y_position = [-240, -160, -80, 0, 80,160]
all_turtles = []
screen = Screen()
# set screen width and height
screen.setup(width = 800, height= 600)
# popup window for input
user_choice = screen.textinput(title= "Make your bet", prompt = "Which turtle will win the race? Enter your choice: [Rainbow Color]")

for i in range(0,6):
    tim = Turtle(shape='turtle')
    tim.color(colors[i])
    tim.penup()
    # set turtle to initial position of race
    tim.goto(x = -380, y= y_position[i])
    all_turtles.append(tim)

if user_choice:
    race_stat = True

while race_stat:
    for turtle in all_turtles:
        if turtle.xcor() > 370:
            wining_color = turtle.pencolor()
            race_stat = False
            if wining_color == user_choice:
                print("You have won!!!")
            else:
                print(f"You have lost! Winning color is {wining_color}")
        rand_distance = randint(0,10)
        turtle.forward(rand_distance)
        

# pencolor -> body of turtle



screen.exitonclick()