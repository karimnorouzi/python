def factorial(n):
	result = 1
	while n > 1:
		result *= n
		n -= 1
	return result

print("Factorial of 5 is:", factorial(5))
print("Factorial of 8 is:", factorial(8))
