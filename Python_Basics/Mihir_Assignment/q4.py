import numpy as np
data = np.random.normal(loc=50, scale=5, size=1000)

print(np.mean(data))
print(np.median(data))
print(np.std(data))
print(np.var(data))
print(np.percentile(data, 25))
print(np.percentile(data, 75))