import matplotlib.pyplot as plt
import numpy as np
x=np.random.exponential(scale=1, size=500)
plt.hist(x)
plt.show()
