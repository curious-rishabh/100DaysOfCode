# Rock Paper Scissors
# Day 2 of 100DaysOfCode

from random import randint, choice

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to Rock Paper Scissors!")
print("Rule of game are: ")
print("                 1) Rock wins against Scissors.")
print("                 2) Scissors win against paper.")
print("                 3) Paper wins against rock")
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
game = [rock,paper,scissors]
computer_choice = randint(0,2)
print("You chose")
if user == 0:
    print(rock)
    print("Computer chose: ")
    print(game[computer_choice])
    if game[computer_choice] == scissors:
        print("You Win")
    elif game[computer_choice] == rock:
        print("Match Draw")
    else:
        print("You Lose")
    print("__")
elif user == 1:
    print(paper)
    print("Computer chose: ")
    print(game[computer_choice])
    if game[computer_choice] == rock:
        print("You Win")
    elif game[computer_choice] == paper:
        print("Match Draw")
    else:
        print("You Lose")
    print("__")
elif user == 2:
    print(scissors)
    print("Computer chose: ")
    print(game[computer_choice])
    if game[computer_choice] == paper:
        print("You Win")
    elif game[computer_choice] == scissors:
        print("Match Draw")
    else:
        print("You Lose")
    print("__")
else:
    print("Invalid Input:(")