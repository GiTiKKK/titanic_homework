import pandas as pd
df = pd.read_csv('titanic.csv')

print(df.shape)
print(df.info())

total_passengers = df.shape[0]
print("Всего пассажиров:", total_passengers)

missing_age = df['Age'].isna().sum()
print("Пропущенных значений Age:", missing_age)