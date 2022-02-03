# Black jack capstone Game
# Day 7 of 100DaysOfCode

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     </RB>
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

from game_data import data
import random, os
# Display art
print(logo)
Score = 0
Game_stat = True

# Generate a random account from the data
account_b = random.choice(data)

#                                    Remember!!!!
def accounting(account):
    '''Take account as input & Format the account data into printable format, and returns the printable format.'''
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

def checking(guess, a_follower, b_follower):
    if a_follower > b_follower:
        if guess == "a":
            return True
        else:
            return False
    else:
        if guess == "b":
            return True
        else:
            return False

while Game_stat:
    # Making account at postion B becomes the next account at pos A if user correct
    account_a = account_b
    account_b = random.choice(data)
    
    while account_a == account_b:
        account_b = random.choice(data)

    # Show players
    print(f"Compare A: {accounting(account_a)}.")
    print(vs)
    print(f"Against B: {accounting(account_b)}.")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # check if user right
    a_follower = account_a["follower_count"]
    b_follower = account_b["follower_count"]

    is_correct = checking(guess, a_follower, b_follower)
    os.system('clear')
    print(logo)

    if is_correct:
        Score +=1
        print(f"You're right! Current score: {Score}")
        print()
    else:
        Game_stat = False
        print(f"Sorry, That's wrong! Final score: {Score}")
        


