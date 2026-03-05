#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 15:11:12 2026

@author: geo
"""

def displayMove(fro, to):
    print(f"moving from {fro} to {to}.")
   
def Towers(n, fro, to, spare):
    if n == 1:
        displayMove(fro, to)
    else:
        Towers(n -1, fro, spare, to)
        Towers(1, fro, to, spare)
        Towers(n-1, spare, to, fro)

Towers(3, 1, 2, 3)        