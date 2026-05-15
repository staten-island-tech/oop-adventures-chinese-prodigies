from buildings import Building, Barracks, Housing, Farm
# import decision
# import farm
# import trade
# import events
# import buy
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
    population = 150
    food = 300
    military = 50
    wealth = 100
    trade = 80
    natural_resources = 100


elif type == "2":
    print("You have chosen Desert Civilization.")
    population = 100
    food = 200
    military = 70
    wealth = 150
    trade = 60
    natural_resources = 50

elif type == "3":
    print("You have chosen Mountain Civilization.")
    population = 80
    food = 150
    military = 100
    wealth = 200
    trade = 40
    natural_resources = 120

elif type == "4":
    print("You have chosen Island Civilization.")
    population = 120
    food = 250
    military = 60
    wealth = 180
    trade = 100
    natural_resources = 90
else:
    print("Invalid choice")


class Kingdom:

    def __init__(self, name, population, food, military,
                 wealth, trade, natural_resources):

        self.name = name
        self.population = population
        self.food = food
        self.military = military
        self.wealth = wealth
        self.trade = []
        self.natural_resources = natural_resources
        self.buildings = []
        self.daynumber = 1


    def build(self):

        print("\nChoose a building:")
        print("1. House (Cost: 208)")
        print("2. Farm (Cost: 30)")
        print("3. Barracks (Cost: 50)")

        choice = input("> ")

        if choice == "1":

            if self.wealth >= 20:
                self.wealth -= 20
                self.population += 10
                self.buildings.append(Housing(100,50))

                print("Building...")
                time.sleep(2)  # Wait 2 seconds

                print("A House was built!")
            else:
                print("Not enough wealth!")

        elif choice == "2":

            if self.wealth >= 30:
                self.wealth -= 30
                self.food += 50
                self.buildings.append(Farm(100,50))
                print("Building...")
                time.sleep(2)  # Wait 2 seconds

                print("A Farm was built!")
            else:
                print("Not enough wealth!")

        elif choice == "3":

            if self.wealth >= 50:
                self.wealth -= 50
                self.military += 25
                self.buildings.append(Barracks(100,50))
                print("Building...")
                time.sleep(2)  # Wait 2 seconds

                print("A Barracks was built!")
            else:
                print("Not enough wealth!")

        else:
            print("Invalid choice.")



    def farm(self):

        food_gained = random.randint(20, 60)

        self.food += food_gained
        
        print("Farming...")
        time.sleep(2)  # Wait 2 seconds

        print(f"\nYour farmers produced {food_gained} food!")

    def train_army(self):
        for building in self.buildings:

            if isinstance(building, Barracks):

                print("1. Send civilians to barracks")
                print("2. Train soldiers")

            print("Training...")
            time.sleep(2)  # Wait 2 seconds

            print("\nYou trained 15 new soldiers!")

        else:
            print("\nNot enough population or food!")

    def buy(self):

        print("\nChoose an item to buy:")
        print("1. Food Supply (Cost: 25)")
        print("2. Weapons (Cost: 40)")
        print("3. Trade Caravan (Cost: 50)")

        choice = input("> ")

        if choice == "1":

            if self.wealth >= 25:
                self.wealth -= 25
                self.food += 50

                print("You bought food supplies!")

            else:
                print("Not enough wealth!")

        elif choice == "2":

            if self.wealth >= 40:
                self.wealth -= 40
                self.military += 20

                print("You bought weapons!")

            else:
                print("Not enough wealth!")

        elif choice == "3":

            if self.wealth >= 50:
                self.wealth -= 50
                self.trade += 25

                print("You bought a trade caravan!")

            else:
                print("Not enough wealth!")

        else:
            print("Invalid choice.")


    def make_political_decision(self):

        print("\nA group of citizens demands more rights.")
        print("1. Give citizens more freedom")
        print("2. Keep strict laws")

        choice = input("> ")

        if choice == "1":

            print("\nThe people celebrate your kindness! Population increased by 20 as more people come to your empire and wealthy by 10. however 10 military are killed bc of free rights")

            self.population += 20
            self.wealth += 10
            self.military -= 10

        elif choice == "2":

            print("\nOrder is maintained through force. 20 mititary were needed and 10 people died from protesting")

            self.military += 20
            self.population -= 10

        else:
            print("Invalid decision.")



    def trade_action(self):
        country = ["China", "England", "Ottoman", "Safavid", "Mughal", "Spain", "Mali" , "Mongols"]
        test_country = random.choice(country)
        max_mat = self.natural_resources
        max_wealth = self.wealth
        trade_mat = random.randint(1, max_mat)
        trade_wealth = random.randint(1, max_wealth)

        print(f"{test_country} would like to trade with you for materials and spices")
        print(f"1. Trade with {test_country}...You will lose {trade_mat} wood and iron but increase wealth by {trade_wealth}")
        print("2. no deal")

        choice = input("> ")

        if choice == "1":
            if max_mat >= trade_mat:
                self.natural_resources -= trade_mat 
                self.wealth+= trade_wealth 
                print(f"{test_country} was extremely pleased with the trade and would like to become an alliance. You will gain 1-10 silver coins everyday in exchange for 10-20 wood material. Do you accept to the conditions? Yes or No")
                choice1_ = input(">")
                
                if choice1_ == "Yes":
                    tradealliance = True
                    self.trade.append(f"{test_country}")


                else: 

                    print(f"{test_country} is extremely mad and attempted to colonize you...")
                    time.sleep()
                    print("Luckily you survived but your army has died along ")


                        


            else:
                print("You dont have enough resources for the trade. ")

        elif choice == "2":

            print("\nOrder is maintained through force. 20 mititary were needed and 10 people died from protesting")

            self.military += 20
            self.population -= 10

        else:
            print("Invalid decision.")

        wealth_gained = random.randint(20, 70)

        self.wealth += wealth_gained
        
        print("Trading...")
        time.sleep(2)  # Wait 2 seconds

        print(f"\nYour traders earned {wealth_gained} wealth!")
    
    def gather_resources(self):

        resources_found = random.randint(10, 40)

        people = random.randint(1, 10)

        self.natural_resources += resources_found
        self.population -= people
        print("Gathering resouces...")
        time.sleep(2)  # Wait 2 seconds

        print(f"\nYour workers gathered {resources_found} natural resources!...BUT {people} people died from overworking in the sun")



    def day(self):
        self.daynumber += 1
        print(f"\nA new day begins... Day {self.daynumber}")
        consumed = self.population * random.randint(1, 5)
        self.food -= consumed
        print(f"\n Your population of {self.population} has consumed {consumed} rice bowls")
            


kingdom = Kingdom(
    name,
    population,
    food,
    military,
    wealth,
    trade,
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
        kingdom.build()
        kingdom.day()

    elif choice == "2":
        kingdom.farm()
        kingdom.day()

    elif choice == "3":
        kingdom.train_army()
        kingdom.day()

    elif choice == "4":
        kingdom.buy()
        kingdom.day()

    elif choice == "5":
        kingdom.make_political_decision()
        kingdom.day()

    elif choice == "6":
        kingdom.trade_action()
        kingdom.day()

    elif choice == "7":
        kingdom.gather_resources()
        kingdom.day()

    elif choice == "8":
        show_status(kingdom)

    elif choice == "9":

        print("\nYour empire has fallen...")
        print("Game Over.")

        break

    else:
        print("Invalid choice.")