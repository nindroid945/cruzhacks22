import cats
class Player:
    def __init__(self):
        self.kibble = 0
        self.fish = 0
        self.milk = 0
        self.cats = {}
        self.upgrades = {"mega kibbler": 0}
        self.kpc = 1
        self.fpc = 0

    def get_cat(self, name, icon, cost):
        self.cats[name] = cats.Cat(name, icon, cost)