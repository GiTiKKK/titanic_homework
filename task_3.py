import pandas as pd
df = pd.read_csv('titanic.csv')

total_survived = df['Survived'].sum()
print("Количество выживших:", total_survived)

survival_rate = round(df['Survived'].mean() * 100, 2)
print("Процент выживших:", survival_rate)

female_survival_rate = round(df[df['Sex'] == 'female']['Survived'].mean() * 100, 2)
print("Выживаемость женщин:", female_survival_rate)

male_survival_rate = round(df[df['Sex'] == 'male']['Survived'].mean() * 100, 2)
print("Выживаемость мужчин:", male_survival_rate)