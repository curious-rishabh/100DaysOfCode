# BMI Calculator
# Day 1 of 100DaysOfCode
print("Welcome to BIM Calculator!")
print("-----------------------------")
print("1 meter equal to 39.37 inches or 3.28ft")
print("------------OR---------------")
print("1.5 meter = 4'11 ")
print("1.6 meter = 5'3 ")
print("1.7 meter = 5'7 ")
print("1.8 meter = 5'11 ")
print("1.9 meter = 6'3 ")
print("-----------------------------")

height = float(input("Enter your height in meter: "))
weight = int(input("Enter your weight in kg: "))

BMI = round(weight/height**2)
if BMI <= 18.4:
    print("You are Underweight")
    print(int(BMI))
    print("Health Risk: Possible nutritional deficiency and osteoporosis")
elif BMI <= 24.5:
    print("You are Normal")
    print(int(BMI))
    print("You are Healthy!")
elif BMI <= 29.9:
    print("You are Overweight")
    print(int(BMI))
    print("Health Risk: Moderate risk of developing heart disease, high blood pressure, stroke, diabetes mellitus")
elif BMI <= 34.9:
    print("You are Obese")
    print(int(BMI))
    print("Health Risk: High risk of developing heart disease, high blood pressure, stroke, diabetes mellitus. Metabolic Syndrome")
else:
    print("You are Extremely Obese")
    print(int(BMI))
    print("Health Risk: High risk of developing heart disease, high blood pressure, stroke, diabetes mellitus. Metabolic Syndrome")
