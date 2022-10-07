import numpy as np    
a = np.array([1, 2, 3])
# b = a.copy()
# b[0] = 100
# print(a)
# print(b)

#Getting into Mathematics
b = np.array([1, 2, 3])

print(b + 2)
print(b)
print(b - 2)
print(a + b)
print(a ** 2)
print(np.sin(a))
print(np.cos(a))
print(np.log(a))

#Linear algebra
a = np.ones((2, 3))
print(a)

b = np.full((3, 2), 2)
print(b)


# The multiplication of two matrices
# It must be ensures that the number of colums and rows must be same
c = np.matmul(a,b)
print(c)

# Finding the determinant of a linear matrix 
# And finding the determinant
d = np.identity(3)
print(np.linalg.det(d))

#Statistics
# Axis can also be included
stats = np.array([[1, 2, 3], [6, 5, 4]])
print(np.min(stats, axis=1))
print(np.max(stats))

# Being able to sum up the elements of an array
e = np.sum(stats, axis=1)
print(e)
