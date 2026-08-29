import pandas as pd

df = pd.read_csv("data.csv")

# 2. Handle missing data
 
df=df.dropna(subset=["Type2"]) # Drops The rows which miss value 
#dropna = Drop Not available 
print(df.to_string())

df_2=df.fillna({"Type2":"None"}) # Fill the Not available value with none
#fillna = Fill Not Available
print(df_2.to_string())

# Output may have a erroe here but understand the logic behind it
