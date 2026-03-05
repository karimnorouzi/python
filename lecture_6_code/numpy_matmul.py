import numpy as np
A = np.array([[1, 2], 
              [3, 4]])
B = np.array([[5, 6], 
              [7, 8]])
# Matrix multiplication
C = np.dot(A, B)  # Output: [[19, 22], [43, 50]]
# same as:
C = A @ B # Output: [[19, 22], [43, 50]]
# Inverse of a matrix
A_inv = np.linalg.inv(A)  # Output: [[-2. , 1. ], [1.5, -0.5]]
