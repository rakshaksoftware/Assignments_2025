# Exercise 3: Matrix Operations
import numpy as np

A = np.random.randint(1, 11, (3, 3))
B = np.random.randint(1, 11, (3, 3))

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Addition
print("A + B:\n", A + B)

# Element-wise multiplication
print("Element-wise Multiplication of A & B:\n", A * B)

# Dot product
print("Dot Product of A & B:\n", np.dot(A, B))

# Determinant of A
print("Determinant of A:", np.linalg.det(A))