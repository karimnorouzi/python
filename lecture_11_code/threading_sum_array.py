#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 12:53:57 2026

@author: geo
"""

import threading
import numpy as np
def sum_array(arr, result, index):
    result[index] = np.sum(arr)
arr = np.random.rand(1000000)

#sum using single process
sum_of_array = [0]
sum_array(arr, sum_of_array, 0)
print(f"summ of array: {sum_of_array[0]}")
# threads are not truely parall in python, not useful for speed up
# helpful by producer, consumer
# damned GIL ie Global Interpreter Lock
# The GIL only blocks CPU-bound Python code. But many real-world tasks are I/O-bound:
# Network requests (HTTP calls, sockets)
# File I/O (reading/writing large files)
# Database queries
# Waiting for user input
result = [0, 0]
thread1 = threading.Thread(target=sum_array, args=(arr[:500000], result, 0))
thread2 = threading.Thread(target=sum_array, args=(arr[500000:], result, 1))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(f"Total sum: {result[0] + result[1]}")
