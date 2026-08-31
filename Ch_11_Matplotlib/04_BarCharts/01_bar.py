import matplotlib.pyplot as plt
import numpy as np

# Bar chart= Compare categories of data by reprsenting each categoryy with a bar

categories=["Grains","Fruit","Vegetable","Protein","Dairy","Sweets"]
values= np.array([4,3,2,5,2,1])

        #X axis    Y axis
#plt.bar(categories,values, color="skyblue") For vertical
plt.barh(categories,values, color="skyblue") #For horizontal bar

plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Consumption")


plt.show()