import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dates = pd.date_range('2025-01-01', '2025-01-31')
temps = 15 + 10 * np.sin(2 * np.pi * np.arange(31) / 31)
df = pd.DataFrame({'Date': dates, 'Temperature': temps})
hot_days = df[df['Temperature'] > 20]
print("Days with temperature above 20°C:")
print(hot_days)
plt.plot(df['Date'], df['Temperature'], label='Temperature')
df['RollingAvg'] = df['Temperature'].rolling(7).mean()
plt.plot(df['Date'], df['RollingAvg'], label='7-Day Average', color='purple')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.show()

