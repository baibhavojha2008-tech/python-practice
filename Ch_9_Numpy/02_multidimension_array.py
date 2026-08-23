import numpy as np


array= np.array([[['A','B', 'C'], ['D','E','F'],['G','H','I']],
               [['J','K', 'L'], ['M','N','O'],['P','Q','R']],    #DImesion+3
               [['S','T', 'U'], ['V','W','X'],['Y','Z','_']]])  

#We can go beyond 3 dimension

print("The numbe of dimension is:",array.ndim)  #Print number of dimesnion of array
print("The Shape of dimension is:",array.shape) #Print shape of dimesnion of array
print(array[1,1,1]) #Prints the element the element in layer 1 , row 1 and column 1

word= array[0,0,0]+array[2,0,0]+array[0,2,1]
print(word)
'''
array= np.array(['A'])           Dimension=0
array= np.array(['A','N','C'])   Dimesion=1
array= np.array(['A','N', C'],
                ['W','X','Y']    #Dimesion=2
                ['A','B','C']])
'''