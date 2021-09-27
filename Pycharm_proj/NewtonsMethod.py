import numpy as np

# f - f(x), df - f', d2f - f'', section - [a,b], ep - epsilon
def start(f,df,d2f,sec,ep):
    a = sec['left']
    b = sec['right']
    if f(a)*f(b) >= 0:
        return 'Wrong sector'

    # Эта проверка не совсем хорошая. на больших отрезках не работает
    if ( np.sign( df(a) ) != np.sign( df(b) ) or np.sign( d2f(a) ) != np.sign( d2f(b) ) ):
        return 'Wrong sector'

    x0 = None
    if np.sign(f(a)) == np.sign(d2f(a)):
        x0 = a
    if np.sign(f(b)) == np.sign(d2f(b)):
        x0 = b

    if(x0 == None):
        return 'Wrong sector'

    xn = x0-f(x0)/df(x0)
    while np.abs(x0-xn) >= ep:
        x0=xn
        xn = x0 - f(x0) / df(x0)

    return xn