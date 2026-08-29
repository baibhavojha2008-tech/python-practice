import pandas as pd

df = pd.read_csv("data.csv")

# 4. Standarize text
df["Name"]= df["Name"].str.lower()
# Changes all name to Lower case

print (df.to_string())
'''
.str.lower()       # Converts all text to lowercase
.str.upper()       # Converts all text to uppercase
.str.capitalize()  # Converts the first character to uppercase
.str.title()       # Converts the first character of each word to uppercase
.str.strip()       # Removes extra spaces from the beginning and end
.str.replace()     # Replaces specified text with other text
'''