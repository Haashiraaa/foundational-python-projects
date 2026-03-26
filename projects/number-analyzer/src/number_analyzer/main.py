
# main.py


import sys
import logging
from typing import Optional
from number_analyzer.input_validator import InputHandler, NumberController
from haashi_pkg.utility import Logger, ScreenUtil as su


# ======================
# Main Menu
# ======================

def main_menu() -> None:
    """Displays the list of available operations.
    Helps users choose what action to perform.
    """
    options: list[str] = [
        "Even or Odd Checker",
        "Prime Checker",
        "Square Root Calculator",
        "Exit."
    ]

    logger.info("Choose an operation:")
    for i, option in enumerate(options, start=1):
        logger.info(f"{i}. {option}")


# ======================
# Main
# ======================

def main(logger: Optional[Logger] = None) -> None:

    logger = logger or Logger(level=logging.INFO)

    su.space()
    logger.info("Hello! Welcome to the Number Analyzer!")
    logger.info(
        "This program will help you with some mathematical operations."
    )
    su.space()

    while True:

        main_menu()

        try:
            user_choice = InputHandler.get_input(
                prompt="Enter your choice (1-4):",
                logger=logger
            )

            if user_choice == 1:
                validate.validate_even_odd()

            elif user_choice == 2:
                validate.validate_prime()

            elif user_choice == 3:
                validate.validate_square_root()

            elif user_choice == 4:
                logger.info("\nExiting...")
                ut.clear_line(n=3, timeout=1)
                sys.exit(0)

            else:
                logger.info("\nChoice out of range!")
                ut.clear_line(n=3, timeout=0.2)

        except ValueError:
            logger.info("\nInvalid choice!")
            ut.clear_line(n=3, timeout=0.2)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info()
        sys.exit(0)
