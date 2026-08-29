import pandas as pd

'''
 Aggregate Function : Reduces a set of value into a  SINGLE SUMMARY VALUE
 Used to summarize and analyze data
 Often used with groupby() function
'''

df= pd.read_csv("data.csv")

print(df.mean(numeric_only=True)) #Finds the mean of columns which are numeric
'''
Output:
No           75.500000
Height        1.200000
Weight       46.231333
Legendary     0.026667
'''
