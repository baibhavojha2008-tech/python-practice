import numpy as np

#Vectorized Math funcs
'''
It is a linear algebar term. Vector is single Dimension.

Using vectorized math function we can apply a function to an entire array without loop
'''
array= np.array([1.04,2.6,3.9])

print(np.sqrt(array)) # Finds square root
print(np.round(array)) # Round ups the numebr || Output = 1,3,4
print(np.floor(array)) # Round down the number|| Output = 1,2,3
