# 03 - Strings
# Strings hold text. They can be created with single or double quotes.

greeting = "Hello, World!"
also_greeting = 'Hello, World!'

# Multi-line strings use triple quotes
poem = """Roses are red,
Violets are blue,
Python is great,
And so are you."""
print(poem)

# String length
print(len(greeting))  # 13

# Accessing characters by index (0-based)
print(greeting[0])   # H
print(greeting[-1])  # !  (negative index counts from the end)

# Slicing: string[start:stop:step]
print(greeting[0:5])   # Hello
print(greeting[7:])    # World!
print(greeting[:5])    # Hello
print(greeting[::2])   # Hlo ol!  (every second character)
print(greeting[::-1])  # !dlroW ,olleH  (reverse)

# Concatenation and repetition
first = "Hello"
second = "World"
combined = first + ", " + second + "!"
print(combined)

repeated = "ha" * 3
print(repeated)  # hahaha

# Common string methods
s = "  python programming  "
print(s.strip())          # remove leading/trailing whitespace
print(s.upper())          # uppercase
print(s.lower())          # lowercase
print(s.title())          # Title Case
print(s.strip().replace("python", "awesome"))

words = "apple,banana,cherry"
print(words.split(","))   # ['apple', 'banana', 'cherry']
print(",".join(["a", "b", "c"]))  # a,b,c

print("python".startswith("py"))  # True
print("python".endswith("on"))    # True
print("python".find("th"))        # 2 (index of first occurrence)
print("python".count("p"))        # 1

# f-strings (formatted string literals) — recommended way to embed variables
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
print(f"Next year I will be {age + 1}.")

# Older formatting styles (still in use)
print("Hello, %s!" % name)
print("Hello, {}!".format(name))

# Checking membership
sentence = "the quick brown fox"
print("quick" in sentence)   # True
print("slow" in sentence)    # False
