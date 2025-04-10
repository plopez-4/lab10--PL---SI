# git link-https://github.com/plopez-4/lab10--PL---SI.git
# Partner 1: Pierce Lopez
# Partner 2: Solomiia Ivanovska

import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order
"""
def square_root(a):
    """Returns the square root of a.

    Raises:
        ValueError: If a is negative.
    """
    if a < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(a)


def hypotenuse(a, b):
    """Returns the hypotenuse of a right triangle given sides a and b."""
    return math.hypot(a, b)


def add(a, b):
    """Returns the sum of a and b."""
    return a + b


def subtract(a, b):
    """Returns the difference between a and b."""
    return a - b


def multiply(a, b):
    """Returns the product of a and b."""

    return a * b




def logarithm(base, value):
    """Returns the logarithm of value with base base.

    Raises:
        ValueError: If base <= 0, value <= 0, or base == 1.
    """
    if base <= 0 or value <= 0 or base == 1:
        raise ValueError("Invalid inputs for logarithm. Base must be > 0, != 1, and value must be > 0.")
    return math.log(value, base)  # Ensure arguments are correctly passed


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
    return a / b
def log(a,b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Invalid inputs for logarithm. Base must be > 0, != 1, and value must be > 0.")
    return math.log(b, a)
def exp(a,b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Invalid inputs for logarithm. Base must be > 0, != 1, and value must be > 0.")
    return math.log(b, a)


