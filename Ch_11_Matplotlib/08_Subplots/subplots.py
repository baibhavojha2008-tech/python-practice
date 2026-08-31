import matplotlib.pyplot as plt
import numpy as np

# Figure = The entire canvas
# Ax = A single plot (subplot)

x=np.array([1,2,3,4,5])

figure,axes = (plt.subplots(2,2)) # 2 rows and 2 colums 

axes[0,0].plot(x,x*2,color="red") #Selects graph of row 0 and column 0
axes[0,0].set_title("x*2")

axes[0,1].bar(x,x*3,color="blue") #Selects graph of row 0 and column 0
axes[0,1].set_title("x**2")

axes[1,0].scatter(x,x*3,color="green") #Selects graph of row 0 and column 0
axes[1,0].set_title("x*3")

axes[1,1].hist(x,x*3,color="pink") #Selects graph of row 0 and column 0
axes[1,1].set_title("x**3")

plt.tight_layout() # Seprates graph properly and keeps it well represented
plt.show()