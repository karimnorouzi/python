# 06 - Tuples
# A tuple is an ordered, immutable collection.
# Once created, its items cannot be changed.

point = (3, 7)
print(point)
print(point[0])  # 3
print(point[1])  # 7

# Tuples can hold mixed types
person = ("Alice", 30, True)
print(person)

# Parentheses are optional
coordinates = 10, 20
print(coordinates)       # (10, 20)
print(type(coordinates)) # <class 'tuple'>

# Single-element tuple needs a trailing comma
single = (42,)
print(type(single))   # <class 'tuple'>
not_a_tuple = (42)
print(type(not_a_tuple))  # <class 'int'>

# Unpacking
x, y = point
print(f"x={x}, y={y}")

name, age, active = person
print(name, age, active)

# Swapping variables with tuple unpacking
a, b = 5, 10
a, b = b, a
print(a, b)  # 10 5

# Tuples support indexing and slicing, just like lists
colors = ("red", "green", "blue", "yellow")
print(colors[1])     # green
print(colors[1:3])   # ('green', 'blue')
print(len(colors))   # 4

# Membership test
print("red" in colors)    # True
print("purple" in colors) # False

# Iterating over a tuple
for color in colors:
    print(color)

# Tuple methods
numbers = (1, 2, 3, 2, 1, 2)
print(numbers.count(2))  # 3
print(numbers.index(3))  # 2

# Tuples are hashable (can be used as dictionary keys or in sets)
locations = {(0, 0): "origin", (1, 0): "right", (0, 1): "up"}
print(locations[(1, 0)])  # right

# Converting between list and tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
back_to_list = list(my_tuple)
print(my_tuple)
print(back_to_list)
