import random


def rssd():
    x = [1, 2, 3, 4, 5, 6]
    return random.choice(x)


input("Press enter to start")
pon = input("Player 1 Name: ")
ptwn = input("Player 2 Name: ")
pthn = input("Player 3 Name: ")
pfn = input("Player 4 Name: ")
players = {"P1": pon, "P2": ptwn, "P3": pthn, "P4": pfn}
p1m = 200
p2m = 200
p3m = 200
p4m = 200
jackpot = 100
while True:
    # -------------------------------------Player 1 Turn--------------------------------
    print(players["P1"] + "'s Turn")
    while True:
        if p1m == 0:
            print("You are bankrupt")
            break
        print("You have $" + str(p1m) + ", you can:")
        if p1m > 49:
            print("1. Spin for $50")
            print("2. Skip Turn for $50")
        if p1m > 99:
            print("3. Take $20 from each player for $100")
        print("What do you want to do?")
        inp = input("")
        if inp == "1" and p1m > 49:
            p1m = p1m - 50
            input("Press enter to spin")
            randomspin = rssd()
            if randomspin == 1 or randomspin == 6:
                print("You added $50 to the jackpot")
                p1m = p1m - 50
                jackpot = jackpot + 50
            elif randomspin == 2:
                print("You won the jackpot!!!")
                p1m = p1m + jackpot
                jackpot = 100
            elif randomspin == 3:
                print("You won $100")
                p1m = p1m + 100
            elif randomspin == 4 or randomspin == 5:
                print("You won $50")
                p1m = p1m + 50
            break
        elif inp == "2" and p1m > 49:
            print("Your turn has been skipped")
            break
        elif inp == "3" and p1m > 99:
            print("You have taken $30 from each player")
            p1m = p1m - 10
            p2m = p2m - 30
            p3m = p3m - 30
            p4m = p4m - 30
            break
        else:
            print("Error: Insufficient Funds or Invalid Input")
    # -------------------------------------Player 2 Turn--------------------------------
    print(players["P2"] + "'s Turn")
    while True:
        if p2m == 0:
            print("You are bankrupt")
            break
        print("You have $" + str(p2m) + ", you can:")
        if p2m > 49:
            print("1. Spin for $50")
            print("2. Skip Turn for $50")
        if p2m > 99:
            print("3. Take $20 from each player for $100")
        print("What do you want to do?")
        inp = input("")
        if inp == "1" and p2m > 49:
            p2m = p2m - 50
            input("Press enter to spin")
            randomspin = rssd()
            if randomspin == 1 or randomspin == 6:
                print("You added $50 to the jackpot")
                p2m = p2m - 50
                jackpot = jackpot + 50
            elif randomspin == 2:
                print("You won the jackpot!!!")
                p2m = p2m + jackpot
                jackpot = 100
            elif randomspin == 3:
                print("You won $100")
                p2m = p2m + 100
            elif randomspin == 4 or randomspin == 5:
                print("You won $50")
                p2m = p2m + 50
            break
        elif inp == "2" and p2m > 49:
            print("Your turn has been skipped")
            break
        elif inp == "3" and p2m > 99:
            print("You have taken $30 from each player")
            p2m = p2m - 10
            p1m = p1m - 30
            p3m = p3m - 30
            p4m = p4m - 30
            break
        else:
            print("Error: Insufficient Funds or Invalid Input")
    # -------------------------------------Player 3 Turn--------------------------------
    print(players["P3"] + "'s Turn")
    while True:
        if p3m == 0:
            print("You are bankrupt")
            break
        print("You have $" + str(p3m) + ", you can:")
        if p3m > 49:
            print("1. Spin for $50")
            print("2. Skip Turn for $50")
        if p3m > 99:
            print("3. Take $20 from each player for $100")
        print("What do you want to do?")
        inp = input("")
        if inp == "1" and p3m > 49:
            p3m = p3m - 50
            input("Press enter to spin")
            randomspin = rssd()
            if randomspin == 1 or randomspin == 6:
                print("You added $50 to the jackpot")
                p3m = p3m - 50
                jackpot = jackpot + 50
            elif randomspin == 2:
                print("You won the jackpot!!!")
                p3m = p3m + jackpot
                jackpot = 100
            elif randomspin == 3:
                print("You won $100")
                p3m = p3m + 100
            elif randomspin == 4 or randomspin == 5:
                print("You won $50")
                p3m = p3m + 50
            break
        elif inp == "2" and p3m > 49:
            print("Your turn has been skipped")
            break
        elif inp == "3" and p3m > 99:
            print("You have taken $30 from each player")
            p3m = p3m - 10
            p1m = p1m - 30
            p2m = p2m - 30
            p4m = p4m - 30
            break
        else:
            print("Error: Insufficient Funds or Invalid Input")
    # -------------------------------------Player 4 Turn--------------------------------
    print(players["P4"] + "'s Turn")
    while True:
        if p4m == 0:
            print("You are bankrupt")
            break
        print("You have $" + str(p4m) + ", you can:")
        if p4m > 49:
            print("1. Spin for $50")
            print("2. Skip Turn for $50")
        if p4m > 99:
            print("3. Take $20 from each player for $100")
        print("What do you want to do?")
        inp = input("")
        if inp == "1" and p4m > 49:
            p4m = p4m - 50
            input("Press enter to spin")
            randomspin = rssd()
            if randomspin == 1 or randomspin == 6:
                print("You added $50 to the jackpot")
                p4m = p4m - 50
                jackpot = jackpot + 50
            elif randomspin == 2:
                print("You won the jackpot!!!")
                p4m = p4m + jackpot
                jackpot = 100
            elif randomspin == 3:
                print("You won $100")
                p4m = p4m + 100
            elif randomspin == 4 or randomspin == 5:
                print("You won $50")
                p4m = p4m + 50
            break
        elif inp == "2" and p4m > 49:
            print("Your turn has been skipped")
            break
        elif inp == "3" and p4m > 99:
            print("You have taken $30 from each player")
            p4m = p4m - 10
            p1m = p1m - 30
            p2m = p2m - 30
            p3m = p3m - 30
            break
        else:
            print("Error: Insufficient Funds or Invalid Input")
