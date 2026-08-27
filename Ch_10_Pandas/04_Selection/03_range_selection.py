# Selecting range of rows
import pandas as pd

df= pd.read_csv("import_eg_tourists.csv",index_col="date") #Proper indexing data for easy selection


print(df.loc["1999-04-01":"1999-07-01",])
#Prints the data between the 2 dates

#Using slice operator ':'

#Using integer loc property

print(df.iloc[0:11])
#Prints the data from SN 0 to 10
#All slicing peoperty can u besd to print data 