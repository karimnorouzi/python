# 02 - Variables and Data Types
# Variables store values. Python infers the type automatically.

# Integer (whole number)
age = 25
print("Age:", age)

# Float (decimal number)
height = 1.75
print("Height:", height)

# String (text)
name = "Alice"
print("Name:", name)

# Boolean (True or False)
is_student = True
print("Is student:", is_student)

# None represents the absence of a value
result = None
print("Result:", result)

# Check the type of a variable with type()
print(type(age))        # <class 'int'>
print(type(height))     # <class 'float'>
print(type(name))       # <class 'str'>
print(type(is_student)) # <class 'bool'>
print(type(result))     # <class 'NoneType'>

# Variables can be reassigned at any time
x = 10
print("x is", x)
x = "now a string"
print("x is", x)

# Multiple assignment on one line
a, b, c = 1, 2, 3
print(a, b, c)

# Assign the same value to several variables at once
p = q = r = 0
print(p, q, r)

# Type conversion (casting)
number_str = "42"
number_int = int(number_str)   # str -> int
number_float = float(number_str)  # str -> float
print(number_int + 1)         # 43
print(number_float + 0.5)     # 42.5
print(str(100) + " dollars")  # int -> str
