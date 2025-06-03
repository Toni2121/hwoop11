import random


def order_summary(*args, **kwargs):
    if not args:
        print("Error: No dishes ordered.")
        return

    print("Ordered Dishes:")
    for dish in args:
        print(f"- {dish}")

    print("\n Customer Info:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

    if "table" not in kwargs:
        random_table = random.randint(1, 20)
        print(f"Auto-assigned table number: {random_table}")
