import buildings
import decision

print("Welcome to your KINGDOM! Congrats On Being a RULER! Please do your people well! Please customize yourself")

name = input("What's your empire's name? ")
""" pet_type = input("What type of pet would you like? (active, calm, lazy, fun): ")
money = int(input("How much money does your pet have? "))
 """

class Kingdom:
    def __init__(self, name, population, food, military, wealth, trade):
        self.name = name
        self.population = population
        self.food = food
        self.military = military
        self.wealth = wealth
        self.trade = trade

    def build(self, minutes=5):

    def farm(self):

    def train(self):

    def buy(self):

    def trade(self):

    def show_status(self):
        print("\n--- Kingdom STATUS ---")
        print(f"Name: {self.name}")
        print(f"Population: {self.population}")
        print(f"Food: {self.food}")
        print(f"Military: {self.military}")
        print(f"Wealth: {self.wealth}")
        print(f"Trade: {self.trade}")

while True:
    print("\nWhat would you like to do? Your Empire relies on you!: ")
    print("1. Build")
    print("2. Farm")
    print("3. Train Army")
    print("4. Buy Item")
    print("5. Make Political Decision")
    print("6. Trade")
    print("7. Show Stats")
    print("8. Quit: Destroy your empire")

    choice = input("> ")

    if choice == "1":
        Kingdom.build()

    elif choice == "2":
        Kingdom.farm()

    elif choice == "3":
        Kingdom.train_army()

    elif choice == "4":
        Kingdom.buy()

    elif choice == "5":
        Kingdom.make_political_decision()

    elif choice == "6":
        Kingdom.trade()

    elif choice == "7":
        Kingdom.show_status()

    elif choice == "8":
        print("You have failed ur empire. Bye u worthless rat.....")
        break

    else:
        print("Invalid choice.")