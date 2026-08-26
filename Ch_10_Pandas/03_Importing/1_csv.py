import pandas as pd

# Importing is used to import CSV and JSON files
# First we have to add the data in our folfer we are working on

df= pd.read_csv("import_eg_tourists.csv")
print(df.to_string()) #Prints entire data

#Prints csv value as df
