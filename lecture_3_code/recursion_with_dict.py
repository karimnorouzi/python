#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 15:24:39 2026

@author: geo
"""

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
    
print(fibonacci(1))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(50))

def fibonacci_(n, d):
    if n in d.keys():
        return d[n]
    elif n == 0 or n == 1:
        return 1
    else:
        d[n] = fibonacci_(n-1, d) + fibonacci_(n-2, d)
        return d[n]
    
d = dict()
fibonacci_(50, d) 