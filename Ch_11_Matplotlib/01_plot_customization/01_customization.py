import matplotlib.pyplot as plt
import numpy as np


x= np.array([2023,2024,2026,2028])
y= np.array([15,20,25,10])

plt.plot(x,y, marker=".",              # Each set of cooordinate willl be shown by dark point(".")
         markersize=15,                # The size of marker can be cutomized also uesd as "ms"
         markerfacecolor="#24080c",  # The color of marker edge can be cutomized   
         markeredgecolor="#24080c",  # The color of marker edge can be cutomized 
         linestyle="dashed",           # The line of graph can also be customized            
         linewidth=4,                  # The width line of graph can also be customized 
         color="Red")              # The line color of graph can also be customized    

plt.show() # Showing plot graphically



