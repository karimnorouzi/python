# 11 - Functions
# Functions let you group reusable code under a name.

# Basic function definition
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")

# Return values
def add(a, b):
    return a + b

result = add(3, 4)
print(result)  # 7

# Default parameter values
def greet_with_title(name, title="Mr."):
    print(f"Hello, {title} {name}!")

greet_with_title("Smith")
greet_with_title("Johnson", "Dr.")

# Keyword arguments (can be passed in any order)
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

describe_pet(name="Whiskers", animal="cat")

# *args — accepts any number of positional arguments as a tuple
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3))       # 6
print(total(10, 20, 30, 40))  # 100

# **kwargs — accepts any number of keyword arguments as a dict
def print_info(**details):
    for key, value in details.items():
        print(f"  {key}: {value}")

print_info(name="Alice", age=30, city="NY")

# Combining all parameter types
def mixed(required, default="yes", *args, **kwargs):
    print(required, default, args, kwargs)

mixed("hello", "no", 1, 2, 3, extra="value")

# Returning multiple values (actually returns a tuple)
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"min={low}, max={high}")

# Docstrings — document what a function does
def celsius_to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

print(celsius_to_fahrenheit(100))  # 212.0
print(celsius_to_fahrenheit.__doc__)

# Scope — variables inside a function are local
def set_x():
    x = 99  # local variable, does not affect outer x

x = 10
set_x()
print(x)  # still 10

# global keyword to modify a module-level variable
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print(counter)  # 2

# Lambda — a small anonymous function (one expression)
square = lambda x: x ** 2
print(square(5))  # 25

# Lambdas are often used with sorted(), map(), filter()
names = ["Charlie", "Alice", "Bob"]
print(sorted(names, key=lambda n: len(n)))  # sort by length

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
doubled = list(map(lambda x: x * 2, numbers))
print(evens)    # [2, 4, 6]
print(doubled)  # [2, 4, 6, 8, 10, 12]

# Recursive functions — a function that calls itself
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
