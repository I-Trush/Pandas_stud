import numpy as np
import pandas as pd

data = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

df = pd.DataFrame(data)

print(df)
#    0  1  2
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9

df = pd.DataFrame(data, index=['a', 'b', 'c'], columns=['x', 'y', 'z'])
print(df)

data = {
    'Name': ['a','b','c'],
    'Age': [10,20,30],
    'Addres': ['xxx','yyy','zzz']
}
df = pd.DataFrame(data)
print(df)

