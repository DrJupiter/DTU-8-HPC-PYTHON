import numpy as np
from time import perf_counter as time
import wandb
# initialize wandb
wandb.init(project="Python High Performance Computing 2024", entity="ai-dtu", name="Measuring Performance")

SIZES = np.logspace(1,4.5,base=10)

for step, SIZE in enumerate(SIZES):
    SIZE = int(SIZE)
    wandb.log({"SIZE": SIZE, "Step": step}, step=step)
    mat = np.random.rand(SIZE, SIZE)
    t = time()
    double_column = 2 * mat[:,0]
    t1 = time()
    double_row = 2 * mat[0,:]
    t2 = time()
    wandb.log({"Column Time": t1-t, "Row Time": t2-t1})
    #print(f"SIZE {SIZE}: Column time {t1-t}, Row time {t2-t1}")