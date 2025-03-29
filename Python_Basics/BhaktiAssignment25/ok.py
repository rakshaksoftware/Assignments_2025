import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-10,11,0.1)
y = x**2
plt.plot(x, y)
plt.title("My First Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()
