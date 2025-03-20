import numpy as np

rg = np.random.default_rng()
a = rg.integers(1,10,size=9).reshape(3,3)
b = rg.integers(1,10,size=9).reshape(3,3)
print(a)
print (b)
print(a+b)
print(a@b)
print(np.dot(a,b))
print(np.linalg.det(a))

