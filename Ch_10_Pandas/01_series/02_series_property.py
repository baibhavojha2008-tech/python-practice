# LOCK PROPERTY

import pandas as pd

data =[100, 102, 104]

series = pd.Series(data, index=["Room#1","Room#2","Room#3"])

print (series.loc["Room#1"]) # Prints the value under room#1 Only

#Output: 100

print (series.iloc[1]) # Prints the value under index 1

#Output: 102