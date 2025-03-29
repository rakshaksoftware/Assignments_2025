import numpy as np

rg = np.random.default_rng(42)

arr1=rg.integers(1, 11, (3,3))
arr2=rg.integers(1, 11, (3,3))

print(arr1, "\n" , arr2)

add = np.add(arr1, arr2)
dot = np.dot(arr1, arr2)
multiply = arr1 * arr2
det1 = np.linalg.det(arr1)

print("Addition of two arrays: \n", add)
print("Dot product of two arrays: \n", dot)     
print("Element wise multiplication of two arrays: \n", multiply)
print("Determinant of first array: \n", det1)
