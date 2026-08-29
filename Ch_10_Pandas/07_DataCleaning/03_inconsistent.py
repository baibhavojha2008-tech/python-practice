import pandas as pd

df = pd.read_csv("data.csv")

# 3. Fix Inconsisitent Value
 
df["Type1"]= df["Type1"].replace({"Grass":"GRASS",
                                  "Fire":"FIRE"})
# Changes all grass to uppercase, Multiple cases can be kept in dictionary

print (df.to_string())
