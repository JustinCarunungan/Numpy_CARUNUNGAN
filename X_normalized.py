import numpy as np
outfile = "X_normalized.npy"
print("Original Array : ")
print()
X = np.random.random((5,5))
print(X)
print()
print("Normalized Array : ")
print()
X = (X - X.mean()) / X.std()
np.save(outfile,X)
F = np.load(outfile)
print(F)
print()
input("Press any key ...")



