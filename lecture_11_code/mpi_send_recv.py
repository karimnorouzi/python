#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 14:34:33 2026

@author: geo
"""

from mpi4py import MPI
comm = MPI.COMM_WORLD  # all processes execute this
rank = comm.Get_rank() # all process execute this
if rank == 0:          # only rank 0
    data = "Hello from the master process!"
    comm.send(data, dest=1)      # send to rank 1 only 
elif rank == 1:      # ranks 1 and up 
    data = comm.recv(source=0)
    print(f"Process 1 received: {data}")
    
    