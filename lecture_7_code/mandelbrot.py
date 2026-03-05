#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 15:43:25 2026

@author: geo
"""

import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(h, w, maxit=20):
    """Returns image of Mandelbrot fractal of size (h, w)"""
    x = np.linspace(-2, 0.8, w)
    y = np.linspace(-1.4, 1.4, h)
    X, Y = np.meshgrid(x, y)

    c = X + 1j * Y
    z = c
    divtime = np.full(c.shape, maxit, dtype=int)
    for iteration in range(maxit):   
        
        z = z**2 + c
        diverge = np.abs(z) > 2**2
        div_now = diverge & (divtime == maxit)
        divtime[div_now] = iteration
        z[diverge] = 2  # prevent overflow
        
    return divtime

plt.imshow(mandelbrot(1600, 1600, 32))
plt.colorbar()
plt.show()