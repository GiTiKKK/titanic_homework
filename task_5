import pandas as pd
df = pd.read_csv('titanic.csv')

median_age = df['Age'].median()
df['Age'].fillna(median_age, inplace=True)

print("Медианный возраст:", median_age)