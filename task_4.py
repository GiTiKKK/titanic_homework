import pandas as pd
df = pd.read_csv('titanic.csv')

avg_fare_first_class = df[df['Pclass'] == 1]['Fare'].mean()
print("Средняя стоимость билета первого класса:", avg_fare_first_class)

third_class_survival_rate = df[df['Pclass'] == 3]['Survived'].mean() * 100
print("Выживаемость третьего класса:", third_class_survival_rate)