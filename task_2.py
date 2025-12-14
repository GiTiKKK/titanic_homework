import pandas as pd
df = pd.read_csv('titanic.csv')

print(df.describe())

categorical_cols = df.select_dtypes(include='object').columns
for col in categorical_cols:
    print(df[col].value_counts())

num_men = (df['Sex'] == 'male').sum()
print("Мужчин на корабле:", num_men)

num_first_class = (df['Pclass'] == 1).sum()
print("Пассажиров первого класса:", num_first_class)