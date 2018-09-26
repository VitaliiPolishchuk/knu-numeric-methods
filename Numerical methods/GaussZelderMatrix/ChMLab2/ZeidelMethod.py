import math
import copy

def iterate(A, iters):
    n = len(A)
    x = [0 for i in range(n)]

    for iter in range(iters):
        newx = copy.deepcopy(x)
        for i in range(n):
            Sum1 = sum(A[i][j]*newx[j] for j in range(i))
            Sum2 = sum(A[i][j]*x[j] for j in range(i+1, n))
            newx[i] = (A[i][n] - Sum1 - Sum2)/A[i][i]
        print('iteration', iter+1, ':   x=', newx)
        x = copy.deepcopy(newx)
    return x



def exe (A, iters):
	print('   | | |   Zeidel Method   | | |')
	print()
	iterate(A, iters)