import numpy 
import random

b=numpy.random.randint(1,11,(3,3),dtype=int)
a=numpy.random.randint(1,11,(3,3),dtype=int)

print("0.1" , a)
print("0.2" , b)

print("1",a+b)
print("2",a*b)
print("3",numpy.dot(a,b))
print("4",int(round(numpy.linalg.det(a))))
