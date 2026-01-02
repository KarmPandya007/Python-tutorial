# Control Flow

"""
This file covers control flow in Python, including if-else statements and loops.
"""

# If-Else
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")

# Nested If-Else
if x > 0:
    if x % 2 == 0:
        print("x is a positive even number")
    else:
        print("x is a positive odd number")
else:
    print("x is not positive")

# Loops
# For Loop
for i in range(5):
    print(f"For Loop Iteration: {i}")

# While Loop
count = 0
while count < 5:
    print(f"While Loop Count: {count}")
    count += 1

# Advanced Loop Control
# Break and Continue
for i in range(10):
    if i == 5:
        break  # Exit the loop
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"Advanced Loop Iteration: {i}")

# Exercise
"""
1. Write an if-else statement to check if a number is even or odd.
2. Use a for loop to iterate over a list of numbers and print each number.
3. Use a while loop to print numbers from 1 to 10.
4. Write a nested if-else statement to categorize a number as positive, negative, or zero.
5. Experiment with break and continue in loops.
"""