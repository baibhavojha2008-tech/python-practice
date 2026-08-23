import numpy as np

''' Aggregate functions:
-->summarize data and typicallly return single value
'''

'''
FUNCTION        WHAT IT DOES

np.sum()	    Adds all values	
np.mean()	    Calculates average	
np.median()	    Finds middle value	
np.min()	    Smallest value	
np.max()	    Largest value	
np.std()	    Standard deviation	
np.var()	    Variance	
np.argmin()	    Index of smallest value	
np.argmax() 	Index of largest value	
np.prod()	    Multiplies all values	
np.cumsum()	    Cumulative sum	
np.cumprod()	Cumulative product	
'''

array= np.array ([[1,2,3,4,5],
                  [6,7,8,9,19]])

print("The sum of array is:",np.sum(array))
print("The sum of all columns is:",np.sum(array,axis=0))
print("The sum of all rows is:",np.sum(array,axis=1))