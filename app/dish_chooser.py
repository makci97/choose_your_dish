import numpy as np
import pandas as pd

from typing import Tuple

from app.settings import FOOD_MATRIX_PATH


class DishChooser:
    def __init__(self):
        self.food_matrix_df = pd.read_csv(FOOD_MATRIX_PATH, sep=';', index_col=0)

    def __call__(self, *args, **kwargs) -> Tuple[str, str]:
        """
        Choose randomly good combination of meat and side_dish.

        Returns:
            (meat, side_dish)
        """
        meat = self._choose_meat()
        side_dish = self._choose_side_dish(meat=meat)
        return meat, side_dish

    def _choose_meat(self) -> str:
        """
        Choose meat with probs from food matrix.

        Returns:
            meat: str
        """
        meat_probs = self.food_matrix_df.sum(axis=1) / self.food_matrix_df.values.sum()
        meat = np.random.choice(meat_probs.index, p=meat_probs.values)
        return meat

    def _choose_side_dish(self, meat: str) -> str:
        """
        Choose side_dish for the meat with probs from food matrix.

        Returns:
            side_dish: str
        """
        side_dish_probs = self.food_matrix_df.loc[meat, :] / self.food_matrix_df.loc[meat, :].sum()
        side_dish = np.random.choice(side_dish_probs.index, p=side_dish_probs.values)
        return side_dish
