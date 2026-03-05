from mpi4py import MPI
import numpy as np
comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size
scatter = comm.scatter
reduce = comm.reduce

N = 1000000
if rank == 0:
    assert N % size == 0
    data = np.random.rand(N)
    chunks = np.array_split(data, size)
else:
    chunks = None
#chunks = [chunk_0, chunk_1, ..., chunk_(size-1)]
local_data = scatter(chunks, root=0)

my_sum = np.sum(local_data)

total_sum = reduce(my_sum, op=MPI.SUM, root=0)

if rank == 0:
    print("Total sum (MPI):", total_sum)
    print("Total sum (serial):", np.sum(data))