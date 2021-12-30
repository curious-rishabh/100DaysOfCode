# Love Calculator
# Day 1 of 100DaysOfCode
# Using lower() , count("aplbhabet") to build
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
names = name2 + name1

count_true = 0
t = names.count('t')
r = names.count('r')
u = names.count('u')
e = names.count('e')
count_true = t + r + u + e

count_love = 0
l = names.count('l')
o = names.count('o')
v = names.count('v')
e = names.count('e')
count_love = l + o + v + e

love_score = int(str(count_true) + str(count_love))
# first change to string for percentage then change to int for comparing value

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")