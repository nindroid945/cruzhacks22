all_cats = ["dogcat", "breadcat", "applecat", "suscat"]
# icons: dogcat_idle.png, etc.

class Cat:
    def __init__(self, name, icon, cost):
        self.level = 0
        self.name = name
        self.icon = icon
        self.cost = cost

    def levelup(self):
        self.level += 1
        if self.level % 5 == 0:
            self.cost += self.cost