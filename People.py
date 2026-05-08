# This is going to have classes of people like soldiers, farmers, civilians, etc
class Roles:
    def __init__(self, health, inventory):
        self.health = health
        self.inventory = inventory

class Civilians(Roles):
    def __init__(self, inventory):
        super().__init__(75, inventory)
