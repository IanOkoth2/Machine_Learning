import numpy as np 
#One dimensional array
a = np.array([1, 2, 3], dtype='int16')
#print(a)

#Two dimensional array
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
#print(b)

#Getting the dimensions of the numpy arrays
print('The dimension of a: ' + str(a.ndim))
print('The dimension of b: ' + str(b.ndim))

#Getting the shape of an array
print('The shape of a: ' + str(a.shape))
print('The shape of b: '+ str(b.shape))#prints out two rows and three columns

#Getting the type and size of our numpy arrays
print('The datatype of a: ' + str(a.dtype))
print('The datatype of b: ' + str(b.dtype))

#Getting the size
print('The size of a: ' + str(a.itemsize))
print('The size of b: ' + str(b.itemsize))