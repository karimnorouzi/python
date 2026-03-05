#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 13:54:42 2026

@author: geo
"""

import threading
import numpy as np
import time

def sum_array(arr, result):
    for i in range(len(arr)):
        tmp = result[0]          # read
        tmp += arr[i]            # modify
        time.sleep(0)            # force context switch
        result[0] = tmp          # write

arr = np.ones(100000)

total = [0]
thread1 = threading.Thread(target=sum_array, args=(arr[:50000], total))
thread2 = threading.Thread(target=sum_array, args=(arr[50000:], total))

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("Expected:", np.sum(arr))
print("Got:", total[0])