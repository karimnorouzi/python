#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def ydot(t, y, m, c, k):
    x, v = y
    return [v, -(c/m) * v - (k/m) * x]


# Oscillator parameters
m = 1.0
lambd = 0.05
k = 1.0

# Initial conditions [x, v]
y0 = [1.0, 5.0]

# Time span and output grid
t_span = (0.0, 50.0)
t_eval = np.linspace(*t_span, 1000)

# Solve the ODE
sol = solve_ivp(
    ydot,
    t_span,
    y0,
    args=(m, lambd, k),
    t_eval=t_eval,
    method="RK45",
)

if not sol.success:
    raise RuntimeError("Integration failed")

x = sol.y[0]
t = sol.t

# Plot x versus t
plt.figure()
plt.plot(t, x)
plt.xlabel("t")
plt.ylabel("x")
plt.title("Damped Harmonic Oscillator")
plt.grid(True)
plt.show()