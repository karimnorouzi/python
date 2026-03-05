#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 14:07:14 2026

@author: geo
"""

import numpy as np
# Load measurements from a file
data = np.loadtxt('measurements.txt', skiprows = 1)
t = data[:, 0]  # Time measurements
y = data[:, 1]  # Height measurements
# Construct the design matrix A
A = np.column_stack((-0.5 * t**2, t, np.ones_like(t)))
# Solve the normal equations A.T @ A @ x = A.T @ b
x = np.linalg.solve(A.T @ A, A.T @ y)
g = x[0]  # Extract g from the solution
v = x[1]       # Extract v from the solution
y_0 = x[2]     # Extract y_0 from the solution
print(f"Estimated parameters: g = {g}, v = {v}, y_0 = {y_0}")


