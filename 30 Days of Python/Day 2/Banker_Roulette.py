# Who will pay the bill? Banker Roulette
# Using random module
# Day 2 of 100DaysOfCode
import random
names = input("Give me everybody's names, seperated by a comma. ")
name = names.split(", ")

person_who_will_pay = random.randint(0, len(name) -1)
# OR -> person_who_will_pay = random.choice(name)
print(name[person_who_will_pay] + " is going to buy the meal today!")