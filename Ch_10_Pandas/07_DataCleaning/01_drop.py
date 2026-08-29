import pandas as pd

# Data Clearing: Process of FIXING/REMOVING:
#              incomplete, incorrect or irrevelant dataa
#        75% of work done with pandas is data clearing

df = pd.read_csv("data.csv")

# 1. Drop Irrelevant columns

df=df.drop(columns=["Legendary"]) # We can drop multiple columns also

print(df)
