import pandas as pd

df = pd.read_csv("import_eg_tourists.csv")

# Filtering : Keeping the rows that match the condition
 
high_value = df[df["value"]>=40]

print(high_value)
# Prints value which satisfy the given condition

# we can use all logical or mathematical operators for filtering to apply condiitons

# we can keep multiple condition by using or "|" and alsp by using and "&" operators

high_value = df [(df["value"] >=40) | 
               (df["date"]=="1999-07-01")]

print(high_value)
