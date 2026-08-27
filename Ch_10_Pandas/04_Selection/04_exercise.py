import pandas as pd

df= pd.read_csv("import_eg_tourists.csv",index_col="date")

date = input("Enter date (YYYY-MM-DD): ")

try:
    print(df.loc[date])
except KeyError:
    print(f"No tourist data found for {date}.")