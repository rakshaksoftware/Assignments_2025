import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates=pd.date_range(start="2025-01-01",end="2025-01-31",freq="D")
temperature=15+10*np.sin(2*np.pi*np.arange(len(dates))/31)

df=pd.DataFrame({
    "Date": dates,"Temperature": temperature
})
df.set_index("Date",inplace=True)


print("Created Dataframe:")
print(df)
print("\n")

plt.plot(dates,df["Temperature"],label="Daily Temperatures")

df["Rolling-Average"]=df["Temperature"].rolling(window=7,center=True).mean()

print("Rolling Average:")
print(df)
print("\n")

df_high=df[df['Temperature']>20][['Temperature']]

print("The days when the temperature was above 20:")
print(df_high)
print("\n")

plt.scatter(df_high.index,df_high['Temperature'],color='green',marker='*',s=50,zorder=3)
plt.show()