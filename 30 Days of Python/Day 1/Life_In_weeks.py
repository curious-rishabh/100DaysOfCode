# Life in weeks 
# Inspiration from https://waitbutwhy.com/2014/05/life-weeks.html
# Day 1 of 100DaysOfCode
print("Welcome to Life In Weeks!")
print("Let's suppose your life expectancy is 90 yrs [Default]")
try :
    life_expectancy = int (input("How much did you expect to live? "))
except:
    life_expectancy = 90
age = int (input("what is your current age? "))
year_left = life_expectancy-age

message = f"You have approx {year_left*365} days, {year_left*52} weeks, and {year_left*12} months left"
print(message)