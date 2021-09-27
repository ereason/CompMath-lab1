import numpy as np

# f - f(x), df - f', d2f - f'', section - [a,b], ep - epsilon
def start(f,df,d2f,sec,ep):
    if f(sec['left'])*f(sec['right']) >= 0:
        return 'Wrong sec'

    x0 = sec['right'] if np.sign(f(sec['right'])) == np.sign(d2f(sec['right'])) else sec['left']
    xn = x0-f(x0)/df(x0)

    while np.abs(x0-xn) < ep:
        x0=xn
        xn = x0 - f(x0) / df(x0)

    return xn