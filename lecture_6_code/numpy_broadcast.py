import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([1, 0, 1])
# Broadcasting b to match the shape of a
c = a + b  # Output: [[2, 2, 4], [5, 5, 7]]
