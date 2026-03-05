# 05 - Lists
# A list is an ordered, mutable collection that can hold items of any type.

fruits = ["apple", "banana", "cherry"]
print(fruits)

# Access by index (0-based)
print(fruits[0])   # apple
print(fruits[-1])  # cherry

# Slicing
print(fruits[1:3])  # ['banana', 'cherry']
print(fruits[:2])   # ['apple', 'banana']

# Lists are mutable — you can change items
fruits[1] = "blueberry"
print(fruits)

# Adding items
fruits.append("date")       # add to the end
fruits.insert(1, "avocado") # insert at index
print(fruits)

# Removing items
fruits.remove("blueberry")  # remove by value (first occurrence)
popped = fruits.pop()      # remove and return last item
popped_index = fruits.pop(0)  # remove and return item at index
print(fruits)
print("Popped:", popped, popped_index)

# List length
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(len(numbers))  # 8

# Sorting
numbers_copy = numbers[:]  # make a copy
numbers_copy.sort()        # sort in place
print(numbers_copy)        # ascending
numbers_copy.sort(reverse=True)
print(numbers_copy)        # descending
print(sorted(numbers))     # returns a new sorted list

# Other useful methods
print(numbers.count(1))   # 2  (number of occurrences)
print(numbers.index(9))   # 5  (index of first occurrence)

numbers.reverse()  # reverse in place
print(numbers)

# Checking membership
print("apple" in ["apple", "banana"])  # True

# Iterating
colors = ["red", "green", "blue"]
for color in colors:
    print(color)

# List comprehension — concise way to build lists
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

evens = [x for x in range(10) if x % 2 == 0]
print(evens)    # [0, 2, 4, 6, 8]

# Nested lists (2D list)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])  # 6  (row 1, column 2)

# Concatenation and repetition
a = [1, 2]
b = [3, 4]
print(a + b)    # [1, 2, 3, 4]
print(a * 3)    # [1, 2, 1, 2, 1, 2]

# Unpacking
first, *rest = [10, 20, 30, 40]
print(first)  # 10
print(rest)   # [20, 30, 40]
