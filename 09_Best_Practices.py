# Best Practices & Clean Code

"""
This file covers best practices and clean code principles in Python programming.
"""

# 1. Use Meaningful Variable Names
# Bad:
a = 10
b = 20
# Good:
width = 10
height = 20

# 2. Write Modular Code
def calculate_area(width, height):
    return width * height

# 3. Follow PEP 8 Guidelines
# Use proper indentation, spacing, and line length.

# 4. Use Docstrings and Comments
"""
This function calculates the area of a rectangle.
"""

# 5. Handle Exceptions Gracefully
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

# 6. Avoid Hardcoding Values
PI = 3.14159
radius = 5
area = PI * radius ** 2

# Exercise
"""
1. Refactor a given piece of code to make it cleaner and more readable.
2. Write a program that adheres to PEP 8 guidelines.
3. Create a function with proper docstrings and comments explaining its purpose.
"""