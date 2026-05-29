import time
import random
from day import day

class Building:
    def __init__(self, name):
        self.name = name

    def fix(self, kingdom, cost):
        if kingdom.wealth >= cost:
            self.health += cost
            kingdom.wealth -= cost
            print(f"{self.name} has {self.health} heath")
            print(f"{kingdom.name} now has {kingdom.wealth} wealth left.")
        else:
            print("Not enough funds")
def build(self):

        print("Choose a building:")
        print("1. House (Cost: 20 wealth and 15 natural resources)\n"
              "With each House you have, you will add 10 civilians to your population while also adding 2 for each house you have every day")
        print("2. Farm (Cost: 30 wealth and 15 natural resources)\n"
              "Every Farm allows you to farm for rice :p")
        print("3. Barracks (Cost: 50 wealth and 15 natural resources)\n"
              "Barracks give you the option to train your army, letting you store civilians and train them into soldiers")
        print("4. Salt Mines (Cost: 60 wealth and 35 natural resources)\n"
              "Salt Mines give you natural resources every day")

        choice = input("> ")

        if choice == "1":

            if self.wealth >= 20 and self.natural_resources >= 15:
                self.wealth -= 20
                self.natural_resources -= 15
                self.house_count += 1
                self.population += self.house_count * 10
                self.buildings.append(Housing())
                
                print("Building...")
                time.sleep(2)  # Wait 2 seconds

                print("A House was built!")
            else:
                print("Not enough wealth or natural resources!")

        elif choice == "2":

            if self.wealth >= 30 and self.natural_resources >= 15:
                self.wealth -= 30
                self.natural_resources -= 15
                self.food += 50
                self.buildings.append(Farm())
                self.farm1 =+1
                print("Building...")
                time.sleep(2)  # Wait 2 seconds

                print("A Farm was built!")
            else:
                print("Not enough wealth or natural resources!")

        elif choice == "3":

            if self.wealth >= 50 and self.natural_resources >= 15:
                self.wealth -= 50
                self.natural_resources -= 15
                self.military += 25
                self.buildings.append(Barracks())
                print("Building...")
                time.sleep(2)  # Wait 2 seconds

                print("A Barracks was built!")
            else:
                print("Not enough wealth or natural resources!")

        elif choice == "4":

            if self.wealth >= 30 and self.natural_resources >= 35:
                self.wealth -= 30
                self.natural_resources -= 35
                self.food += 50
                self.saltmine +=1
                self.buildings.append(Salt_Mines())
                print("Building...")
                time.sleep(2)  # Wait 2 seconds

                print("A Salt Mine was built!")
            else:
                print("Not enough wealth or natural resources!")

        else:
            print("Invalid choice.")

class Housing(Building):
    def __init__(self):
        super().__init__("House")
        self.people = 0
        self.name = "House"
        
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def more_population(self):
        for building in self.buildings:

            if isinstance(building, Housing):
                building.menu(self)
                return
            
            # append to house, then add the poeple to hose population yay
            
        

class Farm(Building):
    def __init__(self):
        super().__init__("Farm")
        self.name = "Farm"

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def farm(self, player): 
        food_gained =self.farm1 * random.randint(20, 60)

        player.food += food_gained

        print("Farming...")
        time.sleep(2)

        print(f"\nYour farmers produced {food_gained} food (rice bowl) using {farm1} farm!")

def farm(self):

    for building in self.buildings:

        if isinstance(building, Farm):
            building.farm(self)
            return
            
    print("You do not have a farm.")

class Salt_Mines(Building):
    def __init__(self):
        super().__init__("Salt Mines")
        self.days = 1
        self.name = "Salt Mines"
        
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
    
    def make_resources(self, kingdom):
        if self.day > kingdom.daynumber:
            self.day = kingdom.daynumber
            resources_made = random.randint(20, 40)
            self.natural_resources += resources_made
            
            

        

class Barracks(Building):
    def __init__(self,):
        super().__init__("Barracks")
        self.capacity = 50
        self.soldiers = 0
        self.people = 0
        self.name = "Barracks"
        
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


    def add_people(self, kingdom, amount):
        if kingdom.population < amount:
            print("Not enough Civilians in the kingdom")
            return
        
        if self.people + amount <= self.capacity:
            self.people += amount
            kingdom.population -= amount
            print(f"{amount} civilian/people entered the barrack")
            print(f"{self.people} number of civilians/people are in the barracks now")
        else:
            print("Not Enough Space")

    def train_soldiers(self, kingdom, amount):
        if self.people < amount:
            print("Not enough Civilians in Baraacks")
            return
        if self.soldiers + amount > self.capacity:
            print("Not enough space in barracks!")
            return
        
        self.people -= amount
        self.soldiers += amount
        print(f"Trained {amount} civilians into soldiers!")
        print(f"Civilians in Barracks Now: {self.people}/{self.capacity}")

    def menu(self, kingdom):

        print("\n=== Barracks ===")
        print("1. Send civilians to barracks\n"
              "This option sends civilians from your empire into the barracks, subtracting your population, capacity is 50")
        print("2. Train soldiers\n"
              "This option gives you the option to turn the civilians inside your barracks into soldiers\n"
                "which will be added to your military and taken out of the barracks automatically")

        choice = input("> ")

        if choice == "1":

            amount = int(input("How many civilians? "))
            self.add_people(kingdom, amount)

        elif choice == "2":

            amount = int(input("How many soldiers to train? "))
            self.train_soldiers(kingdom, amount)

        else:
            print("Invalid choice")


def train_army(self):

    for building in self.buildings:

        if isinstance(building, Barracks):
            building.menu(self)
            return
            
    print("You do not have a barracks.")

