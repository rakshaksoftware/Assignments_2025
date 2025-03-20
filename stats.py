import numpy as np

data = np.random.normal(loc=50, scale=5, size=1000)
mean = np.mean(data)
median = np.median(data)
stddev = np.std(data)
variance = np.var(data)
percentile25 = np.percentile(data, 25)
percentile75 = np.percentile(data, 75)

print(mean, median, stddev, variance, percentile25, percentile75)