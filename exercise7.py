# Exercise 7: Time Series Analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generating daily temperatures for January 2025
days = pd.date_range(start="2025-01-01", end="2025-01-31")
temperature = 15 + 10 * np.sin(2 * np.pi * (days.day - 1) / 31)

df = pd.DataFrame({"Date": days, "Temperature": temperature})
df.set_index("Date", inplace=True)

# Plot time series
df.plot(title="Daily Temperature in January 2025")
plt.show()

# Compute and plot rolling average
df["7-day Rolling Avg"] = df["Temperature"].rolling(window=7).mean()
df.plot(title="Temperature with 7-day Rolling Average")
plt.show()

# Identify days above 20°C
hot_days = df[df["Temperature"] > 20]
print("Days with temperature above 20°C:\n", hot_days)