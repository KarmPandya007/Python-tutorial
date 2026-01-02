# Exception Handling

"""
Exception handling in Python allows you to handle errors gracefully and prevent your program from crashing. It uses the try-except block to catch and handle exceptions.

Key Concepts:
1. **Exception**: An error that occurs during the execution of a program.
2. **Try-Except Block**: Used to catch and handle exceptions.
3. **Raise**: Used to raise an exception explicitly.
4. **Custom Exceptions**: User-defined exceptions for specific use cases.
5. **Nested Try-Except**: Handling exceptions at multiple levels.
"""

# Try-Except
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Explanation:
# The above code tries to divide a number by zero, which raises a ZeroDivisionError.
# The except block catches the error and prints an error message.

# Raising Exceptions
def check_positive(number):
    """
    This function raises a ValueError if the input number is negative.
    """
    if number < 0:
        raise ValueError("Number must be positive")

try:
    check_positive(-5)
except ValueError as e:
    print(f"Error: {e}")

# Custom Exceptions
class CustomError(Exception):
    """
    A custom exception class for demonstration purposes.
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

try:
    raise CustomError("This is a custom exception")
except CustomError as e:
    print(f"Caught CustomError: {e}")

# Nested Try-Except
try:
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Inner exception caught")
        raise
except Exception as e:
    print(f"Outer exception caught: {e}")

# Explanation:
# The inner try-except block catches a ZeroDivisionError and re-raises it.
# The outer try-except block catches the re-raised exception.

# Exercise
"""
1. Write a program that handles a FileNotFoundError when trying to read a non-existent file.
2. Create a function that raises a custom exception if an input string is empty.
3. Use a try-except-else-finally block to demonstrate all its components.
4. Implement nested try-except blocks to handle multiple levels of exceptions.
5. Create a custom exception class and use it in a program.
"""