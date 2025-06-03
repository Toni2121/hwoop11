from builder_burger.builders import CrispyChickenBuilder, BeyondBurgerBuilder, HouseBurgerBuilder


def make_burger(builder):
    builder.add_bun()
    builder.add_veggies()
    builder.add_main()
    builder.add_sauce()
    builder.add_side()
    builder.add_packaging()
    builder.add_price()
    builder.get_burger().show()


if __name__ == "__main__":
    print("=== Crispy Chicken ===")
    make_burger(CrispyChickenBuilder())
    print("\n=== Beyond Burger ===")
    make_burger(BeyondBurgerBuilder())
    print("\n=== House Burger ===")
    make_burger(HouseBurgerBuilder())
