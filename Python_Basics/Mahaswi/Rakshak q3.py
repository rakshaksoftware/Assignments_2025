import numpy as np
A=np.array([[1,2,3],[3,4,7],[2,8,9]])
B=np.array([[1,4,6],[2,3,9],[4,9,1]])
print(A+B)
print(A*B)
print(A.dot(B))
print(np.linalg.det(A))