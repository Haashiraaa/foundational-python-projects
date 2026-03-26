

# number_utils.py

import math
from types import NumberLike, SquareRoot


class NumberUtils:

    @staticmethod
    def is_even(num: NumberLike) -> bool:
        """Checks if a number is even.
        Returns True if even, False if odd.
        """
        return num % 2 == 0

    @staticmethod
    def is_prime(num: NumberLike) -> bool:
        """Checks if a number is prime.
        Returns True for prime numbers, else False.
        """
        if num < 2:
            return False
        if num == 2:
            return True
        return all(num % i != 0 for i in range(2, int(num**0.5) + 1))

    @staticmethod
    def square_root(num: NumberLike, decimals: int = 2) -> SquareRoot:
        """Calculates the square root of a number.
        Returns exact value, rounded value, and rounding precision.
        """
        result = math.sqrt(num)
        rounded_to = round(result, decimals)
        rounded = round(result)

        return result, rounded_to, rounded, decimals
