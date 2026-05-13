class Building:
    def __init__(self, name, health, population):
        self.name = name
        self.health = health
        self.population = population

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

class Barracks(Building):
    def __init__(self, health, capacity):
        super().__init__("Barracks", health)
        self.capacity = capacity
        self.soldiers = 0
        self.people = 0

    def add_people(self, amount):
        if self.people + amount <= self.capacity:
            self.people += amount
            print(f"{amount} civilian/people entered the barrack")
            print(f"{self.people} number of civilians/people are in the barracks now")
        else:
            print("Not Enough Space")

    def train_soldiers(self, amount):
        if self.kingdom.roles["Civilians"] < amount:
            print("Not enough Civilians to train")
            return
        if self.soldiers_training + amount > self.capacity:
            print("Not enough space in barracks!")
            return
        
        self.kingdom.roles["Civilians"] -= amount
        self.kingdom.roles["Soldiers"] -= amount
        self.soldiers_training += amount
        print(f"Trained {amount} civilians into soldiers!")
        print(f"Barracks training: {self.soldiers_training}/{self.capacity}")