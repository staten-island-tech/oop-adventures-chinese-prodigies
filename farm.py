
import time
import random

def farm(self):

    food_gained = random.randint(20, 60)

    self.food += food_gained
        
    print("Farming...")
    time.sleep(2)  # Wait 2 seconds

    print(f"\nYour farmers produced {food_gained} food!")
