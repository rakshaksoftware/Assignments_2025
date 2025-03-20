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
