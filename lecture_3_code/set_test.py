set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union = set1 | set2          # Union of sets
intersection = set1 & set2   # Intersection of sets
difference = set1 - set2     # Difference of sets

print("Union:", union)                 # Output: {1, 2, 3, 4, 5, 6}
print("Intersection:", intersection)   # Output: {3, 4}
print("Difference:", difference)       # Output: {1, 2}
