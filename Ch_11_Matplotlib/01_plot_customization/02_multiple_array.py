import matplotlib.pyplot as plt
import numpy as np


x= np.array([2023,2024,2026,2028])
y1=np.array([11,17,20,18])
y2=np.array([17,5,23,44])
y3=np.array([20,27,30,55])
line_style= dict(marker=".",              
         markersize=15,              
         markerfacecolor="#24080c", 
         markeredgecolor="#24080c", #Dictionary is used to used the style in different plotting
         linestyle="dashed",                       
         linewidth=4,                  
)


plt.plot(x,y1, color="green",  **line_style)  # ** unpacks the dictionary
plt.plot(x,y2, color="Red",    **line_style)  #We use different line color to identify line                 
plt.plot(x,y3, color="Cyan",   **line_style)                 

plt.show() # Showing plot graphically



