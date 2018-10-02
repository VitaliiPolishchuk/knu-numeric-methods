import math 
import numpy as np
import matplotlib.pyplot as plt

error = 0.001

def simps(f,a,b,N):
    '''Approximate the integral of f(x) from a to b by Simpson's rule.

    Simpson's rule approximates the integral \int_a^b f(x) dx by the sum:
    (dx/3) \sum_{k=1}^{N/2} (f(x_{2i-2} + 4f(x_{2i-1}) + f(x_{2i}))
    where x_i = a + i*dx and dx = (b - a)/N.

    Parameters
    ----------
    f : function
        Vectorized function of a single variable
    a , b : numbers
        Interval of integration [a,b]
    N : (even) integer
        Number of subintervals of [a,b]

    Returns
    -------
    float
        Approximation of the integral of f(x) from a to b using
        Simpson's rule with N subintervals of equal length.

    Examples
    --------
    >>> simps(lambda x : 3*x**2,0,1,10)
    1.0
    '''
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    y = f(x)
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S

e = 0.001
f_x =lambda x : 3*x**2

def runge_rule(f):
	N = 1000
	print(f(f_x,0,1,N))
	print(f(f_x,0,1,N/2))
	runge = math.fabs(f(f_x,0,1,N) - f(f_x,0,1,N/2))/15
	while runge > e:
		print(f(f_x,0,1,N))
		print(f(f_x,0,1,N/2))
		runge = math.fabs(f(f_x,0,1,N) - f(f_x,0,1,N/2))/15
		N = N/2
	return runge

f = lambda x:math.log(x)

print("For function 3*x**2 in [0, 10] metod Simpson is : " + str(simps(f_x,0,1,500)))
print("Rule Runge for this function is " + str(runge_rule(simps)))
