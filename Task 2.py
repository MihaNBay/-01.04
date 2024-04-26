import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/MihaNBay/OneDrive/Python programs/MDK 01.04/практические работы/№36 Практическая работа/train.csv")

print(df.head(10))
print(f"Размерность данных: {df.shape}")
print(f"Количество пустых значений в каждом столбце: {df.isnull().sum()}")
print(f"Типы данных: \n {df.dtypes}")
