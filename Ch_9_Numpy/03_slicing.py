import numpy as np

array=np.array([[1,2,3,4],  
                [5,6,7,8],  
                [9,10,11,12],  
                [13,14,15,16]])

#Slicing: array[start:end:step]

print(array[2]) #Output= [9,10,11,12]
print(array[-1]) #Output= [13,14,15,16]

print(array[0:3]) #Prints layer 0,1 and 2 and skips 3 
print(array[0:4:2]) #Prints from layer 0 to 4 skiiping 2 layers
'''
                [1,2,3,4],  Layer=0  starts from 0 print layer 0 and prints every 2nd layer 
                [5,6,7,8],  Layer=1  skip (Skips 1st layer)
                [9,10,11,12], Layer=2   prints (Prints 2nd)
                [13,14,15,16]] Layer=-3  skip
                    
                    '''
print(array[::-1]) #Prints from layer 4 to 0 reverse order

print(array[:,2]) #Selects all row and print only of 2nd column
print(array[:, 0:3]) #Prints first 3 elments form all rows

print(array[0:2,0:2]) #First 2 rows of first 2 columns
