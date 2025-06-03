from .burger import Burger


class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def add_bun(self): pass

    def add_veggies(self): pass

    def add_main(self): pass

    def add_sauce(self): pass

    def add_side(self): pass

    def add_packaging(self): pass

    def add_price(self): pass

    def get_burger(self) -> Burger:
        return self.burger
