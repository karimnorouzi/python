# 08 - Sets
# A set is an unordered collection of unique items.
# Sets are great for removing duplicates and testing membership quickly.

fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)  # duplicate 'apple' is removed

# Create an empty set (must use set(), not {} which creates a dict)
empty = set()
print(type(empty))   # <class 'set'>

# Adding and removing items
fruits.add("date")
fruits.discard("banana")  # no error if not present
print(fruits)

# Remove raises KeyError if the item is not present
try:
    fruits.remove("mango")
except KeyError as e:
    print("KeyError:", e)

# pop() removes an arbitrary item
item = fruits.pop()
print("Removed:", item)

# Membership test — O(1) on average
print("cherry" in fruits)
print("mango" in fruits)

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)    # Union:        {1, 2, 3, 4, 5, 6}
print(a & b)    # Intersection: {3, 4}
print(a - b)    # Difference:   {1, 2}  (in a but not b)
print(b - a)    #               {5, 6}  (in b but not a)
print(a ^ b)    # Symmetric difference: {1, 2, 5, 6}

# Method equivalents
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))

# Subset and superset
small = {1, 2}
print(small.issubset(a))    # True  — every element of small is in a
print(a.issuperset(small))  # True
print(a.isdisjoint({7, 8})) # True  — no common elements

# Iterating (order is not guaranteed)
for fruit in {"kiwi", "mango", "papaya"}:
    print(fruit)

# Converting other collections to a set removes duplicates
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = set(numbers)
print(unique)   # {1, 2, 3, 4}

# Set comprehension
even_squares = {x ** 2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0, 4, 16, 36, 64}

# Frozenset — immutable version, can be used as a dict key
fs = frozenset([1, 2, 3])
print(fs)
