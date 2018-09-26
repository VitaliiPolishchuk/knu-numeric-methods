
def exclusion (A, n, xans):

    for i in range(n):
        Keyel = A[i][i]

        for j in range(n + 1):
            A[i][j] /= Keyel

        for k in range(i + 1, n, 1):
            Keyel = A[k][i]
            for l in range(n+1):
                A[k][l] -= A[i][l]*Keyel

        print('         exclusion', i + 1, ':')
        print()
        for ind in range(n):
            print('   ', A[ind])
        print()
        print()
    return A

def getans (A, n, xans):
    for i in range(n-1, -1, -1):
        xans[i] = A[i][n]
        for j in range(n - 1, i, -1):
            xans[i] -= xans[j]*A[i][j]
    print('   answer:', xans)
    return xans

def exe (A):
	print('   | | |   Gauss Method   | | |')
	print()
	n = len(A)
	xans = [0 for i in range(n)]
	B = exclusion(A, n, xans)
	getans(B, n, xans)
	print()
	print()
	print()