# Object-Oriented Programming (OOP)

"""
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects," which can contain data and methods. It allows for modular, reusable, and organized code.

Key Concepts:
1. **Class**: A blueprint for creating objects.
2. **Object**: An instance of a class.
3. **Inheritance**: A mechanism to create a new class using properties and methods of an existing class.
4. **Polymorphism**: The ability to redefine methods in derived classes.
5. **Encapsulation**: Restricting access to certain details of an object and exposing only the necessary parts.
6. **Abstraction**: Hiding implementation details and showing only the essential features.
"""

# Classes and Objects
class Animal:
    """
    The Animal class is a blueprint for creating animal objects. It has an initializer method to set the name and a method to make the animal speak.
    """
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Inheritance
class Dog(Animal):
    """
    The Dog class inherits from the Animal class and overrides the speak method.
    """
    def speak(self):
        return f"{self.name} barks."

# Polymorphism
class Cat(Animal):
    """
    The Cat class inherits from the Animal class and provides its own implementation of the speak method.
    """
    def speak(self):
        return f"{self.name} meows."

# Encapsulation
class Person:
    """
    The Person class demonstrates encapsulation by making attributes private and providing getter methods.
    """
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age

    def get_details(self):
        return f"Name: {self.__name}, Age: {self.__age}"

# Abstract Classes
from abc import ABC, abstractmethod

class Shape(ABC):
    """
    The Shape class is an abstract class that defines a blueprint for shapes. Subclasses must implement the area method.
    """
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Creating Objects
animal = Animal("Generic Animal")
dog = Dog("Buddy")
cat = Cat("Kitty")
person = Person("Alice", 30)
circle = Circle(5)

print(animal.speak())
print(dog.speak())
print(cat.speak())
print(person.get_details())
print(f"Circle Area: {circle.area()}")

# Exercise
"""
1. Create a class `Vehicle` with attributes `brand` and `model`, and a method to display details.
2. Create a subclass `Car` that inherits from `Vehicle` and adds an attribute `fuel_type`.
3. Implement polymorphism by creating another subclass `Bike` with a different implementation of the display method.
4. Use encapsulation to make some attributes private and provide getter methods.
5. Create an abstract class `Appliance` with an abstract method `power_usage` and implement it in subclasses `WashingMachine` and `Refrigerator`.
"""