import numpy as np

rg = np.random.default_rng()

arr1=rg.normal(loc=50, scale=5, size=1000)
print(arr1)

mean=np.mean(arr1)
median=np.median(arr1)
std=np.std(arr1)
var=np.var(arr1)
percentile25=np.percentile(arr1, 25)
percentile75=np.percentile(arr1, 75)

print("Mean of the array: ", mean)
print("Median of the array: ", median)
print("Standard deviation of the array: ", std) 
print("Variance of the array: ", var)
print("25th percentile of the array: ", percentile25)
print("75th percentile of the array: ", percentile75)

