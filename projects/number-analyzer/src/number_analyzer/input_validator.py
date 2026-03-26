# input_validator.py


import logging
import sys
from haashi_pkg.utility import Logger, ScreenUtil as su
from typing import Optional
from number_analyzer.types import NumberLike
from number_analyzer.number_utils import NumberUtils


class InputHandler:
    @staticmethod
    def get_input(
        msg0: Optional[str] = None,
        msg1: Optional[str] = "or press 'q' to return back to main menu.",
        prompt: str = ">>> ",
        logger: Optional[Logger] = None,
    ) -> Optional[NumberLike]:
        logger = logger or Logger(level=logging.INFO)
        su.space()
        if msg0:
            logger.info(f"{msg0} {msg1 if msg1 else ''}")
        user_input = input(prompt).lower().strip()

        output = InputHandler.parse_input(user_input)
        return output

    @staticmethod
    def parse_input(
        user_input: str, logger: Optional[Logger] = None
    ) -> Optional[NumberLike]:
        logger = logger or Logger(level=logging.INFO)

        if user_input == "q":
            return None

        try:
            if isinstance(user_input, int):
                return int(user_input)

            return float(user_input)

        except ValueError:
            logger.warning(f"{user_input} is not a valid integer or float!")
            logger.info("Falling back to main menu...")
            return None


class NumberController:
    @staticmethod
    def check_even(logger: Optional[Logger] = None) -> Optional[str]:
        logger = logger or Logger(level=logging.INFO)

        num = InputHandler.get_input(
            msg0="Enter a number to check if it's even", prompt=">>> ", logger=logger
        )

        if num is None:
            return num

        if NumberUtils.is_even(num):
            return f"{num} is even."
        return f"{num} is not even."

    @staticmethod
    def check_prime(logger: Optional[Logger] = None) -> Optional[str]:
        logger = logger or Logger(level=logging.INFO)

        num = InputHandler.get_input(
            msg0="Enter a number to check if it's prime", prompt=">>> ", logger=logger
        )

        if num is None:
            return num

        if NumberUtils.is_prime(num):
            return f"{num} is prime."
        return f"{num} is not prime."

    @staticmethod
    def check_square_root(logger: Optional[Logger] = None) -> Optional[str]:
        logger = logger or Logger(level=logging.INFO)

        num = InputHandler.get_input(
            msg0="Enter a number to calculate its square root",
            prompt=">>> ",
            logger=logger,
        )

        if num is None:
            return num

        result, rounded_to, rounded, sf = NumberUtils.square_root(num)
        formatted_result = (
            f"Square root check for {num} "
            f"Exact value: {result} | Rounded ({sf} sf): {rounded_to} | "
            f"Integer: {rounded}"
        )

        return su.format_text(formatted_result)
