# 14 - Classes (Object-Oriented Programming)
# Classes are blueprints for creating objects that bundle data and behaviour.

# --- Defining a class ---
class Dog:
    # Class attribute — shared by all instances
    species = "Canis lupus familiaris"

    # __init__ is the constructor; 'self' refers to the instance
    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age

    # Instance method
    def bark(self):
        print(f"{self.name} says: Woof!")

    def description(self):
        return f"{self.name} is {self.age} year(s) old."

    # Special (dunder) methods
    def __str__(self):
        return f"Dog({self.name}, {self.age})"

    def __repr__(self):
        return f"Dog(name={self.name!r}, age={self.age!r})"


# Create instances
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

dog1.bark()
print(dog2.description())
print(dog1)          # calls __str__
print(repr(dog2))    # calls __repr__

print(Dog.species)        # class attribute via class
print(dog1.species)       # class attribute via instance

# --- Inheritance ---
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement speak().")

    def __str__(self):
        return self.name


class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow!"


class Duck(Animal):
    def speak(self):
        return f"{self.name} says: Quack!"


animals = [Cat("Whiskers"), Duck("Donald"), Cat("Felix")]
for animal in animals:
    print(animal.speak())

# isinstance() checks the type hierarchy
print(isinstance(animals[0], Cat))    # True
print(isinstance(animals[0], Animal)) # True (Cat is an Animal)

# --- Overriding methods ---
class Puppy(Dog):
    def bark(self):
        print(f"{self.name} says: Yip!")

    def description(self):
        base = super().description()  # call parent method
        return base + " (It's a puppy!)"


puppy = Puppy("Tiny", 0)
puppy.bark()
print(puppy.description())

# --- Properties ---
class Circle:
    def __init__(self, radius):
        self._radius = radius  # '_' signals 'private by convention'

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2


c = Circle(5)
print(c.radius)        # 5
print(f"Area: {c.area:.2f}")
c.radius = 10
print(c.radius)        # 10

# --- Class and static methods ---
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        """Alternative constructor from Fahrenheit."""
        return cls((fahrenheit - 32) * 5 / 9)

    @staticmethod
    def is_valid(celsius):
        """No access to instance or class — utility function."""
        return celsius >= -273.15

    def __str__(self):
        return f"{self.celsius:.1f}°C"


t1 = Temperature(100)
t2 = Temperature.from_fahrenheit(212)
print(t1)             # 100.0°C
print(t2)             # 100.0°C
print(Temperature.is_valid(-300))  # False

# --- Dataclasses (Python 3.7+) ---
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float
    label: str = ""

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


p = Point(3.0, 4.0, label="A")
print(p)                          # Point(x=3.0, y=4.0, label='A')
print(p.distance_from_origin())   # 5.0
print(p == Point(3.0, 4.0, "A")) # True  (auto-generated __eq__)
