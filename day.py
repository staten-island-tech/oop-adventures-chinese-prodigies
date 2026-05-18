import random

def day(self):
    self.daynumber += 1
    print(f"\nA new day begins... Day {self.daynumber}")
    consumed = self.population * random.randint(1, 5)
    self.food -= consumed
    print(f"\n Your population of {self.population} has consumed {consumed} rice bowls")