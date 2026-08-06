"""Command line interface for the unit conversion functions."""

import argparse
from typing import Callable, Dict, Optional, Sequence

from unitconv.conversions import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    kilometres_to_miles,
    miles_to_kilometres,
)

CONVERSIONS: Dict[str, Callable[[float], float]] = {
    "c2f": celsius_to_fahrenheit,
    "f2c": fahrenheit_to_celsius,
    "km2mi": kilometres_to_miles,
    "mi2km": miles_to_kilometres,
}


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Run the requested conversion and print the result."""
    parser = argparse.ArgumentParser(
        prog="unitconv", description="Convert between common units."
    )
    parser.add_argument(
        "conversion", choices=sorted(CONVERSIONS), help="the conversion to apply"
    )
    parser.add_argument("value", type=float, help="the numeric value to convert")
    args = parser.parse_args(argv)

    print(CONVERSIONS[args.conversion](args.value))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
