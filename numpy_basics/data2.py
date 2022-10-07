import numpy as np
a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a)

#In order to get a specific element in the array
#array[row, column]
#Note that indexing starts from 0
print(a[1, 5])

#In order to get a whole row(first)
print(a[0, :])

#In order to get a specific colum(first)
print(a[:, 0])

#From a single point to another with steps
print(a[0, 1:6:2])

#Chaning a new element
a[1, 5] = 15
print(a)