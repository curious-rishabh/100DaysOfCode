# Day 1 of 100DaysOfCode Practice

# _____________1_______________
# basic input, output and variable
name = input("What's your name? ")
print("Hello " + name)
# len() function counts string characters
length = str(len(name)) 
# type conversion because "int" can't concatenate with "string"
print("Length of your name is " + length)

# _______________2_____________
# adds the digits in a 2 digit number
num = input("Type a two digit number: ")
# Use of subscripting and Type Conversion
print(type(num))
first = int(num[0])
second = int(num[1])
print(first + second)

# ______________3________________
# conditional statements 
# Odd or Even
number = int(input("Which number do you want to check? "))
if number%2 == 0:
    print("This is an even number.")
    # Indentation -> use tabs instead of spaces
else:
    print("This is an odd number.")