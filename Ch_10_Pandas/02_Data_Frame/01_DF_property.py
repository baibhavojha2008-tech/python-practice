# LOCK PROPERTY

import pandas as pd

data = {
"Name": ["Balen","Sudhaan","Sagar"],
"Age" : [38, 39, 30]
}

df = pd.DataFrame(data,index=["PM","HM","IM"])

print (df.loc["PM"])
'''
Name    Balen
Age        38    
Name: PM, dtype: object  
'''
#  It prints the data under label PM and also prints Label name
#  eg "PM" in this case and also prints data type

print (df.iloc[1]) # Prints the output by integer location
'''
Output:
Name    Sudhaan
Age          39
Name: HM, dtype: object
'''