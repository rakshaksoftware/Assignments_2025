import pandas as pd
data={
    "Name"  : ["Alice","Bob","Charlie","Diana","Ethan"],
    "Age"   : [28,34,23,41,30],
    "Salary": [70000,80000,50000,110000,75000]
}
df=pd.DataFrame(data)
print("Generated dataframe:")
print(df)

df["Tax"]=df["Salary"]*0.2

print("\n")
print("Adding Tax Column:")
print(df)

print("\n")
print("Filtered employee:")
print(df[df["Age"]>=30])

print("\n")
print("Average Salary Of employees aged below 30:")
print(df[df["Age"]<30]["Salary"].mean())

print("\n")
print("Sorted by Salary in descending Order")
print(df.sort_values(by="Salary",ascending=False))