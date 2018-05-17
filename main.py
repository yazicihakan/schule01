'''
Created on 01.05.2018
@author: panjeet
'''
import sys
from random import *
from pirate import pirate
from Ship import Ship
from Fighter import Fighter
from Cargoship import Cargoship
from Industrial import *
from Military import *
from Agriculture import *

money = 1000;
fighter = []
cargo = []
space = 0
wares = {"curry" : 0, "chip" : 0, "weapon" : 0}
continu = True
turns = 1

'''
Function to choose the planet to travel to
'''
def choosePlanet():
    global p
    print("On which planet do you want to go")
    choice = input("Industry [1] , Military [2], Agriculture [3]\n")

    if (choice == "1"):
        p = Industrial()
    elif (choice == "2"):
        p = Military()
    elif (choice == "3"):
        p = Agriculture()

'''
Function that lets the player choose a ship to buy and adds them to their lists
'''
def buy():
    global money, space
    shipch = input("What would you like to buy [1] Fighter Ship, [2] Cargoship\n")
    
    if(shipch == "1"):
        tempShip = Fighter()
        if money >= tempShip.getPrice():
            money = money - tempShip.getPrice()
            print("Here your fighter!")
            fighter.append(tempShip)
            print("you have " + str(money) + " Indian Rupees left")
        else:
            print("You don't have enough money to buy the fighter")
            print()
            return
    if(shipch == "2"):
        tempShip = Cargoship()
        if money >= tempShip.getPrice():
            money = money - tempShip.getPrice()
            space = space + tempShip.getCargospace()
            print("Here your Cargoship!")
            cargo.append(tempShip)
            print("you have " + str(money) + " Indian Rupees left")
        else:
            print("You don't have enough money to buy the fighter")
            print()

'''
Function that lets the player choose and buy a specific amount of wares
'''     
def buystuff():
    global money, p, cargo, space, wares
    buy = input("What would you like to buy? [1] Curry [2] Computer Chips [3] Weapons\n")
    if((buy == "1" or buy == "2" or buy == "3") and space > 0):
        amount = int(input("How much would you like to buy: "))
        if amount <= space:
            if buy == "1":
                ware = "curry"
                money = money - p.getCurryPrice()
            if buy == "2":
                ware = "chip"
                money = money - p.getChipPrice()
            if buy == "3":
                ware = "weapon"
                money = money - p.getWeaponPrice()
            wares[ware] = wares[ware] + amount
            space = space - amount
            print("You bought " + str(amount) + " " + ware)
            print("You now have " + str(wares[ware]) + " " + ware)
            print("you have " + str(money) + " Indian Rupees left")
        else:
            print("You don't have enough space")
    if space == 0:
        print("You don't have enough space")

'''
Function that lets the player sell a specified amount of wares
'''
def sellstuff():
    global money, p, cargo, space, wares
    sell = input("What would you like to sell? [1] Curry [2] Computer Chips [3] Weapons\n")
    if(sell == "1" or sell == "2" or sell == "3"):
        amount = int(input("How much would you like to sell: "))
        if sell == "1":
            ware = "curry"
            price = p.getCurryPrice()
        if sell == "2":
            ware = "chip"
            price = p.getChipPrice()
        if sell == "3":
            ware = "weapon"
            price = p.getWeaponPrice()
        
        if wares[ware] >= amount:
            money = money + price
            wares[ware] = wares[ware] - amount
            space = space + amount
            print("You sold " + str(amount) + " " + ware)
            print("You have " + str(money) + " Indian Rupees")       

'''
Main Menu
'''
def menu():
    global turns
    print("~*~ M E N U ~*~\n")
    print("[1] buy a ship")
    print("[2] buy stuff")
    print("[3] sell stuff")
    print("[4] show items")
    print("[5] leave planet")
    much = input("")
    if (much == "1"):
        buy()
    elif(much == "2"):
        buystuff()
    elif(much == "3"):
        sellstuff()
    elif(much == "4"):
        print()
        print("Curry: " + str(wares["curry"]))
        print("Chips: " + str(wares["chip"]))
        print("Weapons: " + str(wares["weapon"]))
        print()
    elif(much == "5"):
        turns = turns + 1
        if(randint(0,2) == 1):
            print("you've been caught in a brawl with the Aljic space pirate crew")
            p = pirate(turns)
            if(len(fighter) > p.getSize()):
                print("the pirates were defeated!")
                print("you gained 4 XP (not really)")
            elif(len(fighter) == p.getSize()):
                if(randint(0,1) == 1):
                    print("the pirates were defeated!")
                    print("you gained 4 XP (not really)")
                else:
                    print("your fleet was destroyed!")
                    print("the game will now exit")
                    input("Press Enter to continue")
                    sys.exit()
            elif(len(fighter) < p.getSize()):
                print("your fleet was destroyed!")
                print("the game will now exit")
                input("Press Enter to continue")
                sys.exit()
        choosePlanet()

#setup
name = input("Please enter your name: ")
print("\n")
print ("Hello " + name + " welcome to panjeet spacesim")
choosePlanet()
while(continu):
    menu()


