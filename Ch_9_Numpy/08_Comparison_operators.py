import numpy as np

# Comparison operators
'''
Using it we can craete boolean arrays, filter data and use element wise comparison
'''

scores= np.array([91, 100, 73, 29, 69])

print(scores==100) # Output:[False  True False False False]

print(scores >=40) # Output:[ True  True  True False  True]

scores[scores<40] = 0

print (scores)   # Output:[ 91 100  73   0  69]

# This all is prinmer for filtering
