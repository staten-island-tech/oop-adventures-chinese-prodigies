import time
import random

class Building:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def fix(self, kingdom, cost):
        if kingdom.wealth >= cost:
            self.health += cost
            kingdom.wealth -= cost
            print(f"{self.name} has {self.health} heath")
            print(f"{kingdom.name} now has {kingdom.wealth} wealth left.")
        else:
            print("Not enough funds")

class Housing(Building):
    def __init__(self, health, capacity):
        super().__init__("House", health)
        self.capacity = capacity
        self.people = 0

    def add_people(self, amount):
        if self.people + amount <= self.capacity:
            self.people += amount
            print(f"{amount} people moved in")
        else:
            print("Not Enough Space")

class Farm(Building):
    def __init__(self, health):
        super().__init__("Farm", health)

        

class Barracks(Building):
    def __init__(self, health, capacity):
        super().__init__("Barracks", health)
        self.capacity = capacity
        self.soldiers = 0
        self.people = 0

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
        kingdom.military += amount
        print(f"Trained {amount} civilians into soldiers!")
        print(f"Barracks training: {self.soldiers}/{self.capacity}")


    def menu(self, kingdom):

        print("\n=== Barracks ===")
        print("1. Send civilians to barracks")
        print("2. Train soldiers")

        choice = input("> ")

        if choice == "1":

            amount = int(input("How many civilians? "))
            self.add_people(kingdom, amount)

        elif choice == "2":

            amount = int(input("How many soldiers to train? "))
            self.train_soldiers(kingdom, amount)

        else:
            print("Invalid choice")



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




    def train_army(self):

        for building in self.buildings:

            if isinstance(building, Barracks):
                building.menu(self)
                return
            
        print("You do not have a barracks.")

                

