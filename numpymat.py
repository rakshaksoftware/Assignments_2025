import numpy as np
A = np.random.randint(1, 11, (3, 3))
B = np.random.randint(1, 11, (3, 3))

print(A+B)
print(A * B)
print(np.dot(A, B))
print(np.linalg.det(A))
