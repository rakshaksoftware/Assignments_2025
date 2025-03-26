import pandas as pd

data={"Name":['Alice','Bob','Charlie','Diana','Ethan'],
      "Age":[28,34,25,42,30],
      "Salary":[70000,80000,50000,110000,75000]}

df=pd.DataFrame(data)

df['Tax']=df['Salary']*0.2
print(df, '\n')

df2 = df[df['Age'] >= 30]
print(df2, '\n')

df3 = df[df['Age'] < 30]
print(df3['Salary'].mean(), '\n')

df4 = df.sort_values(by='Salary', ascending=False)
df4.reset_index(drop=True, inplace=True)
print(df4)