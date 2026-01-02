# File Handling

"""
This file covers file handling in Python, including reading from and writing to files.
"""

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(f"File Content: {content}")

# Exercise
"""
1. Write a program to create a file and write multiple lines to it.
2. Read the contents of the file and print them line by line.
3. Append new content to the file and verify the changes.
"""