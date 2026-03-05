#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 14:39:21 2026

@author: geo
"""

from mpi4py import MPI

comm = MPI.COMM_WORLD
print(f"I am {comm.rank}, want to recv from {comm.size - 1 - comm.rank}")
msg = comm.recv(source = comm.size - 1 - comm.rank)
comm.send(22, dest = comm.size - 1 - comm.rank)

print(msg)

