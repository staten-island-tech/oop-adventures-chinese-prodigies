# from game import numberchances

def buy(self):

        print("\nChoose an item to buy:")
        print("1. Food Supply (Cost: 25)\n"
              "Will give you +100 Food")
        print("2. Trade Caravan (Cost: 50)\n"
              "dont know what this does")

        choice = input("> ")

        if choice == "1":

            if self.wealth >= 25:
                self.wealth -= 25
                self.food += 100

                print("You bought food supplies!\n")
                return True

            else:
                print("Not enough wealth!")
                return False

        elif choice == "2":

            if self.wealth >= 50:
                self.wealth -= 50
                self.trade += 25

                print("You bought a trade caravan!")
                return True

            else:
                print("Not enough wealth!")
                return False

        else:
            print("Invalid choice.")
            return False


def force_buy(self):

    # if self.force_buy_used == True:
    #     print("You have already used your emergency food purchase.")
    #     print("Your empire has ended.")
    #     return
            
    people = self.population * 1.5
    money = self.wealth * .75
    print("\nYou HAVE to buy this or your kingdom will fall")
    print(f"1. {people} amount of food (Cost: {money})")
    print(f"2. I wanna die")

    choice = input("> ")

    if choice == "1":

        if self.wealth >= money:
            self.wealth -= money
            self.food += people
            self.force_buy_used = True

            print("You bought it")

    elif choice == "2":
        print("Your empire has ended")
    else:
        print("Invalid choice:)")
        return



