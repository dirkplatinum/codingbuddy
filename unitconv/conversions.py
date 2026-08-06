"""Pure unit conversion functions."""

KILOMETRES_PER_MILE = 1.609344


def celsius_to_fahrenheit(value: float) -> float:
    """Convert a temperature in degrees Celsius to degrees Fahrenheit."""
    return value * 9 / 5 + 32


def fahrenheit_to_celsius(value: float) -> float:
    """Convert a temperature in degrees Fahrenheit to degrees Celsius."""
    return (value - 32) * 5 / 9


def kilometres_to_miles(value: float) -> float:
    """Convert a distance in kilometres to miles."""
    return value / KILOMETRES_PER_MILE


def miles_to_kilometres(value: float) -> float:
    """Convert a distance in miles to kilometres."""
    return value * KILOMETRES_PER_MILE
