#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 12:46:00 2026

@author: geo
"""

import threading
from time import sleep 
from numpy import random
def print_square(number):
    sleep(random.rand())
    print(f"The square of {number} is {number**2}")

threads = []
for i in range(5):
    thread = threading.Thread(target=print_square, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
