
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-10, 10, 100)
y = x ** 2
plt.plot(x, y, label="f(x) = x²")
plt.legend()
plt.title("Line Plot")
plt.show()


x_scatter = np.random.uniform(0, 1, 100)
y_scatter = np.random.normal(0.5, 0.1, 100)
plt.scatter(x_scatter, y_scatter)
plt.title("Scatter Plot")
plt.show()


data_hist = np.random.exponential(1, 500)
plt.hist(data_hist, bins=30)
plt.title("Histogram")
plt.show()