# Remember to pip install numpy first
# We us numpy over list as numpy is faster
# Numpy uses fixed type

import numpy as np

# Print the installed NumPy version
print(np.__version__)

# Test a quick array
arr = np.array([1, 2, 3, 4, 5]) *2 #Multiplies the digits by arary
print(type(arr))
print(arr)

#<class 'numpy.ndarray'>
