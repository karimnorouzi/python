# 04 - Numbers
# Python supports integers, floats, and complex numbers.

# Integers
a = 10
b = 3

print(a + b)   # Addition:       13
print(a - b)   # Subtraction:     7
print(a * b)   # Multiplication: 30
print(a / b)   # Division:        3.3333...  (always returns float)
print(a // b)  # Floor division:  3          (rounds down)
print(a % b)   # Modulus:         1          (remainder)
print(a ** b)  # Exponentiation: 1000

# Floats
x = 3.14
y = 2.0
print(x + y)   # 5.140000000000001  (floating-point precision)
print(round(x + y, 2))  # 5.14  (round to 2 decimal places)

# Useful built-in functions
print(abs(-7))      # 7    (absolute value)
print(max(1, 5, 3)) # 5
print(min(1, 5, 3)) # 1
print(sum([1, 2, 3, 4]))  # 10
print(pow(2, 8))    # 256  (same as 2 ** 8)

# Integer division and modulus together
quotient, remainder = divmod(17, 5)
print(f"17 / 5 = {quotient} remainder {remainder}")

# The math module provides additional functions
import math

print(math.pi)           # 3.141592653589793
print(math.sqrt(16))     # 4.0
print(math.floor(3.9))   # 3
print(math.ceil(3.1))    # 4
print(math.factorial(5)) # 120

# Augmented assignment operators
count = 0
count += 1   # same as count = count + 1
count *= 5   # same as count = count * 5
print(count) # 5

# Comparison operators return booleans
print(5 > 3)    # True
print(5 < 3)    # False
print(5 == 5)   # True
print(5 != 4)   # True
print(5 >= 5)   # True
print(5 <= 4)   # False

# Number bases
print(0b1010)  # binary  -> 10
print(0o12)    # octal   -> 10
print(0xA)     # hex     -> 10
print(bin(10)) # '0b1010'
print(oct(10)) # '0o12'
print(hex(10)) # '0xa'
