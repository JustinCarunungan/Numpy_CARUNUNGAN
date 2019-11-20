import numpy as np
outfile = "div_by_3.npy"
X = np.arange(1,101).reshape(10,10)
X = X**2
Y = X[X%3==0]
print(X)
print()
np.save(outfile,Y)
F = np.load(outfile)
print(F)
input()
