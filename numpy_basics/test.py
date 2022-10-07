import numpy as np 

first = np.full((5, 5), 1)
print(first)

second = np.full((3,3), 0)
second[1, 1] = 9
print(second)

first[1:4, 1:4] = second
print(first)

