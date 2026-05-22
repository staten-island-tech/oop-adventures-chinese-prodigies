import random
import time
def gather_resources(self):
        location = input("Where would you like to send your members to search? (Cave, Forest, Mountain, Ocean, etc)")
        amount = int(input("How many people would you like to send?:"))
        if amount > 0 and amount <= self.population:
                resources_found = amount*random.randint(5, 10)+4

                people = random.randint(1, amount)

                self.natural_resources += resources_found
                self.population -= people
                print("Gathering resouces...")
                time.sleep(2)  # Wait 2 seconds

                print(f"\nYour {amount} workers gathered {resources_found} natural resources!...BUT {people} people died from overworking in the sun")

        else:
                print("insufficent amount of people/invalid option")