from order_summary.summary import order_summary

if __name__ == "__main__":
    print("=== Order with all info ===")
    order_summary("House Burger", "Crispy Chicken", name="John", table=4, notes="No onions")

    print("\n=== Order missing table ===")
    order_summary("Beyond Burger", name="Alice", notes="Extra sauce")

    print("\n=== Order missing dishes ===")
    order_summary(name="Eli", table=3)
