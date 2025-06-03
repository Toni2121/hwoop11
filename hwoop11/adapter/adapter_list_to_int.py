from .factorial_calculator import FactorialCalculator


class AdapterList2Int(FactorialCalculator):
    def calc_factorial(self, numbers: list[int]) -> list[int]:
        return [super().calc_factorial(int(n)) for n in numbers]
