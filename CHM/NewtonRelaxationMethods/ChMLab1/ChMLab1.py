import NewtonMethod, RelaxationMethod

x = -1
tau = 2/9

print('| | |   Newton Method   | | |')
print()
NewtonMethod.exe(x)

print()
print()
print()

print('| | |   Relaxation Method   | | |')
print()
RelaxationMethod.exe(x, tau)
