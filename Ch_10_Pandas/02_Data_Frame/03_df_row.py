#Add New row

import pandas as pd

data = {
"Name": ["Balen","Sudhaan","Sagar"],
"Age" : [38, 39, 30]
}

df = pd.DataFrame(data,index=["PM","HM","IM"])

new_row = pd.DataFrame([{"Name":"Shasmit", "Age":35}], index=["EM"])
#To add new row we must make a new data frame and create dictionary om it

df = pd.concat([df,new_row])

#Concat is used to comine data farme created. 

print (df)
'''
Output:
      Name  Age
PM    Balen   38
HM  Sudhaan   39
IM    Sagar   30
EM  Shasmit   35
'''
#We can add multiple rows by creating many dictionarys
