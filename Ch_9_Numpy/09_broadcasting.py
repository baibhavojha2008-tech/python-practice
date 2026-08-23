import numpy as np

'''
Broadcasting allows numpy to perform operations on array
with different shape by virtuallt exapandiing dimension
so they match large number of arrays's shape
'''

'''  CODITION FIOR BROADCASTING

The dimensions have the same size ( WE READ DIMENSION FROM RIGHT TO LEFT)
or
One of the diemsions has size 1
'''

array1= np.array([[1,2,3,4]])
array2= np.array([[1],[2],[3],[4]])

print(array1.shape)
print(array2.shape)

print(array1*array2) #BROADCASTS IF THE CONDITION SATISFY  

'''Output:
[[ 1  2  3  4] 
 [ 2  4  6  8]
 [ 3  6  9 12]
 [ 4  8 12 16]]'''