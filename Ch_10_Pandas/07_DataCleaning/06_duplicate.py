import pandas as pd

df = pd.read_csv("data.csv")

# 6. Remove duplicate value
# I added duplicate data myslef for understanding now
df= df.drop_duplicates()
# Removes all dupliate data

print(df.to_string())

