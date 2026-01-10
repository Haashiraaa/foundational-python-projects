# logic.py

from typing import Union


class ConverterLogic:
    """
    Handles temperature conversions between units.
    Provides clear methods for each conversion path.
    """

    KELVIN_OFFSET = 273.15

    def kelvin_to_celsius(self, value: Union[int, float]) -> float:
        """Convert Kelvin to Celsius."""
        return value - self.KELVIN_OFFSET

    def kelvin_to_fahrenheit(self, value: Union[int, float]) -> float:
        """Convert Kelvin to Fahrenheit."""
        return (value - self.KELVIN_OFFSET) * 9 / 5 + 32

    def celsius_to_kelvin(self, value: Union[int, float]) -> float:
        """Convert Celsius to Kelvin."""
        return value + self.KELVIN_OFFSET

    def celsius_to_fahrenheit(self, value: Union[int, float]) -> float:
        """Convert Celsius to Fahrenheit."""
        return value * 9 / 5 + 32

    def fahrenheit_to_kelvin(self, value: Union[int, float]) -> float:
        """Convert Fahrenheit to Kelvin."""
        return (value - 32) * 5 / 9 + self.KELVIN_OFFSET

    def fahrenheit_to_celsius(self, value: Union[int, float]) -> float:
        """Convert Fahrenheit to Celsius."""
        return (value - 32) * 5 / 9

