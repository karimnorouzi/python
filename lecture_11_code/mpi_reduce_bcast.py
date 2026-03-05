from mpi4py import MPI
import numpy as np
rank = MPI.COMM_WORLD.rank
size = MPI.COMM_WORLD.size
reduce = MPI.COMM_WORLD.reduce 
bcast = MPI.COMM_WORLD.bcast

N = 1000000
segments = None
data = np.zeros(N)
if rank == 0:
    assert N % size == 0
    data = np.random.rand(N)
    segments = N // size

segments = bcast(segments, root=0)
data = bcast(data, root=0)  # Broadcast the entire data to all processes
my_lower_range = rank * segments
my_upper_range = (rank + 1) * segments
my_sum = np.sum(data[my_lower_range:my_upper_range])
total = reduce(my_sum, op=MPI.SUM, root=0)	

if rank == 0:
    print("Total sum is ", total)
    print("Total sum is (serial sum) ", np.sum(data))
