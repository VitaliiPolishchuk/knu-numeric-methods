def func (x):
    return x**3 - 2*x**2 + x + 1

def dfunc (x):
    return 3*x**2 - 4*x + 1

def newx (x):
    return x - func(x)/dfunc(x)

def exe(x):
    for i in range(10):
        print('iteration', i, '; x =', '%.4f' % x, '; f(x) =', '%.4f' % func(x))
        x = newx(x)