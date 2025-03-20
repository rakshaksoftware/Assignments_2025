import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data={"date":pd.date_range(start='1/1/2025', end='31/01/2025'),
      "temperature":15+10*np.sin(np.linspace(0, 2*np.pi, num=31))}
df=pd.DataFrame(data)

print(df, '\n')

df['Rolling Average'] = df['temperature'].rolling(window=7).mean()

plt.plot(df['date'], df['temperature'], color='red', marker='+', markersize=7)
plt.plot(df['date'], df['Rolling Average'], color='blue', marker='*', markersize=7)
plt.title('Temperature variation in January 2025')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.show()

filtered_df = df[df['temperature'] > 20]
print(filtered_df, '\n')


