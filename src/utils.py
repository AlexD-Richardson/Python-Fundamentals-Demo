"""
utils.py - Utility functions for Python Fundamentals Demo
"""
from typing import Any

def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Return the difference of a and b."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b

def divide(a: float, b: float) -> float:
    """Return the quotient of a and b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def reverse_string(s: str) -> str:
    """Return the reverse of the input string."""
    return s[::-1]

def is_palindrome(s: str) -> bool:
    """Return True if the string is a palindrome, False otherwise."""
    return s == s[::-1]