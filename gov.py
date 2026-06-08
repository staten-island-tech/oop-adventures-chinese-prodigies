import random 
import time
def make_decision(kingdom):
    print("\nMake a decision!")
    print("1. Make a political decision")
    print("2. Attack others!!")

    decision = input("What Would you like to do?")

    if decision == "1":
         make_political_decision(kingdom)
         return True

    elif decision == "2":
         fight(kingdom)      
         return True
    else:
        print("\nInvalid choice")
        return False
    
    
def make_political_decision(kingdom):

        print("\nA group of citizens demands more rights.")
        print("1. Give citizens more freedom")
        print("2. Keep strict laws")

        choice = input("> ")

        if choice == "1":

            print("\nThe people celebrate your kindness! Population increased by 20 as more people come to your empire and wealthy by 10. however 10 military are killed bc of free rights")

            kingdom.population += 20
            kingdom.wealth += 10
            kingdom.military -= 10

        elif choice == "2":

            print("\nOrder is maintained through force. 20 mititary were needed and 10 people died from protesting")

            kingdom.military += 20
            kingdom.population -= 10

        else:
            print("Invalid decision.")
            make_political_decision(kingdom)

def fight(kingdom):
        country = ["China", "England", "Ottoman", "Safavid", "Mughal", "Spain", "Mali" , "Mongols"]
        test_country = random.choice(country)
        print(f"\nYou decided to fight the {test_country}")
        time.sleep(1)

        enemy_strength = random.randint(
        10 + kingdom.daynumber // 2,
        80 + kingdom.daynumber
        )

        print(f"{test_country} army strength: {enemy_strength}")
        print(f"Your army strength: {kingdom.military}")

        print("\nWhat will you do?")
        print("1. Fight still?")
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
        print("\n noooooo...You surrendered but theyre mad...")

        wealth_loss = random.randint(20, 60)
        kingdom.wealth = max(0, kingdom.wealth - wealth_loss)

        population_loss = random.randint(1, 10)
        kingdom.population -= population_loss

        print(f"You lost {wealth_loss} wealth as tribute.")
        print(f"{population_loss} people were taken as slaves.")