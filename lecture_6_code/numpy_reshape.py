import numpy as np
arr = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]])
# Reshape the array to 1D
reshaped_arr = arr.reshape(-1)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Transpose the array
transposed_arr = arr.T  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
