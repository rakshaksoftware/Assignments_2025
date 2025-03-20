import pandas as pd


data = {

    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Age": [28, 34, 25, 42, 30],
    "Salary": [70000, 80000, 50000, 110000, 75000],




    
}

df = pd.DataFrame(data)


df["Tax"] = df["Salary"] * 0.20


dffiltered = df[df["Age"] >= 30]


avgsalarybelow30 = df[df["Age"] < 30]["Salary"].mean()


dfsorted = df.sort_values(by="Salary", ascending=False)

print(df)
print(dffiltered)
print(avgsalarybelow30)
print(dfsorted)
