import buildPlot as plot
import NewtonsMethod
import simpleIterationMethod
import halfDivideMethod
import numpy as np

ep = 0.00001


def f(t):
    return (t*t) - 20*np.sin(t) - 5


def df(t):
    return 2*t - 20*np.cos(t)


def d2f(t):
    return 2 + 20*np.sin(t)


plot.build(f)
plot.build(df)
plot.build(d2f)

print("Look at plot and enter section [a,b]. a < b")
a, b = map(float, input().split())

print("\u03B5 = "+str(ep))

result1 = NewtonsMethod.start(f, df, d2f, {'left': a, 'right': b}, ep)
print('Hewton\'s method: ' + str(result1))

result2 = simpleIterationMethod.start(f, df, {'left': a, 'right': b}, ep)
print('Simple iteration method: ' + str(result2))

result3 = halfDivideMethod.start(f, {'left': a, 'right': b}, ep)
print('Half divide method: ' + str(result3))
