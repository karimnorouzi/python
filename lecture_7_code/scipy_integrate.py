from scipy import integrate
import numpy as np
# Define a function to integrate
def f(x):
    return np.sin(x)*np.cos(x)
# Perform numerical integration from 0 to pi
result, error = integrate.quad(f, 0, np.pi)
print("Integral result:", result)
print("Estimated error:", error)
