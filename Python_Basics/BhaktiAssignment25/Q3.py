import numpy as np
a=np.random.randint(2,10,size=(3,3))
b=np.random.randint(2,10,size=(3,3))
print(a)
print(b)
print(a+b)
print(a*b)
print(a@b)
print(np.linalg.det(a))
