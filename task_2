import pandas as pd
df = pd.read_csv('titanic.csv')

print(df.describe())

categorical_cols = df.select_dtypes(include='object').columns
print(df[categorical_cols].value_counts(dropna=False))

num_men = (df['Sex'] == 'male').sum()
print("Мужчин на корабле:", num_men)

num_first_class_cabins = df[df['Pclass'] == 1]['Cabin'].notna().sum()
print("Кают первого класса:", num_first_class_cabins)