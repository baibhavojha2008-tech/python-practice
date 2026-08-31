import matplotlib.pyplot as plt
import numpy as np

# Scatter Graph= Show relation between 2 variables
#                Helps to idnetify a correaltion(+,-,None)
#                Eg: Study hours VS. Test Score

x1= np.array([0,1,2,3,4,5,6,7,8,9])  # hours studied
y1= np.array([55,60,63,60,67,87,91,95,99,88]) #marks

x2= np.array([0,1,2,3,4,5,6,2,8,11])  # hours studied
y2= np.array([15,33,163,60,67,87,71,95,92,77]) #marks


plt.scatter(x1,y1,color="black",
            s=150,
            label="ClassA")

plt.scatter(x2,y2,color="red",
            s=150,
            label="ClassB")

plt.title("Test Score")
plt.xlabel("Hours studied")
plt.ylabel("Total Marks")

plt.legend() #Shows Index
plt.show()
