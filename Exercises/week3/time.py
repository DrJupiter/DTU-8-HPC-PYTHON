import numpy as np
from time import perf_counter as time

SIZE = 10000

mat = np.random.rand(SIZE, SIZE)
t = time()
double_column = 2 * mat[:,0]
t1 = time()
double_row = 2 * mat[0,:]
t2 = time()
print(f"Column time {t1-t}, Row time {t2-t1}")