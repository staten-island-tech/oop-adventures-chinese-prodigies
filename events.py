import random
import time

def trigger_event(kingdom):
    roll = random.randint(1, 100)

    if roll <= 5:
        plague(kingdom)
    elif roll <= 10:
        harvest_blessing(kingdom)
    elif roll <= 15:
        bandit_attack(kingdom)
    elif roll <= 20:
        invasion_event(kingdom)
    elif roll <= 25:
        trade_boost(kingdom)
    else:
        print("\nNothing unusual happens in your kingdom today...")
    

    def plague(kingdom):
        print("\n☠️ A DEADLY PLAGUE SPREADS THROUGH YOUR KINGDOM!")
        time.sleep(1)

        deaths = max(1, int(kingdom.population * random.uniform(0.05, 0.2)))
        kingdom.population -= deaths

        food_loss = random.randint(10, 40)
        kingdom.food = max(0, kingdom.food - food_loss)

        print(f"{deaths} people have died.")
        print(f"You lost {food_loss} food due to chaos and sickness.")