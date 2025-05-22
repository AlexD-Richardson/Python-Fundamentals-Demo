"""
main.py - Entry point for Python Fundamentals Demo
"""

from utils import add, subtract, multiply, divide, reverse_string, is_palindrome
from typing import List, Dict, Set, Tuple

class Greeter:
    """A simple greeter class."""
    def __init__(self, name: str) -> None:
        self.name = name
    def greet(self) -> str:
        """Return a greeting message."""
        return f"Hello, {self.name}!"

def main() -> None:
    print("Welcome to the Python Fundamentals Demo!")
    
    # Demonstrate basic data types
    integer_example: int = 42
    float_example: float = 3.14
    string_example: str = "Hello, World!"
    boolean_example: bool = True
    
    print(f"Integer: {integer_example}, Float: {float_example}, String: {string_example}, Boolean: {boolean_example}")
    
    # Demonstrate a simple function call from utils
    result = add(5, 7)
    print(f"The sum of 5 and 7 is: {result}")

    # Demonstrate data structures
    sample_list: List[int] = [1, 2, 3, 4]
    sample_dict: Dict[str, int] = {'a': 1, 'b': 2}
    sample_set: Set[int] = {1, 2, 3}
    sample_tuple: Tuple[int, ...] = (1, 2, 3)
    print(f"List: {sample_list}, Dict: {sample_dict}, Set: {sample_set}, Tuple: {sample_tuple}")

    # Control flow
    print("Even numbers in list:")
    for num in sample_list:
        if num % 2 == 0:
            print(num)

    # Lambda, map, filter
    squared = list(map(lambda x: x ** 2, sample_list))
    evens = list(filter(lambda x: x % 2 == 0, sample_list))
    print(f"Squared: {squared}, Evens: {evens}")

    # File I/O
    with open("demo.txt", "w") as f:
        f.write("Python fundamentals demo file.\n")
    with open("demo.txt", "r") as f:
        print(f"File contents: {f.read().strip()}")

    # Exception handling
    try:
        x = 1 / 0
    except ZeroDivisionError as e:
        print(f"Caught an exception: {e}")

    # OOP basics
    greeter = Greeter("Pythonista")
    print(greeter.greet())

    # Demonstrate all utility functions
    print(f"5 - 3 = {subtract(5, 3)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    try:
        print(f"10 / 2 = {divide(10, 2)}")
        print(f"10 / 0 = {divide(10, 0)}")  # Will raise exception
    except ValueError as e:
        print(f"Caught an exception: {e}")
    print(f"Reverse of 'Python' is '{reverse_string('Python')}'")
    print(f"Is 'racecar' a palindrome? {is_palindrome('racecar')}")
    print(f"Is 'python' a palindrome? {is_palindrome('python')}")

if __name__ == "__main__":
    main()