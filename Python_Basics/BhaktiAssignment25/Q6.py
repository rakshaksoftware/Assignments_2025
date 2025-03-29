import matplotlib.pyplot as plt
import numpy as np
x=(np.random.randint(1,100,size=(1,100)))/100
y=np.random.normal(0.5,0.1,size=(1,100))
x=x.flatten()
y=y.flatten()
plt.scatter(x,y)
plt.show()
