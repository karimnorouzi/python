# 12 - Modules
# A module is a file containing Python code that you can reuse.
# Python ships with many useful standard-library modules.

# --- Importing modules ---

# Import the whole module
import math
print(math.sqrt(25))   # 5.0
print(math.pi)         # 3.141592653589793

# Import specific names
from math import ceil, floor
print(ceil(3.2))   # 4
print(floor(3.9))  # 3

# Import with an alias
import math as m
print(m.log(math.e))  # 1.0

# Import everything (use sparingly — can cause name clashes)
from math import *
print(sin(0), cos(0))  # 0.0, 1.0

# --- Standard library highlights ---

# os — operating system interface
import os
print(os.getcwd())           # current working directory
print(os.path.join("a", "b", "c.txt"))  # 'a/b/c.txt' (cross-platform)

# sys — interpreter information
import sys
print(sys.version)
print(sys.platform)

# datetime — dates and times
from datetime import date, datetime, timedelta
today = date.today()
print(today)
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M"))
tomorrow = today + timedelta(days=1)
print(tomorrow)

# random — random numbers
import random
print(random.randint(1, 10))           # random integer in [1, 10]
print(random.choice(["a", "b", "c"])) # random element
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(items)
print(random.sample(items, 3))         # 3 unique random elements

# json — reading and writing JSON
import json
data = {"name": "Alice", "age": 30, "scores": [95, 87]}
json_string = json.dumps(data, indent=2)
print(json_string)
restored = json.loads(json_string)
print(restored["name"])

# collections — specialised container types
from collections import Counter, defaultdict, namedtuple

# Counter: count occurrences
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(words)
print(counts)
print(counts.most_common(2))

# defaultdict: dict with a default value factory
from collections import defaultdict
scores = defaultdict(list)
scores["Alice"].append(90)
scores["Alice"].append(85)
scores["Bob"].append(78)
print(dict(scores))

# namedtuple: tuple with named fields
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 7)
print(p.x, p.y)

# itertools — iterator building blocks
import itertools
print(list(itertools.chain([1, 2], [3, 4], [5])))  # flatten
print(list(itertools.combinations("ABC", 2)))
print(list(itertools.permutations("AB", 2)))
