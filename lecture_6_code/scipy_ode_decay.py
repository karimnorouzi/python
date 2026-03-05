#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def ydot(t, y, k):
    return -k*y

y0 = [.1]

# Time span and output grid
t_span = (0.0, 10.0)
t_eval = np.linspace(*t_span, 1000)

sol = solve_ivp(
    ydot,
    t_span,
    y0,
    args=(0.15,),
    t_eval=t_eval,
    method="RK45",
)

if not sol.success:
    raise RuntimeError("Integration failed")

x = sol.y[0]
t = sol.t

plt.figure()
plt.plot(t, x)
plt.xlabel("t")
plt.ylabel("Radio Active Material")
plt.title("Decay")
plt.grid(True)
plt.show()