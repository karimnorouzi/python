#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 13:26:31 2026

@author: geo
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        # raise an error or return NotImplemented
        return NotImplemented
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return NotImplemented
p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1)          # Output: Point(1, 2)
print(p1 + p2)     # Output: Point(4, 6)
print(p1 == p2)    # Output: False
print(p1 == Point(1, 2))  # Output: True