import matplotlib.pyplot as plt
import numpy as np


x= np.array([2023,2024,2026,2028])
y1=np.array([11,17,20,18])
y2=np.array([17,5,23,44])
y3=np.array([20,27,30,55])
line_style= dict(marker=".",              
         markersize=15,              
         markerfacecolor="#24080c", 
         markeredgecolor="#24080c", 
         linestyle="dashed",                       
         linewidth=4,                  
)

plt.title("Class Size by year",fontsize=25,    # Gives Title to graph and customization
                              family="Arial", 
                              fontweight="bold",
                              color="#0f0202")

plt.xlabel("Class Year",fontsize=20,    
                        family="Arial", 
                        fontweight="bold",
                        color="#0f0202")  # Gives title to x axis and customization

plt.ylabel("Students",fontsize=20,    
                        family="Arial", 
                        fontweight="bold",
                        color="#0f0202")  # Gives title to x axis and customization


plt.plot(x,y1, color="green",  **line_style)  
plt.plot(x,y2, color="Red",    **line_style)                 
plt.plot(x,y3, color="Cyan",   **line_style)                 

plt.xticks(x) # Only the inputed value of x comes in graph


plt.tick_params(axis="both",
                colors="#9c1d14") #Customizes the value of x and y axis shown in graph


plt.show() # Showing plot graphically
