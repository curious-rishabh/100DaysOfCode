# Secret Auction
# Day 5 of 100DaysOfCode

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to secret auction program.")
def highest_bidder(user):
    highest_bid = 0
    winner = ""
    for key in user:
        # Remember!!!!!  
        if user[key] >= highest_bid:
            highest_bid = user[key]
            winner = key
    print(f"The winner of auction {winner} and their bid is ${highest_bid}")

user = {}
end_of_auction = True
while end_of_auction:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    user[name] = bid   
    answer = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    
    if answer == 'no':
        end_of_auction = False
        highest_bidder(user)
 

