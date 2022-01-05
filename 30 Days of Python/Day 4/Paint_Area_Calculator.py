# Paint Area Calculator
# Day 4 of 100DaysOfCode

print("Welcome to Paint Area Calculator!")
print("---------------------------------")
print("1 can of paint can cover 5 square meters of wall")
def paint_calc(height, width, cover):
    cans = (height*width) / cover
    print(f"You'll need {round(cans)} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
