from adapter.factorial_calculator import FactorialCalculator
from adapter.adapter_float_to_int import AdapterFloat2Int
from adapter.adapter_list_to_int import AdapterList2Int


def print_factorial_number(factorial, number):
    print(factorial.calc_factorial(number))


if __name__ == "__main__":
    print_factorial_number(FactorialCalculator(), 5)
    print_factorial_number(AdapterFloat2Int(), 3.0)
    print_factorial_number(AdapterList2Int(), [7, 9, 10])
