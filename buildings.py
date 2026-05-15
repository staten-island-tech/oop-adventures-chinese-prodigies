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

