from buildings import *
from gov import make_political_decision
from trade import trade_action
from events import trigger_event
from buy import buy
from gather import gather_resources
from day import day
from status import show_status
import time
import random

print("Welcome to your KINGDOM! Congrats On Being a RULER! Please do your people well! Please customize your KINGDOM: ")

name = input("What's your empire's name? ")
type = input("Where is your empire located?\n"
"1. Forest Civilization\n"
"A peaceful woodland kingdom focused on food production and population growth. \n"
"Forest civilizations gather berries, hunt wildlife, and build with abundant timber.\n"
"Their people thrive in nature, making them excellent farmers and traders. \n"
"Military is usually weaker because dense forests make large armies harder to train and move.\n"

"2. Desert Civilization\n"
"A harsh survival-based empire built around scarce resources and strong discipline.\n"
"Desert kingdoms have smaller populations due to the environment, but their soldiers are highly trained and resilient. \n"
"Trade becomes extremely important because caravans connect distant cities across the sands. \n"
"Food is limited, but wealth can grow quickly through commerce.\n"

"3. Mountain Civilization\n"
"A defensive and war-focused civilization hidden within rocky mountains. \n"
"Mountain kingdoms produce powerful warriors and strong fortresses because natural terrain protects them from enemies. \n"
"Mining provides large amounts of wealth and metal for weapons, but farming is difficult, so food supplies are often low and population growth is slow.\n"

"4. Island Civilization\n"
"A naval empire surrounded by oceans and dependent on fishing and sea trade.\n"
"Island civilizations excel at commerce, exploration, and diplomacy with distant lands. \n"
"Their food supply is stable because of fishing, and wealth grows through shipping routes, but they usually have smaller land armies and rely heavily on naval defense. ")


if type == "1":
    print("You have chosen Forest Civilization.")
    population = 18
    food = 200
    military = 6
    wealth = 100
    natural_resources = 100
    


elif type == "2":
    print("You have chosen Desert Civilization.")
    population = 23
    food = 225
    military = 6
    wealth = 150
    natural_resources = 80

elif type == "3":
    print("You have chosen Mountain Civilization.")
    population = 14
    food = 180
    military = 5
    wealth = 200
    natural_resources = 120

elif type == "4":
    print("You have chosen Island Civilization.")
    population = 20
    food = 217
    military = 15
    wealth = 200
    natural_resources = 90

else:
    print("Invalid choice")
    exit()


class Kingdom:

    def __init__(self, name, population, food, military,
                 wealth, natural_resources):

        self.name = name
        self.population = population
        self.food = food
        self.military = military
        self.wealth = wealth
        self.trade = []
        self.natural_resources = natural_resources
        self.buildings = []
        self.daynumber = 1 
        self.house_count = 0
        self.saltmine=0
        self.farm1 = 0






kingdom = Kingdom(
    name,
    population,
    food,
    military,
    wealth,
    natural_resources
    
)

while True:

    print("\nWhat would you like to do?")
    print("1. Build")
    print("2. Farm")
    print("3. Train Army")
    print("4. Buy Item")
    print("5. Make Political Decision")
    print("6. Trade")
    print("7. Gather Resources")
    print("8. Show Stats")
    print("9. Quit")
    
    choice = input("> ")

    if choice == "1":
        build(kingdom)
        trigger_event(kingdom)
        input("\nPress Enter to continue...")
        day(kingdom)

    elif choice == "2":
        farm(kingdom)
        trigger_event(kingdom)
        input("\nPress Enter to continue...")
        day(kingdom)

    elif choice == "3":
        train_army(kingdom)
        trigger_event(kingdom)
        input("\nPress Enter to continue...")
        day(kingdom)

    elif choice == "4":
        buy(kingdom)
        trigger_event(kingdom)
        input("\nPress Enter to continue...")

    elif choice == "5":
        make_political_decision(kingdom)
        trigger_event(kingdom)
        input("\nPress Enter to continue...")
        day(kingdom)

    elif choice == "6":
        trade_action(kingdom)
        trigger_event(kingdom)
        input("\nPress Enter to continue...")
        day(kingdom)

    elif choice == "7":
        gather_resources(kingdom)
        trigger_event(kingdom)
        input("\nPress Enter to continue...")
        day(kingdom)

    elif choice == "8":
        show_status(kingdom)
        trigger_event(kingdom)
        input("\nPress Enter to continue...")

    elif choice == "9":
        
        print("\nYour empire has fallen...")
        print("Game Over.")

        break

    else:
        print("invalid option ")

    if kingdom.population <=0:
        print("\nYour empire has fallen...")
        print("Game Over.")
        break

    if kingdom.population <=10:
        print("Your Population is low, buy houses or you will die")


    if kingdom.wealth <=0:
        print("\nYour empire has fallen...")
        print("Game Over.")
        break

    if kingdom.wealth <=10:
        print("Your wealth is low...trade or you will die")

    if kingdom.food <=0:
        numberchances = 1
        print("your men are starving!!!!!buy food!!!!!!!!!!(final chance)")
        buy(kingdom)
        numberchances +=1
        if numberchances == 2:
            print("\nYour empire has fallen...")
            print("Game Over.")

            break


    if kingdom.food <=10:
        print("Your food source is low, farm, buy food, or youll die")
        buy(kingdom)



