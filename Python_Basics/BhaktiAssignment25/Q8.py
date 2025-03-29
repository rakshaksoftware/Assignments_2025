import pandas as pd
data={"Name":['Alice','Bob','Charlie','Diana','Ethan'],'Age':[28,34,25,42,30],'Salary':[70000,80000,50000,110000,75000]}
df=pd.DataFrame(data)
print(df)
df['Tax']=df['Salary']*0.2
print(df)
print(df[df['Age']>=30])
age=df[df['Age']<30]
avg=age['Salary'].mean()
print(avg)
print(df.sort_values(by='Salary', ascending=False))
