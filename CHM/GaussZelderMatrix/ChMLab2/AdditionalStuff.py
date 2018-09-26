import numpy as np
from numpy import linalg
import math

def exe(A1, b):
    print('matrix:')
    print(A1[0])
    print(A1[1])
    print(A1[2])
    print()

    print('vector b')
    print(b)
    print()

    print('determinant of matrix', math.ceil(linalg.det(A1)))
    print()

    C = linalg.inv(A1)
    print('inverted matrix:', )
    print(C[0])
    print(C[1])
    print(C[2])
    print()

    NA = linalg.norm(A1)
    NC = linalg.norm(C)
    print('condition number', linalg.cond(A1))
    print()

    M = np.dot(C, A1)
    print('multiplication of matrix and inverted:')
    for i in range(3):
        for j in range(3):
            M[i][j] = '%.0f' % M[i][j]

    print(M[0])
    print(M[1])
    print(M[2])

    print()
    print()
    print()
