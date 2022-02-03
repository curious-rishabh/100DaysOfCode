# Day 2 of 100DaysOfCode Practice

# _____________1_______________
# psuedo number generator -> Mersenne Twister => random module
import random
# randint(a,b) inclusive both a and b
random_integer = random.randint(1,50)
print(random_integer) 
# for floating point random[0.0 to 1.0)
random_float = random.random()
print(random_float)

# _____________2_______________
# using list
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print("America State that join first: ",states_of_america[0])
print("America State that join last: ",states_of_america[-1])
print("Total States of America: ", len(states_of_america))
print("All State names: ",states_of_america)

# _____________2_______________
# Average Heights without using sum() and len() | using for loop
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
sum = 0
count = 0
for student_height in student_heights:
    sum+=student_height
    count+=1
average = sum/count
print(average)


