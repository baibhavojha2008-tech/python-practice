import pandas as pd

df = pd.read_csv("data.csv")

group = df.groupby("Type1")

print(group["Height"].mean()) # Prints the mean height of type 1 by grouping 

#groupby() creates groups; you usually need an aggregation or operation 
#like sum(), mean(), max(), min(), etc. to get a meaningful result.


# Similarly other functions can also be used 
'''
Output:
Type1
Bug         0.900000
Dragon      2.666667
Electric    0.855556
Fairy       0.950000
Fighting    1.185714
Fire        1.216667
Ghost       1.466667
Grass       1.083333
Ground      0.850000
Ice         1.550000
Normal      0.986364
Poison      1.221429
Psychic     1.371429
Rock        1.844444
Water       1.300000
'''