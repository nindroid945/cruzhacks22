class Upgrade:
    def __init__(self, name, cost):
        self.name = name
        self.level = 0
        self.cost = cost

    def levelup(self):
        self.level += 1
        if self.level % 5 == 0:
            self.cost += self.cost