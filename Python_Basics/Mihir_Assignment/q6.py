import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Age": [28, 34, 25, 42, 30],
    "Salary": [70000, 80000, 50000, 110000, 75000]
}

df = pd.DataFrame(data)

df["Tax"] = df["Salary"] * 0.2

df_filter = df[df["Age"] >= 30]

avg_salary_below_30 = df[df["Age"] < 30]["Salary"].mean()

df_sorted = df.sort_values(by="Salary", ascending=False)

print(df)
print(df_filter)
print("Average salary of employees below 30:", avg_salary_below_30)
print(df_sorted)