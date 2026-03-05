from mpi4py import MPI

rank = MPI.COMM_WORLD.rank  # rank  
size = MPI.COMM_WORLD.size  # size 
send = MPI.COMM_WORLD.send  # send function
recv = MPI.COMM_WORLD.recv  # recv function
import numpy as np

N = 1000000
assert(N % size == 0)  # make sure N is divisible by size
lower_bound = rank * N // size
upper_bound = (rank + 1) * N // size
local_sum = np.sum(np.arange(lower_bound, upper_bound))  # compute local sum
if rank != 0: 
	send(local_sum, dest=0)  # send local sum to root process
else:
	total_sum = local_sum  # initialize total sum with local sum of root process
	for i in range(1, size):
		received_sum = recv(source=i)  # receive local sum from other processes
		total_sum += received_sum  # add received local sum to total sum
	print("Total sum:", total_sum)  # print the total sum


