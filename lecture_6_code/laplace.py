import scipy.sparse as sp
import scipy.sparse.linalg as la
import numpy as np
N = 600; h = 1.0 / (N+1)
K = sp.diags(diagonals=[-1, 2, -1], offsets=[-1, 0, 1],
shape=(N, N), format="lil")  # list of lists
rhs = 2 * np.ones(N) * h**2
K[0,:] = 0.0; K[0, 0] = 1.0
K[-1,:] = 0.0; K[-1, -1] = 1.0
rhs[0] = .0; rhs[-1] = 0.0
K = K.tocsr()
u = la.spsolve(K, rhs)
import matplotlib.pyplot as plt   # plot the result with matplotlib
x = np.linspace(0, 1, N)
plt.plot(x, u)
plt.xlabel('x')
plt.ylabel('u(x)')
plt.title('Solution of the Laplacian with Homogeneous Dirichlet Boundary Conditions')
plt.grid()
plt.show()
