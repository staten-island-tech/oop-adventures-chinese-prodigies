import random
from buildings import *

def day(self):
    self.daynumber += 1
    print(f"\nA new day begins... Day {self.daynumber}")
    consumed = self.population + self.military * random.randint(1, 2)+9
    self.food -= consumed
    print(f"\n Your population of {self.population} has consumed {consumed} rice bowls")

    if self.house_count > 0:
        growth = self.house_count*2
        self.population += growth
        print(f"Your population increased by {growth} from the {self.house_count} houses")

    if self.saltmine > 0:
        growth1 = self.saltmine*2
        self.natural_resources += growth1
        print(f"Your resources increased by {growth1} from the {self.saltmine} salt mines")
    

    trade_countries = [
    "China",
    "England",
    "Ottoman",
    "Safavid",
    "Mughal",
    "Spain",
    "Mali",
    "Mongols"
]

    for country in self.trade:
        if country in trade_countries:
            mat_trade = random.randint(10, 20)+4
            coin_trade = random.randint(1, 10)+2
            if self.natural_resources > mat_trade:
                self.natural_resources -= mat_trade
                self.wealth += coin_trade

                print(f"Your alliances {self.trade} has traded you {coin_trade} coins for {mat_trade} wood/metal")