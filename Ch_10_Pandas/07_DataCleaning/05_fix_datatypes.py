import pandas as pd

df = pd.read_csv("data.csv")

# 5. fix data types

df["Legendary"] = df["Legendary"].astype(bool)
# All the legendary status whcih was 0 and 1 comes as True and False 

print(df.to_string())

'''
.astype(int)       # →Converts Integer
.astype(float)     # →Converts  Decimal number
.astype(str)       # → Converts String/Text
.astype(bool)      # → Converts True/False
'''