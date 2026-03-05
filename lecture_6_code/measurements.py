#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 14:07:51 2026

@author: geo
"""

import numpy as np
import matplotlib.pyplot as plt
# --- True physical parameters ---
g_true = 9.81       # gravitational acceleration
v_true = 12.0       # initial velocity
y0_true = 5.0       # initial height

# --- Time sampling ---
n = 25
t = np.linspace(0, 2.5, n)

# --- Exact model ---
y_exact = -0.5 * g_true * t**2 + v_true * t + y0_true

# --- Add measurement noise ---
noise_level = .2  # standard deviation of noise
noise = np.random.normal(0, noise_level, size=n)
y_measured = y_exact + noise

# --- Save to file ---
data = np.column_stack((t, y_measured))
np.savetxt("measurements.txt", data, header="t y", comments='')

print("Synthetic measurement data written to measurements.txt")
print("True parameters:")
print(f"g = {g_true}, v = {v_true}, y0 = {y0_true}")

plt.plot(t, y_measured)