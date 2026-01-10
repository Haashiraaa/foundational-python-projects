# validator.py


import sys
import logging
from typing import Callable, Optional, Generic, TypeVar
from dataclasses import dataclass
from rich.console import Console

from classes.logic import ConverterLogic
from haashi_pkg.utility.utils import Utility


class Constants:
    """Stores all validation messages in one place."""

    INVALID_UNIT_WARNING = "is not a valid unit!"
    INVALID_UNIT = "Invalid unit!"
    INVALID_VALUE = "Value is invalid!"
    INVALID_CONVERSION = "Unsupported conversion!"


T = TypeVar("T")


@dataclass
class ValidationResult(Generic[T]):
    """
    Wraps validation results.
    Holds status, message, and optional data.
    """
    ok: bool
    message: Optional[str] = None
    data: Optional[T] = None


class Routes:
    """Maps unit pairs to their conversion functions."""

    def __init__(self):
        cl = ConverterLogic()
        self.routes: dict[tuple[str, str], Callable[[float], float]] = {
            ("k", "c"): cl.kelvin_to_celsius,
            ("k", "f"): cl.kelvin_to_fahrenheit,
            ("c", "k"): cl.celsius_to_kelvin,
            ("c", "f"): cl.celsius_to_fahrenheit,
            ("f", "k"): cl.fahrenheit_to_kelvin,
            ("f", "c"): cl.fahrenheit_to_celsius,
        }


class Validate:
    """
    Handles user input and validation.
    Connects input flow to conversion logic.
    """

    def __init__(self) -> None:
        self.units: dict[str, str] = {
            "k": "K", "c": "°C", "f": "°F",
        }
        self.routes_map = Routes().routes
        self.ut = Utility(level=logging.WARNING)
        self.ct = Constants()
        self.console = Console()

    def check_exit(self, raw: str) -> str:
        """Exit program if user types 'q'."""
        if raw.lower().strip() == "q":
            sys.exit(0)
        return raw

    def get_unit(self) -> str:
        """Prompt for source unit."""
        return self.check_exit(input("Unit: ").lower().strip())

    def get_value(self) -> str:
        """Prompt for temperature value."""
        return self.check_exit(input("Value: ").lower().strip())

    def get_converted_unit(self) -> str:
        """Prompt for target unit."""
        return self.check_exit(input("Converted Unit: ").lower().strip())

    def parse_returns(self) -> ValidationResult[tuple[str, float, str]]:
        """
        Validates raw user input.
        Returns structured validation result.
        """

        unit = self.get_unit()
        if unit not in self.units:
            return ValidationResult(False, self.ct.INVALID_UNIT)

        try:
            value = float(self.get_value())
        except ValueError:
            return ValidationResult(False, self.ct.INVALID_VALUE)

        converted_unit = self.get_converted_unit()
        if converted_unit not in self.units:
            return ValidationResult(False, self.ct.INVALID_UNIT)

        return ValidationResult(True, data=(unit, value, converted_unit))

    def validate_conversions(self) -> None:
        """
        Runs full validation and conversion flow.
        Displays result or user-friendly errors.
        """

        result = self.parse_returns()

        if not result.ok:
            self.console.print(f"\n[bright_red]{result.message}[/bright_red]")
            self.ut.clear_line(n=7, timeout=0.2)
            return

        assert result.data is not None

        unit, value, converted_unit = result.data

        func = self.routes_map.get((unit, converted_unit))
        if not func:
            self.console.print(
                f"\n[bright_red]{self.ct.INVALID_CONVERSION}[/bright_red]"
            )
            self.ut.clear_line(n=7, timeout=0.2)
            return

        converted_value = func(value)
        unit_symbol = self.units[converted_unit]

        print(f"\nResult = {converted_value}{unit_symbol}")
        self.ut.clear_line(n=7, timeout=7)
