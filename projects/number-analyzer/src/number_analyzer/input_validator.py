

# validator.py


import logging
from haashi_pkg.utility import Logger, ScreenUtil as su
from typing import Optional, Union


class CliHandler:

    @staticmethod
    def get_input(
        msg0: str = "Enter a integer to check if it is even or odd",
        msg1: str = "(or 'q' to return to main-menu)",
        symbol: str = ">>> ",
        logger: Optional[Logger] = None
    ) -> Optional[Union[int, float]]:

        stop = None
        logger = logger or Logger(level=logging.INFO)

        su.space()
        logger.info(f"{msg0} {msg1}")
        user_input = input(symbol).lower().strip()

        stop = user_input.lower().strip() == 'q'
        if stop:
            return

        try:
            if isinstance(user_input, int):
                return int(user_input)

            return float(user_input)

        except ValueError:
            raise ValueError(
                f"{user_input} is not a valid integer or float."
            )


class InputValidator:

    def __init__(self, logger: Optional[Logger] = None) -> None:
        self.logger = logger or Logger(level=logging.INFO)

        # ======================
        # Validate even or odd
        # ======================

    def is_even_validator(self, num:) -> None:
        """Runs the even/odd checker loop.
        Handles user input and displays results.
        """

        while True:
            num = self.parse_input()

            if num is None:
                print("\nExiting..")
                self.ut.clear_line(n=6, timeout=1)
                break

            if num < 0:
                self.ut.clear_line(n=5, timeout=0.2)
                continue

            if self.lc.is_even_or_odd(num):
                print(f"\n{num} is an even number.")
            else:
                print(f"\n{num} is an odd number.")

            self.ut.clear_line(n=5, timeout=5)

    # ======================
    # Validate prime
    # ======================

    def validate_prime(self) -> None:
        """Runs the prime checker loop.
        Displays whether the number is prime or not.
        """

        while True:
            num = self.parse_input(
                prompt_text="Enter a number to check if it is prime"
            )

            if num is None:
                print("\nExiting..")
                self.ut.clear_line(n=6, timeout=1)
                break

            if num < 0:
                self.ut.clear_line(n=5, timeout=0.2)
                continue

            if self.lc.is_prime(num):
                print(f"\n{num} is a prime number.")
            else:
                print(f"\n{num} is not a prime number.")

            self.ut.clear_line(n=5, timeout=5)

    # ======================
    # Validate Square root
    # ======================

    def validate_square_root(self) -> None:
        """Runs the square root calculator loop.
        Shows exact and rounded results.
        """

        while True:
            num = self.parse_input(
                prompt_text="Enter a number to find the square root"
            )

            if num is None:
                print("\nExiting..")
                self.ut.clear_line(n=6, timeout=1)
                break

            if num < 0:
                self.ut.clear_line(n=5, timeout=0.2)
                continue

            result, rounded_to, rounded, decimals = self.lc.square_root(num)

            print(f"\nThe square root of {num} is {result}")
            print(f"Rounded to {decimals}s.f is {rounded_to}")
            print(f"Rounded is {rounded}")

            self.ut.clear_line(n=9, timeout=8)
