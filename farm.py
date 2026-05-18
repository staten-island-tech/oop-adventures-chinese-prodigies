
import time
import random

def farm(kingdom):

    food_gained = random.randint(20, 60)

    kingdom.food += food_gained
        
    print("Farming...")
    time.sleep(2)  # Wait 2 seconds

    print(f"\nYour farmers produced {food_gained} food!")
