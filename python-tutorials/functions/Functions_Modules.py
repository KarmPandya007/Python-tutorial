# Functions & Modules

"""
This file covers functions and modules in Python, including defining functions and importing modules.
"""

# Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Lambda Functions
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")

# Modules
# Importing a built-in module
import math
print(f"Square root of 16: {math.sqrt(16)}")

# Custom Module Example
# Assuming a file named 'custom_module.py' exists with a function 'custom_function'
# from custom_module import custom_function
# print(custom_function())

# Exercise
"""
1. Write a function that takes two numbers as arguments and returns their sum.
2. Import the random module and use it to generate a random number between 1 and 100.
3. Create a custom module with a function and import it into this file.
4. Write a recursive function to calculate the nth Fibonacci number.
5. Use a lambda function to filter even numbers from a list.
"""