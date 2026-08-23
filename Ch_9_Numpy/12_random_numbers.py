import numpy as np

# Random numbers: 
# Useful for simualtion, modeling, applying random transformation and testing purposes

rng = np.random.default_rng()

print (rng.integers(low=1,high=7)) # Random numbers form 1 to 6
print (rng.integers(low=1,high=101,size=3)) # 3 Random numbers from 1 to 100 is generated
                                            # Output is in 1D array

print (rng.integers(low=1,high=101,size=((3,2))))


'''Output:

[[24 29]
[81 41]
[ 2 77]]

'''