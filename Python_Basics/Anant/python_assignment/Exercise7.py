import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

  
x = pd.date_range(start ='1/1/2025', end ='31/01/2025', freq ='D') 
# I am considering 1 cycle of sin is 31 days
y = 15 + 10*(np.sin((2*np.pi*(x-x[0]).days)/31))
data = pd.DataFrame({'Date':x , 'Temp':y} )
data['7-Day Rolling Average'] = data['Temp'].rolling(window=7).mean()
plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['Temp'], marker='o')
plt.plot(data['Date'], data['7-Day Rolling Average'], color='red', label='7-Day Rolling Average', linewidth=2)
plt.title('Daily Temperatures for January 2025 with 7-Day Rolling Average')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.tight_layout()
print(data[data['Temp']>20])
plt.show()