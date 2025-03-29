import matplotlib.pyplot as plt
import numpy as np
plt.subplot(1,3,1)
x= np.arange(-10,11,1)
plt.plot(x,x**2)
plt.title("Part A",loc='left')

plt.subplot(1,3,2)
x=np.random.uniform(0,1,size=100)
y=np.random.normal(0.5,0.1,size=100)
plt.plot(x,y)
plt.title("Part B",loc='left')

plt.subplot(1,3,3)
x=np.random.exponential(1,500)
plt.hist(x)
plt.title("Part C",loc='left')
plt.show()