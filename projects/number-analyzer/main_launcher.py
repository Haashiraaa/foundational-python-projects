
# main_launcher.py


import sys
from classes.validator import Validate
from haashi_pkg.utility.utils import Utility


# ======================
# Main Menu
# ======================

def menu() -> None:
    """Displays the list of available operations.
    Helps users choose what action to perform.
    """
    options: list[str] = [
        "Check if a number is even or odd.",
        "Check if a number is prime.",
        "Calculate the square root of a number.",
        "Exit."
    ]

    print("Choose an operation:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")


# ======================
# Main
# ======================

def main() -> None:
    """Runs the main program loop.
    Handles menu display and user choices.
    """
    validate = Validate()
    ut = Utility()

    ut.clear_screen()

    print("\nHello! Welcome to the Number Analyzer!")
    print("This program will help you with some mathematical operations.\n")

    menu()

    while True:
        try:
            user_choice = int(input("Enter your choice (1-4): ").strip())

            if user_choice == 1:
                validate.validate_even_odd()

            elif user_choice == 2:
                validate.validate_prime()

            elif user_choice == 3:
                validate.validate_square_root()

            elif user_choice == 4:
                print("\nExiting...")
                ut.clear_line(n=3, timeout=1)
                sys.exit(0)

            else:
                print("\nChoice out of range!")
                ut.clear_line(n=3, timeout=0.2)

        except ValueError:
            print("\nInvalid choice!")
            ut.clear_line(n=3, timeout=0.2)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        sys.exit(0)
