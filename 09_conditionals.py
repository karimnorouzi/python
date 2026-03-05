# 09 - Conditionals
# Use if, elif, and else to run code based on conditions.

age = 20

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# elif adds more branches
score = 75

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")

# Comparison operators
# ==  equal
# !=  not equal
# >   greater than
# <   less than
# >=  greater than or equal
# <=  less than or equal

# Logical operators: and, or, not
x = 5
print(x > 0 and x < 10)   # True  (both conditions true)
print(x < 0 or x > 3)     # True  (at least one condition true)
print(not x > 10)          # True  (negation)

# Chained comparisons (Pythonic)
print(0 < x < 10)          # True

# Membership operators: in, not in
colors = ["red", "green", "blue"]
print("red" in colors)       # True
print("yellow" not in colors) # True

# Identity operators: is, is not
a = None
print(a is None)      # True  (use 'is' to compare with None)
print(a is not None)  # False

# Ternary (conditional) expression
status = "adult" if age >= 18 else "minor"
print(status)

# Truthy and falsy values
# Falsy: False, 0, 0.0, "", [], {}, set(), None
# Truthy: everything else

name = ""
if name:
    print(f"Hello, {name}!")
else:
    print("Name is empty.")

items = [1, 2, 3]
if items:
    print(f"List has {len(items)} items.")

# Nested conditions
temperature = 22
humidity = 60

if temperature > 20:
    if humidity < 70:
        print("Nice weather!")
    else:
        print("Warm but humid.")
else:
    print("Cool outside.")

# Short-circuit evaluation
def check():
    print("check() called")
    return True

# 'and' stops at first False; 'or' stops at first True
result = False and check()  # check() is NOT called
result = True or check()    # check() is NOT called
