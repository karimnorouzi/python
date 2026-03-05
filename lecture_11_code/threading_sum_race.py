#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 12:58:24 2026

@author: geo
"""

import threading
import numpy as np

def sum_array(arr, result):
    for i in range(len(arr)):
        result[0] += arr[i]
        
# arr = np.random.rand(10000000)
arr = np.linspace(0, 10000000, 10000000+1)
#sum using single process
sum_of_array = [0]
sum_array(arr, sum_of_array)
print(f"summ of array: {sum_of_array}")

total = [0]
thread1 = threading.Thread(target=sum_array, args=(arr[:500000], total))
thread2 = threading.Thread(target=sum_array, args=(arr[500000:], total))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(f"Total sum: {total}")
