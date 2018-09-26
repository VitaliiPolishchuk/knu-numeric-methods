def func (x):
    return x**3 - 2*x**2 + x + 1

def newx (x, tau):
    return x - tau*func(x)

def exe (x, tau):
    for i in range(10):
        print('iteration', i, '; x =', '%.4f' % x, '; f(x) =', '%.4f' % func(x))
        x = newx(x, tau)