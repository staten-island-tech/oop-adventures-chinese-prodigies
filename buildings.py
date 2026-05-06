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

