"""The Kronecker product produces a block matrix by multiplying each
 element of one matrix by the entirety of another. It is used in ML for tensor operations
 and signal processing"""
import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[0, 5], [6, 7]])
result = np.kron(A, B)
print("Result of Kronecker product is:", result)
