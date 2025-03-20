import numpy as np
arr = np.ones(int(1e6),dtype=bool)
arr[1]=arr[0]=0
for i in range(2, int(1e6)):
    if(arr[i]):
       for j in range(i*i,int(1e6),i):
           arr[j]=0

l,r = map(int, input().split())

for i in range(l,r+1):
    if(arr[i]):
        print(i)

