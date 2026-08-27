import pandas as pd

df= pd.read_csv("import_eg_tourists.csv")

#Selection By Column

print(df["value"].to_string)

# Only the column under value is printed

#Using selection property we can print the data of the columns we want
# It can be multiple columns