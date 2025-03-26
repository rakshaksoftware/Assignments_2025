import numpy as np
import math
arr=np.array([])
i=1
while i<=1000:
    if(i<126):
        arr=np.append(arr,40)
    elif i<500:
        arr=np.append(arr,60)
    else:
       arr= np.append(arr,50)
    i=i+1
Mean=0
t=0
s=0
Variance=0
while t<1000:
    Mean=Mean+arr[t]
    t=t+1
Mean=Mean/1000

Median=arr[500]+arr[499]
Median=Median/2
while s<1000:
    k=arr[s]-Mean
    k=k**2
    Variance=Variance + k
    s=s+1
Variance=Variance/1000
Standarddeviation=math.sqrt(Variance)
print(Mean)
print(Median)
print(Standarddeviation)
print(Variance)
p25=np.percentile(arr,25)
p75=np.percentile(arr,75)
print(p25)
print(p75)