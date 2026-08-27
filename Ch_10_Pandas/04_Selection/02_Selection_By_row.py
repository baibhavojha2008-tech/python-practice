import pandas as pd

df= pd.read_csv("import_eg_tourists.csv",index_col="date") #Proper indexing data for easy selection

print(df)

#Output comes as follow if we index date there wont be automated labels and it will be easy 
#to search the data when in large scale
'''
date        value         
1999-01-01  30.052513
1999-04-01  19.148496
1999-07-01  25.317692
'''

print(df.loc["1999-04-01",[]])
# When we have multiple column in file to print the selected column only
# we can use second argument to select the column we want to print(Now kept empty)

#This prints the value of selected date only

#Selectiong Range of rows
