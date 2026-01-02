# Python Basics

"""
This file covers the basics of Python programming, including syntax, variables, and data types.
"""

# Syntax
print("Hello, World!")  # This is a simple print statement

# Variables
integer_var = 10  # Integer variable
float_var = 3.14  # Float variable
string_var = "Python"  # String variable
boolean_var = True  # Boolean variable

# Data Types
list_var = [1, 2, 3, 4, 5]  # List
tuple_var = (1, 2, 3)  # Tuple
dict_var = {"key1": "value1", "key2": "value2"}  # Dictionary
set_var = {1, 2, 3}  # Set

# Advanced Examples
# String Operations
name = "Python"
print(name.upper())  # Convert to uppercase
print(name.lower())  # Convert to lowercase
print(name[0:3])  # Slicing

# List Operations
list_var.append(6)  # Add an element
print(list_var)
list_var.remove(3)  # Remove an element
print(list_var)

# Dictionary Operations
dict_var["key3"] = "value3"  # Add a new key-value pair
print(dict_var)

# Set Operations
set_var.add(4)  # Add an element
print(set_var)

# Exercise
"""
1. Print a message of your choice.
2. Create variables of different data types and print their values.
3. Create a list, tuple, dictionary, and set, and perform basic operations on them.
4. Experiment with string slicing and methods like upper(), lower().
5. Perform advanced operations on lists, dictionaries, and sets.
"""