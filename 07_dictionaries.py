# 07 - Dictionaries
# A dictionary stores key-value pairs. Keys must be unique and immutable.
# Dictionaries are ordered (insertion order) in Python 3.7+.

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
}
print(person)

# Accessing values
print(person["name"])           # Alice
print(person.get("age"))        # 30
print(person.get("email"))      # None  (no KeyError)
print(person.get("email", "N/A"))  # N/A  (default value)

# Adding and updating entries
person["email"] = "alice@example.com"  # add new key
person["age"] = 31                     # update existing key
print(person)

# Removing entries
del person["city"]               # remove by key
removed = person.pop("email")    # remove and return value
print(removed)
print(person)

# Useful methods
print(person.keys())    # dict_keys([...])
print(person.values())  # dict_values([...])
print(person.items())   # dict_items([...])

# Iterating
for key in person:
    print(key, "->", person[key])

for key, value in person.items():
    print(f"{key}: {value}")

# Check if a key exists
print("name" in person)   # True
print("phone" in person)  # False

# Merging dictionaries (Python 3.9+)
defaults = {"color": "blue", "size": "medium"}
custom = {"size": "large", "weight": "heavy"}
merged = defaults | custom  # custom values override defaults
print(merged)

# Also: update() merges in place
defaults.update(custom)
print(defaults)

# Dictionary comprehension
squares = {x: x ** 2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Nested dictionaries
users = {
    "alice": {"age": 30, "role": "admin"},
    "bob":   {"age": 25, "role": "user"},
}
print(users["alice"]["role"])  # admin

# Length
print(len(person))

# Create from two lists using zip
keys = ["a", "b", "c"]
values = [1, 2, 3]
d = dict(zip(keys, values))
print(d)  # {'a': 1, 'b': 2, 'c': 3}
