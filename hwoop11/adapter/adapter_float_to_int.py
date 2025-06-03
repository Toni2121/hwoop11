from .factorial_calculator import FactorialCalculator


class AdapterFloat2Int(FactorialCalculator):
    def calc_factorial(self, number: float) -> int:
        return super().calc_factorial(int(number))
