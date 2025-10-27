import numpy as np
a = np.array([[1, 2],[1, 3]])
b = np.array([4, 5])
det_a = np.linalg.det(a)
a1 = a.copy()
a2 = a.copy()
a1[:,0] = b
a2[:,1] = b
det_a1 = np.linalg.det(a1)
det_a2 = np.linalg.det(a2)
x1 = det_a1 / det_a
x2 = det_a2 / det_a
print("Solution using Cramer's Rule: x1 =", x1, ", x2 =", x2)
