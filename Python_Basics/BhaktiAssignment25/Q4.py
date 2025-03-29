import numpy as np


a=np.random.normal(50, 5, (1, 1000))
print(np.mean(a))
print(np.median(a))
print(np.std(a))         
print(np.var(a))
print(np.percentile(a,25))
print(np.percentile(a,75))



