import pandas as pd
df = pd.read_csv('titanic.csv')

avg_age_survived = round(df[df['Survived'] == 1]['Age'].mean(), 2)
avg_age_dead = round(df[df['Survived'] == 0]['Age'].mean(), 2)

print("Средний возраст выживших:", avg_age_survived)
print("Средний возраст погибших:", avg_age_dead)