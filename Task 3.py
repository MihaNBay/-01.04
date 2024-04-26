import pandas as pd

df = pd.read_csv("C:/Users/MihaNBay/OneDrive/Python programs/MDK 01.04/практические работы/№36 Практическая работа/train.csv")

columns = ['Name', 'Ticket', 'Cabin', 'Embarked']
df_cleaned = df.drop(columns=columns)

median_age = df_cleaned['Age'].median()
df_cleaned['Age'].fillna(median_age, inplace=True)

df_cleaned['Sex'] = df_cleaned['Sex'].map({'male': 0, 'female': 1})

print(df_cleaned.head(10))
