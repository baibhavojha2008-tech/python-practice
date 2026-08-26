import pandas as pd

df= pd.read_json("import_eg_airports.json")

print(df.to_string())