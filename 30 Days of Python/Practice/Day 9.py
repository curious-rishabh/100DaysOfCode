# Day 9 of 100DaysOfCode Practice

# _____________1_______________
# object oriented programming
# Class is blueprint of object 
# object = data + functionality

from turtle import Turtle, Screen
# Construct a object
kachua = Turtle()
my_screen = Screen()

# accessing a attribute
print(my_screen.canvheight)

# accessing a method 
kachua.shape("turtle")
kachua.color("chocolate")
kachua.forward(100)
my_screen.exitonclick()

# _____________2_______________
# using prettytable
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu" , "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
