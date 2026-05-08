import random
import game


class Decision:
    def __init__(self, decisions):
        self.original = decisions[:]
        self.reset()

    def reset(self):
        self.remaining = self.original[:]
        random.shuffle(self.remaining)

    def get_random_decision(self):
        if not self.remaining:
            return None

        return self.remaining.pop()


    def political_decision(self, kingdom):
        print("\nA group of citizens demands more rights.")
        print("1. Give citizens more freedom")
        print("2. Keep strict laws")

        choice = input("> ")

        if choice == "1":
            print("The people celebrate your kindness.")
            game.Kingdom.population += 20
            game.Kingdom.wealth += 10
            game.Kingdom.military -= 10

        elif choice == "2":
            print("Order is maintained through force.")
            game.Kingdom.military += 20
            game.Kingdom.population -= 10

        else:
            print("Invalid decision.")

