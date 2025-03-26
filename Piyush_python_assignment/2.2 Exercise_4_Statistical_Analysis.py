import numpy as np

random_nos=np.random.normal(50,5,1000)

print("1   :",np.mean(random_nos))
print("2   :",np.median(random_nos))
print("3   :",np.std(random_nos))
print("4   :",np.var(random_nos))
print("5.1 :",np.percentile(random_nos,25))
print("5.2 :",np.percentile(random_nos,75))