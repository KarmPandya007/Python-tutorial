# Object-Oriented Programming (OOP)

"""
This file covers the basics of Object-Oriented Programming in Python, including classes, objects, and inheritance.
"""

# Classes and Objects
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Inheritance
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

# Creating Objects
animal = Animal("Generic Animal")
dog = Dog("Buddy")

print(animal.speak())
print(dog.speak())

# Exercise
"""
1. Create a class `Person` with attributes `name` and `age`, and a method to display the person's details.
2. Create a subclass `Student` that inherits from `Person` and adds an attribute `grade`.
3. Create objects of both classes and demonstrate their functionality.
"""