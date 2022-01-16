import cats
import upgrade


class Player:
    def __init__(self):
        self.click_count = 0
        self.kibble = 0
        self.fish = 0
        self.milk = 0
        self.cats = {}
        self.kpc = 1
        self.fpc = 0
        u1 = upgrade.Upgrade("kibble-inator", 10)
        u2 = upgrade.Upgrade("fish-inator", 25)
        self.upgrades = {"kibble-inator": u1, "fish-inator": u2}

    def get_cat(self, name, icon, cost):
        self.cats[name] = cats.Cat(name, icon, cost)