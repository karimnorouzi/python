# 13 - Exception Handling
# Exceptions are errors that occur at runtime.
# Use try/except blocks to handle them gracefully.

# --- Basic try/except ---
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# --- Catching the exception object ---
try:
    number = int("abc")
except ValueError as e:
    print(f"ValueError: {e}")

# --- Catching multiple exception types ---
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Division by zero!")
    except TypeError:
        print("Invalid types for division!")
    return None

safe_divide(10, 0)
safe_divide(10, "x")

# --- Catching multiple types in one except ---
try:
    value = [1, 2, 3][10]
except (IndexError, KeyError) as e:
    print(f"Lookup error: {e}")

# --- else clause: runs if no exception was raised ---
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error!")
else:
    print(f"Success: {result}")

# --- finally: always runs (for clean-up) ---
try:
    f = open("/tmp/example_exceptions.txt", "w")
    f.write("hello")
except OSError as e:
    print(f"File error: {e}")
finally:
    f.close()
    print("File closed.")

# --- Raising exceptions ---
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer.")
    if age < 0 or age > 150:
        raise ValueError(f"Age {age} is out of valid range.")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(e)

try:
    set_age("thirty")
except TypeError as e:
    print(e)

# --- re-raise an exception ---
def process(value):
    try:
        return 1 / value
    except ZeroDivisionError:
        print("Logging: division by zero occurred.")
        raise  # re-raises the same exception

try:
    process(0)
except ZeroDivisionError:
    print("Caught re-raised exception.")

# --- Custom exceptions ---
class InsufficientFundsError(Exception):
    """Raised when a bank account has insufficient funds."""
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(
            f"Cannot withdraw {amount}. Balance is only {balance}."
        )

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(amount, self.balance)
        self.balance -= amount

account = BankAccount(100)
try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(e)

# --- Common built-in exceptions ---
# Exception          — base class for all non-system-exiting exceptions
# ValueError         — right type, wrong value
# TypeError          — wrong type
# IndexError         — sequence index out of range
# KeyError           — dict key not found
# AttributeError     — attribute doesn't exist
# NameError          — variable name not found
# FileNotFoundError  — file does not exist
# OSError            — operating system error
# ZeroDivisionError  — division by zero
# StopIteration      — iterator exhausted
# RuntimeError       — generic runtime error
