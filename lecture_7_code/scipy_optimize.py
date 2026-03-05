from scipy import optimize
import numpy as np
# Define a function to minimize
def f(x):
    return (x - 2) ** 2 + 1

# Perform optimization to find the minimum
result = optimize.minimize(f, x0=0)
print("Optimal value:", result.fun)
print("Optimal point:", result.x)
#Optimal value: 1.0000000000000007
#Optimal point: [1.99999997]
