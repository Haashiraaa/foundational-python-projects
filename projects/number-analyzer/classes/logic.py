
# logic.py

import math


class Logic:
    def is_even_or_odd(self, num: int | float) -> bool:
        """Checks if a number is even.
        Returns True if even, False if odd.
        """
        return num % 2 == 0

    def is_prime(self, num: int | float) -> bool:
        """Checks if a number is prime.
        Returns True for prime numbers, else False.
        """
        if num < 2:
            return False
        return all(num % i != 0 for i in range(2, int(num**0.5) + 1))

    def square_root(
        self, num: int | float, decimals: int = 3
    ) -> tuple[float, float, int, int]:
        """Calculates the square root of a number.
        Returns exact value, rounded value, and rounding precision.
        """
        result = math.sqrt(num)
        rounded_to = round(result, decimals)
        rounded = round(result)

        return result, rounded_to, rounded, decimals
