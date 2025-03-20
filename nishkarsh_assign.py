import pandas as pd
import numpy as np
import matplotlib.pyplot as mp

days = pd.date_range(start="2025-03-20", end="2025-04-20")
temperature = 15 + 10 * np.sin(2 * np.pi * (days.day - 1) / 31)
df = pd.DataFrame({"Date": days, "Temperature": temperature})
df.set_index("Date", inplace=True)
df.plot()
mp.show()


df["rollingAvg"] = df["Temperature"].rolling(window=7).mean()
df.plot()
mp.show()
hot_days = df[df["Temperature"] > 20]
print( hot_days)




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



import numpy as np
A = np.random.randint(1, 11, (3, 3))
B = np.random.randint(1, 11, (3, 3))

print(A+B)
print(A * B)
print(np.dot(A, B))
print(np.linalg.det(A))


import pandas as pd


data = {

    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Age": [28, 34, 25, 42, 30],
    "Salary": [70000, 80000, 50000, 110000, 75000],




    
}

df = pd.DataFrame(data)


df["Tax"] = df["Salary"] * 0.20


dffiltered = df[df["Age"] >= 30]


avgsalarybelow30 = df[df["Age"] < 30]["Salary"].mean()


dfsorted = df.sort_values(by="Salary", ascending=False)

print(df)
print(dffiltered)
print(avgsalarybelow30)
print(dfsorted)



import numpy as np
arr = np.ones(int(1e6),dtype=bool)
arr[1]=arr[0]=0
for i in range(2, int(1e6)):
    if(arr[i]):
       for j in range(i*i,int(1e6),i):
           arr[j]=0

l,r = map(int, input().split())

for i in range(l,r+1):
    if(arr[i]):
        print(i)



import numpy as np

data = np.random.normal(loc=50, scale=5, size=1000)
mean = np.mean(data)
median = np.median(data)
stddev = np.std(data)
variance = np.var(data)
percentile25 = np.percentile(data, 25)
percentile75 = np.percentile(data, 75)

print(mean, median, stddev, variance, percentile25, percentile75)








for i in range (100):
    if((i+1)%3==0 and (i+1)%5==0):
        print("FizzBuzz")
    elif ((i+1)%5==0):
        print("Buzz")
    elif ((i+1)%3==0):
        print("Fizz")
    else:
        print(i+1)
