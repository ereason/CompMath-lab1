import numpy as np

def start(f, sec, ep):  # f - f(x), section - [a,b], ep - epsilon

    middlePoint = (sec['left'] + sec['right']) / 2.0
    value = f(middlePoint)
    sigValue = np.sign(value)   # root = 0, >0 = 1, <0 = -1
    if ( sec['right']-sec['left'] < 2.0 * ep ):    # exit condition
        return  middlePoint if (sec['right']-sec['left']) > 0  else None    # if b < a - None

    if( sigValue == np.sign( f(sec['right']) ) ):
        return start(f, {'left' : sec['left'], 'right' : middlePoint }, ep)
    else:
        ( sigValue == np.sign( f(sec['left']) ) )
        return start(f, {'left' : middlePoint, 'right' : sec['right'] }, ep)


