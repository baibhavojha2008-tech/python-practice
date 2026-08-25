import pandas as pd

calories={
"Day1":1750,
"Day2":1900,
"Day3":2000,
"Day4":2100
}

series = pd.Series(calories)

series.loc["Day3"] += 500 # Updates day 3 count by 500

print(series.loc["Day3"]) # Output:2500

print(series)
'''
Output:
Day1    1750
Day2    1900
Day3    2500
Day4    2100
dtype: int64
'''

print(series[series >=2000])
'''
Output:
Day3    2500
Day4    2100
dtype: int64
'''