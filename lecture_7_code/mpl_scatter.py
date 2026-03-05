import matplotlib.pyplot as plt
import numpy as np
# Generate random data
x = np.random.rand(100)
y = np.random.rand(100)
# Create a scatter plot
plt.scatter(x, y, color='blue', alpha=0.5)
plt.title('Scatter Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.show()
