import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2*np.pi, 128)
y = np.sin(x) * np.cos(x)
plt.plot(x, y, label='sin(x)*cos(x)')
plt.fill_between(x, y, where=(y > 0), color='lightgreen', alpha=0.5, label='Positive Area')
plt.fill_between(x, y, where=(y <= 0), color='lightcoral', alpha=0.5, label='Negative Area')
plt.title('Positive and Negative Areas of sin(x)*cos(x)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid()
plt.show()
