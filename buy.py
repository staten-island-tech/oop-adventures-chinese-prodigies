def buy(self):

        print("\nChoose an item to buy:")
        print("1. Food Supply (Cost: 25)\n"
              "Will give you +25 Food")
        # print("2. Trade Caravan (Cost: 50)\n"
        #       "dont know what this does")

        choice = input("> ")

        if choice == "1":

            if self.wealth >= 25:
                self.wealth -= 25
                self.food += 50

                print("You bought food supplies!\n")

            else:
                print("Not enough wealth!")

        # elif choice == "2":

        #     if self.wealth >= 50:
        #         self.wealth -= 50
        #         self.trade += 25

        #         print("You bought a trade caravan!")

        #     else:
        #         print("Not enough wealth!")

        # else:
        #     print("Invalid choice.")


