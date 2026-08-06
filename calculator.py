"""Basic arithmetic operations."""

import sys

USAGE = "Usage: python calculator.py <number> <operator> <number>"


def add(a, b):
    """Return the sum of ``a`` and ``b``."""
    return a + b


def subtract(a, b):
    """Return ``b`` subtracted from ``a``."""
    return a - b


def multiply(a, b):
    """Return the product of ``a`` and ``b``."""
    return a * b


def divide(a, b):
    """Return ``a`` divided by ``b``.

    Raises:
        ZeroDivisionError: If ``b`` is zero.
    """
    return a / b


def calculate(a, operator, b):
    """Return the result of applying ``operator`` to ``a`` and ``b``.

    Args:
        a: The left operand.
        operator: One of ``"+"``, ``"-"``, ``"*"`` or ``"/"``.
        b: The right operand.

    Returns:
        The result of the operation, or the message
        ``"Error: division by zero"`` when dividing by zero.

    Raises:
        ValueError: If ``operator`` is not a recognised symbol.
    """
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    if operator not in operations:
        raise ValueError(f"Unknown operator: {operator}")
    try:
        return operations[operator](a, b)
    except ZeroDivisionError:
        return "Error: division by zero"


def main():
    """Calculate the expression given on the command line.

    Returns:
        The exit status: ``0`` on success, ``1`` when the arguments are
        missing, not numbers or use an unsupported operator.
    """
    args = sys.argv[1:]
    if len(args) != 3:
        print(USAGE, file=sys.stderr)
        return 1
    left, operator, right = args
    try:
        a = float(left)
        b = float(right)
    except ValueError:
        print("Error: operands must be numbers", file=sys.stderr)
        print(USAGE, file=sys.stderr)
        return 1
    try:
        result = calculate(a, operator, b)
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        print(USAGE, file=sys.stderr)
        return 1
    print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
