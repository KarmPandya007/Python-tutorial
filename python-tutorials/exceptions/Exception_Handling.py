# Exception Handling

"""
This file covers exception handling in Python, including try-except blocks and raising exceptions.
"""

# Try-Except
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Raising Exceptions
def check_positive(number):
    if number < 0:
        raise ValueError("Number must be positive")

try:
    check_positive(-5)
except ValueError as e:
    print(f"Error: {e}")

# Exercise
"""
1. Write a program that handles a FileNotFoundError when trying to read a non-existent file.
2. Create a function that raises a custom exception if an input string is empty.
3. Use a try-except-else-finally block to demonstrate all its components.
"""