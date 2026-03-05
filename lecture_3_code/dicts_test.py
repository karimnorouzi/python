#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 15:31:13 2026

@author: geo
"""

studnets= ['john', 'hector', 'invictus', 'armitage', 'appolon']
grade = ['A+', 'A', 'B-', 'NA', "D"]
subject = ["math", "chem", "vexelology" ]



grades = dict()

grades['john'] = ('math', 'A+')
grades['hector'] = ('chem', 'A')
grades['armitag'] = ('math', 'B-')


print(grades)

print(grades.keys())

print(grades.values())


print("-"*64)
for k, v in grades.items():
    print(f"{k}: {v}")
