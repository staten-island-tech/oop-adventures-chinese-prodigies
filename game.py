# import buildings
# import decision
# import farm
# import trade
# import events
# import buy

print("Welcome to your KINGDOM! Congrats On Being a RULER! Please do your people well! Please customize your KINGDOM: ")

name = input("What's your empire's name? ")
type = input("Where is your empire located?\n"
"1. Forest Civilization\n"
"A peaceful woodland kingdom focused on food production and population growth. Forest civilizations gather berries, hunt wildlife, and build with abundant timber. Their people thrive in nature, making them excellent farmers and traders, but their military is usually weaker because dense forests make large armies harder to train and move.\n"
"2. Desert Civilization\n"
"A harsh survival-based empire built around scarce resources and strong discipline. Desert kingdoms have smaller populations due to the environment, but their soldiers are highly trained and resilient. Trade becomes extremely important because caravans connect distant cities across the sands. Food is limited, but wealth can grow quickly through commerce.\n"
"3. Mountain Civilization\n"
"A defensive and war-focused civilization hidden within rocky mountains. Mountain kingdoms produce powerful warriors and strong fortresses because natural terrain protects them from enemies. Mining provides large amounts of wealth and metal for weapons, but farming is difficult, so food supplies are often low and population growth is slow.\n"
"4. Island Civilization\n"
"A naval empire surrounded by oceans and dependent on fishing and sea trade. Island civilizations excel at commerce, exploration, and diplomacy with distant lands. Their food supply is stable because of fishing, and wealth grows through shipping routes, but they usually have smaller land armies and rely heavily on naval defense. ")

if type == "1":
    print("You have chosen Forest Civilization.")
    population = 150
    food = 300
    military = 50
    wealth = 100
    trade = 80
    natural_resources = 100

elif type == "2":
    print("You have chosen Desert Civilization.")
    population = 100
    food = 200
    military = 70
    wealth = 150
    trade = 60
    natural_resources = 50

elif type == "3":
    print("You have chosen Mountain Civilization.")
    population = 80
    food = 150
    military = 100
    wealth = 200
    trade = 40
    natural_resources = 120

elif type == "4":
    print("You have chosen Island Civilization.")
    population = 120
    food = 250
    military = 60
    wealth = 180
    trade = 100
    natural_resources = 90
else:
    print("Invalid choice")


class Kingdom:
    def __init__(self, name, population, food, military, wealth, trade, natural_resources, decision):
        self.name = name
        self.population = population
        self.food = food
        self.military = military
        self.wealth = wealth
        self.trade = trade
        self.natural_resources = natural_resources
        self.make_political_decision = decision
        self.buildings = []

    def build(self, building, cost):
        if self.wealth >= cost:
            self.wealth -= cost
            self.building.append(building)

            print(f"{building.name} was constructed!")
            print(f"Wealth remaining: {self.wealth}")
        else:
            print("Not enough wealth!")



        # types_of_buildings = ["House", "Building", "Barracks"]
        # for i, building in enumerate(types_of_buildings, 1):
        #     print(f"{i}. {building}")
        # choice = input("Choose a building to construct: ")
        # if choice == "1":
        #     print("You have constructed a House.")
        # elif choice == "2":
        #     print("You have constructed a Building.")
        # elif choice == "3":
        #     print("You have constructed a Barracks.")
        # else:
        #     print("Invalid choice.")

    # def farm(self):

    # def train(self):

    # def buy(self):

    # def make_political_decision(self):

    # def trade(self):
    
    # def natural_resources(self):
            

    def show_status(self):
        print("\n--- Kingdom STATUS ---")
        print(f"Name: {self.name}")
        print(f"Population: {self.population}")
        print(f"Food: {self.food}")
        print(f"Military: {self.military}")
        print(f"Wealth: {self.wealth}")
        print(f"Trade: {self.trade}")
        print(f"Natural Resources: {self.natural_resources}")

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