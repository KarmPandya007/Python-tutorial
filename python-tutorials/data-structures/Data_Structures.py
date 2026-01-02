# Data Structures

"""
Data structures in Python are used to store and organize data efficiently. Python provides several built-in data structures, each with unique features and use cases.

Key Concepts:
1. **List**: An ordered, mutable collection of items.
2. **Tuple**: An ordered, immutable collection of items.
3. **Set**: An unordered collection of unique items.
4. **Dictionary**: A collection of key-value pairs.
5. **Comprehensions**: A concise way to create lists, sets, or dictionaries.
"""

# Lists
my_list = [1, 2, 3, 4, 5]
my_list.append(6)  # Add an element to the end
my_list.insert(2, 10)  # Insert an element at a specific position
my_list.remove(3)  # Remove the first occurrence of an element
my_list.pop()  # Remove and return the last element
my_list.sort()  # Sort the list in ascending order
my_list.reverse()  # Reverse the order of the list
print(f"List: {my_list}")

# Explanation:
# Lists are mutable, meaning you can add, remove, or modify elements.

# List Comprehension
squared_list = [x ** 2 for x in my_list]
print(f"Squared List: {squared_list}")

# Additional Methods for Lists
my_list.extend([7, 8, 9])  # Extend the list with multiple elements
print(f"Extended List: {my_list}")
print(f"Index of 10: {my_list.index(10)}")  # Find the index of an element
print(f"Count of 5: {my_list.count(5)}")  # Count occurrences of an element

# Tuples
my_tuple = (1, 2, 3, 4, 5)
print(f"Tuple: {my_tuple}")
print(f"First Element: {my_tuple[0]}")  # Access an element by index
print(f"Length: {len(my_tuple)}")  # Get the length of the tuple
print(f"Count of 3: {my_tuple.count(3)}")  # Count occurrences of an element
print(f"Index of 4: {my_tuple.index(4)}")  # Find the index of an element

# Explanation:
# Tuples are immutable, meaning their elements cannot be changed after creation.

# Tuple Methods
concatenated_tuple = my_tuple + (6, 7, 8)  # Concatenate tuples
print(f"Concatenated Tuple: {concatenated_tuple}")
print(f"Slice Tuple: {my_tuple[1:4]}")  # Slice a tuple

# Sets
my_set = {1, 2, 3, 4, 5}
my_set.add(6)  # Add an element
my_set.discard(3)  # Remove an element if it exists
my_set.update([7, 8, 9])  # Add multiple elements
my_set.remove(2)  # Remove an element (raises KeyError if not found)
print(f"Set: {my_set}")

# Set Operations
another_set = {4, 5, 6, 7}
print(f"Union: {my_set | another_set}")  # Combine elements from both sets
print(f"Intersection: {my_set & another_set}")  # Common elements
print(f"Difference: {my_set - another_set}")  # Elements in my_set but not in another_set
print(f"Symmetric Difference: {my_set ^ another_set}")  # Elements in either set but not both

# Explanation:
# Sets are useful for operations like union, intersection, and difference.

# Set Methods
print(f"Is Subset: {my_set.issubset(another_set)}")  # Check if my_set is a subset of another_set
print(f"Is Superset: {my_set.issuperset(another_set)}")  # Check if my_set is a superset of another_set
print(f"Is Disjoint: {my_set.isdisjoint(another_set)}")  # Check if sets have no elements in common

# Dictionaries
my_dict = {"key1": "value1", "key2": "value2"}
my_dict["key3"] = "value3"  # Add a new key-value pair
my_dict.update({"key4": "value4", "key5": "value5"})  # Add multiple key-value pairs
print(f"Dictionary: {my_dict}")
print(f"Keys: {list(my_dict.keys())}")  # Get all keys
print(f"Values: {list(my_dict.values())}")  # Get all values
print(f"Items: {list(my_dict.items())}")  # Get all key-value pairs
my_dict.pop("key2")  # Remove a key-value pair
print(f"After Pop: {my_dict}")

# Nested Dictionary
nested_dict = {"person1": {"name": "Alice", "age": 30}, "person2": {"name": "Bob", "age": 25}}
print(f"Nested Dictionary: {nested_dict}")

# Explanation:
# Dictionaries are mutable and allow for fast lookups using keys.

# Dictionary Methods
print(f"Get Value: {my_dict.get('key1')}")  # Get value for a key
print(f"Default Value: {my_dict.get('key6', 'default')}")  # Get value with default if key doesn't exist
print(f"Key Exists: {'key3' in my_dict}")  # Check if a key exists
my_dict.clear()  # Clear all key-value pairs
print(f"Cleared Dictionary: {my_dict}")

# Exercise
"""
1. Create a list of numbers and find the sum of all elements.
2. Create a tuple with 5 elements and access the third element.
3. Create a set and perform union and intersection operations with another set.
4. Create a dictionary and iterate over its keys and values.
5. Use list comprehension to create a list of squares of numbers from 1 to 10.
6. Create a nested dictionary to store information about multiple people and access specific details.
7. Experiment with at least 8-10 methods for each data structure.
"""