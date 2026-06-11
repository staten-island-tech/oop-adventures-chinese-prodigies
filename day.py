import random
from buildings import *

def day(self):
    self.daynumber += 1
    print(f"\nA new day begins... Day {self.daynumber}")
    consumed = int(self.population + self.military * random.uniform(1.0, 1.50))
    self.food -= consumed
    print(f"\n Your population of {self.population} has consumed {consumed} rice bowls")

    if self.house_count > 0:
        growth = self.house_count*2
        self.population += growth
        print(f"Your population increased by {growth} from the {self.house_count} houses")

    if self.saltmine > 0:
        growth1 = self.saltmine*10
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
    
    if self.trade:
        print(f"\nYou have {len(self.trade)} trade allies.")

    for country in self.trade:
        if country in trade_countries:
            mat_trade = random.randint(40, 70) + 4
            coin_trade = random.randint(10, 50) + 2

            if self.natural_resources > mat_trade:
                self.natural_resources -= mat_trade
                self.wealth += coin_trade

                print(
                    f"{country} traded you {coin_trade} coins "
                    f"for {mat_trade} wood/metal."
                )
            else:
                print(
                    f"{country} wanted to trade, but you only have "
                    f"{self.natural_resources} resources."
                )