# This functions works for single columns only
import pandas as pd

df = pd.read_csv("data.csv")

print(df["Height"].mean()) #Finds the meaan of height column only
print(df["Height"].min()) #Finds the minimum value of hieght columns only
print(df["Height"].max()) #Finds the maximimum value of height column 
print(df["Height"].sum()) #Finds the sun of height
print(df["Height"].count()) #Finds the total counnt of data in hieght
