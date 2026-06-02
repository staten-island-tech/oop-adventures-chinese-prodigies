import random
import time



def plague(kingdom):
        print("\n☠️ A DEADLY PLAGUE SPREADS THROUGH YOUR KINGDOM!...")
        time.sleep(1)

        deaths = max(1, int(kingdom.population * random.uniform(0.05, 0.2)))
        kingdom.population -= deaths

        food_loss = random.randint(10, 40)
        kingdom.food = max(0, kingdom.food - food_loss)

        print(f"{deaths} people have died.")
        print(f"You lost {food_loss} food due to chaos and sickness.")

def harvest_blessing(kingdom):
        print("\n🌾 A BLESSED HARVEST FILLS YOUR FARMS!...")

        food = random.randint(100, 400)
        kingdom.food += food

        print(f"You gained {food} food.")

def trade_boost(kingdom):
        print("\n💰 MERCHANTS BRING GREAT TRADE OFFERS!...")

        wealth = random.randint(100, 400)
        kingdom.wealth += wealth

        print(f"You gained {wealth} wealth from trade.")

def bandit_attack(kingdom):
        print("\n🏴 BANDITS ARE RAIDING YOUR LANDS!...")
        time.sleep(1)

        if kingdom.military < 20:
            loss = random.randint(20, 60)
            kingdom.wealth = max(0, kingdom.wealth - loss)
            kingdom.population -= random.randint(1, 5)

            print("Your army is too weak to defend properly!")
            print(f"You lost {loss} wealth and some civilians were killed.")
        else:
            print("Your army repelled the bandits!")
            loot = random.randint(10, 30)
            kingdom.wealth += loot
            print(f"You gained {loot} wealth from stolen goods. yay")

def invasion_event(kingdom):
        print("\nAN ENEMY ARMY IS INVADING YOUR KINGDOM!..")
        time.sleep(1)

        enemy_strength = int(kingdom.military * random.uniform(0.7, 1.2))

        print(f"Enemy army strength: {enemy_strength}")
        print(f"Your army strength: {kingdom.military}")

        print("\nWhat will you do?")
        print("1. Fight the invaders")
        print("2. Surrender (lose wealth, save lives)")

        choice = input("> ")

        if choice == "1":
            fight_invasion(kingdom, enemy_strength)

        elif choice == "2":
            surrender(kingdom, enemy_strength)

        else:
            print("Confusion leads to disaster...")
            fight_invasion(kingdom, enemy_strength)

def fight_invasion(kingdom, enemy_strength):
        print("\nYOUR ARMY FIGHTTTTTTT THE ENEMY!")

        time.sleep(1)

        power = kingdom.military + random.randint(-10, 20)

        if power >= enemy_strength:
            print("🏆 YOU WON THE BATTLE!")

            loot = random.randint(20, 80)
            kingdom.wealth += loot

            losses = random.randint(1, 5)
            kingdom.population -= losses

            print(f"You gained {loot} wealth.")
            print(f"You lost {losses} soldiers/civilians.")
        else:
            print("💀 YOU LOST THE BATTLE!")

            losses = random.randint(10, 30)
            kingdom.population -= losses

            wealth_loss = random.randint(20, 70)
            kingdom.wealth = max(0, kingdom.wealth - wealth_loss)

            print(f"You lost {losses} people.")
            print(f"You lost {wealth_loss} wealth.")

def surrender(kingdom, enemy_strength):
        print("\n noooooo...You surrendered to avoid destruction...")

        wealth_loss = random.randint(20, 60)
        kingdom.wealth = max(0, kingdom.wealth - wealth_loss)

        population_loss = random.randint(1, 10)
        kingdom.population -= population_loss

        print(f"You lost {wealth_loss} wealth as tribute.")
        print(f"{population_loss} people were taken as slaves.")

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
    