#2.DATA_FRAME
#-> A DataFrame is like a two dimensional labeled column.

import pandas as pd

data = {
"Name": ["Balen","Sudhaan","Sagar"],
"Age" : [38, 39, 30]
}

df = pd.DataFrame(data)

print (df)

'''
Output:
     Name  Age
0    Balen   38
1  Sudhaan   39     #Output comes in a double comlun (2D) || Also gives data type in the output
2    Sagar   30
'''

#We can add index similar to seires in data frame