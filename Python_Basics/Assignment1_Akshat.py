#Conditionals and Loops

#1.1
for i in range(1,101):
    if i%15 == 0:
        print("FizzBuzz")
    elif i%5 == 0:
        print("Buzz")
    elif i%3 == 0:
        print("Fizz")
    else :
        print(i)

#1.2
x = int(input())
y = int(input())
for i in range(x,y+1):
    count = 0
    for j in range(2,i):
        if(i%j==0):
            count+=1
    if(count==0):
        print(i)

#NumPy implementation

#2.1
import numpy as np
A = np.random.randint(1,11,size=(3,3))
B = np.random.randint(1,11,size=(3,3))
C = np.add(A,B)
D = np.multiply(A,B)
E = np.dot(A,B)
F = np.linalg.det(A)

#2.2  
import numpy as np
arr = np.random.normal(loc=50, scale=5, size=1000)
mean = np.mean(arr)
median = np.median(arr)
standard_deviation = np.std(arr)
variance = np.var(arr)
percentile_one = np.percentile(arr,25)
percentile_two = np.percentile(arr,75)

#Matplotlib Implementation

#3.1
import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return x**2
x = np.linspace(-10,10,1000)
y = f(x)
plt.plot(x,y)
plt.show()

#3.2
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,1,100)
y = np.random.normal(loc=0.5,scale=0.1,size=100)
plt.scatter(x,y)
plt.show()

#3.3
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,1,100)
y = np.random.normal(loc=0.5,scale=0.1,size=100)
plt.scatter(x,y)
plt.show()

#3.4
## Not able to understand what is meant by exponential distribution with rate parameter of 1


#Pandas Implementation

#4.1
import pandas as pd
x = {'Name':['Alice','Bob','Charlie','Diana','Ethan'],'Age':[28,34,25,42,30],'Salary':[70000,80000,50000,110000,75000]}
df = pd.Dataframe(x)
df['Tax'] = df['Salary']*0.2
df_filter = df[df['Age']>30]
avg_salary = df[df['Age']<30]['Salary'].mean()
sorted_df = df.sort_values(by='Salary',ascending = False)

#Time Series

#5.1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dates = pd.date_range(start="2025-01-01", end="2025-01-31", freq="D")
temperature = 15 + 10 * np.sin(2 * np.pi * np.arange(31) / 31)
df = pd.DataFrame({"Date": dates, "Temperature": temperature})
df.set_index("Date", inplace=True)
df["Rolling_Avg"] = df["Temperature"].rolling(7).mean()
plt.plot(df.index, df["Temperature"])
plt.plot(df.index, df["Rolling_Avg"])
plt.scatter(df.index[df["Temperature"] > 20], df["Temperature"][df["Temperature"] > 20], color="red")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.show()
print(df.index[df.Temperature > 20])

