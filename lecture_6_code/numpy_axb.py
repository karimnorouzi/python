import numpy as np
A = np.array([[3, 2], 
              [1, 4]])
b = np.array([5, 6])
# Solve for x in Ax = b
x = np.linalg.solve(A, b)  # Output: [1. 1.]

print(f"A={A}, b={b}, x={x}")
