from .burger_builder import BurgerBuilder


class CrispyChickenBuilder(BurgerBuilder):
    def add_bun(self): self.burger.add("Bun")

    def add_veggies(self): self.burger.add("Lettuce, Tomato")

    def add_main(self): self.burger.add("Crispy Chicken")

    def add_sauce(self): self.burger.add("Mayo")

    def add_side(self): self.burger.add("Fries")

    def add_packaging(self): self.burger.add("Box")

    def add_price(self): self.burger.add("Price: $10")


class BeyondBurgerBuilder(BurgerBuilder):
    def add_bun(self): self.burger.add("Whole Wheat Bun")

    def add_veggies(self): self.burger.add("Onion, Pickles")

    def add_main(self): self.burger.add("Beyond Patty")

    def add_sauce(self): self.burger.add("Vegan Sauce")

    def add_side(self): self.burger.add("Salad")

    def add_packaging(self): self.burger.add("Eco Wrap")

    def add_price(self): self.burger.add("Price: $12")


class HouseBurgerBuilder(BurgerBuilder):
    def add_bun(self): self.burger.add("Sesame Bun")

    def add_veggies(self): self.burger.add("Lettuce, Onion, Pickle")

    def add_main(self): self.burger.add("House Special Patty")

    def add_sauce(self): self.burger.add("Special Sauce")

    def add_side(self): self.burger.add("Onion Rings")

    def add_packaging(self): self.burger.add("Tray")

    def add_price(self): self.burger.add("Price: $11")
