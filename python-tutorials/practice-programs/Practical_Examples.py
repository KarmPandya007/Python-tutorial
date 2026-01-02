# Practical Examples & Mini Programs

"""
This file contains practical examples and mini programs to demonstrate Python concepts in action.
"""

# Example 1: Simple Calculator
def calculator():
    operation = input("Choose operation (add, subtract, multiply, divide): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == "add":
        print(f"Result: {num1 + num2}")
    elif operation == "subtract":
        print(f"Result: {num1 - num2}")
    elif operation == "multiply":
        print(f"Result: {num1 * num2}")
    elif operation == "divide":
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Cannot divide by zero.")
    else:
        print("Invalid operation.")

# Example 2: Number Guessing Game
import random
def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("Guess the number (1-100): "))
        attempts += 1
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

# Exercise
"""
1. Create a program that takes a list of numbers and returns the largest and smallest numbers.
2. Write a program to check if a string is a palindrome.
3. Create a mini program that simulates a simple banking system with deposit and withdrawal functionality.
"""