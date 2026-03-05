# 10 - Loops
# Use for loops to iterate over a sequence and while loops to repeat until a condition is false.

# --- for loop ---

# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterate over a string
for char in "Python":
    print(char, end=" ")
print()

# range(stop)         -> 0, 1, ..., stop-1
# range(start, stop)  -> start, ..., stop-1
# range(start, stop, step)
for i in range(5):
    print(i, end=" ")
print()

for i in range(2, 10, 2):
    print(i, end=" ")
print()

# enumerate() provides index and value
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# zip() pairs items from two sequences
names = ["Alice", "Bob", "Carol"]
scores = [95, 87, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Iterating over a dictionary
person = {"name": "Alice", "age": 30, "city": "NY"}
for key, value in person.items():
    print(f"{key} = {value}")

# --- while loop ---

count = 0
while count < 5:
    print(count, end=" ")
    count += 1
print()

# --- break and continue ---

# break exits the loop immediately
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print()

# continue skips the rest of the current iteration
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# --- else clause ---
# The else block runs if the loop finished normally (without break)
for i in range(5):
    if i == 10:  # never true
        break
else:
    print("Loop completed without break")

# Useful with searching
target = 7
numbers = [1, 3, 5, 9]
for n in numbers:
    if n == target:
        print(f"Found {target}")
        break
else:
    print(f"{target} not found")

# --- Nested loops ---
for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row},{col})", end=" ")
    print()

# --- while with break ---
import random
random.seed(0)
while True:
    roll = random.randint(1, 6)
    print(f"Rolled {roll}")
    if roll == 6:
        print("Got a 6, stopping.")
        break

# --- Comprehensions (compact loops) ---
squares = [x ** 2 for x in range(1, 6)]
print(squares)

# Nested comprehension to flatten a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)
