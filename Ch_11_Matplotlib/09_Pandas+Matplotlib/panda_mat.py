import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df= pd.read_csv("data.csv")

type_count = (df["Type1"].value_counts(ascending=True)) # RETURNS COUNT OF EACH TYPE
plt.barh(type_count.index,type_count.values)

plt.title("# Of pokemon by types")
plt.xlabel("Count")
plt.ylabel("Type")

plt.tight_layout()
plt.show()

