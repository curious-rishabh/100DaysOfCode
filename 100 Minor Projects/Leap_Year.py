# Leap Year Check
# Day 1 of 100DaysOfCode

# Leap Year condition -> multiple of 400, mutiple of 4 and not mulitple of 100
year = int(input("Which year do you want to check? "))
if year % 400 == 0:
    print("Leap year.")
elif year % 4 ==0 and year % 100 != 0:
    print("Leap year.")
else:
    print("Not leap year.")
