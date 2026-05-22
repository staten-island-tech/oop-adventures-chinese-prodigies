import random

def day(self):
    self.daynumber += 1
    print(f"\nA new day begins... Day {self.daynumber}")
    consumed = self.population * random.randint(1, 2)+23
    self.food -= consumed
    print(f"\n Your population of {self.population} has consumed {consumed} rice bowls")

    growth = self.house_count * 2
    self.population += growth

    if self.trade == "China"or "England"or  "Ottoman"or "Safavid"or "Mughal"or "Spain" or "Mali" or "Mongols":
              
        mat_trade = random.randint(10, 20)+4
        coin_trade = random.randint(1, 10)+2
        self.natural_resources -= mat_trade
        self.wealth += coin_trade

        print(f"Your alliances {self.trade} has traded you {coin_trade} coins for {mat_trade} wood/metal")