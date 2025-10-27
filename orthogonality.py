# Two vectors are orthogonal if their dot product is zero. This condition is critical in linear algebra and ML for understanding independence and basis construction
import numpy as np
u = np.array([1, 2, 3])
v = np.array([-2, 1, 0])
result = np.dot(u, v)
print("Are the two vectors orthogonal ? ", result == 0)
