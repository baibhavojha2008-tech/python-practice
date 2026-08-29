import pandas as pd


df= pd.read_csv("data.csv")

print(df.sum(numeric_only=True)) #Finds the sun of columns which are numeric
print(df.min(numeric_only=True)) #Finds the minimum value of columns which are numeric
print(df.max(numeric_only=True)) #Finds the maximimum value of columns which are numeric
print(df.sum(numeric_only=True)) #Finds the sun of columns which are numeric
print(df.count()) #Finds the total counnt of data in each columsn

#This functions works in WHOLE DATA FRAME   