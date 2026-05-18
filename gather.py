import random
import time
def gather_resources(self):

        resources_found = random.randint(10, 40)

        people = random.randint(1, 10)

        self.natural_resources += resources_found
        self.population -= people
        print("Gathering resouces...")
        time.sleep(2)  # Wait 2 seconds

        print(f"\nYour workers gathered {resources_found} natural resources!...BUT {people} people died from overworking in the sun")
