# Add new column

import pandas as pd

data = {
"Name": ["Balen","Sudhaan","Sagar"],
"Age" : [38, 39, 30]
}

df = pd.DataFrame(data,index=["PM","HM","IM"])

df["job"] = ["PrimeMinister","HomeMinister","InfrastructureMinister"] 

#New column titled as job is craeted

print (df)
'''
Output:
   Name  Age                     job
PM    Balen   38           PrimeMinister
HM  Sudhaan   39            HomeMinister
IM    Sagar   30  InfrastructureMinister
'''