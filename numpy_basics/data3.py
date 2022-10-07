import numpy as np 

b = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(b)
#All zeros matrix
print(np.zeros((2, 7)))

#All ones matrix
print(np.ones((2, 7)))

#Other numbers
print(np.full((2, 2), 99))

#Using a previous shape
print(np.full_like(b, 66))
print(np.full(b.shape, 66))

#Random decimal numbers
print(np.random.rand(4, 2))
print(np.random.random_sample(b.shape))

#Random integer numbers
print(np.random.randint(4, 7, size=(3, 3)))
a = b[..., np.newaxis]
print(a)

#The identity matrix
print(np.identity(5))

#Repeating a mtrix
r1 = np.repeat(b, 3, axis=1)
print(r1)