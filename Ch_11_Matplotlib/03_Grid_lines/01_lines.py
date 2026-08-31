import matplotlib.pyplot as plt 

import numpy as np

# grid() = Helps, make plots easier to read by adding refrence lines\
# In simple way they are the boxes in the graph of x and y axis

x = np.array([1,2,3,4,5])
y = np.array([5,10,15,20,25])

plt.grid(axis="both",
         linewidth=2,
         color="lightgray",
         linestyle="dashed")


plt.plot(x,y)
plt.show()
