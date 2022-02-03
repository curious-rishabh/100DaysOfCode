# Calculator using dictionary & functions
# Day 6 of 100DaysOfCode
logo = """
 _____________________
|  _________________  |
| |  Rishabh Baghel | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(first,second):
        return first + second
    
def substration(first, second):
    return first - second

def muliply(first, second):
    return first * second

def division(first, second):
    '''This function lets you divide'''
    return first / second

operations = {

    "+" : add,
    "-" : substration,
    "*" : muliply,
    "/" : division
}

#                                          REMEMBER!!!!!
'''function = operations["*"]
function(2,3)
Call functions via dictionary'''


def calculator():
    print(logo)
    first_num = float(input("What's the first number?: "))

    for key in operations:
        print(key)

    calculation_stat = True

    while calculation_stat:
        operation = input("Pick an operation: ")
        second_num = float(input("what's the next number?: "))
        calculation = operations[operation]
        answer = calculation(first_num, second_num)
        print(f"{first_num} {operation} {second_num} = {answer}")

        stat = input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation, or to Exit type 'No': ")
        if stat == 'No':
            calculation_stat = False
            break
        elif stat=='n':
            calculator()
        elif stat == 'y':
            first_num = answer


calculator()