import random
import time
def gather_resources(self):
        location = input("Where would you like to send your members to search? (Cave, Forest, Mountain, Ocean, etc)")

        while True:
                amount_input = input("How many people would you like to send?:")

                if amount_input.strip() == "":
                        print("Insufficient amount of people/invalid option")
                        return False

                if not amount_input.isdigit():
                        print("Insufficient amount of people/invalid option")
                        return False
        
                amount = int(amount_input)

                if amount <= 0 or amount > self.population:
                        print("You dont have enough population")
                        return False

                resources_found = amount*random.randint(3, 10)+2

                people = int(amount * random.uniform(0.1, 0.12))

                self.natural_resources += resources_found
                self.population -= people
                print("Gathering resouces...")
                time.sleep(2)  # Wait 2 seconds

                print(f"\nYour {amount} workers gathered {resources_found} natural resources!...BUT {people} people died from overworking in the sun")
                return True

                