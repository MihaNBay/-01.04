import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/MihaNBay/OneDrive/Python programs/MDK 01.04/Practical work/№36 Practical work/train.csv")
survived_passengers = df['Survived'].values
total_survived = np.sum(survived_passengers)

print(f"Общее количество выживших пассажиров: {total_survived}")
