def chebyshev(n, x):
	if n == 0:
		return 1
	elif n == 1:
		return x
	else:
		return 2 * x * chebyshev(n - 1, x) - chebyshev(n - 2, x)

n = 5
x = 0.5
print(f"Chebyshev T_{n}({x}) is:", chebyshev(n, x))
