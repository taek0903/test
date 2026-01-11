# pd_DataFrame_list.py

import pandas as pd

data =[
    [1, 'Alice', 30],
    [2, 'Bob', 35],
    [3, 'Charlie', 25]
]

df = pd.DataFrame(data, columns=['ID','Name',"Age"], index=[1,2,3])
print(df)
print(type(df))