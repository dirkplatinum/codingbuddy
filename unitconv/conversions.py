"""Pure unit conversion functions."""


def celsius_to_fahrenheit(value: float) -> float:
    """Convert a temperature in degrees Celsius to degrees Fahrenheit."""
    return value * 9 / 5 + 32


def fahrenheit_to_celsius(value: float) -> float:
    """Convert a temperature in degrees Fahrenheit to degrees Celsius."""
    return (value - 32) * 5 / 9
