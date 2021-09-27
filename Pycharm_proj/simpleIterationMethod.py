import numpy as np


def start(f, df, sec, ep):
    a = sec['left']
    b = sec['right']
    if f(a) * f(b) > 0:
        return 'Wrong sector'

    # процесс расходится
    if np.abs(df(a)) > 1 and np.abs(df(b)) > 1:
        return '-inf'

    x0 = (b + a)/2.0
    xn = x0 - np.sign(df(x0)) * 2 * f(x0)

    while np.abs(x0 - xn) >= ep:
        x0 = xn
        xn = x0 - np.sign(df(x0)) * f(x0)

    return xn
