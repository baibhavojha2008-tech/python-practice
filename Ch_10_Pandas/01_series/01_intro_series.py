import pandas as pd

# Series: Think of it like a single column in a spreadsheet (1-D)

data =[100, 102, 104]

series = pd.Series(data)
'''
0    100
1    102
2    104
dtype: int64
'''
print (series)
#Output comes in a single comlun (1D) || Also gives data type in the output

series_adv = series = pd.Series(data, index =["a","b","c"])
'''
a    100
b    102
c    104
dtype: int64
'''
print (series_adv)

