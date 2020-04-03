import numpy as np
import pandas as pd

filename = '/Users/maxim/Desktop/food_matrix.csv'
food_matrix_df = pd.read_csv(filename, sep=';', index_col=0)

meat_probs = food_matrix_df.sum(axis=1) / food_matrix_df.values.sum()
meat = np.random.choice(meat_probs.index, p=meat_probs.values)

side_dish_probs = food_matrix_df.loc[meat, :] / food_matrix_df.loc[meat, :].sum()
side_dish = np.random.choice(side_dish_probs.index, p=side_dish_probs.values)

print(f"{side_dish} и {meat}")
