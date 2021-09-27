import buildPlot as plot
import halfDivideMethod
import numpy as np

def f(t):
    return (t*t) - 20*np.sin(t) - 5
def df(t):
    return 2*t - 20*np.cos(t)
def d2f(t):
    return 2 + 20*np.sin(t)

plot.build(f)

print("Look at plot and enter section [a,b]. a < b")
a, b = map(float, input().split())
ep = 0.000001
print("\u03B5 = "+str(ep))
root = halfDivideMethod.start(f,{'left':a,'right':b},ep)
print(root)