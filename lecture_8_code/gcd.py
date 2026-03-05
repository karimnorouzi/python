#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 16:38:41 2026

@author: geo
"""

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

if __name__ == "__main__":
	assert(gcd(48, 18) == 6)
	assert(gcd(56, 98) == 14)
	assert(gcd(98, 56) == 14)
	assert(gcd(12, 15) ==  3) 
	assert(gcd(7, 1)  ==  1)  

