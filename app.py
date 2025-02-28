import pandas as pd 

df = pd.read_csv('.learn/assets/us_baby_names_right.csv')
names = df.groupby("Name").sum()

print(len(names))