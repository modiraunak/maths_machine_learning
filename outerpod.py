"""The outerproduct generates a matrix by multiplying every element of one vector by every element of another. It is used in tensor operations and constructing
rank-1 matrices"""
import numpy as np 
u = np.array([1, 2])
v = np.array([3, 4, 5])
result =np.outer(u, v)
print("Result of outer product is:", result)