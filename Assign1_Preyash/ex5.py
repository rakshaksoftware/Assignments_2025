import matplotlib.pyplot as plt
import numpy as np

X1 = [-10 + x for x in range(21)]
Y1 = [x**2 for x in X1]

plt.figure(1)
plt.plot(X1, Y1, color='red', marker='*', linewidth=2, markersize=7)
plt.title('Graph of y=x^2')
plt.xlabel('x')
plt.ylabel('x^2')

X2 = np.random.uniform(0, 1, 100)
Y2 = np.random.normal(loc=0.5, scale=0.1, size=100)

plt.figure(2)
plt.scatter(X2, Y2, color='blue', marker='+')
plt.title('Scatter plot of random numbers')

data3 = np.random.exponential(1, 500)

plt.figure(3)
plt.hist(data3, bins=50, color='green')

plt.show()



