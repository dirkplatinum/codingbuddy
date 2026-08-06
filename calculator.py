"""Basic arithmetic operations."""


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
