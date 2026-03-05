#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 20:02:53 2026

@author: geo
"""

def fibonacci(n, memo={}):
	if n in memo:
		return memo[n]
	if n <= 1:
		return n
	memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
	return memo[n]

fibonacci(10)  # Output: 55
fibonacci(50)  # Output: 12586269025 (computed efficiently due to memoization)
print(fibonacci(50))  # Output: 12586269025 (computed efficiently due to memoization))