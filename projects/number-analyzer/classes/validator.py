from haashi_pkg.utility.utils import Utility
from classes.logic import Logic
from typing import Optional


class Validate:
    def __init__(self) -> None:
        """Initializes logic and utility helpers."""
        self.lc = Logic()
        self.ut = Utility()

    # ======================
    # Parse input
    # ======================

    def parse_input(
        self,
        prompt_text: str = "Enter a integer to check if it is even or odd",
        end_prompt_text: str = "(or 'q' to return to main-menu)",
        prompt_symbol: str = ">>> "
    ) -> Optional[float]:
        """Gets user input and converts it to a float.
        Returns None if user quits, -1 if input is invalid.
        """

        print(f"\n{prompt_text} {end_prompt_text}")
        user_input = input(prompt_symbol).lower().strip()

        if user_input == 'q':
            return None

        try:

            parsed_input = float(user_input)

            if parsed_input < 0:
                raise ValueError("\nInvalid integer!")

            return parsed_input

        except ValueError:
            print("\nInvalid integer!")
            return -1

    # ======================
    # Validate even or odd
    # ======================

    def validate_even_odd(self) -> None:
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
