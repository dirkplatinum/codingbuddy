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
