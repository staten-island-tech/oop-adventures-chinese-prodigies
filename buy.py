def buy(self):

        print("\nChoose an item to buy:")
        print("1. Food Supply (Cost: 25)")
        print("2. Weapons (Cost: 40)")
        print("3. Trade Caravan (Cost: 50)")

        choice = input("> ")

        if choice == "1":

            if self.wealth >= 25:
                self.wealth -= 25
                self.food += 50

                print("You bought food supplies!\n")

            else:
                print("Not enough wealth!")

        elif choice == "2":

            if self.wealth >= 40:
                self.wealth -= 40
                self.military += 20

                print("You bought weapons!")

            else:
                print("Not enough wealth!")

        elif choice == "3":

            if self.wealth >= 50:
                self.wealth -= 50
                self.trade += 25

                print("You bought a trade caravan!")

            else:
                print("Not enough wealth!")

        else:
            print("Invalid choice.")


