class Burger:
    def __init__(self):
        self.ingredients = []

    def add(self, part: str):
        self.ingredients.append(part)

    def show(self):
        for part in self.ingredients:
            print(part)
