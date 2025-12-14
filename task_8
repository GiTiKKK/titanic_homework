import pandas as pd
df = pd.read_csv('titanic.csv')

survived_first_class_women = df[(df['Pclass'] == 1) & (df['Sex'] == 'female') & (df['Survived'] == 1)]
print("Количество выживших женщин первого класса:", survived_first_class_women.shape[0])

minors_without_parents = df[(df['Age'] < 18) & (df['SibSp'] == 0) & (df['Parch'] == 0)]
print("Количество пассажиров младше 18 лет без родителей:", minors_without_parents.shape[0])