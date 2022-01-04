# Password generator
# Day 2 of 100DaysOfCode
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Password Generator!")
letter = int(input("How many letters would you like in your password? \n"))
symbol = int(input("How many symbols would you like? \n"))
number = int(input("How many numbers would you like? \n"))
#                                                     Easy Level
# password = ""
# for char in range(1,letter+1):
#     password += random.choice(letters)

# for numb in range(1,number+1):
#     password += random.choice(numbers)

# for symb in range(1,symbol+1):
#     password += random.choice(symbols)
# print(f"Here is your password: {password}")

#                                                 Hard Level
password_list = []
for char in range(1,letter+1):
    password_list += random.choice(letters)
    # password_list.append(random.choice(letters))

for numb in range(1,number+1):
    password_list += random.choice(numbers)

for symb in range(1,symbol+1):
    password_list += random.choice(symbols)

random.shuffle(password_list)
# change order of list

# change list to string
password =""
for char in password_list:
    password += char

print(f"Here is your password: {password}")