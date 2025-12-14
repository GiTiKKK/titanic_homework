import pandas as pd

df = pd.read_csv('titanic.csv')
df['Age'].fillna(df['Age'].median(), inplace=True)

num_survived_first_class_women = df[(df['Pclass'] == 1) & (df['Sex'] == 'female') & (df['Survived'] == 1)].shape[0]
print("Количество выживших женщин первого класса:", num_survived_first_class_women)

num_minors_without_parents = df[(df['Age'] < 18) & (df['SibSp'] == 0) & (df['Parch'] == 0)].shape[0]
print("Количество пассажиров младше 18 лет без родителей:", num_minors_without_parents)