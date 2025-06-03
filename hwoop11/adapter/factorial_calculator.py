class FactorialCalculator:
    def calc_factorial(self, number: int) -> int:
        if number < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result
