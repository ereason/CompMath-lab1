import numpy as np


def start(f, sec, ep):  # f - f(x), section - [a,b], ep - epsilon
    a = sec['left']
    b = sec['right']

    middlePoint = (a + b) / 2.0
    value = f(middlePoint)
    sigValue = np.sign(value)   # root = 0, >0 = 1, <0 = -1

    while b - a >= 2.0 * ep:
        if sigValue == np.sign(f(b)):
            b = middlePoint
            middlePoint = (a + b) / 2.0
            value = f(middlePoint)
            sigValue = np.sign(value)

        else:
            a = middlePoint
            middlePoint = (a + b) / 2.0
            value = f(middlePoint)
            sigValue = np.sign(value)

    return middlePoint if (sec['right'] - sec['left']) > 0 else None  # if b < a - None
