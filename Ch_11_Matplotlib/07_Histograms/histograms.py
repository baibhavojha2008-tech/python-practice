import matplotlib.pyplot as plt
import numpy as np

# Histogram = Visual representation of distribution of quantitaive data.
#             They group values into bins (intervals)
#             and counts how many falls in each range

scores= np.random.normal(loc=80,scale=10, size=100)
# Generates 100 random scores with an average (mean) of 80 and a standard deviation of 10

scores= np.clip(scores,0,100)
# Limits all scores between 0 and 100
# Values below 0 become 0, and values above 100 become 100

plt.hist(scores,bins=10,
         color="lightgreen",
         edgecolor="black")

# bins=10 → Divides the scores into 10 groups (intervals)
# color → Sets the color of the bars
# edgecolor → Adds a black border around each bar

plt.title("Exam scores")
plt.xlabel("Scores")
plt.ylabel("No Of students")

plt.show()