import pandas as pd

data =[100, 102, 104, 204, 220]

series = pd.Series(data, index=["Room#1","Room#2","Room#3","Room#4","Room#5"])

print (series[series >=200])
'''
Output:
Room#4    204
Room#5    220
dtype: int64
'''


