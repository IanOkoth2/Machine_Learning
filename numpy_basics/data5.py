import numpy as np
# Reorganizing arrays
before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(before)

after = before.reshape((2, 4, 1))
print(after)
after1 = before[..., np.newaxis]
print(after1)

# Vertically stacking matrices
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])

f = np.vstack([v1, v2, v1, v2])
print(f)

# Horizontal
g = np.hstack((v2, v1))
print(g)