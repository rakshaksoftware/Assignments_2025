import numpy as np

import matplotlib.pyplot as plt
x = np.linspace(-20, 20, 200)
y = x**2
plt.plot(x, y)
plt.show()
y1 = np.random.normal(0.1, 0.5, 100)
x1 = np.random.uniform(0, 1, 100)
plt.scatter(x1,y1)
plt.show()
data_hist = np.random.exponential(1, 500)
plt.hist(data_hist)
plt.show()
