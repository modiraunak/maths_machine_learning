import numpy as np
from  numpy.linalg import matrix_rank
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
rank = matrix_rank(A)
nulity = A.shape[1] - rank
print("Rank of the matrix is:", rank)
print("Nulity of the matrix is:", nulity)
print("Shape of the matrix is:", A.shape)
print("Number of columns in the matrix is:", A.shape[1])
print("Number of rows in the matrix is:", A.shape[0])
print("Verification: Rank + Nulity =", rank + nulity)
