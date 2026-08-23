import numpy as np

# Filtering = defined as the process of seleveting elements 
#             from array that match a given condition

ages= np.array([[21,17,18,20,65],
               [39,22,15,99,18]])

teen= ages[ages <=18]
print("all the ages recorded:",ages)
print("The teenmagers:",teen)

adults= ages[(ages> 18) & (ages<65)]
print("The adultss:",adults)

'''
we use & | instead of and , or because numpy use C operators
'''
