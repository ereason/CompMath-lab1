import buildPlot as plot
import numpy as np

def f(t):
    return (t*t) - 20*np.sin(t) - 5

plot.build(f)