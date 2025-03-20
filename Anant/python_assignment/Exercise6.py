import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = pd.DataFrame({'Name':['Alice', 'Bob','Charlie' ,'Diana' ,'Ethan'],'Age':[28 ,34, 25, 42 ,30],'Salary':[70000,80000,50000,110000,75000]})
data['Tax'] = 0.2*data['Salary']
print(data)
print("")
data_filtered = data[data['Age'] >= 30] 
print("Filterd Data which include only employees aged 30 and above.")
print(data_filtered)
print("")
data_filtered_ = data[data['Age'] >= 30]
print("average salary of employees aged below 30.")
print(data_filtered_['Age'].mean())
print("")
data_filtered_1 = data.sort_values(by='Salary', ascending=False)
print("Sorted DataFrame by Salary in descending order")
print(data_filtered_1)
print("")