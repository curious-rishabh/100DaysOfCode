# Coffee Machine
# Day 8 of 100DaysOfCode

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk" : 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine_stat = True
money = 0.0

def is_resource_left(order_ingredients):
    """Returns True if resource sufficient in machine"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry not enough {item}")
            return False
    return True

def coin_amount():
    """Returns total calculated coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total
    
def transaction_status(money_received, drink_cost):
    """Returns True when payment is accepted, or False if money is not sufficient"""
    if money_received >= drink_cost:
        global money
        money += drink_cost
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change. ")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

while machine_stat:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        machine_stat = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink = MENU[choice]
        if is_resource_left(drink["ingredients"]):
            amount = coin_amount()
            drink_amount = drink["cost"]
            if transaction_status(amount, drink_amount):
                for item in resources:
                    resources[item] -= drink["ingredients"][item]
                print(f"Here is your {choice} ☕ ")
                 



