# Black jack capstone Game
# Day 6 of 100DaysOfCode

import re
from warnings import resetwarnings

from defer import return_value

import random

from urllib3 import Retry

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


#11 is the Ace.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
      """uses the List below to *return* a random card"""
      return int(random.choice(cards))

def calculate_score(cards):
      if sum(cards) == 21 and len(cards) == 2:
            return 0
      if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
      return sum(cards)

def compare(user_score, computer_score):
      if user_score == computer_score:
            return "Draw"
      elif computer_score == 0:
            return "Lose, opponent has Blackjack"
      elif user_score == 0:
            return "Win with a Blackjack"
      elif user_score > 21:
            return "You went over. You Lose!!!"
      elif computer_score > 21:
            return "Opponent went over. You win!!!"
      elif user_score > computer_score:
            return "You win"
      else:
            return "You lose"

def play_game():
      print(logo)
      game_stat = True
      #Deal the user and computer 2 cards each using deal_card() and append().
      user_cards = []
      computer_cards = []

      for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

      while game_stat:
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            print(f" Your cards: {user_cards}, current score: {user_score}")
            print(f" Computer first cards: {computer_cards[0]}")
            print()
            if user_score == 0 or computer_score == 0 or user_score > 21:
                  game_stat = False
            else:
                  choice = input("Type 'y' to get another card, type 'n' to pass: ")
                  if choice == 'y' or choice == 'Y':
                        user_cards.append(deal_card())
                  else:
                        game_stat = False
      while computer_score !=0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

      print(f"      Your final hand: {user_cards}, final score: {user_score}")
      print(f"      Computer's final hand: {computer_cards}, final score: {computer_score}")
      result = compare(user_score, computer_score)
      print(result)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
      play_game()