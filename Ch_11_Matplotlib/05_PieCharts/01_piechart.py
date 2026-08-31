import matplotlib.pyplot as plt
import numpy as np

# Bar Chart = Circualr chart divided into slices to show % of total.
#            Good for visualizing distribution among categories

categories= ["Freshmen","Sophomores","Juniors","Seniors"]
values=np.array ([300,250,275,225])
colors= ["red","yellow","blue","green"]

plt.pie(values,labels=categories,
        autopct="%1.1f%%", #autocpt= Auto Percentage
        colors=colors,
        explode=[0,0,0,0.1], #Explode creates distance between the selected section and pie chart 
        shadow= True)

plt.show()  
