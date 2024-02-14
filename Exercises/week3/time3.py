import numpy as np
from time import perf_counter as timecounter
import plotly.graph_objects as go
import wandb
# initialize wandb
wandb.init(project="Python High Performance Computing 2024", entity="ai-dtu", name="Measuring Performance")
SIZES = np.logspace(1,4.5,base=10, dtype=int)
column_times = []
row_times = []
for step, SIZE in enumerate(SIZES):
    mat = np.random.rand(SIZE, SIZE)
    t = timecounter()
    double_column = 2 * mat[:,0]
    t1 = timecounter()
    double_row = 2 * mat[0,:]
    t2 = timecounter()
    column_times.append(t1-t)
    row_times.append(t2-t1)

fig = go.Figure()
fig.add_trace(go.Scatter(x=SIZES, y=column_times, mode='lines+markers', name='Column'))
fig.add_trace(go.Scatter(x=SIZES, y=row_times, mode='lines+markers', name='Row'))
fig.update_layout(title='Column vs Row Vectorization', xaxis_title='Matrix Size', yaxis_title='Time (s)')
wandb.log({"Column vs Row Vectorization": fig})
wandb.finish()