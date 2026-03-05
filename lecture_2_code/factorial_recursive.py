def factorial(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n * factorial(n - 1)

print("Factorial of 5 is:", factorial(5))
print("Factorial of 8 is:", factorial(8))
