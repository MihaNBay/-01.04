import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/MihaNBay/OneDrive/Python programs/MDK 01.04/Practical work/№36 Practical work/train.csv")

relatives_array = df[['SibSp', 'Parch']].values
total_relatives = np.sum(relatives_array)
max_relatives_index = np.argmax(np.sum(relatives_array, axis=1))
passenger_with_max_relatives = df.iloc[max_relatives_index]

print(f"Общее количество родственников на борту: {total_relatives}")
print(f"Информация о пассажире с наибольшим количеством родственников: \n{passenger_with_max_relatives}")
