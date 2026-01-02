# File Handling

"""
File handling in Python allows you to work with files for reading, writing, and appending data. Python provides built-in functions and modules for file operations.

Key Concepts:
1. **File Modes**: Modes like 'r' (read), 'w' (write), 'a' (append), and 'r+' (read and write).
2. **Context Manager**: Using `with` to handle files ensures proper resource management.
3. **CSV Files**: Used to store tabular data in plain text.
4. **JSON Files**: Used to store structured data in a human-readable format.
"""

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.")

# Explanation:
# The 'w' mode opens the file for writing. If the file exists, it is overwritten; otherwise, a new file is created.

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(f"File Content: {content}")

# Explanation:
# The 'r' mode opens the file for reading. If the file does not exist, a FileNotFoundError is raised.

# Working with CSV Files
import csv

# Writing to a CSV file
with open("example.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 30, "New York"])
    writer.writerow(["Bob", 25, "Los Angeles"])

# Reading from a CSV file
with open("example.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

# Explanation:
# The csv module provides functionality to read from and write to CSV files.

# Working with JSON Files
import json

# Writing to a JSON file
data = {"name": "Alice", "age": 30, "city": "New York"}
with open("example.json", "w") as jsonfile:
    json.dump(data, jsonfile)

# Reading from a JSON file
with open("example.json", "r") as jsonfile:
    data = json.load(jsonfile)
    print(data)

# Explanation:
# The json module provides functionality to work with JSON data, including serialization and deserialization.

# Exercise
"""
1. Write a program to create a file and write multiple lines to it.
2. Read the contents of the file and print them line by line.
3. Append new content to the file and verify the changes.
4. Write a program to create a CSV file with student data and read it back.
5. Write a program to store and retrieve data from a JSON file.
"""