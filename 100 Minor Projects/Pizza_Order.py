# Pizza Order
# Day 1 of 100DaysOfCode

print("Welcome to Pizza Yum!")
print("---------------------")
print("Small Pizza: $15")
print("Medium Pizza: $20")
print("Large Pizza: $25")
print()
print("Pepperoni for Small Pizza: +$2")
print("Pepperoni for Medium or Large Pizza: +$3")
print("Extra cheese for any size Pizza: +$1")
bill = 0
pizza = input("What sie of pizza do you want? S, M, or L\n")
if pizza == 's' or pizza == 'S':
    bill = 15
    pep = input("Do you want pepperoni? Y or N\n")
    if pep == 'y' or pep == 'Y':
        bill+=2
        cheese = input("Do you want extra cheese? Y or N\n")
        if cheese == 'Y' or cheese == 'y':
            bill +=1
            print(f"Your final bill is: ${bill}")
        elif cheese == 'N' or cheese == 'n':
            print(f"Your final bill is: ${bill}")
        else:
            print("Wrong input:(")
    elif pep == 'N' or pep == 'n':
        print(f"Your final bill is: ${bill}")
    else:
        print("Wrong Input:(")
elif pizza =='M' or pizza == 'm':
    bill = 20
    pep = input("Do you want pepperoni? Y or N\n")
    if pep == 'y' or pep == 'Y':
        bill+=3
        cheese = input("Do you want extra cheese? Y or N\n")
        if cheese == 'Y' or cheese == 'y':
            bill +=1
            print(f"Your final bill is: ${bill}")
        elif cheese == 'N' or cheese == 'n':
            print(f"Your final bill is: ${bill}")
        else:
            print("Wrong input:(")
    elif pep == 'N' or pep == 'n':
        print(f"Your final bill is: ${bill}")
    else:
        print("Wrong Input:(")
elif pizza =='L' or pizza == 'l':
    bill = 25
    pep = input("Do you want pepperoni? Y or N\n")
    if pep == 'y' or pep == 'Y':
        bill+=3
        cheese = input("Do you want extra cheese? Y or N\n")
        if cheese == 'Y' or cheese == 'y':
            bill +=1
            print(f"Your final bill is: ${bill}")
        elif cheese == 'N' or cheese == 'n':
            print(f"Your final bill is: ${bill}")
        else:
            print("Wrong input:(")
    elif pep == 'N' or pep == 'n':
        print(f"Your final bill is: ${bill}")
    else:
        print("Wrong Input:(")
else:
    print("Not  Valid Choice :(")