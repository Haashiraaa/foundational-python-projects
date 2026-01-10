# main_launcher.py


import sys
from classes.validator import Validate
from haashi_pkg.utility.utils import Utility
from guide import print_guide

WELCOME = "Welcome to the Temperature Converter!"


def main() -> None:
    """Runs the main application loop."""

    validate = Validate()
    ut = Utility()

    print(f"{WELCOME}\n")

    request_guide = input(
        "Would you like to see the guide? (y/n): "
    ).lower().strip()

    if request_guide in {"y", "yes"}:
        ut.clear_line()
        print_guide()
        ut.clear_screen(15)
    else:
        ut.clear_screen()

    while True:
        validate.console.print(f"[cyan]{WELCOME}[/cyan]\n")
        validate.validate_conversions()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        sys.exit(0)

