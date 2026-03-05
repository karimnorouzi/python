import numpy as np
# Linspace: Generate 5 evenly spaced numbers between 0 and 1
x = np.linspace(0, 1, 5)  # Output: [0. , 0.25, 0.5 , 0.75, 1. ]
# Logspace: Generate 5 numbers between 10^0 and 10^2
y = np.logspace(0, 2, 5)  # Output: [  1. ,   3.16227766,  10. ,  31.6227766 , 100. ]

# sin and cos functions acting on array
z = np.sin(x)  # Output: [0. , 0.70710678, 1. , 0.70710678, 0. ]
gamma = np.cos(y)
