class Player:
    def __init__(self):
        self.kibble = 0
        self.fish = 0
        self.milk = 0
        self.cats = {}

    def get_cat(self, cat):
        self.cats[cat.name] = cat