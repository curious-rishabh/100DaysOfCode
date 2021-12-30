# Tip Calculator
# Day 1 of 100DaysOfCode
print("Welcome to Tip Calculator!")
bill = float(input("What was the total bill? ₹"))
tip = int(input("What percentage tip would you like to give? 5, 10, 12 or 15? "))
split = int(input("How many people to split the bill? "))

final = round (bill/split * (1+ (tip/100)),2)
# each person should pay bill/split * 1.TipValue[percentage]
# TipValue = tip/100 * bill + bill
print(f"Each person should pay: ₹{final}")

# float precision-> "{:.2f}".format(final)