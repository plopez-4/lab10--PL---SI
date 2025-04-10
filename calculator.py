import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order
"""




def add(a, b):
    """Returns the sum of a and b."""
    return a + b


def subtract(a, b):
    """Returns the difference between a and b."""
    return a - b


def multiply(a, b):
    """Returns the product of a and b."""

    return a * b

def divide(a, b):
    """Returns the result of dividing b by a.

    Raises:
        ZeroDivisionError: If a is zero.
    """
    if a == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return b / a


def logarithm(a, b):
    """Returns the logarithm of b with base a.

    Raises:
        ValueError: If a <= 0, b <= 0, or a == 1.
    """
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Invalid inputs for logarithm. Base must be > 0, != 1, and value must be > 0.")
    return math.log(b, a)


def exponent(a, b):
    """Returns a raised to the power of b."""
    return a ** b

def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    if a == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return b / a
def log(a,b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Invalid inputs for logarithm. Base must be > 0, != 1, and value must be > 0.")
    return math.log(b, a)
def exp(a,b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Invalid inputs for logarithm. Base must be > 0, != 1, and value must be > 0.")
    return math.log(b, a)


