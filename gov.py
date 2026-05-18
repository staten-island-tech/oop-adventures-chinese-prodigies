def make_political_decision(self):

        print("\nA group of citizens demands more rights.")
        print("1. Give citizens more freedom")
        print("2. Keep strict laws")

        choice = input("> ")

        if choice == "1":

            print("\nThe people celebrate your kindness! Population increased by 20 as more people come to your empire and wealthy by 10. however 10 military are killed bc of free rights")

            self.population += 20
            self.wealth += 10
            self.military -= 10

        elif choice == "2":

            print("\nOrder is maintained through force. 20 mititary were needed and 10 people died from protesting")

            self.military += 20
            self.population -= 10

        else:
            print("Invalid decision.")

